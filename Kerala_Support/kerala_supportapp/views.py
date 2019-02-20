from kerala_supportapp.serializers import *
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import *
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import json
from django.db.models import Q



@api_view(["POST"])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    request.session['username'] = username

    if user is not None:
        if user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            user_permissions = list(Permission.objects.filter(user=user).values())
            user_object = User.objects.filter(id=token.user_id).values('id','username','first_name','last_name','email','is_staff','is_active','date_joined').get()
            list_user_permissions = json.dumps(user_permissions).replace('\"',"")

            request.session['auth'] = token.key

        return Response({"success": "Login successfully", "token": token.key, "list_user_permissions": list_user_permissions,"user_object": user_object})

    else:
        return Response({"error": "Invalid Username & Password"}, status=HTTP_401_UNAUTHORIZED)


@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponse("Logout Succesfully")


# Api to Fetch , Delete, Update Data of Specific id
class LanguageMasterGetView(RetrieveUpdateDestroyAPIView):
    queryset = LanguageMaster.objects.all().filter(is_active=True)
    serializer_class = LanguageMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    lookup_field = 'language_id'

    def perform_update(self, serializer):
        serializer.validated_data['modified_by'] = self.request.user.get_full_name()
        return super(LanguageMasterGetView, self).perform_update(serializer)

    def destroy(self, request, language_id):
        modified_by = self.request.user.get_full_name()
        LanguageMaster.objects.filter(language_id=language_id).update(is_active=False, modified_by=modified_by)
        return Response(LanguageMaster.objects.filter(language_id=language_id).values().get())


# Api to fetch all data
class LanguageMasterListView(generics.ListAPIView):
    serializer_class = LanguageMasterSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = LanguageMaster.objects.all().filter(is_active=True)
            filter_by_date = self.request.GET.get('date', None)
            if filter_by_date is not None:
                all_queryset = LanguageMaster.objects.all()
                queryset = all_queryset.filter(Q(modified_date__gt=filter_by_date) | Q(created_date__gt=filter_by_date))
            return queryset


# Api to post data in Ca Service Master
class LanguageMasterPostView(generics.CreateAPIView):
    queryset = LanguageMaster.objects.all()
    serializer_class = LanguageMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.validated_data['created_by'] = self.request.user.get_full_name()
        return super(LanguageMasterPostView, self).perform_create(serializer)


# Api to Fetch , Delete, Update Data of Specific id
class ServiceTypeMasterGetView(RetrieveUpdateDestroyAPIView):
    queryset = ServiceTypeMaster.objects.all().filter(is_active=True)
    serializer_class = ServiceTypeMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    lookup_field = 'service_type_id'

    def perform_update(self, serializer):
        serializer.validated_data['modified_by'] = self.request.user.get_full_name()
        return super(ServiceTypeMasterGetView, self).perform_update(serializer)

    def destroy(self, request, service_type_id):
        modified_by = self.request.user.get_full_name()
        ServiceTypeMaster.objects.filter(service_type_id=service_type_id).update(is_active=False, modified_by=modified_by)
        return Response(ServiceTypeMaster.objects.filter(service_type_id=service_type_id).values().get())


# Api to fetch all data
class ServiceTypeMasterListView(generics.ListAPIView):
    serializer_class = ServiceTypeMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = ServiceTypeMaster.objects.all().filter(is_active=True)
            filter_by_date = self.request.GET.get('date', None)
            if filter_by_date is not None:
                all_queryset = ServiceTypeMaster.objects.all()
                queryset = all_queryset.filter(Q(modified_date__gt=filter_by_date) | Q(created_date__gt=filter_by_date))
            return queryset


# Api to post data in Ca Service Master
class ServiceTypeMasterPostView(generics.CreateAPIView):
    queryset = ServiceTypeMaster.objects.all()
    serializer_class = ServiceTypeMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.validated_data['created_by'] = self.request.user.get_full_name()
        return super(ServiceTypeMasterPostView, self).perform_create(serializer)


