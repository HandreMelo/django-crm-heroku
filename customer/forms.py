from django import forms
from .models import Customer

class DateInput(forms.DateInput):
    input_type = 'date'

class CustomerForm(forms.ModelForm):

    first_name = forms.CharField(error_messages={"max_length":"Não pode ter mais que 30 caracteres"})
    last_name = forms.CharField()
    email = forms.EmailField()
    birth_date = forms.DateField(label="Aniversário", widget=DateInput())
    area_code = forms.RegexField(label="Código de Área com Regex", regex=r"^\+?1?[0-9]{2}$", error_messages={'invalid':"DDD inválido"})
    phone_number= forms.CharField()
    country = forms.CharField()
    state = forms.CharField()
    city = forms.CharField()


    class Meta:
        model = Customer
        fields =[
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "area_code",
            "phone_number",
            "country",
            "state",
            "city"
        ]