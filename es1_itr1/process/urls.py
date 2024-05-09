from django.urls import path

from . import views

app_name = "process"
urlpatterns = [
    path("<int:pk>-<slug:object_name>/", views.detail, name="detail"),
    path("", views.view),
]