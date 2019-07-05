from django.db import models
from django.utils.timezone import now
from datetime import datetime


# Create your models here.
class Company(models.Model):
    class Meta:
        verbose_name_plural = 'Companies'
    company_shortname       = models.CharField(max_length=20)
    company_longname        = models.CharField(max_length=50)
    company_registration    = models.CharField(max_length=25)
    company_addressline1    = models.CharField(max_length=30)
    company_addressline2    = models.CharField(max_length=30)
    company_addressline3    = models.CharField(max_length=30)
    company_addressline4    = models.CharField(max_length=30)
    company_state           = models.CharField(max_length=10)
    company_postalcode      = models.CharField(max_length=10)
    company_country         = models.CharField(max_length=10)
    company_default         = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=False)
    created_date            = models.DateTimeField(default=datetime.now(), blank=True)


    def __str__(self):
        return self.company_shortname


class Branch(models.Model):
    class Meta:
        verbose_name_plural = 'Branches'
    branch_shortname = models.CharField(max_length=20)
    branch_longname = models.CharField(max_length=50)
    branch_addressline1 = models.CharField(max_length=30)
    branch_addressline2 = models.CharField(max_length=30)
    branch_addressline3 = models.CharField(max_length=30)
    branch_addressline4 = models.CharField(max_length=30)
    branch_state = models.CharField(max_length=10)
    branch_postalcode = models.CharField(max_length=10)
    branch_country = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.branch_shortname

class Project(models.Model):
    class Meta:
        verbose_name_plural = 'Projects'

    project_title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    company = models.CharField(max_length=10)
    project_cat = models.CharField(max_length=20, blank=True, null=False)
    create_by = models.CharField(max_length=20, blank=True, null=False)
    create_at = models.DateTimeField(default=now, blank=True)
    modify_by = models.CharField(max_length=20, blank=True, null=False)
    modify_at = models.DateTimeField(default=now, blank=True)
    company = models.ForeignKey('Company', null=True, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField('active', default=True)

    def __str__(self):
        return self.project_title

class Phase(models.Model):
    class Meta:
        verbose_name_plural = 'Phases'

    phase_shortname = models.CharField(max_length=20)
    phase_longname = models.CharField(max_length=50)
    phase_project = models.ForeignKey('Project', null=True, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.phase_shortname

class Block(models.Model):
    class Meta:
        verbose_name_plural = 'Blocks'

    block_shortname = models.CharField(max_length=20)
    block_longname = models.CharField(max_length=50)
    block_prefix = models.CharField(max_length=1)
    block_project = models.ForeignKey('Project', null=True, blank=True, on_delete=models.CASCADE)
    block_phase = models.ForeignKey('Phase', null=True, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.block_shortname

class Floortype(models.Model):
    class Meta:
        verbose_name_plural = 'Floortypes'

    floortype = models.CharField(max_length=2)
    floor_shortname = models.CharField(max_length=20)
    floor_size = models.CharField(max_length=50)
    block_prefix = models.CharField(max_length=1)
    block_project = models.ForeignKey('Project', null=True, blank=True, on_delete=models.CASCADE)
    block_phase = models.ForeignKey('Phase', null=True, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.floor_shortname

class Purchaser(models.Model):
    class Meta:
        verbose_name_plural = 'Purchasers'

    purchaser_name           = models.CharField(max_length=50)
    purchaser_nric           = models.CharField(max_length=30)
    purchaser_email          = models.CharField(max_length=50)
    purchaser_contact_number = models.CharField(max_length=20)
    purchaser_bod            = models.DateField()
    citizen                  = models.CharField(max_length=20)
    sex                      = models.CharField(max_length=10)
    race                     = models.CharField(max_length=15)
    occupation               = models.CharField(max_length=30)
    monthly_income           = models.DecimalField(max_digits=8, decimal_places=2)
    marital_status           = models.CharField(max_length=10)

    def __str__(self):
        return self.purchaser_name


class Property(models.Model):
    class Meta:
        verbose_name_plural = 'Properties'

    property_project = models.ForeignKey('Project', null=True, blank=True, on_delete=models.CASCADE)
    property_phase = models.ForeignKey('Phase', null=True, blank=True, on_delete=models.CASCADE)
    property_unit = models.CharField(max_length=10)
    property_row = models.DecimalField(max_digits=6, decimal_places=2)
    property_size = models.DecimalField(max_digits=6, decimal_places=2)
    property_price = models.DecimalField(max_digits=12, decimal_places=2)
    property_bookingstatus = models.CharField(max_length=10)

    def __str__(self):
        return self.property_unit



