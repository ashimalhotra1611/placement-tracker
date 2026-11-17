from django.shortcuts import render, redirect, get_object_or_404
from .models import Application
from .forms import ApplicationForm

def application_list(request):
    applications = Application.objects.all().order_by('-applied_date')
    return render(request, 'tracker/application_list.html', {'applications': applications})

def add_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('application_list')
    else:
        form = ApplicationForm()
    return render(request, 'tracker/add_application.html', {'form': form})

def edit_application(request, pk):
    application = get_object_or_404(Application, pk=pk)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('application_list')
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'tracker/add_application.html', {'form': form})

def delete_application(request, pk):
    application = get_object_or_404(Application, pk=pk)
    if request.method == 'POST':
        application.delete()
        return redirect('application_list')
    return render(request, 'tracker/confirm_delete.html', {'application': application})