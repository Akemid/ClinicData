from django.contrib import admin
from .models import (
    Comorbidity,
    ExitStatus,
    Patient,
    LaboratoryAnalysis,
    LaboratoryAnalysisDetail,
    PersonalHistory,
    Symptom,
    UnitMeasurement,
)
# Register your models here.
@admin.register(Comorbidity)
class ComorbidityAdmin(admin.ModelAdmin):
    '''Admin View for Comorbidity'''

    list_display = (
        'id',
        'description',
        )
    search_fields = (
        'id',
        'description',
        )
@admin.register(ExitStatus)
class ExitStatusAdmin(admin.ModelAdmin):
    '''Admin View for ExitStatus'''

    list_display = (
        'id',
        'description',
        )
    search_fields = (
        'id',
        'description',
        )

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    '''Admin View for Patient'''

    list_display = (
        'history_code',
        'sex',
        'age',
        'admission_date',
        'departure_date',
        'exit_status',
        )
    list_filter = (
        'sex',
        'age',
        'comorbidity',
        'exit_status',
        'personal_history',
        'symptom',
        )
    search_fields = (
        'history_code',
        )

@admin.register(LaboratoryAnalysis)
class LaboratoryAnalysisAdmin(admin.ModelAdmin):
    '''Admin View for LaboratoryAnalysis'''

    list_display = (
        'id',
        'description',
        )
    search_fields = (
        'id',
        'description',
        )

@admin.register(LaboratoryAnalysisDetail)
class LaboratoryAnalysisDetailAdmin(admin.ModelAdmin):
    '''Admin View for LaboratoryAnalysisDetail'''

    list_display = (
        'id',
        'measure',
        'laboratoryAnalisis',
        'unitMeasurement',
        'patient',
        )
    list_filter = (
        'laboratoryAnalisis',
        'patient',
        )
    search_fields = (
        'id',
        )

@admin.register(PersonalHistory)
class PersonalHistoryAdmin(admin.ModelAdmin):
    '''Admin View for PersonalHistory'''

    list_display = (
        'id',
        'description',
        )
    search_fields = (
        'id',
        'description',
        )

@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    '''Admin View for Symptom'''

    list_display = (
        'id',
        'description',
        )
    search_fields = (
        'id',
        'description',
        )

@admin.register(UnitMeasurement)
class UnitMeasurementAdmin(admin.ModelAdmin):
    '''Admin View for UnitMeasurement'''

    list_display = (
        'id',
        'unit',
        'description',
        )
    search_fields = (
        'id',
        'unit',
        'description',
        )