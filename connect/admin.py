from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Profile),
admin.site.register(Like),
# admin.site.register(Catfish),
admin.site.register(Message),

