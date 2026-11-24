from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Application
from .forms import ApplicationForm, ResumeMatchForm
from .matcher import extract_text, match_resume


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
    applications = Application.objects.filter(user=request.user)

    q = request.GET.get('q', '').strip()
    status = request.GET.get('status', '')

    if q:
        applications = applications.filter(Q(company__icontains=q) | Q(role__icontains=q))
    if status:
        applications = applications.filter(status=status)

    applications = applications.order_by('-applied_date')
    return render(request, 'tracker/application_list.html', {
        'applications': applications,
        'q': q,
        'status': status,
        'status_choices': Application.STATUS_CHOICES,
    })


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


@login_required
def resume_matcher(request):
    result = None
    error = None
    if request.method == 'POST':
        form = ResumeMatchForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                resume_text = extract_text(form.cleaned_data['resume'])
            except Exception:
                resume_text = ''
            if not resume_text.strip():
                error = 'Resume se text nahi nikal paya. Text wali PDF upload karo (scan ya image wali nahi).'
            else:
                percent, matched, missing, total = match_resume(
                    resume_text, form.cleaned_data['job_description']
                )
                result = {
                    'percent': percent,
                    'matched': matched,
                    'missing': missing,
                    'total': total,
                }
    else:
        form = ResumeMatchForm()
    return render(request, 'tracker/resume_matcher.html', {
        'form': form,
        'result': result,
        'error': error,
    })