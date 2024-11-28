from .models import Book,Address,Student,Student2,Address2
from django import forms
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
        model = Student
        fields = ['name', 'age', 'address']
    address = forms.ModelChoiceField(queryset=Address.objects.all(), empty_label="Select Address")

class StudentForm2(forms.ModelForm):
    class Meta:
        model = Student2  # Use Student2 model
        fields = ['name', 'age', 'addresses']  # 'addresses' refers to the ManyToMany field

    addresses = forms.ModelMultipleChoiceField(
        queryset=Address2.objects.all(),  # Make sure this points to Address2
        widget=forms.CheckboxSelectMultiple,
        required=False  # Allows for no addresses to be selected
    )