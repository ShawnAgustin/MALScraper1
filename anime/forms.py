from django.forms import ModelForm, TextInput
from .models import Show

class ShowForm(ModelForm):
	class Meta:
		model = Show
		fields = ['title']