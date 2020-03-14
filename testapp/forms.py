from django import forms
from .models import State, Reqdata, Reqtype
from django.forms.widgets import CheckboxSelectMultiple
class ReqForm(forms.ModelForm):

    class Meta:
        model = Reqdata
        fields = ('Requesttype', 'Reqdisc', 'city', 'state', 'pincode', 'Altermob')

    def __init__(self, *args, **kwargs):
        super(ReqForm, self).__init__(*args, **kwargs)

        self.fields["Requesttype"].widget = CheckboxSelectMultiple()
        self.fields["Requesttype"].queryset = Reqtype.objects.all()
