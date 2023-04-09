from django.shortcuts import render
from .forms import OrderForm
from django.shortcuts import render, redirect
from .models import Order
# Create your views here.
def create_order(request):
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
    return render(request, 'order/create_order.html', {'form': form})


def order_view(request):
    if request.method == "GET":
        user = request.user.is_authenticated
        if user:
            all_orders = Order.objects.all().order_by('marker','-created_at')
            return render(request, 'order/order.html', {'all_orders': all_orders})
        else:
            return redirect('/log-in')
    return render(request, 'oder/order.html')