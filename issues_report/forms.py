from django import forms

class IssueForm(forms.Form):
    name = forms.CharField(label='Seu nome', initial='',max_length=50)
    localization = forms.CharField(label='AP/vaga (ex.: 315/F)', initial='', max_length=5)
    iniciativa = forms.CharField(label='iniciativa (ex.: RedeCasd)', initial='',max_length=20)
    description = forms.CharField(label='Descrição do problema', initial='',max_length=200)