from django.contrib import admin
from .models import *


admin.site.site_header = 'My Hospital'
admin.site.site_title = 'My Hospital administration'
admin.site.index_title = "Welcome to MY Hospital Administration"

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display= ('name',)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display= ('name', 'job_title', 'department', 'address', 'phone', 'email')

@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display= ('name', 'ward_type', 'capacity', 'availability')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display= ('name', 'gender', 'dob', 'address', 'phone', 'email')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display= ('name', 'speciality', 'address', 'phone', 'email')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display= ('patient', 'doctor', 'appointment_date', 'appointment_time')

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display= ('patient', 'doctor', 'diagnosis', 'prescription', 'test_results', 'visit_date')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display= ('patient', 'payment_amount', 'payment_date', 'payment_method')

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display= ('patient', 'ward', 'admission_date', 'discharge_date')


