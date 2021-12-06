from django import forms

from shop.models import City, AreaZone


class CreateCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = "__all__"

    def clean(self):
        data = self.cleaned_data
        name = data.get("name")
        if City.objects.filter(name=name).exists():
            raise forms.ValidationError("This city is already exists")

        code = data.get("code")
        if City.objects.filter(code=code).exists():
            raise forms.ValidationError("This code can not be assigned")
        return data


