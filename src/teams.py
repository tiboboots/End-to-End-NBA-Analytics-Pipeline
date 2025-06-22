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
        all_team_ids = self.get_all_team_ids()
        try:
            self.team_id = all_team_ids[self.full_team_name.strip().title()]
        except KeyError as k:
            print(f"KeyError: {k}")
            self.team_id = None

    def team_roster(self, season: int) -> ep.CommonTeamRoster:
        roster = ep.CommonTeamRoster(team_id= self.team_id, season=season)
        return roster
    
    def team_year_by_year_stats(self, per_mode: str = "PerGame") -> ep.TeamYearByYearStats:
        team_stats = ep.TeamYearByYearStats(team_id=self.team_id, per_mode_simple=per_mode)
        return team_stats
    
    def team_game_stats(self, season: str, season_type: str = "Regular Season") -> ep.TeamGameLog:
        game_stats = ep.TeamGameLog(team_id=self.team_id, season=season, season_type_all_star=season_type)
        return game_stats
    
    def team_diff_lineups(self, season: str, season_type: str = "Regular Season") -> ep.TeamDashLineups:
        team_lineup_data = ep.TeamDashLineups(team_id=self.team_id, season=season, season_type_all_star=season_type)
        return team_lineup_data