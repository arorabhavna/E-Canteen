from django import forms
from shop.models import Item

PRODUCT_QUANTITY_CHOICES=[(i, str(i)) for i in range(1,11)]

class CartAddProductForm(forms.Form):
 	quantity=forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
 	update=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
