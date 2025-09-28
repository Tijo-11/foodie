from django import forms

CHOICES = [
    ('happy', 'Happy'),
    ('neutral', 'Neutral'),
    ('sad', 'Sad'),
]

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    satisfaction = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect
    )

    # Custom validation for email
    def clean_email(self):
        email = self.cleaned_data['email']
        if 'gmail' not in email:
            raise forms.ValidationError("Please use your Gmail email")
        return email
