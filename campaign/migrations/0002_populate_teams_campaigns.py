from django.db import migrations
from datetime import datetime
import csv
import os

pathname = os.path.dirname(__file__)
TEAMS_PATH = f"{pathname}/reference_data/teams.csv"
CAMPAIGN_PATH = f"{pathname}/reference_data/campaigns.csv"


def import_teams(apps, schema_editor):
    Team = apps.get_model("campaign", "Team")
    team_data = []
    with open(TEAMS_PATH) as teams_file:
        spreadsheet = csv.reader(teams_file)
        next(spreadsheet)
        for row in spreadsheet:
            team_id, name, code, color_set = row
            team_data.append(
                Team(id=team_id, name=name, code=code, color_set=color_set)
            )
    Team.objects.bulk_create(team_data)


def import_campaigns(apps, schema_editor):
    Campaign = apps.get_model("campaign", "Campaign")
    campaign_data = []
    with open(CAMPAIGN_PATH) as campaign_file:
        spreadsheet = csv.reader(campaign_file)
        next(spreadsheet)
        for row in spreadsheet:
            campaign_id = row[0]
            name = row[1]
            start_date = datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
            end_date = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
            budget = row[4]
            hashtags = row[5]
            team_id = int(row[6])
            description = row[7]
            campaign_data.append(
                Campaign(
                    id=campaign_id,
                    name=name,
                    start_date=start_date,
                    end_date=end_date,
                    budget=budget,
                    hashtags=hashtags,
                    team_id=team_id,
                    description=description,
                )
            )

    Campaign.objects.bulk_create(campaign_data)


class Migration(migrations.Migration):

    dependencies = [
        ("campaign", "0001_initial"),
    ]
    operations = [
        migrations.RunPython(import_teams),
        migrations.RunPython(import_campaigns),
    ]
