def get_structure (names, goals, goals_avoided, assists):
    players_list = {}
    for n, g, ga, a in zip(names,goals,goals_avoided,assists):
        players_list[n] = {
            "goles_a_favor": g,
            "goles_evitados": ga,
            "asistencias": a
        }
    return players_list

def get_goal_scorer(players_list):
    name, stats = max(players_list.items(), key=lambda x: x[1]["goles_a_favor"])
    return name, stats["goles_a_favor"]

def get_influential_player(players_list):
    max_score = float ("-inf")
    influential_player = None
    for player in players_list:
        score = players_list[player]["goles_a_favor"] * 1.5 + players_list[player]["goles_evitados"] * 1.25 + players_list[player]["asistencias"] 
        if score > max_score:
            max_score=score
            influential_player=player
    return influential_player

def get_team_goal_average (players_list):
    matches_played = 25
    goals = 0
    for player in players_list:
        goals += players_list[player]["goles_a_favor"]
    return goals/matches_played

def get_goal_scorer_goal_average (players_list):
    matches_played = 25
    goal_scorer, goals = get_goal_scorer (players_list)
    return goals/matches_played