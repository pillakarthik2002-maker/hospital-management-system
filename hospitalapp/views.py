from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout

from hospitalapp.forms import (
    DoctorForm,
    CalendarForm,
    JobOpenForm,
    HealthTipsForm,
    HealthCampaignForm,
    AddAppointmentForm,
    PatientFeedbackForm,
    ContactForm
)

from hospitalapp.models import (
    Doctor,
    Calendar,
    HealthTips,
    JobOpen,
    HealthCampaign,
    AddAppointment,
    PatientFeedback,
    Contact
)

import csv


# =========================
# HOME
# =========================

def home_view(request):
    return render(request, 'home.html')


# =========================
# ADMIN ACCESS
# =========================

def admin_only(user):
    return user.is_superuser


@login_required
@user_passes_test(admin_only)
def doctor_view(request):
    return render(request, 'doctor.html')


# =========================
# PATIENT
# =========================

def patient_view(request):
    return render(request, 'patient.html')


# =========================
# LOGOUT
# =========================

def logout_view(request):
    logout(request)
    return redirect('/home/')


# =========================
# ADMIN - DOCTOR MANAGEMENT
# =========================

@login_required
@user_passes_test(admin_only)
def add_doctor_view(request):

    form = DoctorForm()

    if request.method == "POST":
        form = DoctorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/view_doctors/')

    return render(
        request,
        'add_doctor.html',
        {'form': form}
    )


@login_required
@user_passes_test(admin_only)
def view_doctors_view(request):

    doctors = Doctor.objects.all()

    return render(
        request,
        'view_doctors.html',
        {'doctors': doctors}
    )


@login_required
@user_passes_test(admin_only)
def download_doctors_view(request):

    response = HttpResponse(content_type='text/csv')

    response['Content-Disposition'] = (
        'attachment; filename="doctors.csv"'
    )

    data = Doctor.objects.all()

    writer = csv.writer(response)

    writer.writerow([
        'Name',
        'Specialization',
        'Email',
        'Phone Number'
    ])

    for doctor in data:
        writer.writerow([
            doctor.name,
            doctor.specialization,
            doctor.email,
            doctor.phone_number
        ])

    return response


@login_required
@user_passes_test(admin_only)
def update_doctor_view(request, id):

    doctor = Doctor.objects.get(id=id)

    if request.method == 'POST':

        form = DoctorForm(
            request.POST,
            instance=doctor
        )

        if form.is_valid():
            form.save()
            return redirect('/view_doctors/')

    else:
        form = DoctorForm(instance=doctor)

    return render(
        request,
        'update_doctor.html',
        {'form': form}
    )


@login_required
@user_passes_test(admin_only)
def delete_doctor_view(request, id):

    doctor = Doctor.objects.get(id=id)

    doctor.delete()

    return redirect('/view_doctors/')


# =========================
# ADMIN - JOB OPENINGS
# =========================

@login_required
@user_passes_test(admin_only)
def download_campaign_view(request):

    response = HttpResponse(content_type='text/csv')

    response['Content-Disposition'] = (
        'attachment; filename="data.csv"'
    )

    data = JobOpen.objects.all()

    writer = csv.writer(response)

    writer.writerow([
        'Role',
        'Experience',
        'Current CTC',
        'Notice Period'
    ])

    for job in data:

        writer.writerow([
            job.role,
            job.experience,
            job.current_ctc,
            job.notice_period
        ])

    return response


@login_required
@user_passes_test(admin_only)
def job_open_view(request):

    form = JobOpenForm()

    if request.method == 'POST':

        form = JobOpenForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/job_open_data/')

    return render(
        request,
        'job_open.html',
        {'form': form}
    )


@login_required
@user_passes_test(admin_only)
def job_open_data_view(request):

    job_open_data = JobOpen.objects.all()

    return render(
        request,
        'job_open_data.html',
        {'job_open_data': job_open_data}
    )


# =========================
# ADMIN - CALENDAR
# =========================

@login_required
@user_passes_test(admin_only)
def add_calendar_view(request):

    form = CalendarForm()

    if request.method == "POST":

        form = CalendarForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/view_calendar/')

    return render(
        request,
        'add_calendar.html',
        {'form': form}
    )


@login_required
@user_passes_test(admin_only)
def view_calendar_view(request):

    calendars = Calendar.objects.all()

    return render(
        request,
        'view_calendar.html',
        {'calendars': calendars}
    )


# =========================
# ADMIN - HEALTH TIPS
# =========================

@login_required
@user_passes_test(admin_only)
def health_tips_view(request):

    form = HealthTipsForm()

    if request.method == 'POST':

        form = HealthTipsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/health_tips_data/')

    return render(
        request,
        'health_tips.html',
        {'form': form}
    )


@login_required
@user_passes_test(admin_only)
def health_tips_data_view(request):

    health_tips = HealthTips.objects.all()

    return render(
        request,
        'health_tips_data_view.html',
        {'health_tips': health_tips}
    )


# =========================
# ADMIN - HEALTH CAMPAIGN
# =========================

@login_required
@user_passes_test(admin_only)
def health_campaign_view(request):

    form = HealthCampaignForm()

    if request.method == 'POST':

        form = HealthCampaignForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/health_campaign_data/')

    return render(
        request,
        'health_campaign.html',
        {'form': form}
    )


