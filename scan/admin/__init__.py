from django.contrib import admin

from scan.admin.target import TargetAdmin
from scan.admin.subdomain import SubdomainAdmin

from scan.models import (
    Target as TargetModel,
    Subdomain as SubdomainModel
)

admin.site.register(TargetModel, TargetAdmin)
admin.site.register(SubdomainModel, SubdomainAdmin)
