from django import forms

from .models import (
    Doctor,
    Calendar,
    JobOpen,
    HealthTips,
    HealthCampaign,
    AddAppointment,
    PatientFeedback,
    Contact
)


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter doctor name'
            }),
            'specialization': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter specialization'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),
        }


class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter event title'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }


class JobOpenForm(forms.ModelForm):
    class Meta:
        model = JobOpen
        fields = '__all__'

        widgets = {
            'role': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job role'
            }),
            'experience': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Years of experience'
            }),
            'current_ctc': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter CTC'
            }),
            'notice_period': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter notice period'
            }),
        }


class HealthTipsForm(forms.ModelForm):
    class Meta:
        model = HealthTips
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter health tip title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter health tip'
            }),
        }


class HealthCampaignForm(forms.ModelForm):
    class Meta:
        model = HealthCampaign
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter campaign title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter campaign details'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }


class AddAppointmentForm(forms.ModelForm):
    doctor_name = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        empty_label="Select Doctor"
    )

    class Meta:
        model = AddAppointment
        fields = [
            'patient_name',
            'doctor_name',
            'appointment_date',
            'appointment_time'
        ]

        widgets = {
            'patient_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter patient name'
            }),
            'appointment_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'appointment_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['doctor_name'].widget.attrs.update({
            'class': 'form-control'
        })


class PatientFeedbackForm(forms.ModelForm):
    class Meta:
        model = PatientFeedback
        fields = '__all__'

        widgets = {
            'patient_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter patient name'
            }),
            'doctor_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter doctor name'
            }),
            'feedback': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Write your feedback'
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 5,
                'placeholder': 'Rating 1-5'
            }),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter your message'
            }),
        }