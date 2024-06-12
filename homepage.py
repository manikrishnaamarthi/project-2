from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty

from dashboard import DashScreen
from login import LoginScreen

from signup import SignupScreen

KV = """
<WindowManager>:
    MainScreen:
    
<MainScreen>:
    id: main
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos


    BoxLayout:
        orientation: "vertical"
        padding: dp(35)
        spacing: dp(35)  # Adjusted spacing between labels and image

        MDLabel:
            text: ""

            theme_text_color: 'Custom'
            text_color: 0, 0, 0, 1
            bold: True


        Image:
            source: "LOGO.png"
            pos_hint: {'center_x': 0.5, 'center_y': 0.85}
            size_hint: None, None
            size: "150dp", "150dp"




        GridLayout:
            cols: 2
            spacing: dp(20)
            padding: dp(20)
            pos_hint: {'center_x': 0.52, 'center_y': 0.8} 
            size_hint: 1, None

            MDRaisedButton:
                md_bg_color: 1,1,1,1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                line_color: 0, 0, 0, 1  
                line_width: 1

                BoxLayout:
                    orientation: 'horizontal'
                    spacing: dp(10)

                    Image:
                        source: "google-logo-9808.png"
                        size_hint: None, None
                        size: "20dp", "25dp"  

                    MDLabel:
                        text: "  Sign In with Google"

                        theme_text_color: 'Custom'
                        text_color: 0, 0, 0, 1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
                        bold: True

        GridLayout:
            cols: 2
            spacing: dp(20)
            padding: dp(20)
            pos_hint: {'center_x': 0.52, 'center_y': 0.7} 
            size_hint: 1, None

            MDRaisedButton:
                md_bg_color: 0.043, 0.145, 0.278, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

                BoxLayout:
                    orientation: 'horizontal'
                    spacing: 10  # Adjust the spacing as needed

                    Image:
                        source: "logo-facebookpng-32256.png"
                        size_hint: None, None
                        size: "20dp", "25dp"
                        allow_stretch: True
                        keep_ratio: True

                    MDLabel:
                        text: "  Sign In with Facebook"
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1, 1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
                        bold: True

        Label:
            text: ""

        GridLayout:
            cols: 2
            spacing: dp(20)
            padding: dp(20)
            pos_hint: {'center_x': 0.50, 'center_y': 0.6}  # Adjusted y-value
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Login"
                on_release: root.go_to_dashboard()
                md_bg_color: 0.043, 0.145, 0.278, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Sign Up"
                on_release: root.go_to_signup()
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"
        Label:
            text: ""

        Label:
            text: ""
        Label:
            text: ""


"""


class GoogleSignInButton(MDIconButton):
    pass


class MainScreen(Screen):
    Builder.load_string(KV)

    def go_to_login(self):
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        dashboard_screen = DashScreen(name='DashScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(dashboard_screen)

        # Switch to the LoginScreen
        sm.current = 'DashScreen'

    def go_to_signup(self):
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = SignupScreen(name='SignupScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'SignupScreen'

    def go_to_dashboard(self):
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = LoginScreen(name='LoginScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'LoginScreen'


class MyScreenManager(ScreenManager):
    pass
