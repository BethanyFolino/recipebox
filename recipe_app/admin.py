from django.contrib import admin
from recipe_app.models import Author, Recipe

# Register your models here.
admin.site.register(Author)
admin.site.register(Recipe)

# References (entire assessment): Peter's demo
# References for getting venv and poetry properly set up: Matt Perry
# References for help with getting stuck with migration: Jalal Belsifar
# References for CSS and Bootstrap for styling: w3schools.com, getbootstrap.com