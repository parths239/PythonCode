import random

############# Player Class #############
class Player:
    def __init__(self, name: str, position: str, rating: int, goals_scored: int = 0):
        self.name = name
        self.position = position
        self.rating = rating
        self.goals_scored = goals_scored
        self._value = None

    def __str__(self):
        return f"{self.name} ({self.position}) | Rating: {self.rating} | Goals: {self.goals_scored}"

    @property
    def value(self):
        if self._value is None:
            self._value = self.rating * 10000 + self.goals_scored * 500
        return self._value


############# Team Class #############
class Team:
    def __init__(self, name: str, players: list):
        self.name = name
        self.players = players
        self.points = 0
        self.goals_for = 0
        self.goals_against = 0

    def add_player(self, player: Player):
        self.players.append(player)

    def __str__(self):
        return f"{self.name}: {self.points} pts | GF: {self.goals_for}, GA: {self.goals_against}"


############# Match Class #############
class Match:
    def __init__(self, home_team: Team, away_team: Team):
        self.home_team = home_team
        self.away_team = away_team
        self.home_goals = 0
        self.away_goals = 0

    def simulate(self):
        self.home_goals = random.randint(0, 5)
        self.away_goals = random.randint(0, 5)

        self.home_team.goals_for += self.home_goals
        self.home_team.goals_against += self.away_goals
        self.away_team.goals_for += self.away_goals
        self.away_team.goals_against += self.home_goals

        if self.home_goals > self.away_goals:
            self.home_team.points += 3
        elif self.home_goals < self.away_goals:
            self.away_team.points += 3
        else:
            self.home_team.points += 1
            self.away_team.points += 1

    def __str__(self):
        return f"{self.home_team.name} {self.home_goals} - {self.away_goals} {self.away_team.name}"


############# League Class #############
class League:
    def __init__(self, teams: list):
        self.teams = teams

    def play_week(self):
        print("\n🔹 Playing a week of matches...\n")
        matchups = [(self.teams[i], self.teams[i + 1]) for i in range(0, len(self.teams) - 1, 2)]
        for home, away in matchups:
            match = Match(home, away)
            match.simulate()
            print(match)

    def show_standings(self):
        print("\n📊 League Standings:")
        sorted_teams = sorted(self.teams, key=lambda t: t.points, reverse=True)
        for team in sorted_teams:
            print(team)


############# Sample Players #############

barca_players = [
    Player("Robert Lewandowski", "ST", 88),
    Player("Pedri", "CM", 85),
    Player("Frenkie de Jong", "CM", 86),
    Player("Raphinha", "RW", 83),
    Player("João Félix", "LW", 84),
]

madrid_players = [
    Player("Vinicius Jr", "LW", 89),
    Player("Jude Bellingham", "CM", 87),
    Player("Rodrygo", "RW", 85),
    Player("Toni Kroos", "CM", 86),
    Player("Aurélien Tchouaméni", "CDM", 84),
]

############# Teams #############

barcelona = Team("FC Barcelona", barca_players)
madrid = Team("Real Madrid", madrid_players)

############# League Simulation #############

la_liga = League([barcelona, madrid])
la_liga.play_week()
la_liga.show_standings()
