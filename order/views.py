from django.shortcuts import render
from .forms import OrderForm
from django.shortcuts import render, redirect
# Create your views here.
def order(request):
    if request.method == "POST":  # 1
        create_form = OrderForm(request.POST)
        if create_form.is_valid():  # 2 # 5
            print("save")
            create_form.save()
            return redirect('/')
        else:
            print(create_form.errors)
    else:  # 3
        pass
    form = OrderForm()
    return render(request, 'product/order.html', {'form': form})
