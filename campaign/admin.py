from django.contrib import admin
from .models import Team, Campaign


class TeamAdmin(admin.ModelAdmin):
    search_fields = ["name", "code"]


class CampaignAdmin(admin.ModelAdmin):
    search_fields = ["name"]


admin.site.register(Team, TeamAdmin)
admin.site.register(Campaign, CampaignAdmin)
