from django.db import models

# Create your models here.

class Base(models.Model):
    is_active = models.BooleanField(default=True)
    deactivation_reason = models.CharField(max_length=256, blank=True, null=True, default=None)
    is_suspended = models.BooleanField(default=False)
    suspension_reason = models.CharField(max_length=256, blank=True, null=True, default=None)
    is_audit_required = models.BooleanField(default=False)
    created_by = models.CharField(max_length=200, blank=True, null=True, default=None, editable=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_by = models.CharField(max_length=200, blank=True, null=True, default=None, editable=False)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)


    class Meta:
        abstract = True


class LanguageMaster(Base):
    language_id = models.CharField(max_length=16, blank=True, null=True, editable=False, unique=True)
    language_name = models.CharField(max_length=128, null= True, blank=True, default = None)

    class Meta:
        db_table = 'dbo_m_language'
        verbose_name = "Language Master"
        verbose_name_plural = "Language Master"

    def save(self, **kwargs):
        super(LanguageMaster, self).save(**kwargs)
        self.language_id = 'LM%05d' % self.pk
        LanguageMaster.objects.filter(pk=self.pk).update(language_id=self.language_id)

    def __str__(self):
        return str(self.language_name)



class ServiceTypeMaster(Base):
    service_type_id = models.CharField(max_length=16, blank=True, null=True, editable=False, unique=True)
    service_name = models.CharField(max_length=128, null= True, blank=True, default = None)

    class Meta:
        db_table = 'dbo_m_ServiceType'
        verbose_name = "Service Type Master"
        verbose_name_plural = "Service Type Master"

    def save(self, **kwargs):
        super(ServiceTypeMaster, self).save(**kwargs)
        self.service_type_id = 'STM%05d' % self.pk
        ServiceTypeMaster.objects.filter(pk=self.pk).update(service_type_id=self.service_type_id)

    def __str__(self):
        return str(self.service_name)



class EmergencyTypeMaster(Base):
    emergency_type_id = models.CharField(max_length=16, blank=True, null=True, editable=False, unique=True)
    emergency_type_name = models.CharField(max_length=128, null= True, blank=True, default = None)

    class Meta:
        db_table = 'dbo_m_EmergencyType'
        verbose_name = "Emergency Type Master"
        verbose_name_plural = "Emergency Type Master"

    def save(self, **kwargs):
        super(EmergencyTypeMaster, self).save(**kwargs)
        self.emergency_type_id = 'ETM%05d' % self.pk
        EmergencyTypeMaster.objects.filter(pk=self.pk).update(emergency_type_id=self.emergency_type_id)

    def __str__(self):
        return str(self.emergency_type_name)



class ServiceMaster(Base):
    service_id = models.CharField(max_length=16, blank=True, null=True, editable=False, unique=True)
    service_name = models.CharField(max_length=128, null= True, blank=True, default = None)
    service_type = models.ForeignKey(ServiceTypeMaster, to_field="service_type_id", on_delete=models.CASCADE, null= True, blank=True, default = None)
    emergency_category = models.ForeignKey(EmergencyTypeMaster,to_field="emergency_type_id", on_delete=models.CASCADE, null= True, blank=True, default = None)

    class Meta:
        db_table = 'dbo_m_Service'
        verbose_name = "Service Master"
        verbose_name_plural = "Service Master"

    def save(self, **kwargs):
        super(ServiceMaster, self).save(**kwargs)
        self.service_id = 'SM%05d' % self.pk
        ServiceMaster.objects.filter(pk=self.pk).update(service_id=self.service_id)

    def __str__(self):
        return str(self.service_name)


class TeamMaster(Base):
    team_id = models.CharField(max_length=16, blank=True, null=True, editable=False, unique=True)
    team_name = models.CharField(max_length=128, null= True, blank=True, default = None)
    single_skilled = models.BooleanField(default=True)
    parent_team = models.ForeignKey('self',to_field="team_id", on_delete=models.CASCADE, null= True,
                                             blank=True, default=None)

    class Meta:
        db_table = 'dbo_m_Team'
        verbose_name = "Team Master"
        verbose_name_plural = "Team Master"

    def save(self, **kwargs):
        super(TeamMaster, self).save(**kwargs)
        self.team_id = 'EM%05d' % self.pk
        TeamMaster.objects.filter(pk=self.pk).update(team_id=self.team_id)

    def __str__(self):
        return str(self.team_name)


class EmployeeMaster(Base):
    employee_id = models.CharField(max_length=16, blank=True, null=True, editable=False, unique=True)
    employee_name = models.CharField(max_length=128, null= True, blank=True, default = None)
    contact_no = models.CharField(max_length=10, null= True, blank=True, default = None)
    alernate_contact_no = models.CharField(max_length=10, null= True, blank=True, default = None)
    address = models.CharField(max_length=200, null= True, blank=True, default = None)
    languages_known = models.ManyToManyField(LanguageMaster, null= True, blank=True, default = None)
    services = models.ForeignKey(ServiceMaster,to_field="service_id", on_delete=models.CASCADE, null= True, blank=True, default = None)
    reporting_to = models.ForeignKey('self',to_field="employee_id", on_delete=models.CASCADE, null= True,
                                             blank=True, default=None)
    team = models.ManyToManyField(TeamMaster, null= True, blank=True, default = None)

    class Meta:
        db_table = 'dbo_m_Employee'
        verbose_name = "Employee Master"
        verbose_name_plural = "Employee Master"

    def save(self, **kwargs):
        super(EmployeeMaster, self).save(**kwargs)
        self.employee_id = 'EM%05d' % self.pk
        EmployeeMaster.objects.filter(pk=self.pk).update(employee_id=self.employee_id)

    def __str__(self):
        return str(self.employee_name)

    def display_languages_known(self):
        return ', '.join([other.title for other in self.languages_known.all()])

    display_languages_known.short_description = 'languages_known'
    display_languages_known.allow_tags = True

    def display_team(self):
        return ', '.join([other.title for other in self.team.all()])

    display_team.short_description = 'team'
    display_team.allow_tags = True



