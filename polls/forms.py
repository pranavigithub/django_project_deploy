from django import forms

class UserForm(forms.Form):
    name = forms.CharField(required=True, help_text="Enter your full name")
    email = forms.EmailField(help_text="Enter your email")
    phone = forms.IntegerField(help_text="Enter your Phone number")
    #address = forms.CharField(help_text="Enter your address")

    def clean_phone(self):
        phone = self.data["phone"]
        message =''
        #import ipdb;ipdb.set_tarce()
        if not phone.isdigit():
            message = "Phone number should be numeric."
        elif len(phone) !=10:
            message = "Phone number must contain 10 digits."
        elif phone[0] not in "9876":
            message = "phone number must start with  9876."
        if message:
            raise forms.ValidationError(message)
        return phone

    def clean_name(self):
        name = self.data["name"]
        message=''
        #import pdb;pdb.set_trace()
        #if not name.isalpha():
            #message = "Name should be alphabet"
        # words= name.split()
        # if len(words) !=2:
        #     message = "name should contain two words"
        # for word in words:
        #     if not word[0].isupper():
        #         message=" first letter of words in name should be capital"
        if not name.istitle():
            message = "Name should be in title format"
            if message:
                raise forms.ValidationError(message)
            return name
 




