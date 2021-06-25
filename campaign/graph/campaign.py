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
    team_campaigns = graphene.List(
        CampaignType, team_id=graphene.Argument(graphene.ID, required=True)
    )
    all_campaigns = graphene.List(CampaignType)
    all_teams = graphene.List(TeamType)
    team_info = graphene.Field(
        TeamType, team_name=graphene.Argument(graphene.String, required=True)
    )

    def resolve_team_campaigns(self, info, team_id):
        return Campaign.objects.filter(team_id=team_id)

    def resolve_all_campaigns(self, info):
        return Campaign.objects.all()

    def resolve_all_teams(self, info):
        return Team.objects.all()

    def resolve_team_info(self, info, team_name):
        return Team.objects.filter(name__iexact=team_name).first()
