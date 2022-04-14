from django import forms
from .models import StartDate

class DateForm(forms.ModelForm):

    class Meta:
        model = StartDate
        fields = ['start_date','end_date']

