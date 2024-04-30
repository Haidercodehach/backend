from django.urls import path
from .views import DocumentUploadView,ReceiveData

urlpatterns = [
    path('upload/', DocumentUploadView.as_view(), name='document-upload'),
    path('receive-data/', ReceiveData.as_view(), name='receive-data')
]