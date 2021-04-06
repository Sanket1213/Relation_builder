from django.contrib import admin
from .models import User, Relation
# Register your models here.
admin.site.register(Relation)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'name1','relation', 'name2')