from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
	class Meta:
		model=Todo
		app_label="myapp"
		fields="__all__"
