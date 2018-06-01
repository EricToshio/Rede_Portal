from django import forms

from issues_report.models import Problem
from .models import ReservationRede


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ('name', 'localization', 'iniciativa', 'description',)


class ReservationForm(forms.ModelForm):
    class Meta:
        model = ReservationRede
        fields = ('name', 'address', 'details', 'reservation_date', 'status')