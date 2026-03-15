from multiprocessing import context
import sqlite3
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Department # Add this line
from django.utils.cache import add_never_cache_headers

from django.views.decorators.csrf import csrf_exempt
import json



def login(request):
 return render(request, 'login.html')

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Department  # Ensure your model is named Department

# @csrf_exempt
# def login_process(request):  # Renamed from login_view to login_process
#  if request.method == "POST":
#     try:
#         data = json.loads(request.body)
#         hod_name = data.get("hodName")
#         dept_code = data.get("deptCode")

#         # Database query using your model fields
#         department = Department.objects.filter(
#             head_of_department=hod_name, 
#             department_code=dept_code,
#             status='active'
#         ).first()
#         if department:
#             return JsonResponse({
#                 "success": True, 
#                  "message": "Authentication successful"
#             })
#         else:
#                 return JsonResponse({
#                     "success": False, 
#                     "message": "Invalid HOD Name or Department Code"
#                 }, status=401)
#     except Exception as e:
#         return JsonResponse({"success": False, "message": str(e)}, status=400)

#     return JsonResponse({"message": "Method not allowed"}, status=405)

def view(request):
    return JsonResponse({
        "status":"success"
    })

# def dashboard(request):
#     # Fetch all records
#     departments = Department.objects.all()

#     context = {
#     'departments': departments,
#     # Real-time calculations
#     'total_count': departments.count(),
#         'active_count': departments.filter(status='active').count(),
#         'inactive_count': departments.filter(status='inactive').count(),
#     }
#     return render(request, 'dashboard.html', context)

def add_department(request):
    if request.method == "POST":
        # 1. Collect data from the form (the strings in quotes match the 'name' in HTML)
        name = request.POST.get('name')
        code = request.POST.get('code')
        hod = request.POST.get('hod')
        status = request.POST.get('status')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        description = request.POST.get('description')
        created_by = request.POST.get('created_by')

        # 2. Save to Database using your Model fields
        Department.objects.create(
        department_name=name,
        department_code=code,
        head_of_department=hod,
        status=status,
        contact_email=email,
        contact_phone_number=phone,
        department_location=location,
        department_description=description,
        created_by=created_by
    )

        # 3. Redirect back to the dashboard to see the new entry
        return redirect('dashboard')

    # If it's a GET request, just show the empty form
    return render(request, 'add_department.html')

def manage(request, dept_id):
    # Fetch the specific record from SQLite
    department = get_object_or_404(Department, id=dept_id)

    if request.method == "POST":
        # Update the record with new data from the form
        department.department_name = request.POST.get('name')
        department.department_code = request.POST.get('code')
        department.head_of_department = request.POST.get('hod')
        department.status = request.POST.get('status')
        department.contact_email = request.POST.get('email')
        department.contact_phone_number = request.POST.get('phone')
        department.department_location = request.POST.get('location')
        department.department_description = request.POST.get('description')

        department.save()  # Commit changes to the database
        return redirect('dashboard')

    # If GET, send the existing department data to the edit page
    return render(request, 'manage_department.html', {'department': department})

def delete(request, dept_id):
    # 1. Find the department
    department = get_object_or_404(Department, id=dept_id)

    # 2. If the user clicked the "Yes, Delete" button (POST)
    if request.method == "POST":
        department.delete() # This removes it from SQLite
        return redirect('dashboard') # Send them back to the list

    # 3. If they just arrived at the page (GET), show the confirmation
    return render(request, 'delete.html', {'department': department})

def list(request):
    lists = []
    for i in range(1, 6):
        name=f"A.0{i}"
        lists.append(name)
    return render(request, 'task.html', {'lists': lists})


class DisableClientSideCachingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        add_never_cache_headers(response)
        return response

# from django.contrib.auth import logout
# from django.shortcuts import redirect
# def logout_view(request):
#  logout(request)
#  return redirect('login')

# -----------------------------------------------------------------------------
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import Department

# --- 1. LOGIN LOGIC ---

def login_view(request):
    return render(request, 'login.html')

@csrf_exempt
def login_process(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            hod_name = data.get("hodName")
            dept_code = data.get("deptCode")

            # Check if department exists
            dept = Department.objects.filter(
                head_of_department=hod_name, 
                department_code=dept_code,
                status='active'
            ).first()

            if dept:
                # IMPORTANT: We need to link this to a Django User to start a session
                # If you don't use the standard User model, we fetch/create a phantom one
                user, created = User.objects.get_or_create(username=hod_name)
                
                # THIS STARTS THE SESSION
                auth_login(request, user)
                
                return JsonResponse({"success": True, "message": "Authentication successful"})
            else:
                return JsonResponse({"success": False, "message": "Invalid credentials"}, status=401)
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)}, status=400)

    return JsonResponse({"message": "Method not allowed"}, status=405)

def logout_view(request):
    auth_logout(request)
    return redirect('login')

# --- 2. PROTECTED VIEWS ---

@login_required # This only works if auth_login was called above
@never_cache    # Prevents "Back Button" access after logout
def dashboard(request):
    departments = Department.objects.all()
    context = {
        'departments': departments,
        'total_count': departments.count(),
        'active_count': departments.filter(status='active').count(),
        'inactive_count': departments.filter(status='inactive').count(),
    }
    return render(request, 'dashboard.html', context)

# ... (Keep your add_department, manage, and delete functions here) ...
import csv
from django.http import HttpResponse
from .models import Department

def export_departments_csv(request):
    # create response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="departments.csv"'

    writer = csv.writer(response)

    # header row
    writer.writerow(['ID', 'Department Name', 'Head', 'Status'])

    # fetch departments
    departments = Department.objects.all()

    for dept in departments:
        writer.writerow([
            dept.id,
            dept.department_name,     # change if field name different
            dept.head_of_department,
            dept.status
        ])

    return response
