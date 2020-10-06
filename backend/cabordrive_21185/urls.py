"""cabordrive_21185 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from allauth.account.views import confirm_email
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path("", include("home.urls")),
    path("accounts/", include("allauth.urls")),
    path("api/v1/", include("home.api.v1.urls")),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("rest-auth/", include("rest_auth.urls")),
    # Override email confirm to use allauth's HTML view instead of rest_auth's API view
    path("rest-auth/registration/account-confirm-email/<str:key>/", confirm_email),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
    path("api/v1/", include("task.api.v1.urls")),
    path("task/", include("task.urls")),
    path("api/v1/", include("task_profile.api.v1.urls")),
    path("task_profile/", include("task_profile.urls")),
    path("api/v1/", include("tasker_business.api.v1.urls")),
    path("tasker_business/", include("tasker_business.urls")),
    path("api/v1/", include("location.api.v1.urls")),
    path("location/", include("location.urls")),
    path("api/v1/", include("wallet.api.v1.urls")),
    path("wallet/", include("wallet.urls")),
    path("api/v1/", include("task_category.api.v1.urls")),
    path("task_category/", include("task_category.urls")),
    path("home/", include("home.urls")),
]

admin.site.site_header = "CabOrDrive"
admin.site.site_title = "CabOrDrive Admin Portal"
admin.site.index_title = "CabOrDrive Admin"

# swagger
api_info = openapi.Info(
    title="CabOrDrive API",
    default_version="v1",
    description="API documentation for CabOrDrive App",
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns += [
    path("api-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs")
]
