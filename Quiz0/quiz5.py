PLAYERS = {
    'Karim Benzema': 94,  # The player's name: his rating
    'Robert Lewandowski': 93,
    'Kylian Mbappe': 96,
    'Luka Modric': 90,
    'Pedri': 93,
    'Frenkie de Jong': 88,
}

LEGENDARIES = {
    'Lionel Messi': (99, 1.03),
    # Thelegendary player's name: (his rating, his chemistry booster value)
    'Cristiano Ronaldo': (97, 0.98),
}

import math
class Team:
    squad=None
    if squad is None:
        squad=[]
    
    def __init__(self,name, initial_players,):
        self.name=name
        self.initial_players=initial_players     

    def __str__(self):
        """Return a string representation of this team, including the team name and squad.

        Returns:
            str: A string representation of the team.
        """
        return f"team name{self.name} has{self.squad}"
    
    def draft(self,player):
        for player in PLAYERS:
            if player==player:
                self.squad.append(player)
        return self.squad
    
    def calc_rating(self):
        if self.squad==None:
            self.rating=0
        else:
            self.rating=math.average(self.rating)
        return self.rating

   

    def draft_legendary(self, player):
        """Draft a legendary player from LEGENDARIES and update the team's rating, which is the average rating of the entire current squad multiplied by the legendary player's booster.

        Args:
            player (str): The name of the legendary player to be drafted.
        """
        for player in LEGENDARIES:
            if player==player:
                self.squad.append(player[0])
                self.rating=self.rating*player[1]
            return self.squad,self.rating
    
    def __gt__(self,other):
        if self.rating >other.rating:
            return self.rating>other.rating


#############################################
# Please DO NOT change code in main function!
#############################################
def main():
    real_madrid = Team('Real Madrid', initial_players=['Karim Benzema'])
    barcelona = Team('Barcelona')
    print('Before drafting squad:')
    print(real_madrid)
    print(barcelona)



    # print()
    # print('After drafting squad:')
    # barcelona.draft('Robert Lewandowski')
    # real_madrid.draft('Kylian Mbappe')
    # barcelona.draft('Pedri')
    # real_madrid.draft('Luka Modric')
    # barcelona.draft('Frenkie de Jong')
    # print(real_madrid)
    # print(barcelona)
    # print()
    # print('Will Barcelona defeat Real Madrid?')
    # print(barcelona > real_madrid)
    # print()
    # print('After drafting legendary:')
    # real_madrid.draft_legendary('Cristiano Ronaldo')
    # barcelona.draft_legendary('Lionel Messi')
    # print(real_madrid)
    # print(barcelona)
    # print()
    # print('Will Barcelona defeat Real Madrid?')
    # print(barcelona > real_madrid)


if __name__ == '__main__':
    main()

        

