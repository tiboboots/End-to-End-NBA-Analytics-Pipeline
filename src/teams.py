import nba_api.stats.endpoints as ep
from nba_api.stats.static import teams
from dataclasses import dataclass, field

@dataclass
class Team:
    full_team_name: str
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
        self.full_team_name = self.full_team_name.strip().title()
        all_team_ids = self.get_all_team_ids()
        if self.full_team_name in all_team_ids:
            self.team_id = all_team_ids[self.full_team_name]
        else:
            raise KeyError(f"Team ID could not be located using team name: {self.full_team_name}")

    def team_roster(self, season: str):
        return ep.CommonTeamRoster(team_id= self.team_id, season=season)
    
    def team_game_stats(self, season: str, season_type: str = "Regular Season"):
        return ep.TeamGameLog(team_id=self.team_id, season=season, season_type_all_star=season_type)