from django import forms
class ChocoForm(forms.Form):
 to=forms.EmailField()
 sub=forms.CharField(max_length=50)
 cont=forms.CharField(max_length=300)
