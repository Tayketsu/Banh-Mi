import sys
sys.path.append("/".join(x for x in __file__.split("/")[:-1]))
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition
from bookingbanner import bookingBanner
import datetime
from friendbanner import FriendBanner
from kivy.utils import platform
#import requests
from ResourceUpdate import update_bookings
import helperfunctions
from kivy.uix.popup import Popup
from kivy.uix.label import Label


##############################################################################
#################### Import client functions to send data to server #########
from client import 


class HomeScreen(Screen):
    pass

class AddFriendScreen(Screen):
    pass

class AddbookingScreen(Screen):
    pass

class FriendbookingScreen(Screen):
    pass

class FriendsListScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class ChangeAvatarScreen(Screen):
    pass

#GUI =   # Make sure this is after all class definitions!
class MainApp(App):
    my_friend_id = ""
    booking_image = None
    option_choice = None
    booking_image_widget = ""
    previous_booking_image_widget = None
    friends_list = ""
    refresh_token_file = "refresh_token.txt"
    nicknames = {}  # Dictionary of nicknames for each friend id in friends list
    their_friend_id = ""  # Make it so we know which friend's booking screen has been loaded for app.set_friend_nickname
 #   my_firebase = None  # Reference to class in myfirebase.py
    
#    def build(self):
#        print("BEFORE")
##       self.my_firebase = MyFirebase()
##       print(self.my_firebase)
#        print("AFTER")
#        
#        if platform == 'ios':
#            self.refresh_token_file = App.get_running_app().user_data_dir + self.refresh_token_file
#        return Builder.load_file("main.kv")#GUI

    def on_start(self):
            # Populate friends list grid
            friends_list_array = self.friends_list.split(",")
            for friend_id in friends_list_array:
                friend_id = friend_id.replace(" ", "")
                if friend_id == "":
                    continue
                if friend_id in self.nicknames.keys():
                    friend_id_text = "[u]" + self.nicknames[friend_id] + "[/u]"
                else:
                    friend_id_text = "[u]Friend ID: " + friend_id + "[/u]"
                friend_banner = FriendBanner(friend_id=friend_id, friend_id_text=friend_id_text)
                self.root.ids['friends_list_screen'].ids['friends_list_grid'].add_widget(friend_banner)

            self.change_screen("home_screen", "None")

#        except Exception as e:
#            traceback.print_exc()
#            pass
    
    
    def add_booking(self):
        ids = self.root.ids['add_booking_screen'].ids
        
        # F1: Startingtime, Endtime, Starting Date
        timeOutput = ids['time_input'].text.replace("\n","")        
        endtimeOutput = ids['end_input'].text.replace("\n","")
        dayOutput = ids['day_input'].text.replace("\n","")
        monthOutput = ids['month_input'].text.replace("\n","")
        yearOutput = ids['year_input'].text.replace("\n","")

        hour = int(timeOutput[0:2])
        minute = int(timeOutput[3:5])
        date = datetime.datetime(int(yearOutput), int(monthOutput), int(dayOutput), hour, minute)
        date_string = date.isoformat()
        endhour = int(endtimeOutput[0:2])
        endminute = int(endtimeOutput[3:5])
        dateend = datetime.datetime(int(yearOutput), int(monthOutput), int(dayOutput), endhour, endminute)
        date_stringend = date.isoformat()
        #costs
        resultatedCosts = 5
        
        weekdays = [0,1,0,1,0,1,0]
        userid = 100
        recbook={"Weekday": weekdays, "Time":date_string, "Endtime": date_stringend, "UserID": userid}
        send_recbook_to_server(recbook)
        update_bookings(recbook)
        # Popup with F1 information
        popup = Popup(title='Overview',
        content=Label(text="From: " + timeOutput +", until: "+endtimeOutput + ", Price:" +str(resultatedCosts)+ "€ \n \n"+"Startingdate:"+dayOutput+" \ "+monthOutput+ " \ " + yearOutput),
        size_hint=(None, None), size=(400, 400))
        popup.open()
        print(weekdayflag)
    
# TO DO - Toggle    


#Reload the Serial booking Screen
    def load_friend_booking_screen(self, friend_id, widget):
        # Initialize friend streak label to 0
        friend_streak_label = self.root.ids['friend_booking_screen'].ids['friend_streak_label']
        friend_streak_label.text = "0 Day Streak"


        # Make it so we know which friend's booking screen has been loaded for app.set_friend_nickname
        self.their_friend_id = friend_id

        # Get their bookings by using their friend id to query the database
#        friend_data_req = requests.get('https://friendly-fitness.firebaseio.com/.json?orderBy="my_friend_id"&equalTo=' + friend_id)

        friend_data = friend_data_req.json()
        bookings = friend_data.values()[0]['bookings']

        friend_banner_grid = self.root.ids['friend_booking_screen'].ids['friend_banner_grid']

        # Remove each widget in the friend_banner_grid
        for w in friend_banner_grid.walk():
            if w.__class__ == bookingBanner:
                friend_banner_grid.remove_widget(w)

        # Populate their avatar image
        friend_avatar_image = self.root.ids.friend_booking_screen.ids.friend_booking_screen_image
        friend_avatar_image.source = "icons/avatars/" + friend_data.values()[0]['avatar']

        # Populate their friend ID and nickname
        print("Need to populate nickname")
        their_friend_id_label = self.root.ids.friend_booking_screen.ids.friend_booking_screen_friend_id
        if friend_id in self.nicknames.keys():
            their_friend_id_label.text = "[u]" + self.nicknames[friend_id] + "[/u]"
        else:
            their_friend_id_label.text = "[u]Nickname[/u]"

        # Populate the friend_booking_screen
        # Loop through each key in the bookings dictionary
        #    for the value for that key, create a booking banner
        #    add the booking banner to the scrollview
        if bookings == {} or bookings == "":
            # Change to the friend_booking_screen
            self.change_screen("friend_booking_screen")
            return
        booking_keys = bookings.keys()
        booking_keys.sort(key=lambda value: datetime.strptime(bookings[value.encode()]['date'].encode('utf-8'), "%m/%d/%Y"))
        booking_keys = booking_keys[::-1]


        # Populate the streak label
        friend_streak_label.text = helperfunctions.count_booking_streak(bookings) + " Day Streak"


        # Change to the friend_booking_screen
        self.change_screen("friend_booking_screen")

    def change_screen(self, screen_name, direction='forward', mode = ""):
        # Get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager']
        #print(direction, mode)
        # If going backward, change the transition. Else make it the default
        # Forward/backward between pages made more sense to me than left/right
        if direction == 'forward':
            mode = "push"
            direction = 'left'
        elif direction == 'backwards':
            direction = 'right'
            mode = 'pop'
        elif direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return

        screen_manager.transition = CardTransition(direction=direction, mode=mode)

        screen_manager.current = screen_name
    
MainApp().run()
