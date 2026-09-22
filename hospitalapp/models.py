from django.db import models


class Doctor(models.Model):
    username = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=100,default='')

    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Calendar(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField()

    def __str__(self):
        return self.title


class JobOpen(models.Model):
    role = models.CharField(max_length=50)
    experience = models.IntegerField()
    current_ctc = models.DecimalField(max_digits=10, decimal_places=2)
    notice_period = models.CharField(max_length=30)

    def __str__(self):
        return self.role


class HealthTips(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class HealthCampaign(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.title


class AddAppointment(models.Model):
    patient_name = models.CharField(max_length=100)
    doctor_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return self.patient_name


class PatientFeedback(models.Model):
    patient_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    feedback = models.TextField()
    rating = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.patient_name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name