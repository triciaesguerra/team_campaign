import graphene
import campaign.graph.campaign as campaign


class Query(campaign.Query):
    # hello = graphene.String(default_value="Hi!")
    pass


schema = graphene.Schema(query=Query)