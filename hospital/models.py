from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Ward(models.Model):
    name = models.CharField(max_length=50)
    ward_type = models.CharField(max_length=20)
    capacity = models.IntegerField()
    availability = models.IntegerField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    dob = models.DateField()
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=100, blank=True)
    prescription = models.CharField(max_length=100, blank=True)
    test_results = models.CharField(max_length=100, blank=True)
    visit_date = models.DateField()

class Payment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=20, blank=True)

class Admission(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    admission_date = models.DateField()
    discharge_date = models.DateField(blank=True, null=True)
