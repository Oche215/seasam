from django.contrib import admin
from .models import ContactUs, NigeriaMineralDeposit, GeoPoliticalRegion, Minerals

# Register your models here.
admin.site.register(ContactUs)
admin.site.register(NigeriaMineralDeposit)
admin.site.register(GeoPoliticalRegion)
admin.site.register(Minerals)

