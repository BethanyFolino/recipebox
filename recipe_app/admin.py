from django.contrib import admin
from recipe_app.models import Author, Recipe

# Register your models here.
admin.site.register(Author)
admin.site.register(Recipe)

# References: 
# Whole assignment: Peter's demo
# Getting venv and poetry properly set up: Matt Perry
# Help with getting stuck with migration: Jalal Belsifar
# CSS and Bootstrap for styling: w3schools.com, getbootstrap.com
# Alerts for non-staff users who try to add authors: https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html