from rest_framework.permissions import BasePermission


from o2o_rest_framwork.department_model.models import Department
from o2o_rest_framwork.enterprise_model.models import Company


class DepartmentChangingOrDeletingPermission(BasePermission):

    message = 'you are not the owner of this department'

    def has_object_permission(self, request, view, obj):
        if not hasattr(request.user,'company') :
            self.message = 'you are not a company'
            return False
        else:
            department = Department.objects.get(id = obj.id)
            company = Company.objects.filter(user=request.user).first().user
            print type(company)
            departments = company.departments.all()
            if department not in departments:
                return False

        return True


class IsDepartment(BasePermission):
    message = "you are not a department"

    def has_permission(self, request, view):
        if not hasattr(request.user,'department'):

            return False
        else:
            return True