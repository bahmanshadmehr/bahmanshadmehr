from django import forms
from . import models

class EmailForm(forms.ModelForm):
	class Meta:
		model = models.Join
		fields = ['email',]