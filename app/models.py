from enum import Enum
from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class WorkflowStage(models.TextChoices):
    PROCESSED = "processed", "Processed"
    AWAITING_FULFILLMENT = "awaiting_fulfillment", "Awaiting fulfillment"
    FULFILLED = "fulfilled", "Fulfilled"


class PersonManager(models.Manager):
    def get_queryset(self):
        pass


class Person(models.Model):
    inmate_number = models.CharField(max_length=50)
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    legacy_prison_id = models.SmallIntegerField(null=True)
    legacy_last_served_date = models.DateTimeField(null=True, default=None)
    modified_date = models.DateTimeField(auto_now=True)
    modified_by=models.ForeignKey(User, null=True, related_name='person_modified_by_user', on_delete=models.SET_NULL, default=User)
    created_by=models.ForeignKey(User, null=True, related_name='person_created_by_user', on_delete=models.SET_NULL, default=User)

    class Meta:
        # ordering = ('-pending_letter',)
        verbose_name_plural = "people"

    def __str__(self):
        return self.last_name

    @property
    def current_prison(self):
        if person_prison := self.prisons.filter(current=True).first():
            return person_prison.prison

    @property
    def last_served(self):
        if fulfilled_letters := self.letter_set.filter(workflow_stage__in=[WorkflowStage.FULFILLED]):
            return fulfilled_letters.order_by("fulfilled_date").first().fulfilled_date
        elif self.legacy_last_served_date:
            return datetime.date(self.legacy_last_served_date)
        return

    #need to figure out what timedelta ppbp wants
    @property
    def eligibility(self):
        if not self.last_served:
            return "Eligible"
        if self.last_served <= (datetime.now().date() - timedelta(weeks=12)):
            if self.pending_letter_count == 0:
                return "Eligible"
            else:
                return "Eligible, letters pending"
        elif date_last_fulfilled := self.letter_set.filter(workflow_stage__in=[WorkflowStage.FULFILLED]):
            date_last_fulfilled.order_by(
            "fulfilled_date"
            ).first().fulfilled_date
            eligible_date = date_last_fulfilled + timedelta(weeks=12)
            return f"Eligible after {eligible_date.strftime('%B %-d, %Y')}"
        else:
            return f"Eligible after {self.legacy_last_served_date.strftime('%B %-d, %Y')}"

    @property
    def package_count(self):
        return self.letter_set.filter(workflow_stage__in=[WorkflowStage.FULFILLED]).count()

    @property
    def pending_letter_count(self):
        return self.letter_set.filter(
            workflow_stage__in=[
                WorkflowStage.PROCESSED,
                WorkflowStage.AWAITING_FULFILLMENT
            ]
        ).count()

    @property
    def pending_letters(self):
        return self.letter_set.filter(
            workflow_stage__in=[
                WorkflowStage.PROCESSED,
                WorkflowStage.AWAITING_FULFILLMENT
            ]
        ).all()

    @property
    def letter_count(self):
        return self.letter_set.all().count()

    @property
    def all_letters(self):
        return self.letter_set.all()


class Prison(models.Model):
    name = models.CharField(max_length=200)
    prison_type = models.CharField(max_length=50)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=200)
    # Probably omit restrictions ultimately
    restrictions = models.CharField(max_length=200, blank=True)
    legacy_id = models.CharField(max_length=50, unique=True)
    notes = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    modified_by=models.ForeignKey(User, null=True, related_name='prison_modified_by_user', on_delete=models.SET_NULL)
    created_by=models.ForeignKey(User, null=True, related_name='prison_created_by_user', on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Letter(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    modified_by=models.ForeignKey(User, null=True, related_name='letter_modified_by_user', on_delete=models.SET_NULL, default=User)
    created_by=models.ForeignKey(User, null=True, related_name='letter_created_by_user', on_delete=models.SET_NULL, default=User)

    postmark_date = models.DateField(null=True, blank=True)
    processed_date = models.DateField(null=True, blank=True, default=now)
    awaiting_fulfillment_date = models.DateField(null=True, blank=True)
    fulfilled_date = models.DateField(null=True, blank=True)
    # change to choices
    workflow_stage = models.CharField(
        max_length=200,
        choices=WorkflowStage.choices,
        default=WorkflowStage.PROCESSED
    )
    notes = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.person.last_name} - {self.postmark_date}"


class PersonPrison(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='prisons')
    prison = models.ForeignKey('Prison', on_delete=models.CASCADE, related_name='people')
    current = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    modified_by=models.ForeignKey(User, null=True, related_name='personprison_modified_by_user', on_delete=models.SET_NULL)
    created_by=models.ForeignKey(User, null=True, related_name='personprison_created_by_user', on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.prison.name} - {self.person.last_name}"
