from django import forms

class IssueForm(forms.Form):
    name = forms.CharField(label='Seu nome', initial='',max_length=50)
    localization = forms.CharField(label='AP/vaga (ex.: 315/F)', initial='', max_length=5)
    iniciativa = forms.ChoiceField(label='iniciativa (ex.: RedeCasd)', choices= (('RedeCasd','RedeCasd'),('DOO','DOO'),('Casd','Casd')))
    description = forms.CharField(label='Descrição do problema', initial='',max_length=200)

class TicketForm(forms.Form):
    #name = forms.CharField(label='Seu nome', initial='',max_length=50)
    ticket = forms.UUIDField(label='Seu Ticket', initial='')