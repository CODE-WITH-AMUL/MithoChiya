from django.contrib import admin
from .models import Customer , Table , MenuItem , Order , OrderItem , Payment , Feedback 



admin.site.register(Customer)
admin.site.register(Table)
# admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Feedback)