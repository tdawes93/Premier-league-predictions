from django.contrib import admin
from . import models


class TeamAdmin(admin.ModelAdmin):
    pass


class LeagueAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.team, TeamAdmin)
admin.site.register(models.league, LeagueAdmin)
