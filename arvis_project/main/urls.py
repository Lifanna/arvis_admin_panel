from . import views
from django.urls import path


urlpatterns = [
    path('', views.UploadAPKView.as_view(), name='home'),
    path('apks/', views.ApkListView.as_view(), name='apk-list-view'),
    path('upload_apk/', views.UploadAPKView.as_view(), name='upload_apk'),
    path('apk/<int:pk>/file/', views.APKFileView.as_view(), name='apk-file'),
]
