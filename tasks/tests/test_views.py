from django.test import TestCase
from django.urls import reverse

from tasks.models import Tag, Task


class TaskViewTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(content="Test task")

    def test_home_page(self):
        response = self.client.get(reverse("tasks:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.content)

    def test_toggle_task(self):
        self.client.post(reverse("tasks:task-toggle", args=[self.task.id]))

        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)


class TagViewTest(TestCase):
    def test_tag_list_page(self):
        Tag.objects.create(name="Home")

        response = self.client.get(reverse("tasks:tag-list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Home")
