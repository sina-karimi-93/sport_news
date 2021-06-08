from django import forms


class BMIForm(forms.Form):
    height = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class": "form-control text-center", "placeholder": "قد (سانتی متر )"}),
        label='')

    weight = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class": "form-control text-center", "placeholder": "وزن ( کیلوگرم )"}),
        label='')


class ContactUsForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control text-center", "placeholder": "موضوع"}
        ),
        label='موضوع'
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control text-center", "placeholder": "پیام"}
        ),
        label=''
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control text-center", "placeholder": "ایمیل"}
        ),
        label=''
    )
    phone_number = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class": "form-control text-center", "placeholder": "شماره تلفن همراه"}),
        label='')
