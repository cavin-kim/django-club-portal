from django.shortcuts import render

# Create your views here.
from .models import Employee


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "templates/employee_list.html", {"employees": employees})
