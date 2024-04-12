def structure (names, goals, goals_avoided, assists):
    players = {}
    for n, g, ga, a in zip(names,goals,goals_avoided,assists):
        players[n] = {
            "goles_a_favor": g,
            "goles_evitados": ga,
            "asistencias": a
        }
    return players

def get_goal_scorer (players):
    name, goals = max(players, key=lambda x: x["goles_a_favor"])
    return name, goals
