import nba_api.stats.endpoints as ep
from dataclasses import dataclass, field
import pandas as pd

@dataclass
class NBA:
    season: str
    season_type_all_star: str = "Regular Season"

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
    
@dataclass
class Game:
    game_id: int = field(init=False)
    game_date: str = None # YYYY-MM-DD
    home_team_name_short: str
    away_team_name_short: str
    season: str
    season_type_all_star: str = "Regular Season"

    def __post_init__(self):
        self.home_team_name_short = self.home_team_name_short.strip().upper()
        self.away_team_name_short = self.away_team_name_short.strip().upper()

    def game_finder(self):
        df = ep.LeagueGameLog(season=self.season, 
                                     season_type_all_star=self.season_type_all_star).get_data_frames()[0]

        filtered_games = df[df['MATCHUP'].str.contains(self.home_team_name_short) 
                            & df['MATCHUP'].str.contains(self.away_team_name_short)
                            & df['GAME_DATE'] == self.game_date]
    
    def box_score(self):
        return ep.BoxScoreTraditionalV3(game_id=self.game_id)
    
    def box_score_misc(self):
        return ep.BoxScoreMiscV3(game_id=self.game_id)
    
    def box_score_matchups(self):
        return ep.BoxScoreMatchupsV3(game_id=self.game_id)
    
    def box_score_hustle(self):
        return ep.BoxScoreHustleV2(game_id=self.game_id)
    
    def box_score_defense(self):
        return ep.BoxScoreDefensiveV2(game_id=self.game_id)