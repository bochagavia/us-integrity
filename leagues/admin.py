from django.contrib import admin
from leagues.models import Leagues, Teams


class TeamsAdmin(admin.StackedInline):
    model = Teams
    extra = 0


class LeaguesAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None) -> bool:
        return False
    
    inlines = [TeamsAdmin, ]


admin.site.register(Leagues, LeaguesAdmin)