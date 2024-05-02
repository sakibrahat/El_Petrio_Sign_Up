from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse


from django.shortcuts import render, redirect
from .forms import PetForm
from .models import Pet

#pricing page defining

def pricing(request):
    return render(request, 'pricing.html')

def buying(request):
    pets = Pet.objects.filter(is_sold=False)
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('buying')
    return render(request, 'Buying.html', {'form': form, 'pets': pets})

def make_payment(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    if request.method == 'POST':
        pet.is_sold = True
        pet.save()
        return redirect('buying')
    return render(request, 'make_payment.html', {'pet': pet})


def make_payment(request):
    pet_id = request.GET.get('pet_id')
    return HttpResponse("Payment successful")




@login_required(login_url='login')
def homepage(request):
    return render(request, 'home.html')


def signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def logoutpage(request):
    logout(request)
    return redirect('login')


def userpage(request):
    return render(request, 'user.html')


def servicepage(request, form=None):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        gender = request.POST.get('gender')
        pet = request.POST.get('pet')
        special_marks = request.POST.get('special_marks')
        breed = request.POST.get('breed')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        terms_condition = request.POST.get('term_condition')
    return render(request, 'service.html')


def servicespage(request):
    return render(request, 'newservices.html')

def Adoption(request):
    return render(request, 'Adoption.html')



def buying_page(request):
    return render(request, 'Buying.html')
    # Get parameters from the request, if any
    query = request.GET.get('query')
    min_age = request.GET.get('min_age')
    max_age = request.GET.get('max_age')
    location = request.GET.get('location')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Filter pets based on parameters
    pets = Pet.objects.all()
    if query:
        pets = pets.filter(breed__icontains=query)
    if min_age:
        pets = pets.filter(age__gte=min_age)
    if max_age:
        pets = pets.filter(age__lte=max_age)
    if location:
        pets = pets.filter(location__icontains=location)
    if min_price:
        pets = pets.filter(price__gte=min_price)
    if max_price:
        pets = pets.filter(price__lte=max_price)

    context = {
        'pets': pets,
    }
    return render(request, 'homepage/buying_page.html', context)



def pet_buying_page(request):
    query = request.GET.get('q')
    pets = Pet.objects.all()

    if query:
        pets = pets.filter(breed__icontains=query)  
    context = {
        'pets': pets,
        'query': query
    }
    return render(request, 'Buying.html', context)



