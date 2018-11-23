from django import forms
from .models import CoverLetterParagraph


class CoverLetterForm(forms.Form):

    P1_CHOICES = []
    P2_CHOICES = []
    P3_CHOICES = []

    for choice in CoverLetterParagraph.objects.filter(paragraph_position=CoverLetterParagraph.FIRST_PARAGRAPH):
        P1_CHOICES.append((choice.name,choice.name))

    for choice in CoverLetterParagraph.objects.filter(paragraph_position=CoverLetterParagraph.SECOND_PARAGRAPH):
        P2_CHOICES.append((choice.name,choice.name))

    for choice in CoverLetterParagraph.objects.filter(paragraph_position=CoverLetterParagraph.THIRD_PARAGRAPH):
        P3_CHOICES.append((choice.name,choice.name))

    company_name = forms.CharField(widget=forms.TextInput(attrs={'class':'FieldInput TextInput'}), max_length=100)
    company_address_street = forms.CharField(widget=forms.TextInput(attrs={'class': 'FieldInput TextInput'}), max_length=255)
    company_address_city = forms.CharField(widget=forms.TextInput(attrs={'class': 'FieldInput TextInput'}), max_length=100)
    company_address_state = forms.CharField(widget=forms.TextInput(attrs={'class': 'FieldInput TextInput'}), max_length=100)
    company_address_zip = forms.CharField(widget=forms.TextInput(attrs={'class': 'FieldInput TextInput'}), max_length=10)
    job_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'FieldInput TextInput'}), max_length=100)
    paragraph1 = forms.ChoiceField(P1_CHOICES, widget=forms.Select(attrs={'class': 'FieldInput'}, choices=P1_CHOICES))
    paragraph2 = forms.ChoiceField(P2_CHOICES, widget=forms.Select(attrs={'class': 'FieldInput'}, choices=P2_CHOICES))
    paragraph3 = forms.ChoiceField(P3_CHOICES, widget=forms.Select(attrs={'class': 'FieldInput'}, choices=P3_CHOICES))


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'FieldInput TextInput'}), max_length=100)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'FieldInput TextInput'}), max_length=200)
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'FieldInput TextInput'}), max_length=5000)