# Api to Fetch , Delete, Update Data of Specific id
class EmergencyTypeMasterGetView(RetrieveUpdateDestroyAPIView):
    queryset = EmergencyTypeMaster.objects.all().filter(is_active=True)
    serializer_class = EmergencyTypeMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    lookup_field = 'emergency_type_id'

    def perform_update(self, serializer):
        serializer.validated_data['modified_by'] = self.request.user.get_full_name()
        return super(EmergencyTypeMasterGetView, self).perform_update(serializer)

    def destroy(self, request, emergency_type_id):
        modified_by = self.request.user.get_full_name()
        EmergencyTypeMaster.objects.filter(emergency_type_id=emergency_type_id).update(is_active=False, modified_by=modified_by)
        return Response(EmergencyTypeMaster.objects.filter(emergency_type_id=emergency_type_id).values().get())


# Api to fetch all data
class EmergencyTypeMasterListView(generics.ListAPIView):
    serializer_class = EmergencyTypeMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = EmergencyTypeMaster.objects.all().filter(is_active=True)
            filter_by_date = self.request.GET.get('date', None)
            if filter_by_date is not None:
                all_queryset = EmergencyTypeMaster.objects.all()
                queryset = all_queryset.filter(Q(modified_date__gt=filter_by_date) | Q(created_date__gt=filter_by_date))
            return queryset


# Api to post data in Ca Service Master
class EmergencyTypeMasterPostView(generics.CreateAPIView):
    queryset = EmergencyTypeMaster.objects.all()
    serializer_class = EmergencyTypeMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.validated_data['created_by'] = self.request.user.get_full_name()
        return super(EmergencyTypeMasterPostView, self).perform_create(serializer)


# Api to Fetch , Delete, Update Data of Specific id
class ServiceMasterGetView(RetrieveUpdateDestroyAPIView):
    queryset = ServiceMaster.objects.all().filter(is_active=True)
    serializer_class = ServiceMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    lookup_field = 'service_id'

    def perform_update(self, serializer):
        serializer.validated_data['modified_by'] = self.request.user.get_full_name()
        return super(ServiceMasterGetView, self).perform_update(serializer)

    def destroy(self, request, service_id):
        modified_by = self.request.user.get_full_name()
        ServiceMaster.objects.filter(service_id=service_id).update(is_active=False, modified_by=modified_by)
        return Response(ServiceMaster.objects.filter(service_id=service_id).values().get())


# Api to fetch all data
class ServiceMasterListView(generics.ListAPIView):
    serializer_class = ServiceMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = ServiceMaster.objects.all().filter(is_active=True)
            filter_by_date = self.request.GET.get('date', None)
            if filter_by_date is not None:
                all_queryset = ServiceMaster.objects.all()
                queryset = all_queryset.filter(Q(modified_date__gt=filter_by_date) | Q(created_date__gt=filter_by_date))
            return queryset


# Api to post data in Ca Service Master
class ServiceMasterPostView(generics.CreateAPIView):
    queryset = ServiceMaster.objects.all()
    serializer_class = ServiceMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.validated_data['created_by'] = self.request.user.get_full_name()
        return super(ServiceMasterPostView, self).perform_create(serializer)


# Api to Fetch , Delete, Update Data of Specific id
class EmployeeMasterGetView(RetrieveUpdateDestroyAPIView):
    queryset = EmployeeMaster.objects.all().filter(is_active=True)
    serializer_class = EmployeeMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    lookup_field = 'employee_id'

    def perform_update(self, serializer):
        serializer.validated_data['modified_by'] = self.request.user.get_full_name()
        return super(EmployeeMasterGetView, self).perform_update(serializer)

    def destroy(self, request, employee_id):
        modified_by = self.request.user.get_full_name()
        EmployeeMaster.objects.filter(employee_id=employee_id).update(is_active=False, modified_by=modified_by)
        return Response(EmployeeMaster.objects.filter(employee_id=employee_id).values().get())


# Api to fetch all data
class EmployeeMasterListView(generics.ListAPIView):
    serializer_class = EmployeeMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = EmployeeMaster.objects.all().filter(is_active=True)
            filter_by_date = self.request.GET.get('date', None)
            if filter_by_date is not None:
                all_queryset = EmployeeMaster.objects.all()
                queryset = all_queryset.filter(Q(modified_date__gt=filter_by_date) | Q(created_date__gt=filter_by_date))
            return queryset