@login_required
@user_passes_test(admin_only)
def health_campaign_data_view(request):

    health_campaigns = HealthCampaign.objects.all()

    return render(
        request,
        'health_campaign_data.html',
        {'health_campaigns': health_campaigns}
    )


@login_required
@user_passes_test(admin_only)
def update_health_campaign_view(request, id):

    health_campaign = HealthCampaign.objects.get(id=id)

    if request.method == 'POST':

        form = HealthCampaignForm(
            request.POST,
            instance=health_campaign
        )

        if form.is_valid():
            form.save()
            return redirect('/health_campaign_data/')

    else:
        form = HealthCampaignForm(
            instance=health_campaign
        )

    return render(
        request,
        'update_health_campaign.html',
        {'form': form}
    )


# =========================
# ADMIN - APPOINTMENTS
# =========================

@login_required
@user_passes_test(admin_only)
def view_appointments_view(request):

    appointments = AddAppointment.objects.all()

    return render(
        request,
        'view_appointments.html',
        {'appointments': appointments}
    )


# =========================
# APPOINTMENT
# =========================

def add_appointment_view(request):

    form = AddAppointmentForm()

    if request.method == 'POST':

        form = AddAppointmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/thanks/')

    return render(
        request,
        'add_appointment.html',
        {'form': form}
    )


def thanks_view(request):

    return render(
        request,
        'thanks.html'
    )


# =========================
# PUBLIC INFORMATION
# =========================

def view_doctors_only(request):

    data = Doctor.objects.all()

    return render(
        request,
        'v_doctors.html',
        {'view': data}
    )


def view_calendar_only(request):

    data = Calendar.objects.all()

    return render(
        request,
        'v_calendar.html',
        {'view': data}
    )


def view_tips_only(request):

    data = HealthTips.objects.all()

    return render(
        request,
        'v_tips.html',
        {'tips': data}
    )


def view_jobs_only(request):

    data = JobOpen.objects.all()

    return render(
        request,
        'v_job.html',
        {'tips': data}
    )


def view_compaign_only(request):

    data = HealthCampaign.objects.all()

    return render(
        request,
        'v_campaign.html',
        {'tips': data}
    )


# =========================
# DOCTOR PAGE
# =========================
def doctors_view(request):

    doctor_id = request.session.get('doctor_id')

    if not doctor_id:
        return redirect('/doctor_login/')

    doctor = Doctor.objects.get(id=doctor_id)

    return render(
        request,
        'dc.html',
        {'doctor': doctor}
    )


# =========================
# DOCTOR PROFILE
# =========================

def view_profile(request):

    doctor = None

    if request.method == "POST":

        name = request.POST.get('name')

        doctor = Doctor.objects.filter(
            name__icontains=name
        )

    return render(
        request,
        'profiledata.html',
        {'doctor': doctor}
    )


# =========================
# DOCTOR APPOINTMENTS
# =========================

def show_my_appointment(request, name):

    appoint = AddAppointment.objects.filter(
        doctor_name__name__icontains=name
    )

    return render(
        request,
        'myapp.html',
        {'appoint': appoint}
    )


# =========================
# PATIENT FEEDBACK
# =========================

def review_view(request):

    form = PatientFeedbackForm()

    if request.method == 'POST':

        form = PatientFeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/thankspage/')

    return render(
        request,
        'revie.html',
        {'form': form}
    )

def reviewdata_view(request):

    data = PatientFeedback.objects.all()

    return render(
        request,
        'reviewdata.html',
        {'data': data}
    )


def thankspage(request):

    return render(
        request,
        'thankspage.html'
    )


# =========================
# CONTACT
# =========================

def contact_view(request):

    job_open_data = JobOpen.objects.all()

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/contact_thanks/')

    else:

        form = ContactForm()

    return render(
        request,
        'contact.html',
        {
            'form': form,
            'job_open_data': job_open_data
        }
    )


@login_required
@user_passes_test(admin_only)
def contactdata_form(request):

    data = Contact.objects.all()

    return render(
        request,
        'contactdata.html',
        {'data': data}
    )


def contact_thanks(request):

    return render(
        request,
        'contact_thanks.html'
    )


# =========================
# DOCTOR LOGIN
# =========================

def doctor_login_view(request):

    message = ''

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        doctor = Doctor.objects.filter(
            username=username,
            password=password
        ).first()

        if doctor:

            request.session['doctor_id'] = doctor.id

            return redirect('/doctor_dashboard/')

        else:

            message = 'Invalid username or password.'

    return render(
        request,
        'doctor_login.html',
        {'message': message}
    )


# =========================
# DOCTOR DASHBOARD
# =========================

def doctor_dashboard_view(request):

    doctor_id = request.session.get('doctor_id')

    if not doctor_id:
        return redirect('/doctor_login/')

    doctor = Doctor.objects.get(id=doctor_id)

    appointments = AddAppointment.objects.filter(
        doctor_name=doctor
    )

    return render(
        request,
        'doctor_dashboard.html',
        {
            'doctor': doctor,
            'appointments': appointments
        }
    )


# =========================
# DOCTOR LOGOUT
# =========================

def doctor_logout_view(request):

    request.session.flush()

    return redirect('/doctor_login/')