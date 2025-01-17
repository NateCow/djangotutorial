from django.contrib import admin

from .models import LCCEntry, LCCCreator, LCCComp

# Register your models here.

class LCCEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'competition_name', 'competition_year', 'creator', 'production_company')
    readonly_fields = ('competition_year',)
    
    def competition_year(self, obj):
        return obj.competition_year()
    competition_year.short_description = 'Competition Year'

class LCCCreatorAdmin(admin.ModelAdmin):
    list_display = ('name', )

class LCCCompAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')
    

admin.site.register(LCCEntry, LCCEntryAdmin)
admin.site.register(LCCCreator, LCCCreatorAdmin)
admin.site.register(LCCComp, LCCCompAdmin)
