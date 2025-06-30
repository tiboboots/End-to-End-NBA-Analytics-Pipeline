import nba_api.stats.endpoints as ep
from dataclasses import dataclass, field

@dataclass
class NBA:
    season: str
    season_type_all_star: str
        
    def league_team_shot_locations(self):
        return ep.LeagueDashTeamShotLocations(season=self.season, 
                                              season_type_all_star=self.season_type_all_star)
    
    def league_player_shot_locations(self):
        return ep.LeagueDashPlayerShotLocations(season=self.season, 
                                                season_type_all_star=self.season_type_all_star)