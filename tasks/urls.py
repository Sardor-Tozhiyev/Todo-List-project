from django.urls import path

from tasks import views


app_name = "tasks"

urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/add/", views.task_create, name="task-create"),
    path("tasks/<int:pk>/update/", views.task_update, name="task-update"),
    path("tasks/<int:pk>/delete/", views.task_delete, name="task-delete"),
    path("tasks/<int:pk>/toggle/", views.task_toggle, name="task-toggle"),
    path("tags/", views.tag_list, name="tag-list"),
]

