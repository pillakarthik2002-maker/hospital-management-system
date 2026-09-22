from django.contrib import admin
from django.urls import path, include

from hospitalapp import views


urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Home
    path('home/', views.home_view),

    # Main sections
    path('doctor/', views.doctor_view),
    path('patient/', views.patient_view),

    # Authentication
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view),

    # Doctor Management
    path('add_doctor/', views.add_doctor_view),
    path('view_doctors/', views.view_doctors_view),
    path('download/', views.download_doctors_view),
    path('downladcamp/', views.download_campaign_view),

    path(
        'update_doctor/<int:id>/',
        views.update_doctor_view
    ),

    path(
        'delete_doctor/<int:id>/',
        views.delete_doctor_view
    ),

    # Calendar
    path('add_calendar/', views.add_calendar_view),
    path('view_calendar/', views.view_calendar_view),

    # Job Openings
    path('job_open/', views.job_open_view),
    path('job_open_data/', views.job_open_data_view),

    # Health Tips
    path('health_tips/', views.health_tips_view),
    path('health_tips_data/', views.health_tips_data_view),

    # Health Campaign
    path('health_campaign/', views.health_campaign_view),
    path(
        'health_campaign_data/',
        views.health_campaign_data_view
    ),

    path(
        'update_health_campaign/<int:id>/',
        views.update_health_campaign_view
    ),

    # Appointments
    path('add_appointment/', views.add_appointment_view),
    path('view_appointments/', views.view_appointments_view),
    path('thanks/', views.thanks_view),

    # Public Information
    path('viewdoctors/', views.view_doctors_only),
    path('viewcalendar/', views.view_calendar_only),
    path('viewtips/', views.view_tips_only),
    path('viewjobs/', views.view_jobs_only),
    path('viewcampaign/', views.view_compaign_only),

    # Doctor Dashboard
    path('doc/', views.doctors_view),
    path('viewprofile/', views.view_profile),

    path(
        'myappointment/<str:name>/',
        views.show_my_appointment,
        name='myappointment'
    ),

    # Patient Feedback
    path('review/', views.review_view),
    path('reviewdata/', views.reviewdata_view),
    path('thankspage/', views.thankspage),

    # Contact
    path('contact/', views.contact_view),
    path('contactformdata/', views.contactdata_form),
    path('contact_thanks/', views.contact_thanks),

    path('doctor_login/', views.doctor_login_view),
    path('doctor_dashboard/', views.doctor_dashboard_view),
    path('doctor_logout/', views.doctor_logout_view),
]