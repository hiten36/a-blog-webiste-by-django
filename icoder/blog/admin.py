from django.contrib import admin
from .models import post,blogcomment

# Register your models here.
admin.site.register((post,blogcomment))

