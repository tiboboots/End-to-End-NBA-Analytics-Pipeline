import logging
import nba_api.stats.endpoints as ep
from decorators import log
from nba_api.stats.static import teams

logger = logging.getLogger(__name__)

@log()
def extract_game_logs(season: str, player_or_team_abbreviation: str, 
                      season_type_all_star: str = "Regular Season") -> dict:
    
    return ep.LeagueGameLog(season=season, 
                            player_or_team_abbreviation=player_or_team_abbreviation.upper(),
                            season_type_all_star=season_type_all_star).get_dict()


@log()
def extract_shot_locations(season: str, player_or_team: str, 
                           season_type_all_star: str = "Regular Season") -> dict:
    
    if player_or_team.lower() == "player":
        return ep.LeagueDashPlayerShotLocations(season=season, season_type_all_star=season_type_all_star).get_dict()
    
    elif player_or_team.lower() == "team":
        return ep.LeagueDashTeamShotLocations(season=season,season_type_all_star=season_type_all_star).get_dict()

    else:
        logger.error(f"Incorrect value for player_or_team parameter in extract_shot_locations", exc_info= True)
        raise ValueError

@log()
def extract_lineups(season: str, season_type_all_star: str = "Regular Season"):
    return ep.LeagueDashLineups(season=season, season_type_all_star=season_type_all_star).get_dict()

@log()
def extract_hustle_stats(season: str, player_or_team: str, season_type_all_star: str = "Regular Season"):
    if player_or_team.lower() == "player":
        return ep.LeagueHustleStatsPlayer(season=season, season_type_all_star=season_type_all_star).get_dict()
    elif player_or_team.lower() == "team":
        return ep.LeagueHustleStatsTeam(season=season, season_type_all_star=season_type_all_star).get_dict()
    else:
        logger.error(f"Incorrect value: {player_or_team} provided for player_or_team param in {extract_hustle_stats.__name__} function")
        raise ValueError   