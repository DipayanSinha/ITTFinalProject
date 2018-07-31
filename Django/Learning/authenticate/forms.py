from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.forms import User
from django import forms

class WriteCode(forms.Form):
    results = forms.CharField(label="Write your code here",widget=forms.Textarea(attrs={'class':'form-control','width': "100%", 'cols': "80", 'rows': "20" }))
    #code_input = forms.CharField(label="",max_length=2000,widget=forms.Textarea(),help_text='Write your program here!')
    parameters = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Parameters'}))

class AcceptFile(forms.Form):
    file = forms.FileField(label="Upload File")
    parameters = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Parameters'}))

    #file = forms.FileField(label="Java File",widget=forms.FileInput(attrs={'placeholder': 'Upload File'}))

class AcceptParameters(forms.Form):
    parameters = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Parameters'}))

class EditUserForm(UserChangeForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model=User
        fields = ('username','first_name','last_name','email','password')

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = ""
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your Username'

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))

    class Meta:
        model=User
        fields = ('username','first_name','last_name','email','password1','password2',)

    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = ""
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your Username'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = ""
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li> ' \
                                    '<li>Your password can\'t be a commonly used password.</li> <li>Your password can\'t be entirely numeric.</li> ' \
                                    ' </ul>'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = ""
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter your Password'
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


