from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django_extensions.db.models import TimeStampedModel

from apps.address.models import Address
from common import enums


class Proposal(TimeStampedModel):

    full_name = models.CharField(max_length=100)

    cpf = models.CharField(max_length=14, validators=[MinLengthValidator(11)])

    loan_amount = models.FloatField(validators=[MinValueValidator(0.0)])

    status = models.CharField(
        max_length=20,
        choices=[(status.value, status.name)
                 for status in enums.StatusProposal]
    )

    address = models.OneToOneField(Address, on_delete=models.DO_NOTHING)
