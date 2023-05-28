from django import forms
from man_shop import models


class Man_shop_form(forms.ModelForm):
    class Meta:
        model = models.Man_shop
        fields = '__all__'


