from anvil.tables import app_tables
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.modules import cursor
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.screenmanager import SlideTransition
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
import sqlite3
from kivy.factory import Factory
from borrowerlanding import BorrowerLanding
from lender_landing import LenderLanding
import anvil
import server
KV = """


<DashScreen>:
    canvas.before:
        Color:
            rgba:  1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: "LOGO.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.97}
        size_hint: None, None
        size: "100dp", "100dp"

    Label:
        text: 'An RBI registered NBFC '
        font_size:dp(13)

        pos_hint: {'center_x': 0.5, 'center_y': 0.92}
        color:1/255, 26/255, 51/255, 1
        underline:"True"

    Image:
        source: "dashboardlogo.jpg"
        pos_hint: {'center_x': 0.5, 'center_y': 0.69}
        size_hint: None, None
        size: "200dp", "250dp"

    Label:
        id:username
        pos_hint: {'center_x': 0.5, 'center_y': 0.46}
        color: 1/255, 26/255, 51/255, 1
        bold:"True"
        font_size:dp(23)

    Label:
        text: 'Start your journey with us,'
        font_size:dp(20)
        pos_hint: {'center_x': 0.5, 'center_y': 0.52}
        color: 0, 0, 0, 1


    MDBoxLayout:
        orientation: 'horizontal'
        size_hint_x: None
        size_hint_y: None
        height: dp(90)
        width: dp(340)
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        padding: dp(10)  # Adding padding to the box layout
        spacing: dp(1)
        on_touch_down: if self.collide_point(*args[1].pos): root.go_to_borrower_landing()
    
        canvas:
            Color:
                rgba: 0.043, 0.145, 0.278, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [40, 40, 40, 40]  # rounded corners
    
        Image:
            source: "borrowerimg.png"
            size_hint: None, None
            size: dp(100), dp(80)
    
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_x: None
            width: dp(230)
    
            MDLabel:
                text: "Continue as a Borrower"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1  # White color
                halign: 'left'
                font_size: "20sp"
                font_name: "Roboto-Bold"
                
    
            MDLabel:
                text: "I'm looking to borrow"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1  # White color
                halign: 'left'
                font_size: "15sp"
                
            
    MDBoxLayout:
        orientation: 'horizontal'
        size_hint_x: None
        size_hint_y: None
        height: dp(90)
        width: dp(340)
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        padding: dp(10)  # Adding padding to the box layout
        spacing: dp(1)
        on_touch_down: if self.collide_point(*args[1].pos): root.go_to_lender_landing()



        canvas:
            Color:
                rgba: 0.043, 0.145, 0.278, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [40, 40, 40, 40]  # rounded corners


        Image:
            source: "lenderimg.png"
            size_hint_x: None
            width: dp(100)
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_x: None
            width: dp(230)
    
            MDLabel:
                text: "Continue as a Lender"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1  # White color
                halign: 'left'
                font_size: "20sp"
                font_name: "Roboto-Bold"
                
    
            MDLabel:
                text: "I'm looking to Invest"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1  # White color
                halign: 'left'
                font_size: "15sp"
            
            
"""


class DashScreen(Screen):
    Builder.load_string(KV)

    def get_email(self):
        data = anvil.server.call('another_method')
        return data

    def load_user_data(self):
        pass

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        log_email = anvil.server.call('another_method')
        profile = app_tables.fin_user_profile.search(email_user=log_email)
        print(log_email)

        email_user = []
        name_list = []
        for i in profile:
            # Check if email_user or full_name is None
            if i['email_user'] is not None and i['full_name'] is not None:
                email_user.append(i['email_user'])
                name_list.append(i['full_name'])

        # Check if log_email is None
        if log_email is not None:
            # Check if 'logged' is in the status list
            if log_email in email_user:
                log_index = email_user.index(log_email)
                self.ids.username.text = name_list[log_index]
            else:
                # Handle the case when 'logged' is not in the status list
                self.ids.username.text = "User Not Logged In"
        else:
            # Handle the case when log_email is None
            print("No email logged.")

        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashScreen'

    def switch_screen(self, screen_name):
        print(f"Switching to screen: {screen_name}")

        # Get the screen manager
        sm = self.manager

        sm.transition = SlideTransition(direction='left')
        sm.current = screen_name

    def go_to_lender_landing(self):
        # Get the screen manager
        # Get the existing ScreenManager
        self.manager.add_widget(Factory.LenderLanding(name='LenderLanding'))
        self.manager.current = 'LenderLanding'
        '''
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = LenderLanding(name='LenderLanding')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'LenderLanding'
        '''

    def go_to_borrower_landing(self):
        self.manager.add_widget(Factory.BorrowerLanding(name='BorrowerLanding'))
        self.manager.current = 'BorrowerLanding'
        '''
        # Get the screen manager
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = BorrowerLanding(name='BorrowerLanding')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'BorrowerLanding'
        '''
