from django.contrib import admin
from .models import contactform,training_course,projects,gallery,team


class contactpost(admin.ModelAdmin):
    list_display=('name','email','contactNumber','message')

class course(admin.ModelAdmin):
    list_display=('name','image','description')

class proj(admin.ModelAdmin):
    list_display=('name','image','description')

class about(admin.ModelAdmin):
    list_display=('name','description')


admin.site.register(contactform,contactpost)
admin.site.register(training_course,course)
admin.site.register(projects,proj)
admin.site.register(gallery)
admin.site.register(team,about)

