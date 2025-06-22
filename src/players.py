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
            player_name = player['full_name'].lower()
            all_player_ids[player_name] = player_id
        return all_player_ids

    def __post_init__(self):
        all_player_ids = self.get_all_player_ids()
        try:
            self.player_id = all_player_ids[self.player_full_name.strip().lower()]
        except KeyError as k:
            print(f"KeyError: {k}")
            self.player_id = None

    def player_career_stats(self, per_mode: str = "PerGame") -> ep.playercareerstats.PlayerCareerStats:
        player_stats = ep.playercareerstats.PlayerCareerStats(player_id=self.player_id, per_mode36=per_mode)
        return player_stats