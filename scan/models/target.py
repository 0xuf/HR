from utilities.models import GeneralModel
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from datetime import datetime


class Target(GeneralModel):
    """
    Target model
    """

    STATUS_CHOICES = (
        ("finished", "FINISHED"),
        ("ongoing", "ONGOING"),
        ("error", "ERROR")
    )

    scan_id = models.CharField(
        verbose_name=_("UUID of target"),
        max_length=36
    )

    user = models.ForeignKey(
        User,
        verbose_name=_("Target creator"),
        on_delete=models.CASCADE,
        related_name="targets"
    )

    domain = models.CharField(
        verbose_name=_("Domain of target"),
        max_length=150,
        unique=True
    )

    status = models.CharField(
        verbose_name=_("Status of target"),
        max_length=8,
        choices=STATUS_CHOICES,
        default="ongoing"
    )

    def __str__(self):
        return self.domain
