import nba_api.stats.endpoints as ep
from dataclasses import dataclass, field

@dataclass
class NBA:
    season: str
    season_type_all_star: str

    def __post_init__(self):
        self.season_type_all_star = self.season_type_all_star.title()
        valid_season_types = {"Regular Season", "Playoffs"}
        if self.season_type_all_star not in valid_season_types:
            raise ValueError(f"Season type is invalid. Must be one of: {valid_season_types}")
        if len(self.season) != 4 or not self.season.isdigit():
            raise ValueError(f"Invalid season format: {self.season}. Format should be YYYY.")
        
    def league_team_shot_locations(self):
        return ep.LeagueDashTeamShotLocations(season=self.season, 
                                              season_type_all_star=self.season_type_all_star)
    
    def league_player_shot_locations(self):
        return ep.LeagueDashPlayerShotLocations(season=self.season, 
                                                season_type_all_star=self.season_type_all_star)