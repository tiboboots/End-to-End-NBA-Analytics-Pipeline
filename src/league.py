import nba_api.stats.endpoints as ep

class NBA:
    @staticmethod
    def league_player_stats(season: str, season_type_all_star: str = "Regular Season", **kwargs):
        return ep.LeagueDashPlayerStats(season=season, season_type_all_star=season_type_all_star, **kwargs)
    
    @staticmethod
    def league_team_stats(season: str, season_type_all_star: str = "Regular Season", **kwargs):
        return ep.LeagueDashTeamStats(season=season, season_segment_nullable=season_type_all_star, **kwargs)
    
    @staticmethod
    def league_team_shot_location_stats(**kwargs):
        return ep.LeagueDashTeamShotLocations(**kwargs)
    
    @staticmethod
    def league_player_shot_location_stats(**kwargs):
        return ep.LeagueDashPlayerShotLocations(**kwargs)
    
    @staticmethod
    def league_hustle_stats_player(**kwargs):
        return ep.LeagueHustleStatsPlayer(**kwargs)
    
    @staticmethod
    def league_hustle_stats_team(**kwargs):
        return ep.LeagueHustleStatsTeam(**kwargs)
    
    @staticmethod
    def league_standings(season: str):
        return ep.LeagueStandingsV3(season=season)
    
    @staticmethod
    def league_clutch_player_stats(**kwargs):
        return ep.LeagueDashPlayerClutch(**kwargs)