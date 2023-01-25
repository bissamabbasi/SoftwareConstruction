import json
from math import ceil
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import product, order, OrderUpdate, ContactUs
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/loginuser")
    else:
        redirect("/")
        p = product.objects.all()
        products = []
        get_category = product.objects.values('category', 'id')
        category_products = {item['category'] for item in get_category}
        for c in category_products:
            prod = product.objects.filter(category=c)
            n = len(prod)
            nSlides= n//4 + ceil((n/4) - (n//4))
            products.append([prod, range(nSlides), nSlides])
    

    return render(request, 'shop/index.html', { 'products':products})


def preview(request, prid):
    Product = product.objects.filter(id=prid)
    return render(request, "shop/preview.html", {'product':Product[0]})


def checkout(request):
    if request.method == 'POST':
        items_json = request.POST.get('items_json', '')
        firstName = request.POST.get('firstName', '')
        lastName = request.POST.get('lastName', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '') + " " + request.POST.get('address2', '')
        country = request.POST.get('country', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        Order = order(items_json=items_json, firstName=firstName, lastName=lastName, username=username, email=email, address=address, country=country,
                       state=state, zip_code=zip_code, phone=phone)
        
        Order.save()
        thank = True
        id = Order.order_id
        return render(request, 'shop/success.html', {'thank':thank, 'id': id})

    return render(request, 'shop/checkout.html')
    
def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            Order = order.objects.filter(order_id=orderId, email=email)
            if len(Order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, Order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')


def contactUs(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'shop/thanks.html')
        else:
            messages.success(request, 'Must enter the correct email')
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'shop/contactUs.html', {'form': form})

def search(request):
        query = request.GET['query']
        products = product.objects.filter(product_name__icontains = query)
        context = {'products':products}
        return render(request, "shop/search.html", context)
