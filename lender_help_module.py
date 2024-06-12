import os

from anvil.tables import app_tables
from kivy import platform
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import SlideTransition
import anvil.server
from kivymd.uix.filemanager import MDFileManager

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission
    )

Builder.load_string(
    """
<WindowManager>:
    LenderHelpScreen:
    FirstScreen:
    SecondScreen:
    ThirdScreen:
    FourthScreen:
    FifthScreen:
    SixthScreen:
    SeventhScreen:
    EighthScreen:
    NinthScreen:
    TenthScreen:
    EleventhScreen:
    TwelveScreen:
    ThirteenScreen:
    FourteenScreen:

<LenderHelpScreen>:
    name: 'LenderHelpScreen'
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Help Center"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left',lambda x: root.go_back()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1

        MDScrollView:
            BoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

                OneLineListItem:
                    id: item1
                    text: "How to apply for Loan ?"
                    on_release: root.first_screen()

                OneLineListItem:
                    id: item2
                    text: "Request a complaint ? "
                    on_release: root.second_screen()

                OneLineListItem:
                    id: item3
                    text: "How to do payments ?"
                    on_release: root.third_screen()

                OneLineListItem:
                    id: item4
                    text: "How to check loan status ?"
                    on_release: root.fourth_screen()


                OneLineListItem:
                    id: item5
                    text: " where do you find transaction History ?"
                    on_release: root.fifth_screen()
                OneLineListItem:
                    id: item6
                    text: "How to add money to wallet ?"
                    on_release: root.sixth_screen()
                OneLineListItem:
                    id: item7
                    text: "What is the maximum amount for applying loan ?"
                    on_release: root.seventh_screen()
                OneLineListItem:
                    id: item8
                    text: "How to invest Money in GP2P Platform ?"
                    on_release: root.eighth_screen()
                OneLineListItem:
                    id: item9
                    text: "How can platform provide security ?"
                    on_release: root.ninth_screen()
                OneLineListItem:
                    id: item10
                    text: "How much time do you take to disburse the loans ?"
                    on_release: root.tenth_screen()
                OneLineListItem:
                    id: item11
                    text: "How much time do you take to disburse the loans ?"
                    on_release: root.eleventh_screen()
                OneLineListItem:
                    id: item12
                    text: "How easy to get out ?"
                    on_release: root.twelve_screen()
                OneLineListItem:
                    id: item13
                    text: "How much returns I can except ?"
                    on_release: root.thirteenth_screen()
                OneLineListItem:
                    id: item14
                    text: "How many types of loans GP2P provides?"
                    on_release: root.fourteenth_screen()


<FirstScreen>:
    name: 'FirstScreen'
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDTopAppBar:
            title: "Help Center"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)

            MDLabel:
                text: 'Loan Booking Process'
                font_size: dp(20)
                bold: True
                size_hint_y: None
                height: 50

            MDLabel:
                text: "The following steps are loan booking process :"
                size_hint_y: None
                height: 50

            MDGridLayout:
                cols: 2
                spacing: dp(20)  # Adjust spacing between icon and label

                MDIconButton:
                    id: icon1
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label1
                    text: "Open New Loan Request"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon2
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    size_hint_y: None
                    height: 50

                    text_color: 0.043, 0.145, 0.278, 1
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label2
                    text: "Select Product Group,Category,Name --> Click Next "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon3
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label3
                    text: "Enter the Loan Amount --> Loan Tenure --> Select EMI Type --> Click Next"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon4
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label4
                    text: "Check the Total Repayment Amount,Interest,Processing Fees --> Click on Sendrequest "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon5
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                MDLabel:
                    id: label5
                    text: "Loan Booked"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height:dp(50)



<SecondScreen>:
    name: 'SecondScreen'  # Corrected screen name
    MDTopAppBar:
        title: "Help center"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: root.go_back()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            MDLabel:
                text: 'Raise a Complaint'
                halign: 'center'
                bold: True

            MDTextField:
                id: name
                hint_text: 'Enter your name '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
            MDTextField:
                id: email
                hint_text: 'Enter your Email Id '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
            MDTextField:
                id: mobile_number
                hint_text: 'Enter mobile number '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDLabel:
                text: "Upload Attachment "
                halign: 'center'
                bold: True


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('SecondScreen').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Screen shot'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label1
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDTextField:
                id: issue_occured
                hint_text: 'Title'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None
            MDTextField:
                id: issue_description
                hint_text: 'Describe your problem'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None


            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Submit"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    on_release: root.submit(name.text, email.text, mobile_number.text, issue_occured.text, issue_description.text)
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"


<ThirdScreen>:
    name: 'ThirdScreen'  # Corrected screen name
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDTopAppBar:
            title: "Help Center"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)

            MDLabel:
                text: 'Payments'
                font_size: dp(20)
                bold: True
                size_hint_y: None
                height: 50

            MDLabel:
                text: "The following steps are to do payments :"
                size_hint_y: None
                height: 50

            MDGridLayout:
                cols: 2
                spacing: dp(20)  # Adjust spacing between icon and label

                MDIconButton:
                    id: icon1
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label1
                    text: "Open New Loan Request"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon2
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    size_hint_y: None
                    height: 50

                    text_color: 0.043, 0.145, 0.278, 1
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label2
                    text: "Select Product Group,Category,Name --> Click Next "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon3
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label3
                    text: "Enter the Loan Amount --> Loan Tenure --> Select EMI Type --> Click Next"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon4
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label4
                    text: "Check the Total Repayment Amount,Interest,Processing Fees --> Click on Sendrequest "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon5
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                MDLabel:
                    id: label5
                    text: "Loan Booked"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height:dp(50)





<FourthScreen>:
    name: 'FourthScreen'  
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDTopAppBar:
            title: "Help Center"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)

            MDLabel:
                text: 'Loan Status'
                font_size: dp(20)
                bold: True
                size_hint_y: None
                height: 50

            MDLabel:
                text: "The following steps are to check Loan Status :"
                size_hint_y: None
                height: 50

            MDGridLayout:
                cols: 2
                spacing: dp(20)  # Adjust spacing between icon and label

                MDIconButton:
                    id: icon1
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label1
                    text: "Open Application Tracker"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon2
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    size_hint_y: None
                    height: 50

                    text_color: 0.043, 0.145, 0.278, 1
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label2
                    text: "We can see all your loans "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon3
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label3
                    text: "Select your loan"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon4
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label4
                    text: " You can able to see the tracking "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon5
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                MDLabel:
                    id: label5
                    text: " Approved or Awaiting for Approval or Rejected"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50




<FifthScreen>:
    name: 'FifthScreen'  # Corrected screen name
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDTopAppBar:
            title: "Help Center"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)

            MDLabel:
                text: 'Transaction History'
                font_size: dp(20)
                bold: True
                size_hint_y: None
                height: 50

            MDLabel:
                text: "The following steps are loan booking process :"
                size_hint_y: None
                height: 50

            MDGridLayout:
                cols: 2
                spacing: dp(20)  # Adjust spacing between icon and label

                MDIconButton:
                    id: icon1
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label1
                    text: "Open New Loan Request"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon2
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    size_hint_y: None
                    height: 50

                    text_color: 0.043, 0.145, 0.278, 1
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label2
                    text: "Select Product Group,Category,Name --> Click Next "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon3
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label3
                    text: "Enter the Loan Amount --> Loan Tenure --> Select EMI Type --> Click Next"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon4
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label4
                    text: "Check the Total Repayment Amount,Interest,Processing Fees --> Click on Sendrequest "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon5
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                MDLabel:
                    id: label5
                    text: "Loan Booked"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height:dp(50)


<SixthScreen>:
    name: 'SixthScreen'  
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDTopAppBar:
            title: "Help Center"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)

            MDLabel:
                text: 'Adding Money to wallet'
                font_size: dp(20)
                bold: True
                size_hint_y: None
                height: 50

            MDLabel:
                text: "The following steps are money adding process :"
                size_hint_y: None
                height: 50

            MDGridLayout:
                cols: 2
                spacing: dp(20)  # Adjust spacing between icon and label

                MDIconButton:
                    id: icon1
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label1
                    text: "Open the Wallet "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon2
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    size_hint_y: None
                    height: 50

                    text_color: 0.043, 0.145, 0.278, 1
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label2
                    text: "Check the Available Balance "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon3
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label3
                    text: "Select the Deposit and Enter the Amount"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon4
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label4
                    text: "Click on Submit"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon5
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                MDLabel:
                    id: label5
                    text: "Click on Refresh the Amount will Updated in Available Balance"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height:dp(50)



<SeventhScreen>:
    name: 'SeventhScreen'  # Corrected screen name
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDTopAppBar:
            title: "Help Center"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)

            MDLabel:
                text: 'Loan Booking Process'
                font_size: dp(20)
                bold: True
                size_hint_y: None
                height: 50

            MDLabel:
                text: "The following steps are loan booking process :"
                size_hint_y: None
                height: 50

            MDGridLayout:
                cols: 2
                spacing: dp(20)  # Adjust spacing between icon and label

                MDIconButton:
                    id: icon1
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label1
                    text: "Open New Loan Request"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon2
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    size_hint_y: None
                    height: 50

                    text_color: 0.043, 0.145, 0.278, 1
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label2
                    text: "Select Product Group,Category,Name --> Click Next "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon3
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label3
                    text: "Enter the Loan Amount --> Loan Tenure --> Select EMI Type --> Click Next"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon4
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label4
                    text: "Check the Total Repayment Amount,Interest,Processing Fees --> Click on Sendrequest "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon5
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                MDLabel:
                    id: label5
                    text: "Loan Booked"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height:dp(50)




<EighthScreen>:
    name: 'EighthScreen'  # Corrected screen name
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDTopAppBar:
            title: "Help Center"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)

            MDLabel:
                text: 'Loan Booking Process'
                font_size: dp(20)
                bold: True
                size_hint_y: None
                height: 50

            MDLabel:
                text: "The following steps are loan booking process :"
                size_hint_y: None
                height: 50

            MDGridLayout:
                cols: 2
                spacing: dp(20)  # Adjust spacing between icon and label

                MDIconButton:
                    id: icon1
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label1
                    text: "Open New Loan Request"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon2
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    size_hint_y: None
                    height: 50

                    text_color: 0.043, 0.145, 0.278, 1
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label2
                    text: "Select Product Group,Category,Name --> Click Next "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon3
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label3
                    text: "Enter the Loan Amount --> Loan Tenure --> Select EMI Type --> Click Next"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon4
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label4
                    text: "Check the Total Repayment Amount,Interest,Processing Fees --> Click on Sendrequest "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon5
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                MDLabel:
                    id: label5
                    text: "Loan Booked"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height:dp(50)





<NinthScreen>:
    name: 'NinthScreen'  # Corrected screen name
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDTopAppBar:
            title: "Help Center"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)

            MDLabel:
                text: 'Loan Booking Process'
                font_size: dp(20)
                bold: True
                size_hint_y: None
                height: 50

            MDLabel:
                text: "The following steps are loan booking process :"
                size_hint_y: None
                height: 50

            MDGridLayout:
                cols: 2
                spacing: dp(20)  # Adjust spacing between icon and label

                MDIconButton:
                    id: icon1
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label1
                    text: "Open New Loan Request"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon2
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    size_hint_y: None
                    height: 50

                    text_color: 0.043, 0.145, 0.278, 1
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label2
                    text: "Select Product Group,Category,Name --> Click Next "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon3
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label3
                    text: "Enter the Loan Amount --> Loan Tenure --> Select EMI Type --> Click Next"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon4
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label4
                    text: "Check the Total Repayment Amount,Interest,Processing Fees --> Click on Sendrequest "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon5
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                MDLabel:
                    id: label5
                    text: "Loan Booked"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height:dp(50)


<TenthScreen>:
    name: 'TenthScreen'  # Corrected screen name
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDTopAppBar:
            title: "Help Center"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)

            MDLabel:
                text: 'Loan Booking Process'
                font_size: dp(20)
                bold: True
                size_hint_y: None
                height: 50

            MDLabel:
                text: "The following steps are loan booking process :"
                size_hint_y: None
                height: 50

            MDGridLayout:
                cols: 2
                spacing: dp(20)  # Adjust spacing between icon and label

                MDIconButton:
                    id: icon1
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label1
                    text: "Open New Loan Request"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon2
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    size_hint_y: None
                    height: 50

                    text_color: 0.043, 0.145, 0.278, 1
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label2
                    text: "Select Product Group,Category,Name --> Click Next "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon3
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label3
                    text: "Enter the Loan Amount --> Loan Tenure --> Select EMI Type --> Click Next"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon4
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label4
                    text: "Check the Total Repayment Amount,Interest,Processing Fees --> Click on Sendrequest "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon5
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                MDLabel:
                    id: label5
                    text: "Loan Booked"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height:dp(50)





<EleventhScreen>:
    name: 'EleventhScreen'  # Corrected screen name
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDTopAppBar:
            title: "Help Center"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)

            MDLabel:
                text: 'Loan Booking Process'
                font_size: dp(20)
                bold: True
                size_hint_y: None
                height: 50

            MDLabel:
                text: "The following steps are loan booking process :"
                size_hint_y: None
                height: 50

            MDGridLayout:
                cols: 2
                spacing: dp(20)  # Adjust spacing between icon and label

                MDIconButton:
                    id: icon1
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label1
                    text: "Open New Loan Request"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon2
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    size_hint_y: None
                    height: 50

                    text_color: 0.043, 0.145, 0.278, 1
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label2
                    text: "Select Product Group,Category,Name --> Click Next "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon3
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label3
                    text: "Enter the Loan Amount --> Loan Tenure --> Select EMI Type --> Click Next"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon4
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label4
                    text: "Check the Total Repayment Amount,Interest,Processing Fees --> Click on Sendrequest "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon5
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                MDLabel:
                    id: label5
                    text: "Loan Booked"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height:dp(50)





<TwelveScreen>:
    name: 'TwelveScreen'  # Corrected screen name
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDTopAppBar:
            title: "Help Center"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)

            MDLabel:
                text: 'Loan Booking Process'
                font_size: dp(20)
                bold: True
                size_hint_y: None
                height: 50

            MDLabel:
                text: "The following steps are loan booking process :"
                size_hint_y: None
                height: 50

            MDGridLayout:
                cols: 2
                spacing: dp(20)  # Adjust spacing between icon and label

                MDIconButton:
                    id: icon1
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label1
                    text: "Open New Loan Request"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon2
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    size_hint_y: None
                    height: 50

                    text_color: 0.043, 0.145, 0.278, 1
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label2
                    text: "Select Product Group,Category,Name --> Click Next "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon3
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label3
                    text: "Enter the Loan Amount --> Loan Tenure --> Select EMI Type --> Click Next"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon4
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label4
                    text: "Check the Total Repayment Amount,Interest,Processing Fees --> Click on Sendrequest "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon5
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                MDLabel:
                    id: label5
                    text: "Loan Booked"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height:dp(50)





<ThirteenScreen>:
    name: 'ThirteenScreen'  # Corrected screen name
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDTopAppBar:
            title: "Help Center"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)

            MDLabel:
                text: 'Loan Booking Process'
                font_size: dp(20)
                bold: True
                size_hint_y: None
                height: 50

            MDLabel:
                text: "The following steps are loan booking process :"
                size_hint_y: None
                height: 50

            MDGridLayout:
                cols: 2
                spacing: dp(20)  # Adjust spacing between icon and label

                MDIconButton:
                    id: icon1
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label1
                    text: "Open New Loan Request"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon2
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    size_hint_y: None
                    height: 50

                    text_color: 0.043, 0.145, 0.278, 1
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label2
                    text: "Select Product Group,Category,Name --> Click Next "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon3
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label3
                    text: "Enter the Loan Amount --> Loan Tenure --> Select EMI Type --> Click Next"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon4
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label4
                    text: "Check the Total Repayment Amount,Interest,Processing Fees --> Click on Sendrequest "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon5
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                MDLabel:
                    id: label5
                    text: "Loan Booked"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height:dp(50)




<FourteenScreen>:
    name: 'FourteenScreen'  # Corrected screen name
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDTopAppBar:
            title: "Help Center"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)

            MDLabel:
                text: 'Loan Booking Process'
                font_size: dp(20)
                bold: True
                size_hint_y: None
                height: 50

            MDLabel:
                text: "The following steps are loan booking process :"
                size_hint_y: None
                height: 50

            MDGridLayout:
                cols: 2
                spacing: dp(20)  # Adjust spacing between icon and label

                MDIconButton:
                    id: icon1
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label1
                    text: "Open New Loan Request"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon2
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    size_hint_y: None
                    height: 50

                    text_color: 0.043, 0.145, 0.278, 1
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label2
                    text: "Select Product Group,Category,Name --> Click Next "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon3
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label3
                    text: "Enter the Loan Amount --> Loan Tenure --> Select EMI Type --> Click Next"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon4
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)

                MDLabel:
                    id: label4
                    text: "Check the Total Repayment Amount,Interest,Processing Fees --> Click on Sendrequest "
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon5
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                MDLabel:
                    id: label5
                    text: "Loan Booked"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height:dp(50)




"""

)


