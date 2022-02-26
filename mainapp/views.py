from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Product, Cart, CartProduct, Order
from django.http import JsonResponse
from .forms import OrderForm
from django.contrib import messages


def count_cart_products(request):
    return get_cart(request).products.count()


def get_cart(request):

    cart, created = Cart.objects.get_or_create(
        user=request.session.session_key,
        ordered=False
    )
    return cart


class MainPage(View):

    def get(self, request, *args, **kwargs):

        if not request.session.exists(request.session.session_key):
            request.session.create()

        cart = get_cart(request)
        products = Product.objects.all()

        return render(request, 'main_page.html', {
            'products': products,
            'cart': [i.product.name for i in cart.products.all()],
            'cart_counter': count_cart_products(request)
        })

class CatalogueView(View):

    def get(self, request, *args, **kwargs):

        if not request.session.exists(request.session.session_key):
            request.session.create()

        cart = get_cart(request)
        products = Product.objects.all()

        return render(request, 'catalogue.html', {
            'products': products,
            'cart': [i.product.name for i in cart.products.all()],
            'cart_counter': count_cart_products(request)
        })

class CartView(View):

    def get(self, request, *args, **kwargs):

        form = OrderForm

        cart = get_cart(request)
        products = cart.products.all()
        total = cart.get_sum()

        return render(request, 'cart.html', {
            'cart': cart,
            'products': products,
            'cart_counter': count_cart_products(request),
            'total': total,
            'form': form
        })

    def post(self, request, *args, **kwargs):

        form = OrderForm(request.POST)
        cart = get_cart(request)
        products = cart.products.all()

        response = render(request, 'cart.html', {
                'cart': cart,
                'products': products,
                'cart_counter': count_cart_products(request),
                'form': form
            })

        if not products:
            messages.error(request, 'Выберите хотя бы один товар')
            return response

        if form.is_valid():
            cart = get_cart(request)
            new_form = form.save(commit=False)
            new_form.cart = cart
            cart.ordered = True
            cart.save()
            form.save()
            return redirect('/')
        else:
            messages.error(request, 'Ошибка при заполнении формы')
            return response


class AddProduct(View):

    def get(self, request, *args, **kwargs):
        product = self.request.GET.get('product') or None
        if product:
            product = Product.objects.get(id=product)
            cart_product, created = CartProduct.objects.get_or_create(
                product=product,
                count=1
            )
            cart = get_cart(request)
            if cart:
                cart.products.add(cart_product)
                return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error'})


class ChangeCartProduct(View):

    def get(self, request, *args, **kwargs):
        actions = ['change_val', 'remove']

        cart_product = self.request.GET.get('cart_product') or None
        action = self.request.GET.get('action') or None
        value = self.request.GET.get('value') or None
        if value and value.isdigit():
            value = int(value)
        else:
            value = None

        cart_product = CartProduct.objects.filter(id=cart_product)
        if cart_product.exists():
            cart_product = cart_product.first()
        else:
            return JsonResponse({'error': 'invalid cart product'})
        if cart_product not in get_cart(request).products.all():
            return JsonResponse({'error': 'permission denied'})
        if action not in actions:
            return JsonResponse({'error': 'invalid action'})

        response = {'status': '.', 'value': '1'}

        if cart_product and action:
            if action == 'change_val' and value:
                if value < 1:
                    cart_product.count = 1
                elif 1 <= value <= cart_product.product.count:
                    cart_product.count = value
                else:
                    cart_product.count = cart_product.product.count
                cart_product.save()
                response['value'] = cart_product.count


            elif action == 'remove':
                cart_product.delete()
            response['total'] = get_cart(request).get_sum()
            response['status'] = 'success'
            return JsonResponse(response)
        response['status'] = 'error'
        response['value'] = 1
        return JsonResponse(response)