from django.contrib import admin

from hospitalapp.models import (
    Calendar,
    Doctor,
    JobOpen,
    HealthTips,
    HealthCampaign,
    AddAppointment,
    PatientFeedback,
    Contact
)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'specialization',
        'email',
        'phone_number'
    )

    search_fields = (
        'name',
        'specialization',
        'email'
    )


@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'date'
    )

    search_fields = (
        'title',
    )


@admin.register(JobOpen)
class JobOpenAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'role',
        'experience',
        'current_ctc',
        'notice_period'
    )

    search_fields = (
        'role',
    )


@admin.register(HealthTips)
class HealthTipsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title'
    )

    search_fields = (
        'title',
        'content'
    )


@admin.register(HealthCampaign)
class HealthCampaignAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'date'
    )

    search_fields = (
        'title',
        'content'
    )


@admin.register(AddAppointment)
class AddAppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'patient_name',
        'doctor_name',
        'appointment_date',
        'appointment_time'
    )

    search_fields = (
        'patient_name',
        'doctor_name__name'
    )


@admin.register(PatientFeedback)
class PatientFeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'patient_name',
        'doctor_name',
        'rating',
        'date'
    )

    search_fields = (
        'patient_name',
        'doctor_name'
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'phone_number',
        'subject',
        'date'
    )

    search_fields = (
        'name',
        'email',
        'subject'
    )