import nba_api.stats.endpoints as ep
from nba_api.stats.static import teams
from dataclasses import dataclass, field

@dataclass
class Team:
    full_team_name: str
    team_id: int = field(init=False)

    def team_roster(self, season: str):
        return ep.CommonTeamRoster(team_id= self.team_id, season=season)
    
    def team_game_stats(self, season: str, season_type: str = "Regular Season"):
        return ep.TeamGameLog(team_id=self.team_id, season=season, season_type_all_star=season_type)