import re
import os
from anvil.tables import app_tables
from kivy.animation import Animation
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
import sqlite3
from datetime import datetime
from kivy import platform
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
import sqlite3
from kivymd.uix.pickers import MDDatePicker
from kivy.utils import platform
from kivy.clock import mainthread
from datetime import datetime
import anvil.server
from kivy.uix.modalview import ModalView
from kivymd.uix.spinner import MDSpinner
from kivy.clock import Clock
from kivy.uix.popup import Popup
from lender_dashboard import LenderDashboard

# anvil.server.connect("server_6MFSRHQN7TZHDVGRHE4DACOS-MSES5HYVGRJ5LJH4") #published

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission
    )

KV = '''
<WindowManager>:
    LenderScreen:
    LenderScreen1:
    LenderScreen2:
    LenderScreen3:
    LenderScreen4:
    LenderScreen5:
    LenderScreen_Edu_Intermediate:
    LenderScreen_Edu_Bachelors:
    LenderScreen_Edu_Masters:
    LenderScreen_Edu_PHD:
    LenderScreenInstitutionalForm1:
    LenderScreenInstitutionalForm2:
    LenderScreenInstitutionalForm3:
    LenderScreen6:
    LenderScreen7:
    LenderScreen8:
    LenderScreen9:
    LenderScreen10:
    LenderScreen11:
    LenderScreen12:
    LenderScreen13:
    LenderScreen14:
    LenderScreenIndividualBankForm1:
    LenderScreenIndividualBankForm2:

<LenderScreen>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: root.go_to_dashboard()]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(40)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
                ize_hint_y: None
                height:dp(50)

            MDTextField:
                id: username
                hint_text: 'Enter Full Name'
                mFultiline: False
                helper_text: "Enter Valid Name"
                helper_text_mode: 'on_focus'
                height:self.minimum_height
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDLabel:
                text: 'Select Your Gender:'
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                ize_hint_y: None
                height:dp(20)

            Spinner:
                id: spinner_id
                text: "Select Gender"
                font_size: "15dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                multiline: False
                size_hint: 1 , None
                height:"40dp"
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDGridLayout:
                cols: 3
                spacing: dp(10)
                padding: dp(10)

                MDTextField:
                    id: date_textfield
                    hint_text: "Enter Date Of Birth"
                    helper_text: 'YYYY-MM-DD'
                    helper_text_mode: "on_error"
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    input_type:'number'
                    on_touch_down: root.on_date_touch_down()
            MDLabel:
                text:""
                size_hint_y: None
                height:dp(20)

            MDRectangleFlatButton:
                text: 'Next'
                md_bg_color: 0.043, 0.145, 0.278, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"
                on_release: root.add_data(username.text, spinner_id.text, date_textfield.text)

<LenderScreen1>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(30)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(50)

            MDTextField:
                id: mobile_number
                hint_text: 'Enter mobile number'
                multiline: False
                helper_text: 'Enter valid number'
                helper_text_mode: 'on_focus'
                input_type: 'number'  
                on_touch_down: root.on_mobile_number_touch_down()
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: altername_email
                hint_text: ' Enter Alternate Email ID'
                multiline: False
                helper_text: "Enter Valid Alternate Email ID"
                helper_text_mode: 'on_focus'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDLabel:
                text:"Upload Profile Photo:"
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(5)
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
                    id: upload_icon1
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('LenderScreen1').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Profile Photo'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label1
                text:""
                halign: 'center'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(5)

            MDLabel:
                text:""
                size_hint_y: None
                height:dp(20)

            GridLayout:
                cols: 1
                spacing:dp(30)
                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(mobile_number.text, altername_email.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreen2>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen1')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(20)
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: aadhar_number
                hint_text: 'Enter Government ID1 '
                multiline: False
                helper_text: 'Enter Your number'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"

            MDLabel:
                text: "Upload Government ID1"
                bold: True
                size_hint_y:None
                height:dp(50)
                halign: "left"
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
                    id: upload_icon1
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('LenderScreen2').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Govt ID1'
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
                id: pan_number
                hint_text: 'Enter Government ID2 '
                multiline: False
                helper_text: 'Enter Your number'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDLabel:
                text: "Upload Government ID2"
                bold: True
                size_hint_y:None
                height:dp(50)
                halign: "left"

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
                    id: upload_icon2
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('LenderScreen2').check_and_open_file_manager2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Govt ID2'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label2
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDRectangleFlatButton:
                text: "Next"
                on_release: root.add_data(aadhar_number.text, pan_number.text)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"



<LenderScreen3>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen2')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(30)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(20)
            padding: dp(30) 
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
            MDLabel:
                text: 'Address Information'
                halign: 'center'
                bold: True

            MDTextField:
                id: street_address1
                hint_text: 'Enter Street Address1 '
                multiline: False
                helper_text: 'Enter Your address'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"


            MDTextField:
                id: street_address2
                hint_text: 'Enter Street Address2'
                multiline: False
                helper_text: 'Enter Your address'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDLabel:
                text: "Select Type Of Address"
                bold: True
                size_hint_y:None
                height:dp(20)
                halign: "left"

            Spinner:
                id: spinner_id1
                text: "Select Present Address"
                multiline: False
                size_hint: 1 , None
                halign: "left"
                height:"40dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                font_size: "15dp"
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: "How Long You Are Staying At This Address"
                bold: True
                size_hint_y:None
                height:dp(20)
                halign: "left"

            Spinner:
                id: spinner_id2
                text: "Select Staying Address"
                multiline: False
                size_hint: 1 , None
                halign: "left"
                font_size: "15dp"
                height:"40dp"
                background_color: 0,0,0,0
                background_normal:''
                width: dp(200)
                text_size: self.width - dp(20), None
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)    

            MDRectangleFlatButton:
                text: "Next"
                on_release: root.add_data(street_address1.text, street_address2.text, spinner_id1.text, spinner_id2.text)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"


<LenderScreen4>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(30)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(20)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
            MDLabel:
                text: 'Address Information'
                halign: 'center'
                bold: True

            MDTextField:
                id: city
                hint_text: 'Enter City Name '
                multiline: False
                helper_text: 'Enter Your city'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"

            MDTextField:
                id: zip_code
                hint_text: 'Enter postal/zipcode'
                multiline: False
                helper_text: 'Enter Your zipcode'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                input_type: 'number'
                on_touch_down: root.on_mobile_number_touch_down()

            MDTextField:
                id: state
                hint_text: 'Enter State Name'
                multiline: False
                helper_text: 'Enter Your State'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: country
                hint_text: 'Enter Country Name'
                multiline: False
                helper_text: 'Enter Your Country'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
            MDRectangleFlatButton:
                text: "Next"
                on_release: root.add_data(city.text, zip_code.text, state.text, country.text)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreen5>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen4')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(50)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(30)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Education Details'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"


            MDLabel:
                text: "Select Education Details:"
                halign: 'left'
                bold:True
                size_hint_y: None
                font_size: "15dp"
                height:dp(5)

            Spinner:
                id: spinner_id
                text: "Please Select Education Details"
                multiline: False
                size_hint: 1 , None
                font_size: "15dp"
                halign: "left"
                height:"40dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: ' '
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
            MDRectangleFlatButton:
                text: "Next"
                on_press: root.next_pressed(spinner_id.text)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"


<LenderScreen_Edu_10th>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen5')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)
        MDLabel:
            text: ""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Education Details'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(0)

            MDLabel:
                text: "Upload 10th standard certificate"
                halign: 'left'
                bold:True
                size_hint_y: None
                font_size: "15dp"
                height:dp(5)


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
                    on_release: app.root.get_screen('LenderScreen_Edu_10th').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
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

            MDRectangleFlatButton:
                text: "Next"
                on_release: root.go_to_lender_screen4()
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"


<LenderScreen_Edu_Intermediate>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen5')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)
        MDLabel:
            text: ""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(20)
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Education Details'
                halign: 'center'
                bold: True
            MDLabel:
                text: "Upload 10th standard"
                halign: 'left'
                bold: True
                font_size: "15dp"


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
                    on_release: app.root.get_screen('LenderScreen_Edu_Intermediate').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
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
            MDLabel:
                text: "Upload Intermediate/PUC"
                halign: 'left'
                bold: True
                font_size: "15dp"

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
                    on_release: app.root.get_screen('LenderScreen_Edu_Intermediate').check_and_open_file_manager2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                id: image_label2
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDRectangleFlatButton:
                text: "Next"
                on_release: root.go_to_lender_screen4()
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreen_Edu_Bachelors>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen5')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title"
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)
        MDLabel:
            text: ""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(20)
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: "Upload 10th standard Certificate"
                halign: 'left'
                font_size: "15dp"
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
                    on_release: app.root.get_screen('LenderScreen_Edu_Bachelors').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
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
            MDLabel:
                text: "Upload Intermediate/PUC Certificate"
                halign: 'left'
                bold: True
                font_size: "15dp"


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
                    on_release: app.root.get_screen('LenderScreen_Edu_Bachelors').check_and_open_file_manager2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label2
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                text: "Upload Bachelors certificate"
                halign: 'left'
                font_size: "15dp"
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
                    on_release: app.root.get_screen('LenderScreen_Edu_Bachelors').check_and_open_file_manager3()

                MDLabel:
                    id: upload_label3
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                id: image_label3
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDRectangleFlatButton:
                text: "Next"
                on_release: root.go_to_lender_screen4()
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreen_Edu_Masters>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen5')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)
        MDLabel:
            text: ""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(20)
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            MDLabel:
                text: 'Education Details'
                halign: 'center'
                bold: True
            MDLabel:
                text: "Upload 10th standard Certificate"
                halign: 'left'
                bold: True
                font_size: "15dp"


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
                    on_release: app.root.get_screen('LenderScreen_Edu_Masters').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
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
            MDLabel:
                text: "Upload Intermediate/PUC Certificate"
                halign: 'left'
                bold: True
                font_size: "15dp"


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
                    on_release: app.root.get_screen('LenderScreen_Edu_Masters').check_and_open_file_manager2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label2
                text: ''
                halign: 'left'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                text: "Upload Bachelors certificate"
                halign: 'left'
                bold: True
                font_size: "15dp"


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
                    on_release: app.root.get_screen('LenderScreen_Edu_Masters').check_and_open_file_manager3()

                MDLabel:
                    id: upload_label3
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label3
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Masters Certificate"
                halign: 'left'
                bold: True
                font_size: "15dp"


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
                    on_release: app.root.get_screen('LenderScreen_Edu_Masters').check_and_open_file_manager4()

                MDLabel:
                    id: upload_label4
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                id: image_label4
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDRectangleFlatButton:
                text: "Next"
                on_release: root.go_to_lender_screen4()
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreen_Edu_PHD>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen5')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)
        MDLabel:
            text: ""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(20)
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Education Details'
                halign: 'center'
                bold: True
            MDLabel:
                text: ''
                halign: 'center'
                bold: True
            MDLabel:
                text: "Upload 10th standard Certificate"
                halign: 'left'
                font_size: "15dp"
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
                    on_release: app.root.get_screen('LenderScreen_Edu_PHD').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
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
            MDLabel:
                text: "Upload Intermediate/PUC Certificate"
                halign: 'left'
                bold: True
                font_size: "15dp"

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
                    on_release: app.root.get_screen('LenderScreen_Edu_PHD').check_and_open_file_manager2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                id: image_label2
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                text: "Upload Bachelors certificate"
                halign: 'left'
                font_size: "15dp"
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
                    on_release: app.root.get_screen('LenderScreen_Edu_PHD').check_and_open_file_manager3()

                MDLabel:
                    id: upload_label3
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                id: image_label3
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                text: "Upload Masters Certificate"
                halign: 'left'
                font_size: "15dp"
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
                    on_release: app.root.get_screen('LenderScreen_Edu_PHD').check_and_open_file_manager4()

                MDLabel:
                    id: upload_label4
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label4
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}


            MDLabel:
                text: "Upload PHD Certificate"
                halign: 'left'
                font_size: "15dp"
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
                    on_release: app.root.get_screen('LenderScreen_Edu_PHD').check_and_open_file_manager5()
                MDLabel:
                    id: upload_label5
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                id: image_label5
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDRectangleFlatButton:
                text: "Next"
                on_release: root.go_to_lender_screen4()
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"


<LenderScreen6>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen5')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(30)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(50)

            MDLabel:
                text: 'Select Loan Type:'
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                ize_hint_y: None
                height:dp(20)

            Spinner:
                id: spinner
                text: "Select Loan Type"
                font_size: "15dp"
                multiline: False
                size_hint: 1 , None
                height:"40dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            MDTextField:
                id: investment
                hint_text: 'Enter investment Amount'
                multiline: False
                helper_text: "Enter above 100000"
                helper_text_mode: 'on_focus'
                height:self.minimum_height
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                on_touch_down: root.on_investment_touch_down()
            MDLabel:
                text: 'Select Lending Period:'
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                ize_hint_y: None
                height:dp(20)

            Spinner:
                id: spinner2
                text: "Select Lending Period"
                font_size: "15dp"
                multiline: False
                size_hint: 1 , None
                width: dp(200)
                text_size: self.width - dp(20), None
                height:"40dp"
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            GridLayout:
                cols: 1
                spacing:dp(30)
                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.next_pressed(spinner.text, investment.text, spinner2.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"


<LenderScreenInstitutionalForm1>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen6')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(30)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(20)
            padding: dp(30) 
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
            MDLabel:
                text: 'Business Information'
                halign: 'center'
                bold: True

            MDTextField:
                id: business_name
                hint_text: 'Enter Business Name '
                multiline: False
                helper_text: 'Enter Your Business Name'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"

            MDTextField:
                id: business_address
                hint_text: 'Enter Business Address'
                multiline: False
                helper_text: 'Enter Your Business Address'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDLabel:
                text: 'Select Business Type:'
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                ize_hint_y: None
                height:dp(20)
            Spinner:
                id: spin
                text: "Select Business Type"
                multiline: False
                size_hint: 1 , None
                height:"40dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                font_size: "15dp"
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Select No.Of Employees Working:'
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                ize_hint_y: None
                height:dp(20)

            Spinner:
                id: spinner_id
                text: "Select No.Of Employees Working"
                multiline: False
                size_hint: 1 , None
                height:"40dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                background_color: 0,0,0,0
                background_normal:''
                font_size: "15dp"
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDRectangleFlatButton:
                text: "Next"
                on_release: root.add_data(business_name.text,spin.text,spinner_id.text, business_address.text)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"


<LenderScreenInstitutionalForm2>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenInstitutionalForm1')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
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
            padding: dp(30) 
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
            MDLabel:
                text: 'Business Information'
                halign: 'center'
                bold: True

            MDTextField:
                id: year_of_estd
                hint_text:'Enter Year of Estd'
                multiline: False
                helper_text: 'YYYY-MM-DD'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                input_type: 'number'
                on_touch_down: root.on_estd_touch_down()
                helper_text_color_normal: "black"
                font_size: "15dp"

            MDTextField:
                id: industry_type
                hint_text: 'Enter Industry Type'
                multiline: False
                helper_text: 'Enter Your Industry Type'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
            MDTextField:
                id: last_six_months_turnover
                hint_text: 'Enter last 6 months turnover'
                multiline: False
                helper_text: 'Enter Your last 6 months turnover'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                input_type: 'number'
                on_touch_down: root.on_last_six_months_turnover_touch_down()

            MDLabel:
                text: 'Last 6 months bank statements:'
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                ize_hint_y: None
                height:dp(20)

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
                    on_release: app.root.get_screen('LenderScreenInstitutionalForm2').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Document'
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

            MDRectangleFlatButton:
                text: "Next"
                on_release: root.add_data(industry_type.text,last_six_months_turnover.text,year_of_estd.text)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreenInstitutionalForm3>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenInstitutionalForm2')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
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
            spacing: dp(20)
            padding: dp(30)
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            MDLabel:
                text: 'Business Information'
                halign: 'center'
                bold: True

            MDTextField:
                id: din
                hint_text:'Enter DIN'
                multiline: False
                helper_text: 'Enter DIN'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"

            MDTextField:
                id: cin
                hint_text: 'Enter CIN'
                multiline: False
                helper_text: 'Enter CIN'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
            MDTextField:
                id: reg_office_address
                hint_text: 'Enter Registered Office Address'
                multiline: False
                helper_text: 'Enter Valid Registered Office Address'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
            MDLabel:
                text: 'Upload Proof Of Verification:'
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                ize_hint_y: None
                height:dp(20)

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
                    on_release: app.root.get_screen('LenderScreenInstitutionalForm3').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Document'
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

            MDRectangleFlatButton:
                text: "Next"
                on_release: root.add_data(din.text,cin.text,reg_office_address.text)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"


<LenderScreenIndividualForm1>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen6')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(20)
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Employment Details'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)

            MDLabel:
                text: 'Select Employment Type:'
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                ize_hint_y: None
                height:dp(20)

            Spinner:
                id: spinner1
                text: "Select Employment Type"
                multiline: False
                size_hint: 1 , None
                height:"40dp"
                background_color: 0,0,0,0
                background_normal:''
                font_size: "15dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDTextField:
                id: company_name
                hint_text: 'Enter company Name'
                multiline: False
                helper_text: "Enter Valid company Name"
                helper_text_mode: 'on_focus'
                height:self.minimum_height
                font_size: "15dp"
                font_name: "Roboto-Bold"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
            MDLabel:
                text: 'Select Organisation Type:'
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                ize_hint_y: None
                height:dp(20)

            Spinner:
                id: spinner2
                text: "Select Organisation Type"
                multiline: False
                size_hint: 1 , None
                height:"40dp"
                background_color: 0,0,0,0
                background_normal:''
                font_size: "15dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            MDLabel:
                text: 'Select Occupation Type:'
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                ize_hint_y: None
                height:dp(20)

            Spinner:
                id: spinner3
                text: "Select Occupation Type"
                multiline: False
                size_hint: 1 , None
                height:"40dp"
                background_color: 0,0,0,0
                background_normal:''
                font_size: "15dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            MDRectangleFlatButton:
                text: "Next"
                on_release: root.add_data(spinner1.text,spinner3.text, company_name.text, spinner2.text)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreenIndividualForm2>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenIndividualForm1')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(35)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30) 
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Forms'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Employment Details'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(30)

            MDTextField:
                id: annual_salary
                hint_text: 'Enter annual salary'
                multiline: False
                helper_text: "Enter Valid Annual Salary"
                helper_text_mode: 'on_focus'
                height:self.minimum_height
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                input_type: 'number'
                on_touch_down: root.on_annual_salary_touch_down()
                helper_text_color_normal: "black"

            MDTextField:
                id: designation
                hint_text: 'Enter Designation'
                multiline: False
                helper_text: "Enter Valid designation"
                helper_text_mode: 'on_focus'
                height:self.minimum_height
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"

            MDLabel:
                text: 'Upload Employee ID:'
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                ize_hint_y: None
                height:dp(20)

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
                    on_release: app.root.get_screen('LenderScreenIndividualForm2').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Document'
                    halign: 'left'
                    theme_text_color: "Custom"

            MDLabel:
                id: image_label1
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                height:dp(15)
                size_hint_y: None

            MDLabel:
                text: 'Select Upload last 6 months bank statements:'
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                ize_hint_y: None
                height:dp(20)

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
                    on_release: app.root.get_screen('LenderScreenIndividualForm2').check_and_open_file_manager2()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Document'
                    halign: 'left'
                    theme_text_color: "Custom"

            MDLabel:
                id: image_label2
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_y: None
                height:dp(15)

            MDRectangleFlatButton:
                text: "Next"
                on_release: root.add_data(annual_salary.text, designation.text)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"


<LenderScreenIndividualForm3>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenIndividualForm2')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

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
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Employment Details'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)

            MDTextField:
                id: company_address
                hint_text: 'Enter company address'
                helper_text: 'Enter valid company address'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0,0,0, 1
                font_name: "Roboto-Bold"
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"

            MDTextField:
                id: company_pin_code
                hint_text: 'Enter Company Pincode'
                helper_text: 'Enter valid Company Pincode'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0,0,0, 1
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                font_name: "Roboto-Bold"
                input_type: 'number'  
                on_touch_down: root.on_company_pin_code_touch_down()


            MDTextField:
                id: company_country
                hint_text: 'Enter Company Country'
                helper_text: 'Enter valid Company Country'
                multiline: False
                helper_text_mode: 'on_focus'
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                font_size: "15dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: landmark
                hint_text: 'Enter landmark'
                multiline: False
                font_size: "15dp"
                helper_text: 'Enter valid landmark'
                helper_text_mode: 'on_focus'
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                font_name: "Roboto-Bold"

            MDTextField:
                id:business_phone_number
                hint_text: 'Enter business phone number'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                input_type: 'number'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"
                on_touch_down: root.on_business_phone_number_touch_down()
                input_type: 'number'


            MDRectangleFlatButton:
                text: "Next"
                on_release: root.add_data(company_address.text, company_pin_code.text, company_country.text, landmark.text, business_phone_number.text)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"


<LenderScreen7>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen6')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(50)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(30)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Marital Status'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"


            MDLabel:
                text: "Select Marital Status:"
                halign: 'left'
                bold:True
                size_hint_y: None
                font_size: "15dp"
                height:dp(5)

            Spinner:
                id: marital_status_id
                text: "Select Marital Status"
                multiline: False
                size_hint: 1 , None
                font_size: "15dp"
                height:"40dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: ' '
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(marital_status_id.text)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreen8>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30) # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(50)

            MDLabel:
                text: 'Father Information'
                halign: 'center'
                bold: True

            MDTextField:
                id: father_name
                hint_text: 'Enter Father Name'
                helper_text: 'Enter valid Father Name'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_name: "Roboto-Bold"
                font_size: "15dp"

            MDTextField:
                id: father_dob
                hint_text: "Enter Father D.O.B"
                helper_text: 'YYYY-MM-DD'
                helper_text_mode: "on_error"
                font_name: "Roboto-Bold"
                theme_text_color: 'Custom'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                height:self.minimum_height
                font_size: "15dp"
                input_type:'number'
                on_touch_down: root.on_date_touch_down()

            MDTextField:
                id: father_address
                hint_text: 'Enter Father Address'
                helper_text: 'Enter valid Father Address'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: father_occupation
                hint_text: 'Enter Father Occupation'
                helper_text: 'Enter valid Father Occupation'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: father_ph_no
                hint_text: 'Enter Father Phone NO'
                multiline: False
                font_size: "15dp"
                helper_text: 'Enter valid PH No'
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_name: "Roboto-Bold"
                input_type: 'number'  
                on_touch_down: root.on_father_ph_no_touch_down()


            MDRectangleFlatButton:
                text: "Next"
                on_release: root.add_data(father_name.text, father_address.text, father_occupation.text, father_ph_no.text, father_dob.text)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreen9>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
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
            padding: dp(30) # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Mother Information'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)

            MDTextField:
                id: mother_name
                hint_text: 'Enter Mother Name'
                helper_text: 'Enter valid Mother Name'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0,0,0, 1
                font_name: "Roboto-Bold"
                font_size: "15dp"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: mother_dob
                hint_text: "Enter Father D.O.B"
                helper_text: 'YYYY-MM-DD'
                font_name: "Roboto-Bold"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                input_type:'number'
                font_size: "15dp"
                on_touch_down: root.on_date_touch_down()
            MDTextField:
                id: mother_address
                hint_text: 'Enter Mother Address'
                helper_text: 'Enter valid Mother Address'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: mother_occupation
                hint_text: 'Enter Mother Occupation'
                helper_text: 'Enter valid Mother Occupation'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: mother_ph_no
                hint_text: 'Enter Mother Phone NO'
                multiline: False
                font_size: "15dp"
                helper_text: 'Enter valid PH No'
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_name: "Roboto-Bold"
                input_type: 'number'  
                on_touch_down: root.on_mother_ph_no_touch_down()

            MDRectangleFlatButton:
                text: "Next"
                on_release: root.add_data(mother_name.text, mother_address.text, mother_occupation.text, mother_ph_no.text, mother_dob.text)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"


<LenderScreen10>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
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
            spacing: dp(25)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Spouse Details'
                halign: 'center'
                bold:True

            MDTextField:
                id: spouse_name
                hint_text: 'Enter Spouse Name'
                multiline: False
                helper_text: "Enter Valid Spouse Name"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                height:self.minimum_height
                font_size: "15dp"

            MDTextField:
                id: spouse_marriage_date
                hint_text: "Enter Spouse Marriage Date"
                helper_text: 'YYYY-MM-DD'
                helper_text_mode: "on_error"
                font_name: "Roboto-Bold"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                height:self.minimum_height
                font_size: "15dp"
                input_type:'number'
                on_touch_down: root.on_date_touch_down()

            MDTextField:
                id: spouse_mobile
                hint_text: 'Enter Spouse Mobile No'
                multiline: False
                helper_text: "Enter Valid Spouse Mobile No"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                height:self.minimum_height
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"
                input_type: 'number'
                on_touch_down: root.on_spouse_mobile_touch_down()

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]
                MDRectangleFlatButton:
                    text: 'Next'
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
                    on_release: root.add_data(spouse_name.text, spouse_marriage_date.text, spouse_mobile.text)


<LenderScreen11>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen10')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
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
            spacing: dp(25)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Spouse Details'
                halign: 'center'
                bold:True

            MDLabel:
                text:"Select Spouse Profession Type:"
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(20)

            Spinner:
                id: spouse_profession
                text: "Select Spouse Profession"
                multiline: False
                size_hint: 1 , None
                font_size: "15dp"
                height:"40dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDTextField:
                id: spouse_company_name
                hint_text: 'Enter Spouse Company Name'
                multiline: False
                helper_text: "Enter Valid Spouse Company Name (if working)"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                height:self.minimum_height
                font_size: "15dp"

            MDTextField:
                id: spouse_annual_salary
                hint_text: 'Enter Annual Salary'
                font_size: "15dp"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                multiline: False
                helper_text: 'Enter valid Annual Salary (if working)'
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                input_type: 'number'
                on_touch_down: root.on_spouse_annual_salary_touch_down()

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]
                MDRectangleFlatButton:
                    text: 'Next'
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
                    on_release: root.add_data(spouse_company_name.text, spouse_profession.text, spouse_annual_salary.text)

<LenderScreen12>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text: "Family Members Details"
            size_hint_y: None
            height: dp(40)
            padding: [0, dp(40), 0, 0]  # Padding: [left, top, right, bottom]
            halign: "center"
            bold: True
            font_name: "Roboto-Bold"
        BoxLayout:
            orientation: "vertical"
            spacing: "7dp"
            padding: "15dp"

            MDLabel:
                text: "Provide Another Person Details"
                halign: "center"
                size_hint_y: None
                height: dp(70)

            MDGridLayout:
                cols: 4
                spacing: dp(10)
                pos_hint: {'center_x': 0.3, 'center_y': 0.5}  # Fixed the typo here
                MDFillRoundFlatButton:
                    id: id1
                    text: "Father"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed1()
                MDFillRoundFlatButton:
                    id: id2
                    text: "Mother"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed2()
                MDFillRoundFlatButton:
                    id: id3
                    text: "Spouse"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed3()
                MDFillRoundFlatButton:
                    id: id4
                    text: "Other"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed4()

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data()
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreen13>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text: "Family Members Details"
            size_hint_y: None
            height: dp(40)
            padding: [0, dp(40), 0, 0]
            halign: "center"
            bold: True
            font_name: "Roboto-Bold"

        BoxLayout:
            orientation: "vertical"
            spacing: dp(10)
            padding: dp(10)

            MDLabel:
                text: "Provide Another Person Details"
                halign: "center"
                size_hint_y: None
                height: dp(70)
            MDGridLayout:
                cols: 4
                spacing: dp(10)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}  # Fixed the typo here
                MDFillRoundFlatButton:
                    id: id1
                    text: "Father"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed1()
                MDFillRoundFlatButton:
                    id: id2
                    text: "Mother"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed2()

                MDFillRoundFlatButton:
                    id: id4
                    text: "Other"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed4()

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data()
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"
<LenderScreen14>:
    MDTopAppBar:
        title: "P2P LENDING"
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
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
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Person Details'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)


            MDTextField:
                id: relation_name
                hint_text: 'How is the person related to you'
                helper_text: 'Enter Valid Person Relation'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: person_name
                hint_text: 'Enter Person Name'
                helper_text: 'Enter Valid Person Name'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: person_dob
                hint_text: 'Enter Person D.O.B'
                helper_text: 'YYYY-MM-DD'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                input_type:'number'
                on_touch_down: root.on_date_touch_down()
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"


            MDTextField:
                id: person_ph_no
                hint_text: 'Enter Person Phone No'
                helper_text: 'Enter Valid Person Phone No'
                helper_text_mode: 'on_focus'
                halign: 'left'
                input_type: 'number'  
                on_touch_down: root.on_mother_ph_no_touch_down()
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: person_proffission
                hint_text: 'Enter Person Profession'
                helper_text: 'Enter valid Person Profession'
                multiline: False
                helper_text_mode: 'on_focus'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: [0, "30dp", 0, 0]
                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(relation_name.text, person_name.text, person_dob.text, person_ph_no.text, person_proffission.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreenIndividualBankForm1>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
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
                text: 'Applicant Bank Details'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
            MDTextField:
                id: account_holder_name
                hint_text: 'Enter account holder name '
                helper_text: 'Enter Your account holder name'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y:None
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDLabel:
                text: 'Select Account Type:'
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(20)

            Spinner:
                id: spinner_id
                text: "Select Account Type"
                font_size: "15dp"
                multiline: False
                size_hint: 1 , None
                height:"40dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDTextField:
                id: account_number
                hint_text: 'Enter account number '
                multiline: False
                helper_text: 'Enter Your account number'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                input_type: 'number'

            MDTextField:
                id: bank_name
                hint_text: 'Enter bank name '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y:None
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]
                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(account_holder_name.text, spinner_id.text, account_number.text, bank_name.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreenIndividualBankForm2>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenIndividualBankForm1')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
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
            spacing: dp(25)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Applicant Bank Details'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: ifsc_code
                hint_text: 'Enter Bank ID '
                multiline: False
                helper_text: 'Enter valid Bank ID'
                helper_text_mode: 'on_focus'
                size_hint_y:None
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: branch_name
                hint_text: 'Enter branch name'
                hint_text_mode: 'on_focus'
                hint_text_mode: 'on_focus'
                multiline: False
                halign: 'left'
                multiline: False
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
            BoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                height: "29dp"
                spacing:dp(5)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                MDCheckbox:
                    id: check
                    size_hint: None, None
                    size: "30dp", "30dp"
                    active: False
                    on_active: root.on_checkbox_active(self, self.active)

                MDLabel:
                    text: "I Agree Terms and Conditions"
                    size: "30dp", "30dp"
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1
                    halign: "left"
                    valign: "center"
                    on_touch_down: app.root.get_screen("LenderScreenIndividualBankForm2").show_terms_dialog() if self.collide_point(*args[1].pos) else None


            GridLayout:
                cols: 1
                spacing:dp(30)
                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.go_to_lender_dashboard(ifsc_code.text, branch_name.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

'''

