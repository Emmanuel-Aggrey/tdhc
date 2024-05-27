from django.db import models

# Create your models here.
from literals.models import BaseModel, Group, Status, Location

from members.service import random_with_N_digits
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Member(BaseModel):

    class MARITAL_STATUS:
        MARRIED = "married"
        SINGLE = "single"
        DIVORCED = "divorced"
        SEPARATED = "separated"

        ALL = (MARRIED, SINGLE)

        CHOICES = (
            (MARRIED, ("Married")),
            (SINGLE, ("Single")),
            (DIVORCED, ("Divorced")),
            (SEPARATED, ("Separate")),

        )

    class GENDER:
        MALE = "male"
        FEMALE = "female"

        ALL = (MALE, FEMALE)

        CHOICES = (
            (MALE, ("Male")),
            (FEMALE, ("Female")),


        )
    gender = models.CharField(
        max_length=20, blank=True, null=True, choices=GENDER.CHOICES)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    group = models.ManyToManyField(Group, blank=True)
    marital_status = models.CharField(
        max_length=20, choices=MARITAL_STATUS.CHOICES, default=MARITAL_STATUS.SINGLE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    secondary_phone_number = models.CharField(
        max_length=15, null=True, blank=True)

    baptismal_date = models.DateField(null=True, blank=True)
    digital_address = models.CharField(
        max_length=200, null=True, blank=True, help_text="House or digital address")
    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, help_text='Location or Residencial area')
    profile = models.ImageField(null=True, blank=True)

    occupation = models.CharField(max_length=200, null=True, blank=True)
    place_of_work = models.CharField(max_length=200, null=True, blank=True)
    unique_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


@receiver(pre_save, sender=Member)
def generate_lead_id(sender, instance: Member, **kwargs):
    if not instance.unique_id:
        instance.unique_id = random_with_N_digits(
            no_digits=4,

        )
