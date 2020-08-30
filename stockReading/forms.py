from django import forms
from .models import article,articleExpiryDates


class stockReaderForm(forms.ModelForm):
    # refrence = forms.CharField()
    # name = forms.CharField()
    # dateExpiration = forms.DateTimeField()
    # # class Meta :
    # #     model = Article()
    class Meta:
        model = article
        fields = ('referenceId', 'nom', 'descirption')


class ExpiryDateForm(forms.ModelForm):
    class Meta:
        model = articleExpiryDates
        fields = ('referenceId', 'expiryDate')