conn = sqlite3.connect("fin_user.db")
cursor = conn.cursor()


class LenderScreen(Screen):
    Builder.load_string(KV)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_gender.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['gender'])
        unique_list = []
        for i in data_list:
            if i not in unique_list:
                unique_list.append(i)
        print(unique_list)
        if len(unique_list) >= 1:
            self.ids.spinner_id.values = ['Select Gender'] + unique_list
        else:
            self.ids.spinner_id.values = ['Select Gender']

        user_email = anvil.server.call('another_method')
        data = app_tables.fin_user_profile.search(email_user=user_email)

        id_list = []
        for i in data:
            id_list.append(i['email_user'])
        if user_email in id_list:
            index = id_list.index(user_email)
            self.ids.username.text = data[index]['full_name']
        else:
            print('email not found')

    def on_date_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.date_textfield.input_type = 'number'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, name, gender, date):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(name, gender, date, modal_view), 2)

    def perform_data_addition_action(self, name, gender, date, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if not all([name, date, gender]):
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if there are missing fields

        if not name or len(name.split()) < 2 or not re.match(r'^[a-zA-Z\s]+$', name):
            self.show_validation_error("Please enter a valid full name with at least a first name and last name.")
            return

        if not gender or gender == 'Select Gender':
            self.show_validation_error("Please select your gender.")
            return
            # Check if date of birth is provided
        if not date:
            self.show_validation_error("Please enter your date of birth.")
            return

        # Parse date string to datetime object
        try:
            dob = datetime.strptime(date, '%Y-%m-%d')
            # Calculate age based on current date
            today = datetime.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

            # Check if age is less than 18
            if age < 18:
                self.show_validation_error("You must be at least 18 years old to register.")
                return

        except ValueError:
            self.show_validation_error("Invalid date format. Please use YYYY-MM-DD.")
            return

        if date == '':
            self.ids.date.error = True
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        email_list = []
        status = []

        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
            email_list.append(row[2])
        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET name = ?, gender = ?, date_of_birth = ? WHERE customer_id = ?",
                (name, gender, date, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")
        user_email = anvil.server.call('another_method')
        data = app_tables.fin_user_profile.search()

        id_list = []
        for i in data:
            id_list.append(i['email_user'])
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['full_name'] = name
            data[index]['gender'] = gender
            data[index]['date_of_birth'] = date
            data[index]['form_count'] = 1
        else:
            print("email not there")

        sm = self.manager
        lender_screen1 = LenderScreen1(name='LenderScreen1')
        sm.add_widget(lender_screen1)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreen1'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

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
        self.manager.current = 'LenderLanding'  # Replace with the actual name of your previous screen

    def refresh(self):
        pass

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'


class LenderScreen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        user_email = anvil.server.call('another_method')
        data = app_tables.fin_user_profile.search(email_user=user_email)
        id_list = []
        for i in data:
            id_list.append(i['email_user'])
        if user_email in id_list:
            index = id_list.index(user_email)
            self.ids.mobile_number.text = data[index]['mobile']
        else:
            print('email not found')

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
        self.manager.get_screen('LenderScreen1').ids[image_label_id].text = file_name  # Update the label text
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

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET upload_photo = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()

        self.ids.upload_label1.text = 'Upload Successfully'

    # Repeat similar methods for file manager 2...
    def refresh(self):
        pass

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, mobile_number, alternate_email):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(mobile_number, alternate_email, modal_view), 2)

    def perform_data_addition_action(self, mobile_number, alternate_email, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        if not all([mobile_number, alternate_email]):
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if there are missing fields

        # Check if mobile number is provided and has exactly 10 digits
        if not mobile_number or not re.match(r'^\d{10}$|^\d{12}$', mobile_number):
            self.show_validation_error("Please enter a valid 10-digit mobile number.")
            return

        # Check if alternate email is provided and is valid
        if alternate_email and not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', alternate_email):
            self.show_validation_error("Please enter a valid email address for alternate email.")
            return
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        email_list = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
            email_list.append(row[2])
        if 'logged' in status:
            log_index = status.index('logged')

            cursor.execute(
                "UPDATE fin_registration_table SET mobile_number = ?, alternate_email = ? WHERE customer_id = ?",
                (mobile_number, alternate_email, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")
        user_email = anvil.server.call('another_method')
        data = app_tables.fin_user_profile.search(email_user=user_email)
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['mobile'] = mobile_number
            data[index]['another_email'] = alternate_email
            data[index]['form_count'] = 2
        else:
            print('no email found')

        sm = self.manager
        lender_screen2 = LenderScreen2(name='LenderScreen2')
        sm.add_widget(lender_screen2)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreen2'

    def on_mobile_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mobile_number.input_type = 'number'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'


class LenderScreen2(Screen):

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1")

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label2")

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
        self.manager.get_screen('LenderScreen2').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path2(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreen2').ids[image_label_id].text = file_name  # Update the label text
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

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET aadhar_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()

        self.ids.upload_label1.text = 'Upload Successfully'

    # Repeat similar methods for file manager 2...

    def add_data(self, aadhar_number, pan_number):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(aadhar_number, pan_number, modal_view), 2)

    def perform_data_addition_action(self, aadhar_number, pan_number, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        if not all([aadhar_number, pan_number]):
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if there are missing fields

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET aadhar_number = ?, pan_number = ? WHERE customer_id = ?",
                           (aadhar_number, pan_number, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")
        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['aadhaar_no'] = aadhar_number
            data[index]['pan_number'] = pan_number
        else:
            print('no email found')
        # self.manager.current = 'LenderScreen3'
        sm = self.manager
        lender_screen3 = LenderScreen3(name='LenderScreen3')
        sm.add_widget(lender_screen3)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreen3'

    def refresh(self):
        pass

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen1'


class LenderScreen3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_present_address.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['present_address'])
        self.unique_list = []
        for i in data_list:
            if i not in self.unique_list:
                self.unique_list.append(i)
        print(self.unique_list)
        if len(self.unique_list) >= 1:
            self.ids.spinner_id1.values = ['Select Present Address'] + self.unique_list
        else:
            self.ids.spinner_id1.values = ['Select Present Address']

        spinner_data = app_tables.fin_duration_at_address.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['duration_at_address'])
        self.unique_list = []
        for i in data_list:
            if i not in self.unique_list:
                self.unique_list.append(i)
        print(self.unique_list)
        if len(self.unique_list) >= 1:
            self.ids.spinner_id2.values = ['Select Staying Address'] + self.unique_list
        else:
            self.ids.spinner_id2.values = ['Select Staying Address']

    def refresh(self):
        pass

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, street_address1, street_address2, spinner_id1, spinner_id2):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action4(street_address1, street_address2, spinner_id1, spinner_id2,
                                                          modal_view), 2)

    def perform_data_addition_action4(self, street_address1, street_address2, spinner_id1, spinner_id2, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        # Check for missing fields
        if not all([street_address1, street_address2, spinner_id1, spinner_id2]):
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if there are missing fields
        if len(street_address1) < 3:
            self.show_validation_error('Enter a valid Street Name')
            return
        if not spinner_id1 or spinner_id1 == 'Select Present Address':
            self.show_validation_error("Please Select Your Present Address.")
            return
        if not spinner_id2 or spinner_id2 == 'Select Staying Address':
            self.show_validation_error("Please Select Your Duration At Address.")
            return
        if len(street_address2) < 3:
            self.show_validation_error('Enter a valid Street Name')
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')


        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['street_adress_1'] = street_address1
            data[index]['street_address_2'] = street_address2
            data[index]['present_address'] = spinner_id1
            data[index]['duration_at_address'] = spinner_id2
        else:
            print('no email found')
        sm = self.manager
        lender_screen = LenderScreen4(name='LenderScreen4')
        sm.add_widget(lender_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreen4'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen3'


class LenderScreen4(Screen):

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, city, zip_code, state, country):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action4(city, zip_code, state, country, modal_view), 2)

    def perform_data_addition_action4(self, city, zip_code, state, country, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        # Check for missing fields
        if not all([city, zip_code, state, country]):
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if there are missing fields
        if len(city) < 3:
            self.show_validation_error('Enter a valid City Name')
            return
        if len(zip_code) < 3:
            self.show_validation_error('Enter a valid Zipcode Name')
            return
        if len(state) < 2:
            self.show_validation_error('Enter a valid Sate Name')
            return
        if len(country) < 3:
            self.show_validation_error('Enter a valid Country Name')
            return
            # Check if zip code is provided and has a valid format

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')

            cursor.execute(
                "UPDATE fin_registration_table SET city_name = ?, zip_code = ?, state_name = ?, country_name = ? WHERE customer_id = ?",
                (city, zip_code, state, country, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['city'] = city
            data[index]['pincode'] = zip_code
            data[index]['state'] = state
            data[index]['country'] = country
        else:
            print('no email found')
        sm = self.manager
        lender_screen = LenderScreen5(name='LenderScreen5')
        sm.add_widget(lender_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreen5'

    def refresh(self):
        pass

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def on_mobile_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.zip_code.input_type = 'number'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen3'


class LenderScreen5(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_lendor_qualification.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['lendor_qualification'])
        unique_list = []
        for i in data_list:
            if i not in unique_list:
                unique_list.append(i)
        print(unique_list)
        if len(unique_list) >= 1:
            self.ids.spinner_id.values = ['Select Education Details'] + unique_list
        else:
            self.ids.spinner_id.values = ['Select Education Details']

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def next_pressed(self, id):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(id, modal_view), 2)

    def perform_data_addition_action(self, id, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        if not id or id == 'Select Education Details':
            self.show_validation_error("Please Select Your Education Details.")
            return
        if id == '10th class' or id == '10th standard':
            LenderScreen_Edu_10th()
            sm = self.manager
            lender_screen = LenderScreen_Edu_10th(name='LenderScreen_Edu_10th')
            sm.add_widget(lender_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen_Edu_10th'
        elif id == 'Intermediate' or id == '12th standard':
            LenderScreen_Edu_Intermediate()
            sm = self.manager
            lender_screen = LenderScreen_Edu_Intermediate(name='LenderScreen_Edu_Intermediate')
            sm.add_widget(lender_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen_Edu_Intermediate'
        elif id == 'Bachelors' or id == "Bachelor's degree":

            sm = self.manager
            lender_screen = LenderScreen_Edu_Bachelors(name='LenderScreen_Edu_Bachelors')
            sm.add_widget(lender_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen_Edu_Bachelors'
        elif id == 'Masters' or id == "Master's degree":

            sm = self.manager
            lender_screen = LenderScreen_Edu_Masters(name='LenderScreen_Edu_Masters')
            sm.add_widget(lender_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen_Edu_Masters'
        elif id == 'PHD' or id == 'PhD':

            sm = self.manager
            lender_screen = LenderScreen_Edu_PHD(name='LenderScreen_Edu_PHD')
            sm.add_widget(lender_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen_Edu_PHD'
        print(id)
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET highest_qualification = ? WHERE customer_id = ?",
                           (id, row_id_list[log_index]))
            conn.commit()
            data = app_tables.fin_user_profile.search()
            id_list = []
            for i in data:
                id_list.append(i['email_user'])

            user_email = anvil.server.call('another_method')
            if user_email in id_list:
                index = id_list.index(user_email)
                data[index]['qualification'] = id
            else:
                print('email not found')
        else:
            print('User is not logged in.')

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def refresh(self):
        pass

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen4'


class LenderScreen_Edu_10th(Screen):
    def refresh(self):
        pass

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

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
        self.manager.get_screen('LenderScreen_Edu_10th').ids[image_label_id].text = file_name  # Update the label text
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

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        else:
            print('User is not logged in.')

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen5'

    def go_to_lender_screen4(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_loan_request_action10th(modal_view), 2)

    def perform_loan_request_action10th(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        lender_screen4 = LenderScreen6(name='LenderScreen6')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(lender_screen4)

        # Switch to the LoginScreen
        sm.current = 'LenderScreen6'


class LenderScreen_Edu_Intermediate(Screen):
    def refresh(self):
        pass

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1")

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label2")

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
        self.manager.get_screen('LenderScreen_Edu_Intermediate').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path2(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreen_Edu_Intermediate').ids[
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

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label2.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen5'

    def go_to_lender_screen4(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_loan_request_action11th(modal_view), 2)

    def perform_loan_request_action11th(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        lender_screen4 = LenderScreen6(name='LenderScreen6')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(lender_screen4)

        # Switch to the LoginScreen
        sm.current = 'LenderScreen6'


class LenderScreen_Edu_Bachelors(Screen):
    def refresh(self):
        pass

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1")

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label2")

    def check_and_open_file_manager3(self):
        self.check_and_open_file_manager("upload_icon3", "upload_label3", "selected_file_label3", "selected_image3",
                                         "image_label3")

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
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreen_Edu_Bachelors').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path2(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreen_Edu_Bachelors').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path3(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreen_Edu_Bachelors').ids[
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

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label2.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_3(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label3.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen5'

    def go_to_lender_screen4(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_loan_request_action_bachelors(modal_view), 2)

    def perform_loan_request_action_bachelors(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        lender_screen4 = LenderScreen6(name='LenderScreen6')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(lender_screen4)

        # Switch to the LoginScreen
        sm.current = 'LenderScreen6'


class LenderScreen_Edu_Masters(Screen):
    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1")

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label2")

    def check_and_open_file_manager3(self):
        self.check_and_open_file_manager("upload_icon3", "upload_label3", "selected_file_label3", "selected_image3",
                                         "image_label3")

    def check_and_open_file_manager4(self):
        self.check_and_open_file_manager("upload_icon4", "upload_label4", "selected_file_label4", "selected_image4",
                                         "image_label4")

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
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreen_Edu_Masters').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path2(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreen_Edu_Masters').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path3(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreen_Edu_Masters').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path4(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreen_Edu_Masters').ids[
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

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label2.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_3(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label3.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_4(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET masters_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label4.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen5'

    def go_to_lender_screen4(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_masters_action(modal_view), 2)

    def refresh(self):
        pass

    def perform_masters_action(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        lender_screen4 = LenderScreen6(name='LenderScreen6')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(lender_screen4)

        # Switch to the LoginScreen
        sm.current = 'LenderScreen6'


class LenderScreen_Edu_PHD(Screen):
    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1")

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label2")

    def check_and_open_file_manager3(self):
        self.check_and_open_file_manager("upload_icon3", "upload_label3", "selected_file_label3", "selected_image3",
                                         "image_label3")

    def check_and_open_file_manager4(self):
        self.check_and_open_file_manager("upload_icon4", "upload_label4", "selected_file_label4", "selected_image4",
                                         "image_label4")

    def check_and_open_file_manager5(self):
        self.check_and_open_file_manager("upload_icon5", "upload_label5", "selected_file_label5", "selected_image5",
                                         "image_label5")

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
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreen_Edu_PHD').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path2(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreen_Edu_PHD').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path3(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreen_Edu_PHD').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path4(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreen_Edu_PHD').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path5(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreen_Edu_PHD').ids[image_label_id].text = file_name  # Update the label text
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

    def refresh(self):
        pass

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label2.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_3(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label3.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_4(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET masters_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label4.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_5(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET phd_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label5.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen5'

    def go_to_lender_screen4(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_phd_action(modal_view), 2)

    def perform_phd_action(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        lender_screen4 = LenderScreen6(name='LenderScreen6')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(lender_screen4)

        # Switch to the LoginScreen
        sm.current = 'LenderScreen6'


class LenderScreen6(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_lendor_lending_type.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['lendor_lending_type'])
        unique_list = []
        for i in data_list:
            if i not in unique_list:
                unique_list.append(i)
        print(unique_list)
        if len(unique_list) >= 1:
            self.ids.spinner.values = ['Select Loan Type'] + unique_list
        else:
            self.ids.spinner.values = ['Select Loan Type']

        spinner_data = app_tables.fin_lendor_lending_period.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['lendor_lending_period'])
        unique_list = []
        for i in data_list:
            if i not in unique_list:
                unique_list.append(i)
        print(unique_list)
        if len(unique_list) >= 1:
            self.ids.spinner2.values = ['Select Lending Period'] + unique_list
        else:
            self.ids.spinner2.values = ['Select Lending Period']

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def next_pressed(self, spinner, investment, spinner2):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action4(spinner, investment, spinner2, modal_view), 2)

    def perform_data_addition_action4(self, spinner, spinner2, investment, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        # Check for missing fields
        if not all([spinner, spinner2, investment]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if there are missing fields

        if spinner not in spinner == 'Select Loan Type':
            self.show_validation_error('Select valid Loan type')
            return
        if spinner2 not in spinner2 == 'Select Lending Period':
            self.show_validation_error('Select valid Lending Period')
            return
        if investment.isdigit():
            investment = float(investment)
            if investment <= 100000:
                self.show_validation_error("Investment amount must be greater than or equal to 1 lakh.")
            else:
                self.show_validation_error("Invalid investment amount.")

        if spinner == 'Individual':
            sm = self.manager
            lender_screen = LenderScreenIndividualForm1(name='LenderScreenIndividualForm1')
            sm.add_widget(lender_screen)
            sm.transition.direction = 'left'
            sm.current = 'LenderScreenIndividualForm1'

        elif spinner == 'Institutional':
            sm = self.manager
            borrower_screen = LenderScreenInstitutionalForm1(name='LenderScreenInstitutionalForm1')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'LenderScreenInstitutionalForm1'

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET loan_type = ?, investment = ?, lending_period = ? WHERE customer_id = ?",
                (spinner, investment, spinner2, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['loan_type'] = spinner
            data[index]['investment'] = investment
            data[index]['lending_period'] = spinner2
        else:
            print('email not found')

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def on_investment_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.investment.input_type = 'number'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen5'


class LenderScreenInstitutionalForm1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_lendor_business_type.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['lendor_business_type'])
        unique_list = []
        for i in data_list:
            if i not in unique_list:
                unique_list.append(i)
        print(unique_list)
        if len(unique_list) >= 1:
            self.ids.spin.values = ['Select Business Type'] + unique_list
        else:
            self.ids.spin.values = ['Select Business Type']

        spinner_data = app_tables.fin_lendor_no_of_employees.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['lendor_no_of_employees'])
        unique_list = []
        for i in data_list:
            if i not in unique_list:
                unique_list.append(i)
        print(unique_list)
        if len(unique_list) >= 1:
            self.ids.spinner_id.values = ['Select No.Of Employees Working'] + unique_list
        else:
            self.ids.spinner_id.values = ['Select No.Of Employees Working']

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, business_name, business_address, business_type, no_of_employees_working):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action4(business_name, business_type, no_of_employees_working,
                                                          business_address,
                                                          modal_view), 2)

    def perform_data_addition_action4(self, business_name, business_type, no_of_employees_working, business_address,
                                      modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        # Check for missing fields
        if not all([business_name, business_address, business_type, no_of_employees_working]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if there are missing fields
        if not re.match(r'^[a-zA-Z\s]+$', business_name):
            self.show_validation_error('Enter a valid business Name')
            return
        if len(business_address) < 3:
            self.show_validation_error('Enter a valid business address')
            return
        if business_type not in business_type == 'Select Business Type':
            self.show_validation_error('Select valid business type')
            return
        if no_of_employees_working not in no_of_employees_working == 'Select No.Of Employees Working':
            self.show_validation_error('Select valid no of employees')
            return
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        email_list = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
            email_list.append(row[2])
        if 'logged' in status:
            log_index = status.index('logged')

            cursor.execute(
                "UPDATE fin_registration_table SET business_name = ?, business_address = ? WHERE customer_id = ?",
                (business_name, business_address, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")
        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['business_name'] = business_name
            data[index]['business_add'] = business_address
            data[index]['business_type'] = business_type
            data[index]['employees_working'] = no_of_employees_working
        else:
            print('no email found')
        sm = self.manager
        lender_screen = LenderScreenInstitutionalForm2(name='LenderScreenInstitutionalForm2')
        sm.add_widget(lender_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreenInstitutionalForm2'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen6'


class LenderScreenInstitutionalForm2(Screen):

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, industry_type, last_six_months_turnover, year_of_estd):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action4(industry_type, last_six_months_turnover, year_of_estd,
                                                          modal_view), 2)

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
        self.manager.get_screen('LenderScreenInstitutionalForm2').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def on_estd_touch_down(self):
        self.ids.year_of_estd.input_type = 'number'

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

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET last_six_months_turnover_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def perform_data_addition_action4(self, industry_type, last_six_months_turnover, year_of_estd,
                                      modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        # Check for missing fields
        if not all([industry_type, last_six_months_turnover, year_of_estd]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if there are missing fields
        if not re.match(r'^[a-zA-Z]{3,}$', industry_type):
            self.show_validation_error("Enter a valid industryy type.")
            return
        if len(last_six_months_turnover) < 3 or not last_six_months_turnover.isdigit():
            self.show_validation_error("Enter a valid last six months turnover.")
            return
        try:
            dob = datetime.strptime(year_of_estd, "%Y-%m-%d")

        except ValueError:
            self.show_validation_error("Please enter a valid date of birth in the format YYYY-MM-DD")
            return
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        email_list = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
            email_list.append(row[2])
        if 'logged' in status:
            log_index = status.index('logged')

            cursor.execute(
                "UPDATE fin_registration_table SET year_of_estd = ? WHERE customer_id = ?",
                (year_of_estd, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")
        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['year_of_estd'] = year_of_estd
            data[index]['industry_type'] = industry_type
            data[index]['six_month_turnover'] = last_six_months_turnover
        else:
            print('email not found')
        # self.manager.current = 'LenderScreenInstitutionalForm3'
        sm = self.manager
        lender_screen = LenderScreenInstitutionalForm3(name='LenderScreenInstitutionalForm3')
        sm.add_widget(lender_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreenInstitutionalForm3'

    def on_last_six_months_turnover_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.last_six_months_turnover.input_type = 'number'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreenInstitutionalForm1'


class LenderScreenInstitutionalForm3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
        self.manager.get_screen('LenderScreenInstitutionalForm3').ids[
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

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET proof_of_verification_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, cin, din, registered_office_address):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action4(registered_office_address, cin, din, modal_view), 2)

    def perform_data_addition_action4(self, cin, din, registered_office_address, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        # Check for missing fields
        if not all([cin, din, registered_office_address]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if there are missing fields
        if len(cin) < 3:
            self.show_validation_error("Enter a valid cin.")
            return
        if len(din) < 3:
            self.show_validation_error("Enter a valid din.")
            return
        if len(registered_office_address) < 3:
            self.show_validation_error("Enter a valid registered_office_address.")
            return
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        email_list = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
            email_list.append(row[2])
        if 'logged' in status:
            log_index = status.index('logged')

            cursor.execute(
                "UPDATE fin_registration_table SET cin = ?,registered_office_address = ?, din = ? WHERE customer_id = ?",
                (cin, din, registered_office_address, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")
        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['cin'] = cin
            data[index]['din'] = din
            data[index]['registered_off_add'] = registered_office_address

        else:
            print('email not found')
        # self.manager.current = 'LenderScreenInstitutionalForm4'
        sm = self.manager
        lender_screen = LenderScreen7(name='LenderScreen7')
        sm.add_widget(lender_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreen7'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreenInstitutionalForm2'


class LenderScreenIndividualForm1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_lendor_employee_type.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['lendor_employee_type'])
        unique_list = []
        for i in data_list:
            if i not in unique_list:
                unique_list.append(i)
        print(unique_list)
        if len(unique_list) >= 1:
            self.ids.spinner1.values = ['Select Employment Type'] + unique_list
        else:
            self.ids.spinner1.values = ['Select Employment Type']

        spinner_data = app_tables.fin_lendor_organization_type.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['lendor_organization_type'])
        unique_list = []
        for i in data_list:
            if i not in unique_list:
                unique_list.append(i)
        print(unique_list)
        if len(unique_list) >= 1:
            self.ids.spinner2.values = ['Select Organisation Type'] + unique_list
        else:
            self.ids.spinner2.values = ['Select Organisation Type']

        spinner_data = app_tables.fin_occupation_type.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['occupation_type'])
        unique_list = []
        for i in data_list:
            if i not in unique_list:
                unique_list.append(i)
        print(unique_list)
        if len(unique_list) >= 1:
            self.ids.spinner3.values = ['Select Occupation Type'] + unique_list
        else:
            self.ids.spinner3.values = ['Select Occupation Type']

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, spinner1, company_name, spinner2, spinner3):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action4(spinner1, company_name, spinner2, spinner3, modal_view), 2)

    def perform_data_addition_action4(self, spinner1, company_name, spinner2, spinner3, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        # Check for missing fields
        if not all([spinner1, company_name, spinner2, spinner3]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if spinner1 not in spinner1 == 'Select Employment Type':
            self.show_validation_error('Select a valid employment type')
            return
        if not re.match(r'^[a-zA-Z\s]{3,}$', company_name):
            self.show_validation_error('Enter a valid company name')
            return
        if spinner2 not in spinner2 == 'Select Organisation Type':
            self.show_validation_error('Select a valid organisation type')
            return
        if spinner3 not in spinner3 == 'Select Occupation Type':
            self.show_validation_error('Select a valid occupation  type')
            return
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        email_list = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
            email_list.append(row[2])
        if 'logged' in status:
            log_index = status.index('logged')

            cursor.execute(
                "UPDATE fin_registration_table SET employment_type = ?, company_name = ?, organization_type = ? WHERE customer_id = ?",
                (spinner1, company_name, spinner2, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")
        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['employment_type'] = spinner1
            data[index]['company_name'] = company_name
            data[index]['organization_type'] = spinner2
            data[index]['occupation_type'] = spinner3
        else:
            print('email not found')
        sm = self.manager
        lender_screen = LenderScreenIndividualForm2(name='LenderScreenIndividualForm2')
        sm.add_widget(lender_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreenIndividualForm2'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen6'


class LenderScreenIndividualForm2(Screen):
    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1")

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label2")

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
        self.manager.get_screen('LenderScreenIndividualForm2').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path2(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreenIndividualForm2').ids[
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

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET employee_id_file = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET six_months_bank_statement_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

    def add_data(self, annual_salary, designation):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_data_addition_action4(annual_salary, designation, modal_view), 2)

    def perform_data_addition_action4(self, annual_salary, designation, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        # Check for missing fields
        if not all([annual_salary, designation]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if not re.match(r'^[a-zA-Z\s]{2,}$', designation):
            self.show_validation_error("Please Enter Valid designation.")
            return
        if len(annual_salary) < 3 and not annual_salary.isdigit():
            self.show_validation_error("Please Enter Valid Company Number.")
            return
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        email_list = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
            email_list.append(row[2])
        if 'logged' in status:
            log_index = status.index('logged')

            cursor.execute(
                "UPDATE fin_registration_table SET annual_salary = ?, designation = ? WHERE customer_id = ?",
                (annual_salary, designation, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")
        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['annual_salary'] = annual_salary
            data[index]['designation'] = designation
        else:
            print('email not found')
        sm = self.manager

        # Create a new instance of the LenderScreenIndividualForm3
        lender_screen = LenderScreenIndividualForm3(name='LenderScreenIndividualForm3')

        # Add the LenderScreenIndividualForm3 to the existing ScreenManager
        sm.add_widget(lender_screen)

        # Switch to the LenderScreenIndividualForm3
        sm.current = 'LenderScreenIndividualForm3'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def on_annual_salary_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.annual_salary.input_type = 'number'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreenIndividualForm1'


class LenderScreenIndividualForm3(Screen):

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, company_address, company_pincode, company_country, landmark, business_number):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action4(company_address, company_pincode, company_country, landmark,
                                                          business_number, modal_view), 2)

    def perform_data_addition_action4(self, company_address, company_pincode, company_country, landmark,
                                      business_number, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        # Check for missing fields
        if not all([company_address, company_pincode, company_country, landmark, business_number]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if len(company_address) < 3:
            self.show_validation_error("Please Enter Valid Company Address.")
            return
        if len(company_pincode) < 3 or not company_pincode.isdigit():
            self.show_validation_error("Please Enter Valid Company Pincode.")
            return
        if len(company_country) < 3 or not re.match(r'^[a-zA-Z]+$', company_country):
            self.show_validation_error("Please Enter Valid Company Country.")
            return
        if len(landmark) < 3:
            self.show_validation_error("Please Enter Valid Landmark.")
            return
        if not business_number.isdigit() or len(business_number) not in (10, 12):
            self.show_validation_error("Please Enter Valid Business Number.")
            return
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        email_list = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
            email_list.append(row[2])
        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET company_address = ?, company_pincode = ?, company_country = ?, landmark = ?, business_number = ? WHERE customer_id = ?",
                (company_address, company_pincode, company_country, landmark, business_number, row_id_list[log_index]))
            conn.commit()

        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")
        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['company_address'] = company_address
            data[index]['company_landmark'] = landmark
            data[index]['business_no'] = business_number
            data[index]['company_country'] = company_country
            data[index]['company_pincode'] = company_pincode
        else:
            print('email not found')
        sm = self.manager

        # Create a new instance of the LenderScreenIndividualBankForm1
        lender_screen = LenderScreen7(name='LenderScreen7')

        # Add the LenderScreenIndividualBankForm1 to the existing ScreenManager
        sm.add_widget(lender_screen)

        # Switch to the LenderScreenIndividualBankForm1
        sm.current = 'LenderScreen7'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def on_company_pin_code_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.company_pin_code.input_type = 'number'

    def on_business_phone_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.business_phone_number.input_type = 'number'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreenIndividualForm2'


class LenderScreen7(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_lendor_marrital_status.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['lendor_marrital_status'])
        unique_list = []
        for i in data_list:
            if i not in unique_list:
                unique_list.append(i)
        print(unique_list)
        if len(unique_list) >= 1:
            self.ids.marital_status_id.values = ['Select Marital Status'] + unique_list
        else:
            self.ids.marital_status_id.values = ['Select Marital Status']

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, marital_status_id):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(marital_status_id, modal_view), 2)

    def perform_data_addition_action(self, marital_status_id, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if not all([marital_status_id]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if marital_status_id not in marital_status_id == 'Select Marital Status':
            self.show_validation_error('Select a valid Marital status')
            return
        if marital_status_id == 'Un-Married' or marital_status_id == 'Not Married':
            sm = self.manager
            borrower_screen = LenderScreen13(name='LenderScreen13')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'LenderScreen13'

        elif marital_status_id == 'Married':
            sm = self.manager
            borrower_screen = LenderScreen12(name='LenderScreen12')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'LenderScreen12'

        elif marital_status_id == 'Divorced':
            sm = self.manager
            borrower_screen = LenderScreen13(name='LenderScreen13')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'LenderScreen13'
        elif marital_status_id == 'Other':
            sm = self.manager
            borrower_screen = LenderScreen13(name='LenderScreen13')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'LenderScreen13'

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET marital_status = ? WHERE customer_id = ?",
                (marital_status_id, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['marital_status'] = marital_status_id
        else:
            print('email not found')

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen6'


class LenderScreen8(Screen):
    def on_date_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.father_dob.input_type = 'number'

    def on_father_ph_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.father_ph_no.input_type = 'number'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, father_name, father_address, father_occupation, father_ph_no, father_dob):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(father_name, father_address, father_occupation, father_ph_no,
                                                         father_dob,
                                                         modal_view), 2)

    def perform_data_addition_action(self, father_name, father_address, father_occupation, father_ph_no, father_dob,
                                     modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        # Check for missing fields
        if not all([father_name, father_address, father_occupation, father_ph_no, father_dob]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing

        if not father_ph_no.isdigit() or len(father_ph_no) not in (10, 12):
            self.show_validation_error("Please Enter Valid Father Number.")
            return
        if not re.match(r'^[a-zA-Z\s]{3,}$', father_name):
            self.show_validation_error("Please Enter Valid Father Name.")
            return
        if len(father_occupation) < 3:
            self.show_validation_error("Please Enter Valid Father Occupation.")
            return
        if not re.match(r'^[a-zA-Z\s]{3,}$', father_address):
            self.show_validation_error("Please enter valid father Age.")
            return
        try:
            dob = datetime.strptime(father_dob, "%Y-%m-%d")


        except ValueError:
            self.show_validation_error("Please enter a valid date of birth in the format YYYY-MM-DD")
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET father_name = ?, father_address = ?, father_occupation = ?, father_ph_no = ? WHERE customer_id = ?",
                (father_name, father_address, father_occupation, father_ph_no, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['guarantor_name'] = father_name
                data2[index2]['guarantor_address'] = father_address
                data2[index2]['guarantor_mobile_no'] = int(father_ph_no)
                data2[index2]['guarantor_profession'] = father_occupation
                data2[index2]['guarantor_date_of_births'] = father_dob
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = LenderScreenIndividualBankForm1(name='LenderScreenIndividualBankForm1')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreenIndividualBankForm1'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen7'


class LenderScreen9(Screen):
    def on_date_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mother_dob.input_type = 'number'

    def on_mother_ph_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mother_ph_no.input_type = 'number'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, mother_name, mother_address, mother_occupation, mother_ph_no, mother_dob):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(mother_name, mother_address, mother_occupation, mother_ph_no,
                                                         mother_dob,
                                                         modal_view), 2)

    def perform_data_addition_action(self, mother_name, mother_address, mother_occupation, mother_ph_no, mother_dob,
                                     modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        # Check for missing fields
        if not all([mother_name, mother_address, mother_occupation, mother_ph_no, mother_dob]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing

        if not mother_ph_no.isdigit() and len(mother_ph_no) not in (10, 12):
            self.show_validation_error("Please Enter Valid Mother Number.")
            return

        if not re.match(r'^[a-zA-Z\s]{3,}$', mother_name):
            self.show_validation_error("Please Enter Valid Mother Name.")
            return
        if not re.match(r'^[a-zA-Z\s]{3,}$', mother_occupation):
            self.show_validation_error("Please Enter Valid Mother Occupation.")
            return
        if not re.match(r'^[a-zA-Z\s]{3,}$', mother_address):
            self.show_validation_error("Please Enter Valid Mother Address.")
            return
        try:
            dob = datetime.strptime(mother_dob, "%Y-%m-%d")


        except ValueError:
            self.show_validation_error("Please enter a valid date of birth in the format YYYY-MM-DD")
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET mother_name = ?, mother_address = ?, mother_occupation = ?, mother_ph_no = ? WHERE customer_id = ?",
                (mother_name, mother_address, mother_occupation, mother_ph_no, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['guarantor_name'] = mother_name
                data2[index2]['guarantor_address'] = mother_address
                data2[index2]['guarantor_mobile_no'] = int(mother_ph_no)
                data2[index2]['guarantor_profession'] = mother_occupation
                data2[index2]['guarantor_date_of_births'] = mother_dob
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = LenderScreenIndividualBankForm1(name='LenderScreenIndividualBankForm1')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreenIndividualBankForm1'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen7'


class LenderScreen10(Screen):
    def on_date_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_marriage_date.input_type = 'number'

    def on_spouse_mobile_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_mobile.input_type = 'number'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, spouse_name, spouse_marriage_date, spouse_mobile):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(spouse_name, spouse_marriage_date, spouse_mobile
                                                         , modal_view), 2)

    def perform_data_addition_action(self, spouse_name, spouse_marriage_date, spouse_mobile,
                                     modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if not all([spouse_name, spouse_marriage_date, spouse_mobile]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if not re.match(r'^[a-zA-Z\s]{3,}$', spouse_name):
            self.show_validation_error("Please Enter Valid Name.")
            return
        if not spouse_mobile.isdigit() or len(spouse_mobile) not in (10, 12):
            self.show_validation_error("Please Enter Valid Number.")
            return
        try:
            dob = datetime.strptime(spouse_marriage_date, "%Y-%m-%d").date()
            today = datetime.today().date()

            # Check if dob is less than today's date
            if dob > today:
                self.show_validation_error("Spouse's marriage date must be less than today's date.")
                return


        except ValueError:
            self.show_validation_error("Invalid date format. Please use YYYY-MM-DD")
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET spouse_name = ?,spouse_date_textfield = ?, spouse_mobile = ? WHERE customer_id = ?",
                (spouse_name, spouse_marriage_date, spouse_mobile, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['guarantor_name'] = spouse_name
                data2[index2]['guarantor_mobile_no'] = int(spouse_mobile)
                data2[index2]['guarantor_marriage_dates'] = str(spouse_marriage_date)
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = LenderScreen11(name='LenderScreen11')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreen11'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen7'


class LenderScreen11(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_spouse_profession.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['spouse_profession'])
        unique_list = []
        for i in data_list:
            if i not in unique_list:
                unique_list.append(i)
        print(unique_list)
        if len(unique_list) >= 1:
            self.ids.spouse_profession.values = ['Select Spouse Profession Type'] + unique_list
        else:
            self.ids.spouse_profession.values = ['Select Spouse Profession Type']

    def on_spouse_annual_salary_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_annual_salary.input_type = 'number'

    def on_spouse_office_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_office_no.input_type = 'number'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, spouse_company_name, spouse_profession, spouse_annual_salary):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(spouse_company_name, spouse_profession,
                                                                         spouse_annual_salary,
                                                                         modal_view), 2)

    def perform_data_addition_action(self, spouse_company_name, spouse_profession, spouse_annual_salary
                                     , modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if not all([spouse_profession]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if spouse_profession not in spouse_profession == 'Select Spouse Profession':
            self.show_validation_error('Select a valid Spouse Profession')
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET spouse_company_name = ?,spouse_company_address = ?, spouse_annual_salary = ? WHERE customer_id = ?",
                (spouse_company_name, spouse_profession, spouse_annual_salary,
                 row_id_list[log_index]))
            conn.commit()
        else:
            print('User is not logged in.')

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['guarantor_company_name'] = spouse_company_name
                data2[index2]['guarantor_annual_earning'] = spouse_annual_salary
                data2[index2]['guarantor_profession'] = spouse_profession
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = LenderScreenIndividualBankForm1(name='LenderScreenIndividualBankForm1')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreenIndividualBankForm1'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen10'


class LenderScreen12(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = None

    def on_yes_button_pressed1(self):
        self.ids.id1.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.ids.id2.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id3.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id3.text_color = (1, 1, 1, 1)
        self.ids.id4.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.type = "Father"

    def on_yes_button_pressed2(self):
        self.ids.id2.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id1.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.ids.id3.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id3.text_color = (1, 1, 1, 1)
        self.ids.id4.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.type = "Mother"

    def on_yes_button_pressed3(self):
        self.ids.id3.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id3.text_color = (1, 1, 1, 1)
        self.ids.id2.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id1.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.ids.id4.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.type = "Spouse"

    def on_yes_button_pressed4(self):
        self.ids.id4.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.ids.id2.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id3.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id3.text_color = (1, 1, 1, 1)
        self.ids.id1.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.type = "Other"

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(modal_view), 2)

    def perform_data_addition_action(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if self.type == None:
            # Display a validation error dialog
            self.show_validation_error("Please Select Valid Type.")
            return  # Prevent further execution if any field is missing

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['another_person'] = self.type
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        if self.type == 'Father':
            sm = self.manager
            borrower_screen = LenderScreen8(name='LenderScreen8')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen8'
        elif self.type == 'Mother':
            sm = self.manager
            borrower_screen = LenderScreen9(name='LenderScreen9')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen9'
        elif self.type == "Spouse":
            sm = self.manager
            borrower_screen = LenderScreen10(name='LenderScreen10')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen10'
        elif self.type == 'Other':
            sm = self.manager
            borrower_screen = LenderScreen14(name='LenderScreen14')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen14'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen7'


class LenderScreen13(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = None

    def on_yes_button_pressed1(self):
        self.ids.id1.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.ids.id2.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id4.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.type = "Father"

    def on_yes_button_pressed2(self):
        self.ids.id2.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id1.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.ids.id4.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.type = "Mother"

    def on_yes_button_pressed4(self):
        self.ids.id4.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.ids.id2.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id1.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.type = "Other"

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(modal_view), 2)

    def perform_data_addition_action(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if self.type == None:
            # Display a validation error dialog
            self.show_validation_error("Please Select Valid Type.")
            return  # Prevent further execution if any field is missing

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['another_person'] = self.type
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        if self.type == 'Father':
            sm = self.manager
            borrower_screen = LenderScreen8(name='LenderScreen8')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen8'
        elif self.type == 'Mother':
            sm = self.manager
            borrower_screen = LenderScreen9(name='LenderScreen9')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen9'
        elif self.type == 'Other':
            sm = self.manager
            borrower_screen = LenderScreen14(name='LenderScreen14')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen14'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen7'


class LenderScreen14(Screen):
    def on_date_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.person_dob.input_type = 'number'

    def on_mother_ph_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.person_ph_no.input_type = 'number'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, relation_name, person_name, person_dob, person_ph_no, person_proffession):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(relation_name, person_name, person_dob, person_ph_no,
                                                         person_proffession,
                                                         modal_view), 2)

    def perform_data_addition_action(self, relation_name, person_name, person_dob, person_ph_no, person_proffession,
                                     modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        # Check for missing fields
        if not all([relation_name, person_name, person_dob, person_ph_no, person_proffession]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing

        if not person_ph_no.isdigit() and len(person_ph_no) not in (10, 12):
            self.show_validation_error("Please Enter Valid Mother Number.")
            return
        if not re.match(r'^[a-zA-Z\s]{3,}$', relation_name):
            self.show_validation_error("Relation name should contain only letters and spaces.")
            return

        # Validate person_name
        if not re.match(r'^[a-zA-Z\s]{3,}$', person_name):
            self.show_validation_error("Person name should contain only letters.")
            return
        try:
            dob = datetime.strptime(person_dob, "%Y-%m-%d")
            today = datetime.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

            # Check if age is less than 18
            if age < 18:
                self.show_validation_error("You must be at least 18 years old to register.")
                return

        except ValueError:
            self.show_validation_error("Invalid date format. Please use YYYY-MM-DD")
            return
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')

        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['guarantor_name'] = person_name
                data2[index2]['guarantor_person_relation'] = relation_name
                data2[index2]['guarantor_mobile_no'] = int(person_ph_no)
                data2[index2]['guarantor_profession'] = person_proffession
                data2[index2]['guarantor_date_of_births'] = person_dob
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = LenderScreenIndividualBankForm1(name='LenderScreenIndividualBankForm1')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreenIndividualBankForm1'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen7'


class LenderScreenIndividualBankForm1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_lendor_account_type.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['lendor_account_type'])
        unique_list = []
        for i in data_list:
            if i not in unique_list:
                unique_list.append(i)
        print(unique_list)
        if len(unique_list) >= 1:
            self.ids.spinner_id.values = ['Select Account Type'] + unique_list
        else:
            self.ids.spinner_id.values = ['Select Account Type']

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, account_holder_name, account_type, account_number, bank_name):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action4(account_holder_name, account_type, account_number, bank_name,
                                                          modal_view), 2)

    def perform_data_addition_action4(self, account_holder_name, account_type, account_number, bank_name, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        # Check for missing fields
        if not all([account_holder_name, account_type, account_number, bank_name]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if not re.match(r'^[a-zA-Z]{3,}$', account_holder_name):
            self.show_validation_error('Enter a valid account name')
            return
        if account_type not in account_type == 'Select Account Type':
            self.show_validation_error('Enter a valid account type')
            return
        if len(account_number) < 3 or not account_number.isdigit():
            self.show_validation_error('Enter a valid account number')
            return
        if not re.match(r'^[a-zA-Z]{3,}$', bank_name):
            self.show_validation_error('Enter a valid bank name')
            return
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        email_list = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
            email_list.append(row[2])
        if 'logged' in status:
            log_index = status.index('logged')

            cursor.execute(
                "UPDATE fin_registration_table SET account_holder_name = ?, account_type = ?, account_number = ?, bank_name = ? WHERE customer_id = ?",
                (account_holder_name, account_type, account_number, bank_name, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")
        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['account_name'] = account_holder_name
            data[index]['account_type'] = account_type
            data[index]['account_number'] = account_number
            data[index]['bank_name'] = bank_name
        else:
            print('email not valid')

        # self.manager.current = 'LenderScreenInstitutionalBankForm2'
        sm = self.manager
        lender_screen = LenderScreenIndividualBankForm2(name='LenderScreenIndividualBankForm2')
        sm.add_widget(lender_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreenIndividualBankForm2'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen7'


class LenderScreenIndividualBankForm2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.check = None

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.check = True
        else:
            self.check = False

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def go_to_lender_dashboard(self, bank_id, branch_name):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action4(bank_id, branch_name, modal_view), 2)

    def perform_data_addition_action4(self, bank_id, branch_name, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        # Check for missing fields
        if not all([bank_id, branch_name]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if not re.match(r'^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{3,}$', bank_id):
            self.show_validation_error(
                "Bank ID should contain at least 3 characters, including both numbers and letters.")
            return
        if not branch_name.isalpha() or len(branch_name) < 3:
            self.show_validation_error('Enter a valid branch name')
            return
        if self.check != True:
            self.show_validation_error('Select The Terms and Conditions')
            return
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        email_list = []
        b = 'lender'
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
            email_list.append(row[2])
        if 'logged' in status:
            log_index = status.index('logged')

            cursor.execute(
                "UPDATE fin_registration_table SET bank_id = ?, branch_name = ?, user_type = ? WHERE customer_id = ?",
                (bank_id, branch_name, b, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['bank_id'] = bank_id
            data[index]['account_bank_branch'] = branch_name
            data[index]['usertype'] = b
            data[index]['registration_approve'] = True
            data[index]['last_confirm'] = True
        else:
            print('email not found')
        sm = self.manager
        lender_screen = LenderDashboard(name='LenderDashboard')
        sm.add_widget(lender_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderDashboard'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def show_terms_dialog(self):
        dialog = MDDialog(
            title="Terms and Conditions",
            text="Agreements, Privacy Policy and Applicant should accept following:Please note that any information concealed (as what we ask for), would be construed as illegitimate action on your part and an intentional attempt to hide material information which if found in future, would attract necessary action (s) at your sole cost. Hence, request to be truthful to your best knowledge while sharing your details)",
            size_hint=(0.8, 0.5),
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda *args: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreenIndividualBankForm1'
