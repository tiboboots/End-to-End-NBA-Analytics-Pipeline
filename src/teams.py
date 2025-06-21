from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.static import teams
from dataclasses import dataclass, field

@dataclass
class Team:
    team_name: str
    season: int
    team_id: int = field(init=False)

    def get_all_team_ids(self) -> dict:
        all_nba_teams = teams.get_teams()
        all_team_ids = {}
        for team in all_nba_teams:
            team_id = team['id']
            team_name = team['full_name']
            all_team_ids[team_name] = team_id
        return all_team_ids
    
    def __post_init__(self):
        all_team_ids = self.get_all_team_ids()
        try:
            self.team_id = all_team_ids[self.team_name.strip().title()]
        except KeyError as k:
            print(f"KeyError: {k}")
            self.team_id = None

    def get_roster(self):
        players_and_coaches = commonteamroster.CommonTeamRoster(team_id=self.team_id, season=self.season).get_normalized_dict()
        team_roster = players_and_coaches["CommonTeamRoster"]
        players = {}
        for player_dict in team_roster:
            player_name = player_dict['PLAYER']
            player_id = player_dict['PLAYER_ID']
            players[player_name] = player_id
        return players