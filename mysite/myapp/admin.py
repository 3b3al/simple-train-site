from django.contrib import admin
from .models import *


admin.site.site_header = "railway admin"
admin.site.site_title = "railway Admin Area"
admin.site.index_title = "welcome to the railway admin area"
# Register your models here.
admin.site.register(Station)
admin.site.register(Train)

admin.site.register(Seat_Chart)
admin.site.register(Ticket)