class LocationTypeMaster(Base):
    location_type_id = models.CharField(max_length=16, blank=True, null=True, editable=False, unique=True)
    location_type = models.CharField(max_length=128, null= True, blank=True, default = None)

    class Meta:
        db_table = 'dbo_m_LocationType'
        verbose_name = "Location Type Master"
        verbose_name_plural = "Location Type Master"

    def save(self, **kwargs):
        super(LocationTypeMaster, self).save(**kwargs)
        self.location_type_id = 'LTM%05d' % self.pk
        LocationTypeMaster.objects.filter(pk=self.pk).update(location_type_id=self.location_type_id)

    def __str__(self):
        return str(self.location_type)


class LocationMaster(Base):
    location_id = models.CharField(max_length=16, blank=True, null=True, editable=False, unique=True)
    location_name = models.CharField(max_length=128, null= True, blank=True, default = None)
    location_short_name = models.CharField(max_length=128, null= True, blank=True, default = None, unique=True)
    location_parent_id = models.ForeignKey('self',to_field="location_id", on_delete=models.CASCADE, null= True, blank=True, default = None)
    latitude = models.FloatField(blank=True, null=True, default=None)
    longitude = models.FloatField(blank=True, null=True, default=None)
    location_type_id = models.ForeignKey(LocationTypeMaster,to_field="location_type_id", on_delete=models.CASCADE, null= True, blank=True, default = None)

    class Meta:
        db_table = 'dbo_m_Location'
        verbose_name = "Location Master"
        verbose_name_plural = "Location Master"

    def save(self, **kwargs):
        super(LocationMaster, self).save(**kwargs)
        self.location_id = 'L%05d' % self.pk
        LocationMaster.objects.filter(pk=self.pk).update(location_id=self.location_id)

    def __str__(self):
        return str(self.location_name)


class StatusMaster(Base):
        status_id = models.CharField(max_length=16, blank=True, null=True, editable=False, unique=True)
        status_name = models.CharField(max_length=128, null= True, blank=True, default=None)
        parent_status_id = models.ForeignKey('self',to_field="status_id", on_delete=models.CASCADE, null= True,
                                             blank=True, default=None)
        Priority = models.PositiveIntegerField(null= True, blank=True, default = None, unique=True)

        class Meta:
            db_table = 'dbo_m_Status'
            verbose_name = "Status Master"
            verbose_name_plural = "Status Master"

        def save(self, **kwargs):
            super(StatusMaster, self).save(**kwargs)
            self.status_id = 'S%05d' % self.pk
            StatusMaster.objects.filter(pk=self.pk).update(status_id=self.status_id)

        def __str__(self):
            return str(self.status_name)



class ServiceRequiredTransaction(Base):
    service_transaction_id = models.CharField(max_length=16, blank=True, null=True, editable=False, unique=True)
    victim_name = models.CharField(max_length=128, null= True, blank=True, default = None)
    contact_no = models.TextField(max_length=128, null= True, blank=True, default = None)
    services = models.ManyToManyField(ServiceMaster, null= True, blank=True, default = None)
    description = models.TextField(max_length=1024, null= True, blank=True, default = None)
    latitude = models.FloatField(blank=True, null=True, default=None)
    longitude = models.FloatField(blank=True, null=True, default=None)
    location_id = models.ForeignKey(LocationMaster,to_field="location_id", on_delete=models.CASCADE, null= True, blank=True, default = None)
    image_url = models.CharField(max_length=128, null= True, blank=True, default = None)
    status = models.ForeignKey(StatusMaster,to_field="status_id", on_delete=models.CASCADE, null= True, blank=True, default = None)
    assigned_to_name = models.CharField(max_length=128, null= True, blank=True, default = None)
    assigned_to_contact_no = models.CharField(max_length=128, null= True, blank=True, default = None)
    assigned_to_employee = models.ForeignKey(EmployeeMaster,to_field="employee_id", on_delete=models.CASCADE, null= True, blank=True, default = None)
    # fixme: later change to ManyTo Many Field
    assigned_team = models.ForeignKey(TeamMaster,to_field="team_id", on_delete=models.CASCADE, null= True, blank=True, default = None)
    priority = models.PositiveIntegerField(null=True, blank=True, default=None, unique=True)

    class Meta:
        db_table = 'dbo_m_ServiceRequiredTransaction'
        verbose_name = "Service Request Transaction"
        verbose_name_plural = "Service Request Transaction"

    def save(self, **kwargs):
        super(ServiceRequiredTransaction, self).save(**kwargs)
        self.service_transaction_id = 'SRT%05d' % self.pk
        ServiceRequiredTransaction.objects.filter(pk=self.pk).update(service_transaction_id=self.service_transaction_id)

    def __str__(self):
        return str(self.victim_name)

    def display_services(self):
        return ', '.join([other.title for other in self.services.all()])

    display_services.short_description = 'services'
    display_services.allow_tags = True
