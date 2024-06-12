from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton

from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.modalview import ModalView

from borrower_registration_forms import BorrowerScreen

BorrLanding = '''
<WindowManager>:
    BorrowerLanding:
    BorrowerHowScreen:
    
<BorrowerLanding>:
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
                text: 'Get any type of loan for'
                font_size:dp(18)
                font_name: "Roboto-Bold"

                pos_hint: {'center_x': 0.5, 'center_y': 0.77}
                color: 0, 0, 0, 1

            Label:
                text: 'whatever you need'
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
                            text: "Disbursal in 2 Hours   "
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
                            text: "Flexible Loan Tenure"
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
                            text: "100% Digital Process"
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
                            text: "Direct Transfer to Bank Account"
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
                on_release: root.go_to_borrower_landing()
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
                on_release: root.go_to_borrower_screen()

<BorrowerHowScreen>:



    MDFloatLayout:
        md_bg_color:0.9, 0.9, 0.9, 1

        MDIconButton:

            icon: 'arrow-left'
            on_release: app.root.current = 'BorrowerLanding'
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
                        text_color:  1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
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
                        text: "2. Invest Profile Approval"
                        font_size:dp(15)

                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color: 1,1,1,1
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
                        text: "3. View Loan Listing"
                        font_size:dp(15)

                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color: 1,1,1,1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 4/255, 94/255, 154/255, 1
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "4.Fund Loans"
                        font_size:dp(15)

                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color: 1,1,1,1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 4/255, 94/255, 154/255, 1
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "5.Sign Agreement With Borrower"
                        font_size:dp(15)

                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color: 1,1,1,1
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
                md_bg_color: 0.090, 0.157, 0.208, 1
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "7.EMI Profit Realization"
                        font_size:dp(15)

                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color: 1,1,1,1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 4/255, 94/255, 154/255, 1
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "8.Further Reinvestment"
                        font_size:dp(15)

                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:  1,1,1,1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}





'''


class BorrowerLanding(Screen):
    Builder.load_string(BorrLanding)

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

    def go_to_borrower_landing(self):
        # self.root.current = "BorrowerScreen"
        sm = self.manager
        borrower_screen = BorrowerHowScreen(name='BorrowerHowScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerHowScreen'

    def go_to_borrower_screen(self):
        # self.root.current = "BorrowerScreen"
        sm = self.manager
        borrower_screen = BorrowerScreen(name='BorrowerScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen'

    def switch_screen(self, screen_name):
        print(f"Switching to screen: {screen_name}")

        # Get the screen manager
        sm = self.manager

        sm.transition = SlideTransition(direction='left')
        sm.current = screen_name


class BorrowerHowScreen(Screen):
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
        self.manager.current = 'BorrowerLanding'  # Replace with the actual name of your previous screen


class MyScreenManager(ScreenManager):
    pass
