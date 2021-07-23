from django.db import models

# Create your models here.
class Comorbidity(models.Model):
    """Model definition for Comorbidity."""

    # TODO: Define fields here
    description = models.CharField(
        'Comorbidity',
        max_length=30,
        unique=True,
    )
    class Meta:
        """Meta definition for Comorbidity."""

        verbose_name = 'Comorbidity'
        verbose_name_plural = 'Comorbidities'

    def __str__(self):
        """Unicode representation of Comorbidity."""
        return self.description

class ExitStatus(models.Model):
    """Model definition for ExitStatus."""

    # TODO: Define fields here
    description = models.CharField(
        'Estado',
        max_length=50,
        unique=True,
        )
    class Meta:
        """Meta definition for ExitStatus."""

        verbose_name = 'Exit Status'
        verbose_name_plural = 'Exit Statuss'

    def __str__(self):
        """Unicode representation of ExitStatus."""
        return self.description

class PersonalHistory(models.Model):
     """Model definition for PersonalHistory."""
 
     # TODO: Define fields here
     description = models.CharField(
         'Antecedente Personal',
         max_length=30,
         unique=True
         )       
     class Meta:
         """Meta definition for PersonalHistory."""
 
         verbose_name = 'Personal History'
         verbose_name_plural = 'Personal Histories'
 
     def __str__(self):
         """Unicode representation of PersonalHistory."""
         return self.description

class Symptom(models.Model):
    """Model definition for Symptom."""

    # TODO: Define fields here
    description = models.CharField(
        'Symptom',
        max_length=50,
        unique=True
        )
    class Meta:
        """Meta definition for Symptom."""

        verbose_name = 'Symptom'
        verbose_name_plural = 'Symptoms'

    def __str__(self):
        """Unicode representation of Symptom."""
        return self.description
 

class LaboratoryAnalysis(models.Model):
    """Model definition for LaboratoryAnalysis."""

    # TODO: Define fields here
    description = models.CharField(
        'Nombre de análisis', max_length=30)
    

    class Meta:
        """Meta definition for LaboratoryAnalysis."""

        verbose_name = 'Laboratory Analysis'
        verbose_name_plural = 'Laboratory Analysis'

    def __str__(self):
        """Unicode representation of LaboratoryAnalysis."""
        return self.description

class UnitMeasurement(models.Model):
    """Model definition for UnitMeasurement."""

    # TODO: Define fields here
    unit = models.CharField(
        'unit',
        max_length=10,
        unique=True
        )
    description=models.CharField(
        'description',
        max_length=20,
        unique=True,
    )
    class Meta:
        """Meta definition for UnitMeasurement."""

        verbose_name = 'UnitMeasurement'
        verbose_name_plural = 'UnitMeasurements'

    def __str__(self):
        """Unicode representation of UnitMeasurement."""
        return self.unit

class Patient(models.Model):
    """Model definition for Patient."""
    SEX={
        'M':'Male',
        'F':'Femenine',
    }
    # TODO: Define fields here
    history_code = models.CharField(
        'History code',
        max_length=10,
        unique=True
        )
    sex = models.CharField(
        'sex',
        choices=SEX
        )
    age = models.PositiveSmallIntegerField(
        'age',
    )
    admission_date = models.DateField(
        'Admission date',
        auto_now=False,
        auto_now_add=False
        )
    departure_date = models.DateField(
        'Departure date',
        auto_now=False,
        auto_now_add=False
        )
    comorbidity = models.ManyToManyField(
        Comorbidity,
        on_delete=models.CASCADE
        )
    exit_status = models.ForeignKey(
        ExitStatus,
        on_delete=models.CASCADE
        )
    personal_history=models.ManyToManyField(
        PersonalHistory,
        on_delete=models.CASCADE,
    )
    symptom=models.ManyToManyField(
        Symptom,
        on_delete=models.CASCADE,
    )

    class Meta:
        """Meta definition for Patient."""

        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

    def __str__(self):
        """Unicode representation of Patient."""
        return self.history_code


class LaboratoryAnalysisDetail(models.Model):
    """Model definition for LaboratoryAnalysisDetail."""
    # TODO: Define fields here

    measure = models.FloatField(
        'measure',
    )
    laboratoryAnalisis = models.ForeignKey(
        LaboratoryAnalysis,
        on_delete=models.CASCADE
        )
    unitMeasurement = models.ForeignKey(
        UnitMeasurement,
        on_delete=models.CASCADE
        )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
    )
    class Meta:
        """Meta definition for LaboratoryAnalysisDetail."""

        verbose_name = 'Laboratory Analysis Detail'
        verbose_name_plural = 'Laboratory Analysis Details'

    def __str__(self):
        """Unicode representation of LaboratoryAnalysisDetail."""
        return f"{self.laboratoryAnalisis} {self.measure} {self.unitMeasurement} - Patient:{self.patient}"
