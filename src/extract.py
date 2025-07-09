import logging
import nba_api.stats.endpoints as ep

logger = logging.getLogger(__name__)

def extract_game_logs(season: str, player_or_team_abbreviation: str, 
                      season_type_all_star: str = "Regular Season") -> dict:
    
    return ep.LeagueGameLog(season=season, 
                            player_or_team_abbreviation=player_or_team_abbreviation.upper(),
                            season_type_all_star=season_type_all_star).get_dict()


def extract_team_roster(season: str, team_id: int) -> dict:
    return ep.CommonTeamRoster(team_id=team_id, season=season).get_dict()


def extract_shot_locations(season: str, player_or_team: str, 
                           season_type_all_star: str = "Regular Season") -> dict:
    
    if player_or_team.lower() == "player":
        return ep.LeagueDashPlayerShotLocations(season=season, season_type_all_star=season_type_all_star).get_dict()
    
    elif player_or_team.lower() == "team":
        return ep.LeagueDashTeamShotLocations(season=season,season_type_all_star=season_type_all_star).get_dict()

    else:
        logger.error(f"Incorrect value for player_or_team parameter in extract_shot_locations", exc_info= True)
        raise ValueError
    

def extract_box_scores(game_id: str, box_score_type: str) -> dict:

    endpoints = {"traditional": ep.BoxScoreTraditionalV3,
                 "matchups": ep.BoxScoreMatchupsV3,
                 "hustle": ep.BoxScoreHustleV2,
                 "defense": ep.BoxScoreDefensiveV2,
                 "misc": ep.BoxScoreMiscV3}
    
    if box_score_type.lower() in endpoints:
        return endpoints[box_score_type](game_id=game_id).get_dict()

    else:
        logger.error(f"Invalid value provided for the box_score_type parameter: {box_score_type}", exc_info=True)
        raise ValueError 