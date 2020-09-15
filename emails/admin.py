from django.contrib import admin

# Register your models here.
from .models import email_entry

admin.site.register(email_entry)
