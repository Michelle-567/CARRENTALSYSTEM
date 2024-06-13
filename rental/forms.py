# from django import forms
# from .models import Contact  # If you have a Contact model

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['name', 'email', 'message']
#         # Add any other fields and validation as needed
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'message': 'Your Message',
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),  # Adjust widget attributes as needed
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your message here'})