class LenderHelpScreen(Screen):
    def go_back(self):
        from lender_dashboard import LenderDashboard
        sm = self.manager
        borrower_screen = LenderDashboard(name='LenderDashboard')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderDashboard'
        print(borrower_screen)

    def first_screen(self):
        sm = self.manager
        borrower_screen = FirstScreen(name='FirstScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'FirstScreen'

    def second_screen(self):
        sm = self.manager
        borrower_screen = SecondScreen(name='SecondScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'SecondScreen'

    def third_screen(self):
        sm = self.manager
        borrower_screen = ThirdScreen(name='ThirdScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'ThirdScreen'

    def fourth_screen(self):
        sm = self.manager
        borrower_screen = FourthScreen(name='FourthScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'FourthScreen'

    def fifth_screen(self):
        sm = self.manager
        borrower_screen = FifthScreen(name='FifthScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'FifthScreen'

    def sixth_screen(self):
        sm = self.manager
        borrower_screen = SixthScreen(name='SixthScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'SixthScreen'

    def seventh_screen(self):
        sm = self.manager
        borrower_screen = SeventhScreen(name='SeventhScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'SeventhScreen'

    def eighth_screen(self):
        sm = self.manager
        borrower_screen = EighthScreen(name='EighthScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'EighthScreen'

    def ninth_screen(self):
        sm = self.manager
        borrower_screen = NinthScreen(name='NinthScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'NinthScreen'

    def tenth_screen(self):
        sm = self.manager
        borrower_screen = TenthScreen(name='TenthScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'TenthScreen'

    def eleventh_screen(self):
        sm = self.manager
        borrower_screen = EleventhScreen(name='EleventhScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'EleventhScreen'

    def twelve_screen(self):
        sm = self.manager
        borrower_screen = TwelveScreen(name='TwelveScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'TwelveScreen'

    def thirteenth_screen(self):
        sm = self.manager
        borrower_screen = ThirteenScreen(name='ThirteenScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'ThirteenScreen'

    def fourteenth_screen(self):
        sm = self.manager
        borrower_screen = FourteenScreen(name='FourteenScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'FourteenScreen'


class FirstScreen(Screen):
    def go_back(self):
        self.manager.current = 'LenderHelpScreen'


class Permission:
    pass


def check_permission(READ_MEDIA_IMAGES):
    pass


def request_permissions(param, permission_callback):
    pass


class SecondScreen(Screen):
    def go_back(self):
        self.manager.current = 'LenderHelpScreen'

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1")

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):

        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('SecondScreen').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def submit(self, name, email, mobile_number, issue_occured, issue_description):
        # Now you can use the provided arguments in your submit method
        app_tables.fin_reported_problems.add_row(
            name=name,
            email=email,
            mobile_number=mobile_number,
            issue_occured=issue_occured,
            issue_description=issue_description
        )
        self.manager.current = 'LenderHelpScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def on_mobile_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mobile_number.input_type = 'number'


class ThirdScreen(Screen):
    def go_back(self):
        self.manager.current = 'LenderHelpScreen'


class FourthScreen(Screen):
    def go_back(self):
        self.manager.current = 'LenderHelpScreen'


class FifthScreen(Screen):
    def go_back(self):
        self.manager.current = 'LenderHelpScreen'


class SixthScreen(Screen):
    def go_back(self):
        self.manager.current = 'LenderHelpScreen'


class SeventhScreen(Screen):
    def go_back(self):
        self.manager.current = 'LenderHelpScreen'


class EighthScreen(Screen):
    def go_back(self):
        self.manager.current = 'LenderHelpScreen'


class NinthScreen(Screen):
    def go_back(self):
        self.manager.current = 'LenderHelpScreen'


class TenthScreen(Screen):
    def go_back(self):
        self.manager.current = 'LenderHelpScreen'


class EleventhScreen(Screen):
    def go_back(self):
        self.manager.current = 'LenderHelpScreen'


class TwelveScreen(Screen):
    def go_back(self):
        self.manager.current = 'LenderHelpScreen'


class ThirteenScreen(Screen):
    def go_back(self):
        self.manager.current = 'LenderHelpScreen'


class FourteenScreen(Screen):
    def go_back(self):
        self.manager.current = 'LenderHelpScreen'


class MyScreenManager(ScreenManager):
    pass
