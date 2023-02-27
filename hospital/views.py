from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from .models import Patient
from .forms import PatientForm


def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient added successfully.')
            return redirect('patient_management')
    else:
        form = PatientForm()
    return render(request, 'add_patient.html', {'form': form})



def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'dashboard.html', locals())


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            error_message = "Login Successful"
            return render(request, 'dashboard.html', locals())
        else:
            error_message = "Invalid Username or Password"
            return render(request,'login.html', locals())
    return render(request,'login.html', locals())
    
        



@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'dashboard.html', locals())

@login_required(login_url='/login/')
def patient(request):
   
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Create and save a new patient object
        patient = Patient(name=name, gender=gender, dob=dob, address=address, phone=phone, email=email)
        patient.save()

        # Redirect to a success page
        return render(request, 'patient.html', locals())
    return render(request, 'patient.html', locals())

def patient_update(request, id):

    if not request.user.is_authenticated:
        return redirect('login')
    
    patient_update = Patient.objects.get(id = id)
    print('-------------------------------',patient_update, '------------------------')
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Create and save a new patient object
        patient = Patient(name=name, gender=gender, dob=dob, address=address, phone=phone, email=email)
        patient.save()

        # Redirect to a success page
        return render(request, 'patient update.html', locals())
    return render(request, 'patient update.html', locals())


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')