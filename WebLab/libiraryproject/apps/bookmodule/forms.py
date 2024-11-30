from .models import Book,Address,Student,Student2
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class BookForm(forms.ModelForm):
    class Meta: 
        model = Book # tell form that model to map
        fields = ['title', 'author', 'price', 'edition']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields='__all__'
        exclude = []
    name = forms.CharField(max_length=100,label='Name',required=True,widget=forms.TextInput())
    age = forms.IntegerField(initial=0,label='Age',required=True,widget=forms.NumberInput())
    address=forms.ModelChoiceField(label='City',queryset=Address.objects.all(),required=True, widget=forms.Select())

class StudentForm2(forms.ModelForm):
    class Meta:
        model= Student2
        fields='__all__'
        exclude = []
    name = forms.CharField(max_length=100,label='Name',required=True,widget=forms.TextInput())
    age = forms.IntegerField(initial=0,label='Age',required=True,widget=forms.NumberInput())
    addresses=forms.ModelMultipleChoiceField(label='City',queryset=Address.objects.all(),required=True, widget=forms.CheckboxSelectMultiple())

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  'password1', 'password2')