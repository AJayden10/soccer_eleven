import random

class Player:
    def __init__(self, name, position, stats):
        self.name = name
        self.position = position
        self.stats = stats

    def get_composite_score(self):
        return sum(self.stats.values()) / len(self.stats)

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def get_best_lineup(self, formation):
        lineup = {pos: [] for pos in formation}
        for position in formation:
            eligible_players = [p for p in self.players if p.position == position]
            eligible_players.sort(key=lambda x: x.get_composite_score(), reverse=True)
            lineup[position] = eligible_players[:formation[position]]
        return lineup

def get_player_stats(position):
    stats = {}
    print(f"Enter stats for {position} (0-100):")
    if position == 'GK':
        stats['Reflexes'] = int(input("Reflexes: "))
        stats['Positioning'] = int(input("Positioning: "))
        stats['Aerial Ability'] = int(input("Aerial Ability: "))
    elif position in ['CB', 'LB', 'RB']:
        stats['Tackling'] = int(input("Tackling: "))
        stats['Marking'] = int(input("Marking: "))
        stats['Physical'] = int(input("Physical: "))
    elif position in ['CM', 'CAM', 'CDM']:
        stats['Passing'] = int(input("Passing: "))
        stats['Vision'] = int(input("Vision: "))
        stats['Stamina'] = int(input("Stamina: "))
    else:  # Forwards (ST, LW, RW)
        stats['Finishing'] = int(input("Finishing: "))
        stats['Dribbling'] = int(input("Dribbling: "))
        stats['Pace'] = int(input("Pace: "))
    return stats

def main():
    team_name = input("Enter team name: ")
    team = Team(team_name)

    num_players = int(input("Enter number of players: "))
    for _ in range(num_players):
        name = input("Enter player name: ")
        position = input("Enter player position (GK/CB/LB/RB/CM/CAM/CDM/LW/RW/ST): ")
        stats = get_player_stats(position)
        player = Player(name, position, stats)
        team.add_player(player)

    formation = {
        'GK': 1, 'CB': 2, 'LB': 1, 'RB': 1,
        'CM': 2, 'CAM': 1, 'CDM': 1,
        'LW': 1, 'RW': 1, 'ST': 1
    }

    best_lineup = team.get_best_lineup(formation)

    print("\nBest Starting Lineup:")
    for position, players in best_lineup.items():
        for player in players:
            print(f"{position}: {player.name} (Score: {player.get_composite_score():.2f})")
            for stat, value in player.stats.items():
                print(f"  {stat}: {value}")

if __name__ == "__main__":
    main()

