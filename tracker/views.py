from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Application
from .forms import ApplicationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('application_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def application_list(request):
    applications = Application.objects.filter(user=request.user).order_by('-applied_date')
    return render(request, 'tracker/application_list.html', {'applications': applications})

@login_required
def add_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('application_list')
    else:
        form = ApplicationForm()
    return render(request, 'tracker/add_application.html', {'form': form})

@login_required
def edit_application(request, pk):
    application = get_object_or_404(Application, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('application_list')
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'tracker/add_application.html', {'form': form})

@login_required
def delete_application(request, pk):
    application = get_object_or_404(Application, pk=pk, user=request.user)
    if request.method == 'POST':
        application.delete()
        return redirect('application_list')
    return render(request, 'tracker/confirm_delete.html', {'application': application})

@login_required
def dashboard(request):
    applications = Application.objects.filter(user=request.user)
    context = {
        'total': applications.count(),
        'applied': applications.filter(status='applied').count(),
        'interview': applications.filter(status='interview').count(),
        'offer': applications.filter(status='offer').count(),
        'rejected': applications.filter(status='rejected').count(),
        'recent': applications.order_by('-applied_date')[:5],
    }
    return render(request, 'tracker/dashboard.html', context)