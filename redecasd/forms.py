from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.models import User
from issues_report.models import Problem
from .models import ReservationRede


class ProblemForm(forms.ModelForm):
    STATUS_CATEGORIES=(
        ('Enviado', 'Enviado'),
        ('Em avaliação', 'Em avaliação'),
        ('Resolvido', 'Resolvido'),
    )
    status = forms.ChoiceField(choices=STATUS_CATEGORIES)

    class Meta:
        model = Problem
        fields = ('name', 'localization', 'iniciativa', 'description', 'status', 'people_in_charge')

    def __init__(self, *args, **kwargs):
        
        super(ProblemForm, self).__init__(*args, **kwargs)
        
        self.fields["people_in_charge"].widget = CheckboxSelectMultiple()
        self.fields["people_in_charge"].widget.attrs['class'] = 'list-style'
        self.fields["people_in_charge"].queryset = User.objects.filter(groups__name='RedeCasd')

class ReservationForm(forms.ModelForm):
    class Meta:
        model = ReservationRede
        fields = ('name', 'address', 'details', 'reservation_date', 'status')
