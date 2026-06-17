from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from product.models import Product

class CartDetailView(View):
    def get(self, request):
        return render(request, 'cart/cart_detail.html', {})
    

class CartAddView(View):
    def post(self, request,pk):
        product = get_object_or_404(Product, id=pk)
        size, color, quantity = request.POST.get('size'), request.POST.get('color'),  request.POST.get('quantity')
        return redirect('cart:cart_detail')