# Api to post data in Ca Service Master
class EmployeeMasterPostView(generics.CreateAPIView):
    queryset = EmployeeMaster.objects.all()
    serializer_class = EmployeeMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.validated_data['created_by'] = self.request.user.get_full_name()
        return super(EmployeeMasterPostView, self).perform_create(serializer)


# Api to Fetch , Delete, Update Data of Specific id
class LocationTypeMasterGetView(RetrieveUpdateDestroyAPIView):
    queryset = LocationTypeMaster.objects.all().filter(is_active=True)
    serializer_class = LocationTypeMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    lookup_field = 'location_type_id'

    def perform_update(self, serializer):
        serializer.validated_data['modified_by'] = self.request.user.get_full_name()
        return super(LocationTypeMasterGetView, self).perform_update(serializer)

    def destroy(self, request, location_type_id):
        modified_by = self.request.user.get_full_name()
        LocationTypeMaster.objects.filter(location_type_id=location_type_id).update(is_active=False, modified_by=modified_by)
        return Response(LocationTypeMaster.objects.filter(location_type_id=location_type_id).values().get())


# Api to fetch all data
class LocationTypeMasterListView(generics.ListAPIView):
    serializer_class = LocationTypeMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = LocationTypeMaster.objects.all().filter(is_active=True)
            filter_by_date = self.request.GET.get('date', None)
            if filter_by_date is not None:
                all_queryset = LocationTypeMaster.objects.all()
                queryset = all_queryset.filter(Q(modified_date__gt=filter_by_date) | Q(created_date__gt=filter_by_date))
            return queryset


# Api to post data in Ca Service Master
class LocationTypeMasterPostView(generics.CreateAPIView):
    queryset = LocationTypeMaster.objects.all()
    serializer_class = LocationTypeMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.validated_data['created_by'] = self.request.user.get_full_name()
        return super(LocationTypeMasterPostView, self).perform_create(serializer)


# Api to Fetch , Delete, Update Data of Specific id
class LocationMasterGetView(RetrieveUpdateDestroyAPIView):
    queryset = LocationMaster.objects.all().filter(is_active=True)
    serializer_class = LocationMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    lookup_field = 'location_id'

    def perform_update(self, serializer):
        serializer.validated_data['modified_by'] = self.request.user.get_full_name()
        return super(LocationMasterGetView, self).perform_update(serializer)

    def destroy(self, request, location_id):
        modified_by = self.request.user.get_full_name()
        LocationMaster.objects.filter(location_id=location_id).update(is_active=False, modified_by=modified_by)
        return Response(LocationMaster.objects.filter(location_id=location_id).values().get())


# Api to fetch all data
class LocationMasterListView(generics.ListAPIView):
    serializer_class = LocationMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = LocationMaster.objects.all().filter(is_active=True)
            filter_by_date = self.request.GET.get('date', None)
            if filter_by_date is not None:
                all_queryset = LocationMaster.objects.all()
                queryset = all_queryset.filter(Q(modified_date__gt=filter_by_date) | Q(created_date__gt=filter_by_date))
            return queryset


# Api to post data in Ca Service Master
class LocationMasterPostView(generics.CreateAPIView):
    queryset = LocationMaster.objects.all()
    serializer_class = LocationMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.validated_data['created_by'] = self.request.user.get_full_name()
        return super(LocationMasterPostView, self).perform_create(serializer)


# Api to Fetch , Delete, Update Data of Specific id
class StatusMasterGetView(RetrieveUpdateDestroyAPIView):
    queryset = StatusMaster.objects.all().filter(is_active=True)
    serializer_class = StatusMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    lookup_field = 'status_id'

    def perform_update(self, serializer):
        serializer.validated_data['modified_by'] = self.request.user.get_full_name()
        return super(StatusMasterGetView, self).perform_update(serializer)

    def destroy(self, request, status_id):
        modified_by = self.request.user.get_full_name()
        StatusMaster.objects.filter(status_id=status_id).update(is_active=False, modified_by=modified_by)
        return Response(StatusMaster.objects.filter(status_id=status_id).values().get())


