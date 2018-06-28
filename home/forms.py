from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'sub_title', 'iniciativa_name', 'text', 'pic')