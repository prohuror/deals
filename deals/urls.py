from django.urls import path

from deals.api.views import DealUploader

urlpatterns = [
        path('upload-file/', DealUploader.as_view())
]
