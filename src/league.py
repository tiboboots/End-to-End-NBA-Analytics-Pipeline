import nba_api.stats.endpoints as ep

class NBA:
    @staticmethod
    def league_player_stats(**kwargs):
        return ep.LeagueDashPlayerStats(**kwargs)
    
    @staticmethod
    def league_team_stats(**kwargs):
        return ep.LeagueDashTeamStats(**kwargs)
    
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