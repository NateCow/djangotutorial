from django.contrib import admin

from .models import LCCEntry, LCCCreator, LCCComp, LCCCompany, CrewRole

# Register your models here.

class LCCEntryInline(admin.TabularInline):
    model = LCCEntry
    extra = 0  # Number of empty forms to display

class CrewRoleInline(admin.TabularInline):
    model = CrewRole
    extra = 0

class LCCEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_competition_name_display', 'creator', 'production_company')
    # inlines = [CrewRoleInline]

    def get_competition_name_display(self, obj):
        return obj.get_competition_name_display()
    get_competition_name_display.short_description = 'Competition Name'

class LCCCompaniesAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'owner')

class CrewRoleAdmin(admin.ModelAdmin):
    list_display = ('role', )   

class LCCCreatorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = [LCCEntryInline]

class LCCCompAdmin(admin.ModelAdmin):
    list_display = ('name', 'year',)
    inlines = [LCCEntryInline]
    

admin.site.register(LCCEntry, LCCEntryAdmin)
admin.site.register(LCCCreator, LCCCreatorAdmin)
admin.site.register(LCCComp, LCCCompAdmin)
admin.site.register(LCCCompany, LCCCompaniesAdmin)
admin.site.register(CrewRole, CrewRoleAdmin)