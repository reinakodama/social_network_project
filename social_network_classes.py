import social_network_ui

# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        #json.load(file)
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        #implement function that creates account here
        name = input("Enter full name: ")
        age = input("Enter age: ")
        print("Creating ...")
        account = Person(name, age)
        self.list_of_people.append(account)
        print("Your account has been recorded")
        pass


class Person:
    messages = []
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []

    def add_friend(self):
        #implement adding friend. Hint add to self.friendlist
        friend = input("friend you want to add: ")
        self.friendlist.append(friend)
        pass

    def edit_details(self):
        edit_details_choice = social_network_ui.manageEditDetails()
        if edit_details_choice == "1":
            self.id = input("Enter edited name: ")
        elif edit_details_choice == "2":
            self.year = input("Enter edited age: ")
        elif edit_details_choice == "3":
            inner_menu_choice = social_network_ui.manageAccountMenu()
        else:
            print("invalid input")
            edit_details_choice = social_network_ui.manageEditDetails()
    
        
    def send_message(self):
        #implement sending message to friend here
        # recipient = None
        # recipientName = input("Who are you sending the message to?: ")
        # for user in self.friendlist:
        #     if recipientName == user.id:
        #         recipientName = user
        recipientName = input("Who are you sending the message to?: ")
        text = input("Type message here: ")
        Person.messages.append(text) #how to make this the recieving end
        print(recipientName, "has recieved the message: ", text)
        pass

    def block(self):
        bad_friend = input("friend you want to block: ")
        self.friendlist.remove(bad_friend)
        print(bad_friend , "has been blocked")


# class message:
#     messages = []
        
#     def send_message(self):
#         #implement sending message to friend here
#         recipient = None
#         recipientName = input("Who are you sending the message to?: ")
#         for user in self.friendlist:
#             if recipientName == user.name:
#                 recipientName = user
#         text = input("Type message here: ")
#         message.messages.append(text) #how to make this the recieving end
#         print(personn, "has recieved the message: ", message)
#         pass


        


