from django.http import HttpResponse, Http404
from django.shortcuts import render
from webshop.models import Product

def starting_instructions(request):
    return render(request, "webshop/instructions.html", {})

def about(request):
    return HttpResponse("about page")

def productview(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    r = render (request, 'webshop/product_view.html', {'product': product}, content_type='application/xhtml+xml')

    return HttpResponse(r)

def available_products(request):
    try:
        products = Product.objects.filter(quantity__gt=0)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    r = render (request, 'webshop/product_list.html', {'products': products}, content_type='application/xhtml+xml')

    return HttpResponse(r)
