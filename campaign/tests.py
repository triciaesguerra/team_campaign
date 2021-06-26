import pytest
from graphene.test import Client
from campaign.schema import schema

client = Client(schema)


QUERY_GET_ALL_CAMPAIGNS = """
query getAllCampaigns {
   allCampaigns {
    id
    name
    startDate
    endDate
    budget
    hashtags
    description
  }
}
"""

QUERY_GET_ALL_TEAMS = """
query teams {
  allTeams {
    id
    name
    code
    colorSet
  }
}
"""

QUERY_GET_TEAM_INFO_NAME = """
query teams ($byTeamName: String) {
  queryTeam(byTeamName: $byTeamName) {
    id
    name
    code
    colorSet
  }
}
"""


QUERY_GET_TEAM_INFO_CODE = """
query teams ($byTeamCode: String) {
  queryTeam(byTeamCode: $byTeamCode) {
    id
    name
    code
    colorSet
  }
}
"""

QUERY_GET_TEAM_CAMPAIGN_ID = """
query teamCampaigns($byTeamId: ID){
   queryTeamCampaigns(byTeamId: $byTeamId){
    id
    name
    startDate
    endDate
    budget
    hashtags
    description
  }
}
"""

QUERY_TEAM_CAMPAIGN_CODE = """
query teamCampaigns($byTeamCode: String){
   queryTeamCampaigns(byTeamCode: $byTeamCode){
    id
    name
    startDate
    endDate
    budget
    hashtags
    description
  }
}
"""
QUERY_TEAM_CAMPAIGN_NAME = """
query teamCampaigns($byTeamName: String){
   queryTeamCampaigns(byTeamName: $byTeamName){
    id
    name
    startDate
    endDate
    budget
    hashtags
    description
  }
}
"""


QUERY_TEAM_CAMPAIGN_ID = """
query teamCampaigns($byTeamId: ID){
   queryTeamCampaigns(byTeamId: $byTeamId){
    id
    name
    startDate
    endDate
    budget
    hashtags
    description
  }
}
"""


@pytest.mark.django_db
def test_get_all_campaigns():
    response = client.execute(
        QUERY_GET_ALL_CAMPAIGNS,
    )
    campaigns = response["data"]["allCampaigns"]
    assert len(campaigns) == 20


@pytest.mark.django_db
def test_get_all_teams():
    response = client.execute(
        QUERY_GET_ALL_TEAMS,
    )
    teams = response["data"]["allTeams"]
    assert len(teams) == 3


@pytest.mark.django_db
def test_team_info_by_name():
    response = client.execute(
        QUERY_GET_TEAM_INFO_NAME, variables={"byTeamName": "Prado"}
    )
    team_info = response["data"]["queryTeam"]
    assert team_info["id"] == "1"
    assert team_info["name"] == "Prado"
    assert team_info["code"] == "prado"
    assert team_info["colorSet"] == "blue"


@pytest.mark.django_db
def test_team_info_by_code():
    response = client.execute(
        QUERY_GET_TEAM_INFO_CODE, variables={"byTeamCode": "prado"}
    )
    team_info = response["data"]["queryTeam"]
    assert team_info["id"] == "1"
    assert team_info["name"] == "Prado"
    assert team_info["code"] == "prado"
    assert team_info["colorSet"] == "blue"


@pytest.mark.django_db
def test_team_campaign_by_code():
    response = client.execute(
        QUERY_TEAM_CAMPAIGN_CODE, variables={"byTeamCode": "adidios"}
    )
    adidios_campaigns = response["data"]["queryTeamCampaigns"]
    assert len(adidios_campaigns) == 8


@pytest.mark.django_db
def test_team_campaign_by_name():
    response = client.execute(
        QUERY_TEAM_CAMPAIGN_NAME, variables={"byTeamName": "Adidos"}
    )
    adidios_campaigns = response["data"]["queryTeamCampaigns"]
    assert len(adidios_campaigns) == 8


@pytest.mark.django_db
def test_team_campaign_by_id():
    response = client.execute(
        QUERY_TEAM_CAMPAIGN_ID, variables={"byTeamId": 2}
    )
    adidios_campaigns = response["data"]["queryTeamCampaigns"]
    assert len(adidios_campaigns) == 8


@pytest.mark.django_db
def test_team_campaign_with_no_team():
    response = client.execute(
        QUERY_TEAM_CAMPAIGN_NAME, variables={"byTeamName": ""}
    )
    campaign_campaigns = response["data"]["queryTeamCampaigns"]
    assert len(campaign_campaigns) == 0
