from django import forms
from django.template.loader import render_to_string

class SliderWidget(forms.widgets.TextInput):
	template = 'jokes/slider.html'
	
	def render(self, name, value, attrs=None):
		min_val = attrs.get('min_value', self.attrs['min_value'])
		return render_to_string(self.template, {
			'min': min_val,
			'max': attrs.get('max_value', self.attrs['max_value']),
			'step': attrs.get('step', self.attrs['step']),
			'value': value or min_val,
			'name': name,
			'id': attrs['id']
		})