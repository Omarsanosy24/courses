from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(college)
admin.site.register(year)
#admin.site.register(CatCourses)
admin.site.register(Teacher)
admin.site.register(Banars)
admin.site.register(Courses)
admin.site.register(Cart)

class CartItemAdmin(admin.ModelAdmin):
    list_display = [ 'userCartItem','id', 'Courses']

admin.site.register(CartItem,CartItemAdmin)

class CatCourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']

admin.site.register(CatCourses,CatCourseAdmin)
