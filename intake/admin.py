from django.contrib import admin
from .models import Form, Section, Row, Field

admin.site.register(Form)
admin.site.register(Section)
admin.site.register(Row)
admin.site.register(Field)