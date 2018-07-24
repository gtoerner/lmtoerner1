from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=200, required=True)
    contact_email = forms.EmailField(required=True)
    contact_subject = forms.CharField(required=True)
    contact_message = forms.CharField(required=True, widget=forms.Textarea)

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Name"
        self.fields['contact_email'].label = "Email"
        self.fields['contact_subject'].label = "Subject"
        self.fields['contact_message'].label = "Message"