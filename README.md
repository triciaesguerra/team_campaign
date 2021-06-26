# Team Campaign

GraphQL API for getting campaign data

## Queries

#### `queryTeam`

Look up for team information. This query accepts either of the arguments below.

##### Arguments

| Name                               | Description |
| ---------------------------------- | ----------- |
| `byTeamCode` `(String)` (optional) | Team code   |
| `byTeamName` `(String)` (optional) | Team name   |

##### Sample Query

Get team by `team name`

```graphql
query teams($byTeamName: String) {
  queryTeam(byTeamName: $byTeamName) {
    id
    name
    code
    colorSet
  }
}
```

Get team by `team code`

```graphql
query teams($byTeamCode: String) {
  queryTeam(byTeamCode: $byTeamCode) {
    id
    name
    code
    colorSet
  }
}
```

#### `allTeams`

Look up for all team information in the database.

##### Arguments

None

##### Sample Query

```graphql
query teams {
  allTeams {
    id
    name
    code
    colorSet
  }
}
```

#### `queryTeamCampaigns`

Look up for all the campaigns related to the team. This query accepts either of the arguments below.

##### Arguments

| Name                               | Description      |
| ---------------------------------- | ---------------- |
| `byTeamCode` `(String)` (optional) | Team code        |
| `byTeamName` `(String)` (optional) | Team name        |
| `byTeamId` `(ID)` (optional)       | Team database id |

##### Sample Query

Query team campaign by `team code`

```graphql
query teamCampaigns($byTeamCode: String) {
  queryTeamCampaigns(byTeamCode: $byTeamCode) {
    id
    name
    startDate
    endDate
    budget
    hashtags
    description
  }
}
```

Query team campaign by `team ID`

```graphql
query teamCampaigns($byTeamId: ID) {
  queryTeamCampaigns(byTeamId: $byTeamId) {
    id
    name
    startDate
    endDate
    budget
    hashtags
    description
  }
}
```

Query team campaign by `team name`

```graphql
query teamCampaigns($byTeamName: String) {
  queryTeamCampaigns(byTeamName: $byTeamName) {
    id
    name
    startDate
    endDate
    budget
    hashtags
    description
  }
}
```

#### `allCampaigns`

Look up for all team campaign information in the database.

##### Arguments

None

##### Sample Query

Query all team campaigns

```graphql
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
```

## Dev

### Running the app

```sh
./run_dev
```

Locally, this is likely to be accessible via: `https://localhost:8000`

### Accessing the GraphiQL view

Accessible via: `https://localhost:8000/graphql`

### Unit tests

```sh
./run_unit_tests
```
