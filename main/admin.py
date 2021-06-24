from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)

# contact page create
admin.site.register(Contact)