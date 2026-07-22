from django.urls import path
from django.views import View

from tasks import views
from tasks.views import (TaskListView,
                         TaskCreateView, TaskUpdateView, TaskDeleteView, TaskToggleView, TagListView, TagCreateView,
                         TagUpdateView, TagDeleteView,
                         )

app_name = "tasks"

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("tasks/add/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/toggle/", TaskToggleView.as_view(), name="task-toggle"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/add/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

