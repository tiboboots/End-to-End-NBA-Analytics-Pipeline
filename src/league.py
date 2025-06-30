import nba_api.stats.endpoints as ep
from dataclasses import dataclass

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
    
    def league_game_stats(self):
        return ep.LeagueGameLog(season=self.season, season_type_all_star=self.season_type_all_star)
    
    def box_score(self, game_id: int):
        return ep.BoxScoreTraditionalV3(game_id=game_id)