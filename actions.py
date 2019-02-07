# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "MG"
my_age = -1
my_bio = "Graduated fro USA in 2018, "
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
    # your code goes here!
    print ("""Would you like to: \n 1) Create a new club. \n or: \n 2)Browse and join clubs. \n or: \n 3) View existing clubs.\n or: n\ 4) Display members of clubs. \n or: \n -1) Close application.""")
    number = input("Enter a number please ")
    if number == 1: 
        create_club()
    elif number == 2:
        join_clubs()
    elif number == 3:
        view_clubs()
    elif number == 4:
        view_club_members()
    else:
        print ("You didnt choose anything")
        exit
        

def create_club():
    # your code goes here!
    club_name = input("Create a name for your club: ")
    club_target = input("what is your club about: ")
    user_club = Club(club_name, club_target)
    print ("how many people you would like to be in your club?")
    index = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
    i = 0
    #overseer = []
    for contender in population:
        print ("[%s] %s" % (index[i], contender.name))
        for x in index:
            int(x)
        i += 1
    while True:
            user_input = int(input())
            if user_input in [1, 2, 3, 4,5, 6, 7, 8, 9, 10, 11, 12, 14, 15]:
                user_club.recruit_member(population[uesr_index-1])
                #overseer.append(user_input)
            elif user_input == -1:
                user_club.recruit_member(myself)
                user_club.assign_president(myself)
                #overseer.append(my_name)
            elif user_input == 0 :
                break
            else:
                print ("please input an valid number:")
            print ("your cloub is: ")
            print (user_club.name)
            print (user_club.description)
            print ("members:")
            user_club.print_member_list()
            total = 0 
            for member in user_club.members:
                total += member.my_age
            print ("average age in the club: %s years" % (total/len(user_club.members)))
            clubs.append(user_club)
            options

    

def view_clubs():
    # your code goes here!
    for club in clubs:
        print ("name: %s" %(club.name))
        print ("description: %s" %(club.description))
        print ("members %d" %(club.members))

    

def view_club_members():
    # your code goes here!
    #for club in clubs:
       # print ("name: %s" %(club.name))
       # print ("description: %s" %(club.description))
       # print ("members %d" %(club.members))
    #club_name = input("Enter the name of the clue to see the member in it:")
    view_clubs()
    club_name = input("Enter the name of the club to see the member in it: ")
    for club in clubs:
        if club.name == club_name:
            club.print_member_list()
            break
    else:
        print ("no such a club that muches your input ")
    options()
            

    

def join_clubs():
    # your code goes here!
    view_clubs()
    club_name = input("Enter the name of the club you want to join: ")
    for club in clubs:
        if club.name == club_name.lower:
            club.recruit_member_list()
            print ("%s your now member of %s" %(my_name,club.name))
            break
    else:
        print ("no such a club that muches your input ")
    options()

def application():
    introduction()
    # your code goes here!
    
