from django.contrib import admin
from .models import *

admin.site.register(Clients)
admin.site.register(Team)
admin.site.register(Testimonial)
admin.site.register(ContactForm)
admin.site.register(Subscribe)
admin.site.register(HomeFaq)
# admin.site.register(Project)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  
    list_display = ('title', 'category', 'slug')
admin.site.register(HomeAbouts)
class ServiceFAQInline(admin.TabularInline):
    model = ServiceFAQ
    extra = 1
admin.site.register(ServiceFAQ)



class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceFAQInline]

    list_display = ('service_name', 'slug')  # show these columns in the admin list
    prepopulated_fields = {'slug': ('service_name',)}  # auto-fill slug from name
admin.site.register(Service, ServiceAdmin)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'formatted_date']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'category']

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'blog', 'approved', 'created_at']
    list_filter = ['approved', 'created_at']
    search_fields = ['name', 'message']
