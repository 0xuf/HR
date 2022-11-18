from django.urls import path
from scan.api import CreateViewTarget, GetResult


urlpatterns = [
    path("scan/", CreateViewTarget.as_view(), name="create_new_target_api"),
    path("result/<str:scan_id>/", GetResult.as_view(), name="get_result_api")
]
