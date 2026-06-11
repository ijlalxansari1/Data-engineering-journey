class ucl:
    def __init__(self, club,city, titles , goals):
        self.club = club
        self.city = city
        self.titles = titles
        self.goals = goals


    def display_info (self):
        print(f"{self.club} is from {self.city} , has {self.titles} UCL titles and have scored {self.goals} goals.")

    def is_elite(self):
       if self.titles >= 10 and self.goals >= 1000 :
           print(f"{self.club} is an elite club.")
       else:
           print(f"{self.club} is a strong club.")


    def comparision(self , other_club):
        if self.titles > other_club.titles:
           print(f"{self.club} has more UCL titles than {other_club.club}.")
        elif self.titles == other_club.titles:
           print(f"{self.club} has same UCL titles as {other_club.club}.")
        else:
            print(f"{self.club} has less UCL titles than {other_club.club}.")


Barcelona = ucl("FC Barcelona" , "Barcelona" , 5,762)
Barcelona.display_info()
Barcelona.is_elite()
Realmadrid = ucl("Real Madrid" , "Madrid" , 15, 1137)
Realmadrid.display_info()
Realmadrid.is_elite()

Bayernmunich = ucl("Bayern Munich" ,"Bavaria" , 6 , 760)
Bayernmunich.display_info()
Bayernmunich.is_elite()


Bayernmunich.comparision(Barcelona)
Barcelona.comparision(Realmadrid)
Realmadrid.comparision(Barcelona)
Realmadrid.comparision(Bayernmunich)
Barcelona.comparision(Bayernmunich)
