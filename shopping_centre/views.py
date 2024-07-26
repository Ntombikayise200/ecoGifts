from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from .models import Product, Cart, Wishlist, Order, Review, DiscountCode, ProductImage
from .forms import CheckoutForm, CustomLoginForm, UserRegisterForm

from django.contrib.auth import login as auth_login
def product_list(request):
    """View to list all products with optional category filtering."""
    products = Product.objects.all()
    category = request.GET.get('category')
    if category:
        products = products.filter(category__name=category)
    return render(request, 'product_list.html', {'products': products})

def home(request):
    
    return render(request, 'base.html')
def product_detail(request, pk):
    """View to show details of a specific product, including reviews and images."""
    product = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=product)
    images = ProductImage.objects.filter(product=product)
    return render(request, 'product_detail.html', {'product': product, 'reviews': reviews, 'images': images})

@login_required
def cart(request):
    """View to display items in the user's cart and calculate the total cost."""
    cart_items = Cart.objects.filter(user=request.user)
    total_cost = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_cost': total_cost})

@login_required
def wishlist(request):
    """View to display items in the user's wishlist."""
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

def checkout(request):
    """View to handle the checkout process with payment and order processing."""
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Handle payment and order processing here
            # For example, create an order and send a confirmation email
            return redirect('order_confirmation')
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form})

def search(request):
    """View to handle product search based on query."""
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'products': products})

def signup(request):
    """View to handle user registration and login after successful signup."""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('product_list')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})


def custom_login(request):
    """View to handle user login with a custom form."""
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect('product_list')  # Redirect to a page after login
    else:
        form = CustomLoginForm()
    
    return render(request, 'login.html', {'form': form})

