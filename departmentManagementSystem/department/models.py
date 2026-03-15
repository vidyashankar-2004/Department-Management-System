from django.db import models

class Department(models.Model):
    # Defining status choices for better data integrity
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('archived', 'Archived'),
    ]

    department_name = models.CharField(max_length=200)
    department_code = models.CharField(max_length=10, unique=True) # Added unique=True
    department_description = models.TextField()
    head_of_department = models.CharField(max_length=200)
    contact_email = models.EmailField()
    contact_phone_number = models.CharField(max_length=15) # Increased to 15 for international formats
    department_location = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_by = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.department_name} ({self.department_code})"
    
    