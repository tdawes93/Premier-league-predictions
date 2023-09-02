from django.contrib import admin
from . import models


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'country',
        'get_league',
        'games_played',
        'wins',
        'draws',
        'losses',
        'points',
    )
    
    def get_league(self, obj):
        return obj.league.friendly_name
    get_league.admin_order_field  = 'name'  #Allows column order sorting
    get_league.short_description = 'League'  #Renames column head
    
    ordering = ('friendly_name',)

    search_fields = ('friendly_name',)

class LeagueAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'country',
        'tier_in_country'
    )
    ordering = (
        'country',
        'tier_in_country',
    )


admin.site.register(models.team, TeamAdmin)
admin.site.register(models.league, LeagueAdmin)
