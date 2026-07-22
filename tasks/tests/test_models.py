from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from tasks.models import Tag, Task

class TagModelTest(TestCase):
    def test_str_returns_name(self):
        tag = Tag.objects.create(name="Work")

        self.assertEqual(str(tag), "Work")


class TaskModelTest(TestCase):
    def test_str_returns_content(self):
        task = Task.objects.create(content="Finish Django project")

        self.assertEqual(str(task), "Finish Django project")

    def test_is_overdue_returns_true(self):
        task = Task.objects.create(
            content="Expired task",
            deadline=timezone.now() - timedelta(days=1),
        )

        self.assertTrue(task.is_overdue)

    def test_is_overdue_returns_false_for_completed_task(self):
        task = Task.objects.create(
            content="Completed task",
            deadline=timezone.now() - timedelta(days=1),
            is_done=True,
        )

        self.assertFalse(task.is_overdue)