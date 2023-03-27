from django.forms import ModelForm
from .models import Lead


class LeadForm(ModelForm):
    class Meta:
        model = Lead
        exclude = ('created_at','status')


class AssignAgentForm(ModelForm):
    class Meta:
        model = Lead
        fields = ('agent',)