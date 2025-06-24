import nba_api.stats.endpoints as ep

class NBA:
    @staticmethod
    def league_player_stats(season: str, per_mode_detailed: str = "Totals", 
                            season_type_all_star: str = "Regular Season", **kwargs):
        return ep.LeagueDashPlayerStats(season=season, season_type_all_star=season_type_all_star, 
                                        per_mode_detailed= per_mode_detailed, **kwargs)
    
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