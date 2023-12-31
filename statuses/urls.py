from django.urls import path

from statuses import views

urlpatterns = [
    path("", views.StatusesListView.as_view(), name="all_statuses"),
    path("create/", views.StatusCreateView.as_view(), name="status_create"),
    path(
        "<int:pk>/update/", views.StatusUpdateView.as_view(), name="status_update"
    ),  # noqa E501
    path(
        "<int:pk>/delete/", views.StatusDeleteView.as_view(), name="status_delete"
    ),  # noqa E501
]

app_name = "statuses"
