from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Product, Cart
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


def home(request):

    products = Product.objects.all()

    return render(request, 'home.html', {
        'products': products
    })

def signup(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        email = request.POST.get('email')

        password = request.POST.get('password')

        role = request.POST.get('role')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        if role == 'admin':
            user.is_staff = True
        else:
            user.is_staff = False

        user.save()

        return redirect('/login/')

    return render(request, 'signup.html')

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            auth_login(request, user)

            return redirect('/')

    return render(request, 'login.html')

def logout_view(request):

    logout(request)

    return redirect('/')


@login_required
def profile(request):

    return render(request, 'profile.html')

def add_product(request):

    if not request.user.is_staff:
        return redirect('/')

    if request.method == 'POST':

        name = request.POST['name']
        price = request.POST['price']
        category = request.POST['category']
        image = request.FILES['image']

        Product.objects.create(
            name=name,
            price=price,
            category=category,
            image=image
        )

        return redirect('/')

    return render(request, 'add_product.html')

@login_required
def cart(request):

    cart_items = Cart.objects.filter(
        user=request.user
    )

    return render(request, 'cart.html', {
        'cart_items': cart_items
    })    

@login_required
def remove_from_cart(request, cart_id):

    cart_item = Cart.objects.get(
        id=cart_id
    )

    cart_item.delete()

    return redirect('/cart/')    


@login_required
def delete_product(request, product_id):

    if not request.user.is_staff:
        return redirect('/')

    product = Product.objects.get(id=product_id)

    product.delete()

    return redirect('/')

def product_detail(request, product_id):

    product = Product.objects.get(id=product_id)

    return render(request, 'product_detail.html', {
        'product': product
    })

@login_required
def edit_product(request, product_id):

    if not request.user.is_staff:
        return redirect('/')

    product = Product.objects.get(id=product_id)

    if request.method == 'POST':

        product.name = request.POST['name']
        product.price = request.POST['price']
        product.category = request.POST['category']

        if request.FILES.get('image'):
            product.image = request.FILES['image']

        product.save()

        return redirect('/')

    return render(request, 'edit_product.html', {
        'product': product
    })

@login_required
def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)

    Cart.objects.create(
        user=request.user,
        product=product
    )

    return redirect('/cart/')