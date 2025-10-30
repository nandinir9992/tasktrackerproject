from django import forms
from myapp.models import task
class taskForm(forms.ModelForm):
	class Meta:
		model=task
		fields='__all__'