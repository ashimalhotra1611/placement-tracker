from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['company', 'role', 'status', 'applied_date', 'interview_date', 'notes']
        widgets = {
            'applied_date': forms.DateInput(attrs={'type': 'date'}),
            'interview_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ResumeMatchForm(forms.Form):
    resume = forms.FileField(label='Resume (PDF)')
    job_description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 8}),
        label='Job description',
    )

    def clean_resume(self):
        f = self.cleaned_data['resume']
        if not f.name.lower().endswith('.pdf'):
            raise forms.ValidationError('Sirf PDF file upload karo.')
        if f.size > 5 * 1024 * 1024:
            raise forms.ValidationError('File 5 MB se chhoti honi chahiye.')
        return 