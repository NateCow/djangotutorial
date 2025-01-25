from django.contrib import admin

from .models import LCCEntry, LCCCreator, LCCComp

# Register your models here.

class LCCEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_competition_name_display', 'creator', 'production_company')

    def get_competition_name_display(self, obj):
        return obj.get_competition_name_display()
    get_competition_name_display.short_description = 'Competition Name'

   

class LCCCreatorAdmin(admin.ModelAdmin):
    list_display = ('name', )

class LCCCompAdmin(admin.ModelAdmin):
    list_display = ('name', 'theme', 'year',)
    

admin.site.register(LCCEntry, LCCEntryAdmin)
admin.site.register(LCCCreator, LCCCreatorAdmin)
admin.site.register(LCCComp, LCCCompAdmin)
