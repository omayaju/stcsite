from django.forms import ModelForm
from shop.models import GoodApp

class AppForm(ModelForm):
	class Meta:
		model = GoodApp
		fields = ['count','country', 'district', 'town', 'addres', 'email', 'phone']

	def __init__(self, *args, **kwargs):
		super(AppForm, self).__init__(*args, **kwargs)
		self.fields['count'].widget.attrs['class'] = 'form-control space'
		self.fields['country'].widget.attrs['class'] = 'form-control space'
		self.fields['district'].widget.attrs['class'] = 'form-control space'
		self.fields['town'].widget.attrs['class'] = 'form-control space'
		self.fields['addres'].widget.attrs['class'] = 'form-control space'
		self.fields['email'].widget.attrs['class'] = 'form-control space'
		self.fields['phone'].widget.attrs['class'] = 'form-control space'