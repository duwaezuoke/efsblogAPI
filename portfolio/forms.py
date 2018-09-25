from django import forms
from .models import Customer, Investment, Stock, Fund


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_number', 'name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone',)


class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = (
            'customer', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value',
            'recent_date',)


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('customer', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date',)

class FundForm(forms.ModelForm):
    class Meta:
        model = Fund
        fields = ('customer', 'symbol', 'name', 'quantity', 'purchase_price', 'purchase_date', 'recent_value', 'recent_date')

class EmailForm(forms.Form):
    email = forms.EmailField(max_length=30)
    subject = forms.CharField(max_length=100)
    attach = forms.Field(widget = forms.FileInput)
    message = forms.CharField(max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!')

    def clean(self):
        cleaned_data = super(EmailForm, self).clean()
        subject = cleaned_data.get('subject')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        # attach = input.FILES['attach']
        if not subject and not email and not message:
            raise forms.ValidationError('You have to write something!')        