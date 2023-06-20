from django.core.validators import MinLengthValidator
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Address(TimeStampedModel):

    street = models.CharField(max_length=255)

    city = models.CharField(max_length=100)

    number = models.CharField(max_length=10, null=True, blank=True)

    complement = models.CharField(max_length=100, null=True, blank=True)

    state = models.CharField(max_length=100)

    postal_code = models.CharField(
        max_length=9,
        validators=[MinLengthValidator(8)]
    )

    country = models.CharField(max_length=50)
