from utilities.models import GeneralModel
from django.db import models
from scan.models import Target
from django.utils.translation import gettext as _


class Subdomain(GeneralModel):
    target = models.ForeignKey(
        Target,
        verbose_name=_("Target of subdomain"),
        on_delete=models.CASCADE,
        related_name='subdomains'
    )

    subdomain = models.CharField(
        verbose_name=_("subdomain"),
        max_length=1024,
        unique=True
    )

    nuclei_result = models.TextField(
        verbose_name=_("Nuclei result"),
        null=True,
        blank=True
    )

    ip_address = models.GenericIPAddressField(
        verbose_name=_("Ip address of subdomain"),
    )

    def __str__(self):
        return f"{self.subdomain} - {self.target.domain}" # noqa
