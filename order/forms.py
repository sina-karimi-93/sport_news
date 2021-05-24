from django import forms


class UserNewOrderFOrm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput()
    )
    count = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'تعداد', 'class': 'form-control text-center'})
    )
