import nba_api.stats.endpoints as ep

class NBA:
    @staticmethod
    def league_player_stats(season: str, season_type_all_star: str = "Regular Season", **kwargs):
        return ep.LeagueDashPlayerStats(season=season, season_type_all_star=season_type_all_star, **kwargs)
    
    @staticmethod
    def league_team_stats(season: str, season_type_all_star: str = "Regular Season", **kwargs):
        return ep.LeagueDashTeamStats(season=season, season_segment_nullable=season_type_all_star, **kwargs)
    
    @staticmethod
    def league_team_shot_location_stats(season: str, season_type_all_star: str = "Regular Season", **kwargs):
        return ep.LeagueDashTeamShotLocations(season=season, season_type_all_star=season_type_all_star, **kwargs)
    
    @staticmethod
    def league_player_shot_location_stats(season: str, season_type_all_star: str="Regular Season", **kwargs):
        return ep.LeagueDashPlayerShotLocations(season=season, season_type_all_star=season_type_all_star, **kwargs)
    
    @staticmethod
    def league_hustle_stats_player(season: str, season_type_all_star: str="Regular Season", **kwargs):
        return ep.LeagueHustleStatsPlayer(season=season, season_type_all_star=season_type_all_star, **kwargs)
    
    @staticmethod
    def league_hustle_stats_team(season: str, season_type_all_star: str="Regular Season", **kwargs):
        return ep.LeagueHustleStatsTeam(season=season, season_type_all_star=season_type_all_star, **kwargs)
    
    @staticmethod
    def league_standings(season: str):
        return ep.LeagueStandingsV3(season=season)
    
    @staticmethod
    def league_clutch_player_stats(season: str, season_type_all_star: str="Regular Season", **kwargs):
        return ep.LeagueDashPlayerClutch(season=season, season_type_all_star=season_type_all_star, **kwargs)