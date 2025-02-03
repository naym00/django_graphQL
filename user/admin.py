from django.contrib import admin
from user import models

admin.site.register([
    models.Designation,
    models.Grade,
    models.Religion,
    models.Shift,
    models.User,
    models.Ethnicgroup,
    models.Note
])