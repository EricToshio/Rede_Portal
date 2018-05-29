from django import forms

from issues_report.models import Problem


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ('name', 'localization', 'iniciativa', 'description',)