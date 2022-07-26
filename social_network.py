#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui

#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                current_user = None
                currentUserName = input("name of current user: ")
                for person in ai_social_network.list_of_people:
                    if currentUserName == person.id:
                        current_user = person
                if inner_menu_choice == "7":
                    break
                elif inner_menu_choice == "1":
                    print("You are now in the edit my details menu")
                    current_user.edit_details()
                    break
                elif inner_menu_choice == "2":
                    print("You are now in the add a friend menu")
                    current_user.add_friend()
                    break
                elif inner_menu_choice == "3":
                    print("You are now in the view all my friends menu")
                    print(current_user.friendlist)
                    break
                elif inner_menu_choice == "4":
                    print("You are now in the send a message menu")
                    current_user.send_message()
                    break
                elif inner_menu_choice == "5":
                    print("You are now in the view all my messages menu")
                    print(current_user.messages)
                    break
                elif inner_menu_choice == "6":
                    current_user.block()
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()


        elif choice == "3":
            print("Thank you for visiting. Goodbye3")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        