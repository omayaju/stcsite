from django.forms import ModelForm
from tours.models import App

class AppForm(ModelForm):
	class Meta:
		model = App
		fields = ['country', 'district', 'town', 'addres', 'email', 'phone']

	def __init__(self, *args, **kwargs):
		super(AppForm, self).__init__(*args, **kwargs)
		self.fields['country'].widget.attrs['class'] = 'form-control space'
		self.fields['district'].widget.attrs['class'] = 'form-control space'
		self.fields['town'].widget.attrs['class'] = 'form-control space'
		self.fields['addres'].widget.attrs['class'] = 'form-control space'
		self.fields['email'].widget.attrs['class'] = 'form-control space'
		self.fields['phone'].widget.attrs['class'] = 'form-control space'