import graphene
from graphene_django.types import DjangoObjectType
from campaign.models import Team, Campaign


class CampaignType(DjangoObjectType):
    class Meta:
        model = Campaign


class TeamType(DjangoObjectType):
    class Meta:
        model = Team


class Query(graphene.ObjectType):

    query_team_campaigns = graphene.List(
        CampaignType,
        by_team_id=graphene.Argument(graphene.ID, required=False),
        by_team_name=graphene.Argument(graphene.String, required=False),
        by_team_code=graphene.Argument(graphene.String, required=False),
    )
    all_campaigns = graphene.List(CampaignType)
    query_team = graphene.Field(
        TeamType,
        by_team_name=graphene.Argument(graphene.String),
        by_team_code=graphene.Argument(graphene.String),
    )
    all_teams = graphene.List(TeamType)

    def resolve_all_campaigns(self, info):
        return Campaign.objects.all()

    def resolve_all_teams(self, info):
        return Team.objects.all()

    def resolve_query_team_campaigns(self, info, **kwargs):

        team_name = kwargs.get("by_team_name")
        team_code = kwargs.get("by_team_code")
        team_id = kwargs.get("by_team_id")

        if team_name:
            return Campaign.objects.filter(team__name__exact=team_name)
        elif team_code:
            return Campaign.objects.filter(team__code__exact=team_code)
        elif team_id:
            return Campaign.objects.filter(team_id=team_id)
        else:
            return []

    def resolve_query_team(self, info, **kwargs):
        team_name = kwargs.get("by_team_name")
        team_code = kwargs.get("by_team_code")
        if team_code:
            return Team.objects.filter(code__exact=team_code).first()
        if team_name:
            return Team.objects.filter(name__exact=team_name).first()
        return
