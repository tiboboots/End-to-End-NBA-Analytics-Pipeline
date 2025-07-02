from dataclasses import dataclass, field
import nba_api.stats.endpoints as ep

@dataclass
class Player:
    player_id: int
    season: str
    season_type_all_star: str
    
    def player_game_stats(self):
        return ep.PlayerGameLog(player_id=self.player_id, season=self.season, season_type_all_star=self.season_type_all_star)