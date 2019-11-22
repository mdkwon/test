from django import forms
from .models import Year, Make, CarModel

class VehicleYearForm(forms.ModelForm):
    class Meta:
        model = Year
        fields = ('year',)

class VehicleMakeForm(forms.ModelForm):
    class Meta:
        model = Make
        fields = ('make',)

class VehicleCarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ('model',)


