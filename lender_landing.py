from kivy.base import EventLoop
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton

from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.modalview import ModalView

from lender_registration_form import LenderScreen

Landing = '''

<MyScreenManager>:
    LenderLanding:
    LenderHowScreen:
    

<LenderLanding>:

    ScrollView:
        MDFloatLayout:
            md_bg_color:1,1,1,1



            Image:
                source: "LOGO.png"
                pos_hint: {'center_x': 0.5, 'center_y': 0.91}
                size_hint_x: None
                size_hint_y: None
                height: dp(30)
                spacing: dp(40)
                size: "100dp", "100dp"
                allow_stretch: True
                keep_ratio: False

            Label:
                text: 'Welcome to P2P '
                font_size:dp(23)
                pos_hint: {'center_x': 0.5, 'center_y': 0.81}
                color: 4/255, 104/255, 153/255, 1
                height: dp(10)
                underline: "True"
                size_hint_y: None
                font_name: "Roboto-Bold"

            Label:
                text: 'Use the power of P2P lending'
                font_size:dp(18)
                font_name: "Roboto-Bold"

                pos_hint: {'center_x': 0.5, 'center_y': 0.77}
                color: 0, 0, 0, 1

            Label:
                text: 'to get high returns'
                font_size:dp(18)
                font_name: "Roboto-Bold"

                pos_hint: {'center_x': 0.5, 'center_y': 0.74}
                color: 0, 0, 0, 1
                height: dp(50)

            MDGridLayout:
                cols: 2
                spacing:dp(10)

                size_hint_y: None
                pos_hint: {'center_x': 0.5, 'center_y': 0.53}
                height: self.minimum_height
                width: self.minimum_width
                size_hint_x: None
                MDRaisedButton:
                    size_hint: None, None
                    size: "150dp", "40dp"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    md_bg_color: 1/255, 26/255, 51/255, 1
                    size_hint_y: None
                    height: dp(80)
                    size_hint_x: None
                    width: dp(130)
                    BoxLayout:
                        orientation: 'horizontal'
                        spacing:dp(10)
                        MDLabel:
                            text: "Diversification of Funds as low as $1   "
                            font_size:dp(14)

                            theme_text_color: 'Custom'
                            halign: "center"
                            text_color: 1, 1, 1, 1
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                MDRaisedButton:
                    size_hint: None, None
                    size: "150dp", "40dp"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    md_bg_color: 1/255, 26/255, 51/255, 1
                    size_hint_y: None
                    height: dp(80)
                    size_hint_x: None
                    width: dp(130)
                    BoxLayout:
                        orientation: 'horizontal'
                        spacing:dp(10)
                        MDLabel:
                            text: "Investment starting $10,000 onwards"
                            font_size: "14sp"

                            theme_text_color: 'Custom'
                            halign: "center"
                            text_color: 1, 1, 1, 1
                            pos_hint: {'center_x': 0.8, 'center_y': 0.5}
                MDRaisedButton:
                    size_hint: None, None
                    size: "150dp", "40dp"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    md_bg_color: 1/255, 26/255, 51/255, 1
                    size_hint_y: None
                    height: dp(80)
                    size_hint_x: None
                    width: dp(130)
                    BoxLayout:
                        orientation: 'horizontal'
                        spacing:dp(10)
                        MDLabel:
                            text: "Returns up to 15%"
                            font_size:dp(14)

                            theme_text_color: 'Custom'
                            halign: "center"
                            text_color: 1, 1, 1, 1
                            pos_hint: {'center_x': 0.8, 'center_y': 0.5}
                MDRaisedButton:
                    size_hint: None, None
                    size: "150dp", "40dp"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    md_bg_color: 1/255, 26/255, 51/255, 1
                    size_hint_y: None
                    height: dp(80)
                    size_hint_x: None
                    width: dp(130)
                    BoxLayout:
                        orientation: 'horizontal'
                        spacing:dp(10)
                        MDLabel:
                            text: "Invest for 1,2,3,4,5 or 6 years"
                            font_size:dp(14)

                            theme_text_color: 'Custom'
                            halign: "center"
                            text_color: 1, 1, 1, 1
                            pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDTextButton:
                text: 'How do I get started?'
                font_size:dp(16)
                underline: "True"
                font_name: "Roboto"
                bold:"True"
                pos_hint: {'center_x': 0.5, 'center_y': 0.32}

                color: 0, 0, 0, 1
                on_release: root.go_to_lender_landing()
            Widget:
                # Widget to draw a line below the image
                size_hint_y: None
                height: dp(10)
                pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                canvas.before:
                    Color:
                        rgba: 155/255, 160/255, 162/255, 1  # Change the color to blue (R, G, B, A)
            MDRaisedButton:
                text: "Proceed to Registration"
                font_name: "Roboto-Bold"
                font_size:dp(17)
                padding:dp(15)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                border_radius: [1, 1, 1, 1]
                on_release: root.go_to_lenderscreen()

<LenderHowScreen>:



    MDFloatLayout:
        md_bg_color:0.9, 0.9, 0.9, 1

        MDIconButton:

            icon: 'arrow-left'
            on_release: app.root.current = 'LenderLanding'
            pos_hint: {'center_x': 0.045, 'center_y': 0.95}
            theme_text_color: 'Custom'
            text_color: 0,0,0,1  # Set color to white



        MDLabel:
            text: "Here's how it works"

            underline: "True"
            font_name: "Roboto-Bold"
            font_size:dp(18)
            theme_text_color: 'Custom'
            text_color:0,0,0,1
            halign:"center"
            pos_hint: {'center_x': 0.5, 'center_y': 0.81}


        MDGridLayout:
            cols: 2
            spacing:dp(10)

            size_hint_y: None
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            height: self.minimum_height
            width: self.minimum_width
            size_hint_x: None
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.55}
                md_bg_color:4/255, 94/255, 154/255, 1
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "1.Registration "
                        font_size:dp(15)

                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color: 1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.090, 0.157, 0.208, 1
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "2. Profile Evaluation"
                        font_size:dp(15)

                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color:0.090, 0.157, 0.208, 1
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "3. Listing On Platform"
                        font_size:dp(15)

                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color: 1,1,1,1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color:  4/255, 94/255, 154/255, 1
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "4.Funding"
                        font_size:dp(15)

                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color: 1,1,1,1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color:  4/255, 94/255, 154/255, 1
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "5.Sign Agreement With Lender"
                        font_size:dp(15)

                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.090, 0.157, 0.208, 1
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "6.Disbursement"
                        font_size:dp(15)

                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color: 1,1,1,1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color:  0.090, 0.157, 0.208, 1

                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "7.EMI Repayment"
                        font_size:dp(15)

                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color: 1,1,1,1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color:  4/255, 94/255, 154/255, 1

                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "8.Loan Closure"
                        font_size:dp(15)

                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:  1,1,1,1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}




'''


class LenderLanding(Screen):
    Builder.load_string(Landing)

    def __init__(self, **kwargs):
        super(LenderLanding, self).__init__(**kwargs)

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashScreen'  # Replace with the actual name of your previous screen

    def go_to_lender_landing(self):
        print("Going to LenderHowScreen")
        sm = self.manager
        how_screen = LenderHowScreen(name='LenderHowScreen')
        sm.add_widget(how_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderHowScreen'
        print("Switched to LenderHowScreen")

    def go_to_lenderscreen(self):
        sm = self.manager
        lender_screen = LenderScreen(name='LenderScreen')
        sm.add_widget(lender_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreen'


class LenderHowScreen(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'LenderLanding'


class MyScreenManager(ScreenManager):
    pass
