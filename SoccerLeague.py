#############  Player Class #############
import random

class Player:
  
  def __init__(self, name: str, position: str, rating: int, goals_scored: int):
    self.name = name
    self.position = position
    self.rating = rating
    self.goals_scored = goals_scored
    self._value = None
  
  def __str__(self):
    return f'Name : {self.name} \nPosition: {self.position} \nRatings: {self.rating} \nGoals: {self.goals_scored} \nValue: ${self.value}\n'
  
  def score_goal(self):
    self.goals_scored += 1


  @property
  def value(self):
    if self._value is not None:
      return self._value
    return round(self.rating*10_00_00_00)
    
  @value.setter
  def value(self, custom_value: int):
    if custom_value < 0:
      raise ValueError("Negative value is not possible")
    self._value = custom_value

###### example ##### 
"""
Messi = Player("Leo Messi", "Winger",9.5, 91)
print(Messi)

Messi.value = 100000000
print(Messi)

Cristiano = Player("Cristiano Ronaldo", "Winger",9.4, 72)
Cristiano.value = 80000000
print(Cristiano)
"""

#############  Team Class #############

# Team
# Attributes: name, players (list), points, goals_for, goals_against

# Methods: add_player(), remove_player(), team_rating()

# Dunder: __str__ and __len__ (number of players)

# Logic: Auto-calculate rating based on average of players

class Team:
  
  def __init__(self, name: str, players=None, points=0, goals_for=0, goals_against=0):
    self.name = name
    self.players = players if players is not None else []
    self.points = points
    self.goals_for = goals_for
    self.goals_against = goals_against
    
  def add_player(self, new_player: Player):
    self.players.append(new_player)
  
  def remove_player(self, player_tobe_removed: Player):
    if player_tobe_removed in self.players:
        self.players.remove(player_tobe_removed)
  
  def team_rating(self):
    total_points = 0
    for x in self.players:
      total_points = total_points + x.rating
    
    return total_points/len(self.players)
  
  def __str__(self):
        return (
            f"Team: {self.name}\n"
            f"Points: {self.points} | Goals For: {self.goals_for} | Goals Against: {self.goals_against}\n"
            f"Players:\n" + "\n".join(str(p) for p in self.players)
        )
  
  def __len__(self):
    return f"Number of players: {len(self.players)}"
  
  # FC Barcelona Players
barcelona_players = [
    Player("Marc-André ter Stegen", "Goalkeeper", 90, 0),
    Player("Jules Koundé", "Defender", 85, 0),
    Player("Ronald Araújo", "Defender", 86, 1),
    Player("Alejandro Balde", "Defender", 83, 0),
    Player("Frenkie de Jong", "Midfielder", 87, 2),
    Player("Pedri", "Midfielder", 88, 4),
    Player("Gavi", "Midfielder", 85, 3),
    Player("Raphinha", "Forward", 84, 9),
    Player("Robert Lewandowski", "Forward", 89, 3),
    Player("Lamine Yamal", "Forward", 82, 3),
    Player("Ferran Torres", "Forward", 83, 4),
]

# Real Madrid Players
real_madrid_players = [
    Player("Thibaut Courtois", "Goalkeeper", 91, 0),
    Player("Dani Carvajal", "Defender", 85, 1),
    Player("Antonio Rüdiger", "Defender", 86, 3),
    Player("Aurélien Tchouaméni", "Midfielder", 87, 2),
    Player("Federico Valverde", "Midfielder", 88, 9),
    Player("Jude Bellingham", "Midfielder", 89, 13),
    Player("Vinícius Júnior", "Forward", 90, 21),
    Player("Rodrygo", "Forward", 85, 14),
    Player("Kylian Mbappé", "Forward", 92, 36),
    Player("Brahim Díaz", "Forward", 83, 6),
    Player("Arda Güler", "Midfielder", 80, 5),
]

# Creating Team Instances
barcelona = Team("FC Barcelona", barcelona_players)
real_madrid = Team("Real Madrid", real_madrid_players)

print(barcelona)
print("\n" + "-"*50 + "\n")
print(real_madrid)


#######

# 🔹 Match
# Attributes: home_team, away_team, home_goals, away_goals

# Method: simulate() – randomly assigns goals, updates team stats

# Dunder: __str__ for match summary

# 🔹 League
# Attributes: teams (list)

# Methods: play_week(), show_standings(), transfer_player()

# File I/O (optional): Save/load standings or team data

#######

class Match():
  
  def __init__(self, home_team: Team, away_team: Team, home_goals = 0, away_goals = 0):
    self.home_team = home_team
    self.away_team = away_team
    self.home_goals =  home_goals
    self.away_goals = away_goals
    
  def simulate(self):
    homeRandomScore = random.randrange(5)
    awayRandomScore = random.randrange(5)
    
    self.home_goals = homeRandomScore
    self.away_goals = awayRandomScore
    
  def __str__(self):
    
    return f'Final Score: {self.home_team} {self.home_goals} - {self.away_team} {self.away_goals}'