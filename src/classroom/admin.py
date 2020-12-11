from django.contrib import admin
from .models import *

admin.site.register(Announcement)
# admin.site.register(Subject)



class SubjectInline(admin.TabularInline):
    model = ClassRoom.subject.through
    extra = 0

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    inlines=[SubjectInline]
    exclude=('subject',)



admin.site.register(Assignment)
