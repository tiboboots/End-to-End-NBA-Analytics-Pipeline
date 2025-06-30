from dataclasses import dataclass, field
from nba_api.stats.static import players
import nba_api.stats.endpoints as ep

@dataclass
class Player:
    player_full_name: str
    player_id: int = field(init=False)

    def get_all_player_ids(self) -> dict:
        all_nba_players = players.get_players()
        all_player_ids = {}
        for player in all_nba_players:
            player_id = player['id']
            player_name = player['full_name']
            all_player_ids[player_name] = player_id
        return all_player_ids

    def __post_init__(self):
        self.player_full_name = self.player_full_name.strip().title()
        all_player_ids = self.get_all_player_ids()
        if self.player_full_name in all_player_ids:
            self.player_id = all_player_ids[self.player_full_name]
        else:
            raise KeyError(f"Could not retrieve player id for {self.player_full_name}")
    
    def player_game_stats(self, season: str, season_type: str = "Regular Season", **kwargs):
        return ep.PlayerGameLog(player_id=self.player_id, season=season, 
                                season_type_all_star=season_type, **kwargs)