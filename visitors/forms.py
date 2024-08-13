from django import forms
from visitors.models import Visitor

class VisitorsForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ["fullname", "person_identity", "born_date", "house_number", "vehicle_sign"]