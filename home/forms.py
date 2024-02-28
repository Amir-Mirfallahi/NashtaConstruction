from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=156,
                                widget=forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Full Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'contactus', 'placeholder': 'Email'}))
    phone_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'contactus', 'placeholder': 'Your phone number'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Message'}))

