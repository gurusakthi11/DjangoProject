from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # SAVE ROLE
        user.profile.role = role
        user.profile.save()

        return redirect('login')

    return render(request, 'signup.html')