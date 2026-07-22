from django.shortcuts import render, redirect, get_object_or_404

from todo.forms import TaskForm
from todo.models import Task, Tag


def home(request):
    tasks = Task.objects.prefetch_related("tags").all()
    return render(request, "home.html", {"tasks": tasks})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm()
    return render(
        request,
        "task_form.html",
        {"form": form, "title": "New task"}
    )


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task)
    return render(
        request,
        "task_form.html",
        {"form": form, "title": "Edit task"}
    )


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("home")
    else:
        return render(request, "confirm_delete.html",
                      {"task": task})


def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save(update_fields=["is_done"])
    return redirect("home")

def tag_list(request):
    tags = Tag.objects.all()
    return render(
        request,
        "tag_list.html",
        {"tags": tags}
    )
