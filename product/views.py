
from django.contrib.auth import models, login
from django.shortcuts import render, redirect
from .forms import CreateProductForm
from .models import Products
# Create your views here.
def create_product_view(request):

    if request.method == "POST":  # 1
        create_form = CreateProductForm(request.POST)
        if create_form.is_valid():  # 2 # 5
            print("save")
            create_form.save()
            return redirect('/')
        else:
            print(create_form.errors)
    else:  # 3
        pass
    form = CreateProductForm()
    return render(request, 'product/create_product.html', {'form': form})

def products_view(request):
    if request.method =="GET":
        user = request.user.is_authenticated
        if user:
            all_products = Products.objects.all().order_by('-created_at')

            return render(request,'product/products.html',{'all_products':all_products})
        else:
            return redirect('/log-in')
    return render(request, 'product/products.html')