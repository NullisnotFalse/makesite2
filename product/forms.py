from django import forms
from .models import Products

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['producter','name','description','prise','size','amount',]
        labels = {'name':'제품명',
                    'description':'설명',
                  'prise':'가격',
                  'size':'사이즈',
                  'amount':'수량',}
