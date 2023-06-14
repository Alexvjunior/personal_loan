from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django_extensions.db.models import TimeStampedModel
from common import enums
from apps.address.models import Address


class Proposal(TimeStampedModel):

    full_name = models.CharField(max_length=100)

    cpf = models.CharField(max_length=14, validators=[MinLengthValidator(11)])

    loan_amount = models.FloatField(validators=[MinValueValidator(0.0)])

    status = models.CharField(
        max_length=20,
        choices=[(status.value, status.name)
                 for status in enums.StatusProposal]
    )

    adress = models.OneToOneField(Address, on_delete=models.DO_NOTHING)
