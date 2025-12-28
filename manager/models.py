from django.db import models
from core.models import TimeStampModel
import random
import string


# -------------------------
# CHOICES
# -------------------------

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)

MARITAL_STATUS_CHOICES = (
    ('single', 'Single'),
    ('married', 'Married'),
)

STAFF_ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('manager', 'Manager'),
    ('chef', 'Chef'),
    ('waiter', 'Waiter'),
    ('cashier', 'Cashier'),
)


# -------------------------
# STAFF MODEL
# -------------------------

class Staff(TimeStampModel):
    # Basic Info
    name = models.CharField(max_length=100)
    role = models.CharField(
        max_length=20, choices=STAFF_ROLE_CHOICES
    )

    # Contact Info
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    alternate_phone_number = models.CharField(
        max_length=15, blank=True, null=True
    )

    # Address Info
    permanent_address = models.TextField()
    temporary_address = models.TextField(blank=True)
    street_address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    # Personal Info
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES
    )
    nationality = models.CharField(max_length=100)
    marital_status = models.CharField(
        max_length=10, choices=MARITAL_STATUS_CHOICES
    )

    # Documents (Sensitive)
    document = models.FileField(
        upload_to='staff/documents/'
    )

    # Staff ID
    staff_id_no = models.CharField(
        max_length=12, unique=True, editable=False
    )

    def save(self, *args, **kwargs):
        if not self.staff_id_no:
            self.staff_id_no = self.generate_staff_id()
        super().save(*args, **kwargs)

    def generate_staff_id(self):
        random_part = ''.join(
            random.choices(string.digits, k=4)
        )
        return f"STF{random_part}"

    def __str__(self):
        return f"{self.name} ({self.staff_id_no})"
