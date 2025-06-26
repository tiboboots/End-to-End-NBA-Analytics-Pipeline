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
        
    @staticmethod
    def _validate_season(season):
        if not season.isdigit() or len(season) != 4:
            print(f"Invalid season format: {season}. Should be YYYY")
            return False
        else:
            return True
        
    @staticmethod 
    def _validate_season_type(season_type):
        season_type = season_type.strip().title()
        valid_season_types = {"Regular Season", "Playoffs"}
        if season_type not in valid_season_types:
            print(f"Invalid season type: {season_type}. Should be one of: {valid_season_types}")
            return False
        else:
            return True

    def team_roster(self, season: str):
        valid_season = self._validate_season(season)
        if not valid_season:
            return None
        else:
            return ep.CommonTeamRoster(team_id= self.team_id, season=season)
    
    def team_game_stats(self, season: str, season_type: str = "Regular Season", **kwargs):
        valid_season = self._validate_season(season)
        valid_season_type = self._validate_season_type(season_type)
        if not valid_season or not valid_season_type:
            return None
        else:
            return ep.TeamGameLog(team_id=self.team_id, season=season, season_type_all_star=season_type, **kwargs)