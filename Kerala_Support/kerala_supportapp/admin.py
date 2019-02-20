from django.contrib import admin
from kerala_supportapp.models import *

@admin.register(LanguageMaster)
class LanguageMasterAdmin(admin.ModelAdmin):
    list_display = ('language_id', 'language_name', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    ordering = ['language_id']
    search_fields = ('language_id', 'language_name', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    list_display_links = ('language_id', 'language_name', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    fieldsets = (
        ('Language Master', {
            'fields': ('language_name', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required')
        }),
    )
    list_per_page = 25

@admin.register(ServiceTypeMaster)
class ServiceTypeMasterAdmin(admin.ModelAdmin):
    list_display = ('service_type_id', 'service_name', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    ordering = ['service_type_id']
    search_fields = ('service_type_id', 'service_name', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    list_display_links = ('service_type_id', 'service_name', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    fieldsets = (
        ('Service Type Master', {
            'fields': ('service_name', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required')
        }),
    )
    list_per_page = 25

@admin.register(EmergencyTypeMaster)
class EmergencyTypeMasterAdmin(admin.ModelAdmin):
    list_display = ('emergency_type_id', 'emergency_type_name', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    ordering = ['emergency_type_id']
    search_fields = ('emergency_type_id', 'emergency_type_name', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    list_display_links = ('emergency_type_id', 'emergency_type_name', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    fieldsets = (
        ('Emergency Type Master', {
            'fields': ('emergency_type_name', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required')
        }),
    )
    list_per_page = 25

@admin.register(ServiceMaster)
class ServiceMasterAdmin(admin.ModelAdmin):
    list_display = ('service_id', 'service_name', 'service_type', 'emergency_category', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    ordering = ['service_id']
    search_fields = ('service_id', 'service_name', 'service_type', 'emergency_category', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    list_display_links = ('service_id', 'service_name', 'service_type', 'emergency_category', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    fieldsets = (
        ('Service Master', {
            'fields': ('service_name', 'service_type', 'emergency_category', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required')
        }),
    )
    list_per_page = 25


@admin.register(EmployeeMaster)
class EmployeeMasterAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name','contact_no', 'alernate_contact_no', 'address', 'display_languages_known', 'services', 'reporting_to', 'display_team', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    ordering = ['employee_id']
    search_fields = ('employee_id', 'employee_name', 'contact_no', 'alernate_contact_no', 'address', 'display_languages_known', 'services', 'reporting_to', 'display_team', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    list_display_links = ('employee_id', 'employee_name', 'contact_no', 'alernate_contact_no', 'address', 'display_languages_known', 'services', 'reporting_to', 'display_team','is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    fieldsets = (
        ('Employee Master', {
            'fields': ('employee_name', 'contact_no', 'alernate_contact_no', 'address', 'languages_known', 'services', 'reporting_to', 'team', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required')
        }),
    )
    list_per_page = 25


@admin.register(LocationTypeMaster)
class LocationTypeMaster(admin.ModelAdmin):
    list_display = ('location_type_id', 'location_type', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    ordering = ['location_type_id']
    search_fields = ('location_type_id', 'location_type', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    list_display_links = ('location_type_id', 'location_type', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    fieldsets = (
        ('LocationType Master', {
            'fields': ('location_type', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required')
        }),
    )
    list_per_page = 25


@admin.register(LocationMaster)
class LocationMasterAdmin(admin.ModelAdmin):
    list_display = ('location_id', 'location_name', 'location_short_name', 'location_parent_id', 'latitude', 'longitude', 'location_type_id', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    ordering = ['location_id']
    search_fields = ('location_id', 'location_name', 'location_short_name', 'location_parent_id', 'latitude', 'longitude', 'location_type_id', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    list_display_links = ('location_name', 'location_short_name', 'location_parent_id', 'latitude', 'longitude', 'location_type_id', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    fieldsets = (
        ('Location Master', {
            'fields': ('location_name', 'location_short_name', 'location_parent_id', 'latitude', 'longitude', 'location_type_id', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required')
        }),
    )
    list_per_page = 25


@admin.register(StatusMaster)
class StatusMasterAdmin(admin.ModelAdmin):
    list_display = ('status_id', 'status_name', 'parent_status_id', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    ordering = ['status_id']
    search_fields = ('status_id', 'status_name', 'parent_status_id', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    list_display_links = ('status_id', 'status_name', 'parent_status_id', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    fieldsets = (
        ('Status Master', {
            'fields': ('status_name', 'parent_status_id', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required')
        }),
    )
    list_per_page = 25


@admin.register(ServiceRequiredTransaction)
class ServiceRequiredTransactionAdmin(admin.ModelAdmin):
    list_display = ('victim_name', 'contact_no', 'display_services', 'description', 'latitude', 'longitude', 'location_id', 'image_url', 'status', 'assigned_to_name', 'assigned_to_contact_no', 'assigned_to_employee', 'assigned_team', 'priority', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')

    search_fields = ('victim_name', 'contact_no', 'display_services', 'description', 'latitude', 'longitude', 'location_id', 'image_url', 'status', 'assigned_to_name', 'assigned_to_contact_no', 'assigned_to_employee', 'assigned_team', 'priority', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    list_display_links = ('victim_name', 'contact_no', 'display_services', 'description', 'latitude', 'longitude', 'location_id', 'image_url', 'status', 'assigned_to_name', 'assigned_to_contact_no', 'assigned_to_employee', 'assigned_team', 'priority', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    fieldsets = (
        ('Service Required Transaction', {
            'fields': ('victim_name', 'contact_no', 'services', 'description', 'latitude', 'longitude', 'location_id', 'image_url', 'status', 'assigned_to_name', 'assigned_to_contact_no', 'assigned_to_employee', 'is_active','deactivation_reason', 'assigned_team', 'priority', 'is_suspended', 'suspension_reason', 'is_audit_required')
        }),
    )
    list_per_page = 25


@admin.register(TeamMaster)
class TeamMasterAdmin(admin.ModelAdmin):
    list_display = ('team_id', 'team_name', 'single_skilled', 'parent_team', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    ordering = ['team_id']
    search_fields = ('team_id', 'team_name', 'single_skilled', 'parent_team', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    list_display_links = ('team_id', 'team_name', 'single_skilled', 'parent_team', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required', 'created_by','modified_by', 'created_date', 'modified_date')
    fieldsets = (
        ('Team Master', {
            'fields': ('team_name', 'single_skilled', 'parent_team', 'is_active','deactivation_reason', 'is_suspended', 'suspension_reason', 'is_audit_required')
        }),
    )
    list_per_page = 25