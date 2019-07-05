from django.contrib import admin
from .models import Company, Branch, Project, Phase, Block, Floortype


# Register your models here.
admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Project)
admin.site.register(Phase)
admin.site.register(Block)
admin.site.register(Floortype)