# Api to fetch all data
class StatusMasterListView(generics.ListAPIView):
    serializer_class = StatusMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = StatusMaster.objects.all().filter(is_active=True)
            filter_by_date = self.request.GET.get('date', None)
            if filter_by_date is not None:
                all_queryset = StatusMaster.objects.all()
                queryset = all_queryset.filter(Q(modified_date__gt=filter_by_date) | Q(created_date__gt=filter_by_date))
            return queryset


# Api to post data in Ca Service Master
class StatusMasterPostView(generics.CreateAPIView):
    queryset = StatusMaster.objects.all()
    serializer_class = StatusMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.validated_data['created_by'] = self.request.user.get_full_name()
        return super(StatusMasterPostView, self).perform_create(serializer)


# Api to Fetch , Delete, Update Data of Specific id
class ServiceRequiredTransactionGetView(RetrieveUpdateDestroyAPIView):
    queryset = ServiceRequiredTransaction.objects.all().filter(is_active=True)
    serializer_class = ServiceRequiredTransactionSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    lookup_field = 'service_transaction_id'

    def perform_update(self, serializer):
        serializer.validated_data['modified_by'] = self.request.user.get_full_name()
        return super(ServiceRequiredTransactionGetView, self).perform_update(serializer)

    def destroy(self, request, service_transaction_id):
        modified_by = self.request.user.get_full_name()
        ServiceRequiredTransaction.objects.filter(service_transaction_id=service_transaction_id).update(is_active=False, modified_by=modified_by)
        return Response(ServiceRequiredTransaction.objects.filter(service_transaction_id=service_transaction_id).values().get())


# Api to fetch all data
class ServiceRequiredTransactionListView(generics.ListAPIView):
    serializer_class = ServiceRequiredTransactionSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = ServiceRequiredTransaction.objects.all().filter(is_active=True)
            filter_by_date = self.request.GET.get('date', None)
            if filter_by_date is not None:
                all_queryset = ServiceRequiredTransaction.objects.all()
                queryset = all_queryset.filter(Q(modified_date__gt=filter_by_date) | Q(created_date__gt=filter_by_date))
            return queryset


# Api to post data in Ca Service Master
class ServiceRequiredTransactionPostView(generics.CreateAPIView):
    queryset = ServiceRequiredTransaction.objects.all()
    serializer_class = ServiceRequiredTransactionSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.validated_data['created_by'] = self.request.user.get_full_name()
        return super(ServiceRequiredTransactionPostView, self).perform_create(serializer)


# Api to fetch all data
class TeamMasterListView(generics.ListAPIView):
    serializer_class = TeamMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = TeamMaster.objects.all().filter(is_active=True)
            filter_by_date = self.request.GET.get('date', None)
            if filter_by_date is not None:
                all_queryset = TeamMaster.objects.all()
                queryset = all_queryset.filter(Q(modified_date__gt=filter_by_date) | Q(created_date__gt=filter_by_date))
            return queryset


# Api to Fetch , Delete, Update Data of Specific id
class TeamMasterGetView(RetrieveUpdateDestroyAPIView):
    queryset = TeamMaster.objects.all().filter(is_active=True)
    serializer_class = TeamMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    lookup_field = 'team_id'

    def perform_update(self, serializer):
        serializer.validated_data['modified_by'] = self.request.user.get_full_name()
        return super(TeamMasterGetView, self).perform_update(serializer)

    def destroy(self, request, team_id):
        modified_by = self.request.user.get_full_name()
        TeamMaster.objects.filter(team_id=team_id).update(
            is_active=False, modified_by=modified_by)
        return Response(TeamMaster.objects.filter(
            team_id=team_id).values().get())


# Api to post data in Ca Service Master
class TeamMasterPostView(generics.CreateAPIView):
    queryset = TeamMaster.objects.all()
    serializer_class = TeamMasterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.validated_data['created_by'] = self.request.user.get_full_name()
        return super(TeamMasterPostView, self).perform_create(serializer)