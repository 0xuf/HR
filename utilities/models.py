from django.db import models
from django.utils.translation import gettext as _


class GeneralModel(models.Model):
    """
    General model is created to use in all models with some default fields like (Create time, Update time)
    """
    created_at = models.DateTimeField(
        verbose_name=_("Create time"),
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name=_("Update time"),
        auto_now=True
    )

    class Meta:
        abstract = True
