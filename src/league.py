import nba_api.stats.endpoints as ep
from dataclasses import dataclass

@dataclass
class NBA:
    season: str
    season_type_all_star: str

    def __post_init__(self):
        self.season_type_all_star = self.season_type_all_star.strip().title()
        
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
    
    def box_score_misc(self, game_id: int):
        return ep.BoxScoreMiscV3(game_id=game_id)
    
    def box_score_matchups(self, game_id: int):
        return ep.BoxScoreMatchupsV3(game_id=game_id)
    
    def box_score_hustle(self, game_id: int):
        return ep.BoxScoreHustleV2(game_id=game_id)
    
    def box_score_defense(self, game_id: int):
        return ep.BoxScoreDefensiveV2(game_id=game_id)