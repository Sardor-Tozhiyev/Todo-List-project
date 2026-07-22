from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
        ),
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "What need to be done?",
                    "class": "form-control",
                }
            ),
            "is_done": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
            "tags": forms.CheckboxSelectMultiple(),
        }
