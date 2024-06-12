from datetime import datetime, timezone

import anvil.server
from kivy.animation import Animation
from kivy.factory import Factory
from kivy.metrics import dp
from kivy.uix.filechooser import platform
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
import sqlite3
import anvil.server
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget
import anvil.users
from anvil.tables import app_tables
from kivy.uix.modalview import ModalView
from kivy.clock import Clock

if platform == 'android':
    from kivy.uix.button import Button

    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission)

import anvil.server

lender_view_extension = """
<WindowManager>:
    NewExtension:
    ApprovedLoansEX:
    RejectedLoansEX:
    UnderProcessLoansEX:
    ViewProfileE:
    ViewProfileEX:
    ViewProfileEXE:

<NewExtension>
    MDFloatLayout:
        md_bg_color:1,1,1,1
        size_hint: 1, 1 

        MDTopAppBar:
            title: "View Extension Request"
            title_align: 'left'
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            pos_hint: {'top': 1}
            md_bg_color: 0.043, 0.145, 0.278, 1


        MDGridLayout:
            cols: 2
            spacing: dp(15)
            size_hint_y: None
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            height: self.minimum_height
            width: self.minimum_width
            size_hint_x: None

            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.043, 0.145, 0.278, 1 

                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)
                on_release: root.go_to_approved_loans()
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "Approved Loans"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.043, 0.145, 0.278, 1 
                on_release: root.go_to_under_process_loans()
                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)

                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "UnderProcess Loans"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.043, 0.145, 0.278, 1
                on_release: root.go_to_rejected_loans()
                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)

                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "Rejected Loans"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDFlatButton:
                size_hint: None, None
                md_bg_color: 0.043, 0.145, 0.278, 1 

                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)
                on_release: root.all_loan_screen()
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "All Loans"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1

<ApprovedLoansEX>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Approved Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container11

<UnderProcessLoansEX>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Under Process Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container12
<RejectedLoansEX>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Rejected Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container13               

<ALLLoansEX>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "ALL Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container14               

<ViewProfileE>
    GridLayout:
        cols: 1
        MDTopAppBar:
            title: "Lender Extension"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1 
            title_align: 'left'

        ScrollView:
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height 

                BoxLayout:
                    orientation: 'vertical'
                    spacing: dp(50)
                    padding: dp(30)
                    size_hint_y: None
                    height: self.minimum_height
                    canvas.before:
                        Color:
                            rgba: 230/255, 245/255, 255/255, 1 
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [1, 1, 1, 1]
                            source: "background.jpg"
                    MDGridLayout:
                        cols: 2

                        MDLabel:
                            text: 'Loan Amount:'
                            halign: 'left'
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                    MDGridLayout:
                        cols: 2
                        MDIconButton:
                            icon: 'currency-inr'
                            halign: 'left'
                            size_hint_y: None
                            height: dp(1)
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1

                        MDLabel:
                            id: amount
                            halign: 'left'
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                            bold: True

                    MDLabel:
                        text: ''
                        halign: 'left'
                        size_hint_y: None
                        height: dp(5)

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Borrower Name"
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: name
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                    MDGridLayout: 
                        cols: 2    
                        MDLabel:
                            text: "Extension Fee(%)" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: extension
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True
                    MDGridLayout: 
                        cols: 2       
                        MDLabel:
                            text: "Extension Amount" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: extension_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True
                    MDGridLayout: 
                        cols: 2 
                        MDLabel:
                            text: "Remaining Amount" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: remaining_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True
                    MDGridLayout: 
                        cols: 2 
                        MDLabel:
                            text: "Reason For Extension" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: reason
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                    MDGridLayout: 
                        cols: 2 
                        MDLabel:
                            text: "New EMI" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: interest
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                MDGridLayout:
                    cols: 2
                    spacing: 10

                    CheckBox:
                        id: check
                        size_hint: (None, None)
                        width: 50
                        bold: True
                        on_active: root.checkbox_callback(self, self.active)
                        color: (195/255,110/255,108/255,1)

                    MDLabel:
                        text: "I Agree Terms and Conditions"
                        multiline: False

                MDLabel:
                    text: ''
                    halign: 'left'
                    size_hint_y: None
                    height: dp(65)
                MDBoxLayout:
                    orientation: 'horizontal'
                    spacing: dp(30)
                    padding: dp(30)
                    size_hint_y: None
                    height: self.minimum_height
                    canvas.before:
                        Color:
                            rgba: 249/255, 249/255, 247/255, 1 
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [25, 25, 25, 25]
                    MDRaisedButton:
                        text: "Decline"
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        on_release: root.reject_request()
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1, 1
                        size_hint: 1, 1

                    MDRaisedButton:
                        text: "Approve"
                        theme_text_color: 'Custom'
                        on_release: root.accept_request() 
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        size_hint: 1, 1


<ViewProfileEx>
    GridLayout:
        cols: 1
        MDTopAppBar:
            title: "Lender Extension"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1 
            title_align: 'left'

        ScrollView:
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height 

                BoxLayout:
                    orientation: 'vertical'
                    spacing: dp(50)
                    padding: dp(30)
                    size_hint_y: None
                    height: self.minimum_height
                    canvas.before:
                        Color:
                            rgba: 230/255, 245/255, 255/255, 1 
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [1, 1, 1, 1]
                            source: "background.jpg"

                    MDGridLayout:
                        cols: 2

                        MDLabel:
                            text: 'Loan Amount:'
                            halign: 'left'
                            bold: True
                    MDGridLayout:
                        cols: 2
                        MDIconButton:
                            icon: 'currency-inr'
                            halign: 'left'
                            size_hint_y: None
                            height: dp(1)
                            bold: True

                        MDLabel:
                            id: amount
                            halign: 'left'
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                            bold: True

                    MDLabel:
                        text: ''
                        halign: 'left'
                        size_hint_y: None
                        height: dp(5)
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Borrower Name" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: name
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold : True


                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Extension Fee(%)" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: extension
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold : True

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Extension Amount" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: extension_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold : True

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Remaining Amount" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: remaining_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold : True

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Reason For Extension" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: reason
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold : True

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "New EMI" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: interest
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold : True

                MDBoxLayout:
                    orientation: 'horizontal'
                    spacing: dp(30)
                    padding: dp(30)
                    size_hint_y: None
                    height: self.minimum_height
                    canvas.before:
                        Color:
                            rgba: 249/255, 249/255, 247/255, 1 
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [25, 25, 25, 25]
                    MDLabel:
                        text: "Your Extension Loan has been approved" 
                        bold: True 
                        halign: "center" 


<ViewProfileEXE>
    GridLayout:
        cols: 1
        MDTopAppBar:
            title: "Lender Extension"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1 
            title_align: 'left'

        ScrollView:
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height 

                BoxLayout:
                    orientation: 'vertical'
                    spacing: dp(50)
                    padding: dp(30)
                    size_hint_y: None
                    height: self.minimum_height
                    canvas.before:
                        Color:
                            rgba: 230/255, 245/255, 255/255, 1 
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [1, 1, 1, 1]
                            source: "background.jpg"

                    MDGridLayout:
                        cols: 2

                        MDLabel:
                            text: 'Loan Amount:'
                            halign: 'left'
                            bold: True
                    MDGridLayout:
                        cols: 2
                        MDIconButton:
                            icon: 'currency-inr'
                            halign: 'left'
                            size_hint_y: None
                            height: dp(1)
                            bold: True

                        MDLabel:
                            id: amount
                            halign: 'left'
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                            bold: True

                    MDLabel:
                        text: ''
                        halign: 'left'
                        size_hint_y: None
                        height: dp(5)
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Borrower Name" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: name
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold : True


                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Extension Fee(%)" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: extension
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold : True


                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Extension Amount" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: extension_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold : True


                    MDGridLayout:
                        cols: 2

                        MDLabel:
                            text: "Remaining Amount" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: remaining_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold : True


                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Reason For Extension" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: reason
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold : True

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "New EMI" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: interest
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold : True

                MDBoxLayout:
                    orientation: 'horizontal'
                    spacing: dp(30)
                    padding: dp(30)
                    size_hint_y: None
                    height: self.minimum_height
                    canvas.before:
                        Color:
                            rgba: 249/255, 249/255, 247/255, 1 
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [25, 25, 25, 25]
                    MDLabel:
                        text: "Your Extension Loan has been Rejected" 
                        bold: True 
                        halign: "center"                                 

"""
Builder.load_string(lender_view_extension)


class NewExtension(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = app_tables.fin_extends_loan.search()
        today_date = datetime.now(timezone.utc).date()
        loan = app_tables.fin_loan_details.search()
        loan_id = []
        request_time = []
        loan_status = []
        a = 0
        for i in data:
            a += 1
            loan_id.append(i['loan_id'])
            request_time.append(i['extension_request_date'])
            loan_status.append(i['status'])
        loan_id1 = []
        loan_status1 = []
        s = 0
        for i in loan:
            s += 1
            loan_id1.append(i['loan_id'])
            loan_status1.append(i['loan_updated_status'])

        for i in range(a):
            day_left = (today_date - request_time[i].date()).days
            if day_left >= 2 and loan_status[i] == "under process":
                data[i]["status"] = "approved"
                if loan_id[i] in loan_id1:
                    index = loan_id1.index(loan_id[i])
                    loan[i]["loan_updated_status"] = "extension"
            print(day_left)

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
        self.manager.current = 'LenderDashboard'

    def on_back_button_press(self):
        self.manager.current = 'LenderDashboard'

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

    def go_to_approved_loans(self):
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
        Clock.schedule_once(lambda dt: self.performance_go_to_approved_loans(modal_view), 2)

    def performance_go_to_approved_loans(self, modal_view):
        # Cancel the animation
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        self.manager.add_widget(Factory.ApprovedLoansEX(name='ApprovedLoansEX'))
        self.manager.current = 'ApprovedLoansEX'

    def go_to_under_process_loans(self):
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
        Clock.schedule_once(lambda dt: self.performance_go_to_under_process_loans(modal_view), 2)

    def performance_go_to_under_process_loans(self, modal_view):
        # Cancel the animation
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        self.manager.add_widget(Factory.UnderProcessLoansEX(name='UnderProcessLoansEX'))
        self.manager.current = 'UnderProcessLoansEX'

    def go_to_rejected_loans(self):
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
        Clock.schedule_once(lambda dt: self.performance_go_to_rejected_loans(modal_view), 2)

    def performance_go_to_rejected_loans(self, modal_view):
        # Cancel the animation
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        self.manager.add_widget(Factory.RejectedLoansEX(name='RejectedLoansEX'))
        self.manager.current = 'RejectedLoansEX'

    def all_loan_screen(self):
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
        Clock.schedule_once(lambda dt: self.performance_all_loan_screen(modal_view), 2)

    def performance_all_loan_screen(self, modal_view):
        # Cancel the animation
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        self.manager.add_widget(Factory.ALLLoansEX(name='ALLLoansEX'))
        self.manager.current = 'ALLLoansEX'


class ApprovedLoansEX(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        view = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        data = app_tables.fin_extends_loan.search()
        loan_id = []
        borrower_name = []
        loan_status = []
        cus_id = []
        s = 0
        for i in data:
            s += 1
            cus_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['status'])

        customer_id = []
        product_name = []
        for i in view:
            customer_id.append(i['borrower_customer_id'])
            product_name.append(i['product_name'])
        profile_customer_id = []
        profile_mobile_number = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[c] == 'approved':
                index_list.append(c)

        b = 1
        k = -1
        for i in reversed(index_list):
            b += 1
            k += 1
            if i < len(customer_id):
                print(customer_id[i])
                if customer_id[i] in profile_customer_id:
                    number = profile_customer_id.index(customer_id[i])
                else:
                    number = 0
                item = ThreeLineAvatarIconListItem(

                    IconLeftWidget(
                        icon="card-account-details-outline"
                    ),
                    text=f"Borrower Name : {borrower_name[i]}",
                    secondary_text=f"Borrower Mobile Number : {profile_mobile_number[number]}",
                    tertiary_text=f"Product Name : {product_name[i]}",
                    text_color=(0, 0, 0, 1),  # Black color
                    theme_text_color='Custom',
                    secondary_text_color=(0, 0, 0, 1),
                    secondary_theme_text_color='Custom',
                    tertiary_text_color=(0, 0, 0, 1),
                    tertiary_theme_text_color='Custom'
                )
                item.bind(
                    on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
                self.ids.container11.add_widget(item)

    def icon_button_clicked(self, instance, loan_id):
        value = instance.text.split(':')
        value = value[-1][1:]
        data = app_tables.fin_extends_loan.search()
        sm = self.manager
        # Create a new instance of the LoginScreen
        disbursed = ViewProfileEX(name='ViewProfileEX')
        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(disbursed)

        # Switch to the LoginScreen
        sm.current = 'ViewProfileEX'
        self.manager.get_screen('ViewProfileEX').initialize_with_value(loan_id, data)

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
        self.manager.current = 'NewExtension'

    def refresh(self):
        self.ids.container11.clear_widgets()
        self.__init__()


class ALLLoansEX(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        view = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        data = app_tables.fin_extends_loan.search()
        loan_id = []
        borrower_name = []
        loan_status = []
        cus_id = []
        s = 0
        for i in data:
            s += 1
            cus_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['status'])

        customer_id = []
        product_name = []
        for i in view:
            customer_id.append(i['borrower_customer_id'])
            product_name.append(i['product_name'])
        profile_customer_id = []
        profile_mobile_number = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
        c = -1
        index_list = []
        for i in range(s):
            c += 1
            index_list.append(c)

        b = 1
        k = -1
        for i in reversed(index_list):
            b += 1
            k += 1
            if i < len(customer_id):
                print(customer_id[i])
                if customer_id[i] in profile_customer_id:
                    number = profile_customer_id.index(customer_id[i])
                else:
                    number = 0
                item = ThreeLineAvatarIconListItem(

                    IconLeftWidget(
                        icon="card-account-details-outline"
                    ),
                    text=f"Borrower Name : {borrower_name[i]}",
                    secondary_text=f"Borrower Mobile Number : {profile_mobile_number[number]}",
                    tertiary_text=f"Product Name : {product_name[i]}",
                    text_color=(0, 0, 0, 1),  # Black color
                    theme_text_color='Custom',
                    secondary_text_color=(0, 0, 0, 1),
                    secondary_theme_text_color='Custom',
                    tertiary_text_color=(0, 0, 0, 1),
                    tertiary_theme_text_color='Custom'
                )
                item.bind(
                    on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
                self.ids.container14.add_widget(item)

    def icon_button_clicked(self, instance, loan_id):
        # Handle the on_release event here
        value = instance.text.split(':')
        value = value[-1][1:]
        data = app_tables.fin_extends_loan.search()
        loan_status = None
        for loan in data:
            if loan['loan_id'] == loan_id:
                loan_status = loan['status']
                break

        if loan_status == 'approved':
            # Open the screen for approved loans

            sm = self.manager

            # Create a new instance of the LoginScreen
            approved = ViewProfileEX(name='ViewProfileEX')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(approved)

            # Switch to the LoginScreen
            sm.current = 'ViewProfileEX'
            self.manager.get_screen('ViewProfileEX').initialize_with_value(loan_id, data)

        elif loan_status == 'under process':
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            under_process = ViewProfileE(name='ViewProfileE')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(under_process)

            # Switch to the LoginScreen
            sm.current = 'ViewProfileE'
            self.manager.get_screen('ViewProfileE').initialize_with_value(loan_id, data)

        elif loan_status == 'rejected':
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            rejected = ViewProfileEXE(name='ViewProfileEXE')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(rejected)

            # Switch to the LoginScreen
            sm.current = 'ViewProfileEXE'
            self.manager.get_screen('ViewProfileEXE').initialize_with_value(loan_id, data)
        else:
            # Handle other loan statuses or show an error message
            pass

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
        self.manager.current = 'NewExtension'

    def refresh(self):
        self.ids.container14.clear_widgets()
        self.__init__()

    def on_back_button_press(self):
        self.manager.current = 'NewExtension'


class RejectedLoansEX(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        view = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        data = app_tables.fin_extends_loan.search()
        loan_id = []
        borrower_name = []
        loan_status = []
        cus_id = []
        s = 0
        for i in data:
            s += 1
            cus_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['status'])

        customer_id = []
        product_name = []
        for i in view:
            customer_id.append(i['borrower_customer_id'])
            product_name.append(i['product_name'])
        profile_customer_id = []
        profile_mobile_number = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[c] == 'rejected':
                index_list.append(c)

        b = 1
        k = -1
        for i in reversed(index_list):
            b += 1
            k += 1
            if i < len(customer_id):
                print(customer_id[i])
                if customer_id[i] in profile_customer_id:
                    number = profile_customer_id.index(customer_id[i])
                else:
                    number = 0
                item = ThreeLineAvatarIconListItem(

                    IconLeftWidget(
                        icon="card-account-details-outline"
                    ),
                    text=f"Borrower Name : {borrower_name[i]}",
                    secondary_text=f"Borrower Mobile Number : {profile_mobile_number[number]}",
                    tertiary_text=f"Product Name : {product_name[i]}",
                    text_color=(0, 0, 0, 1),  # Black color
                    theme_text_color='Custom',
                    secondary_text_color=(0, 0, 0, 1),
                    secondary_theme_text_color='Custom',
                    tertiary_text_color=(0, 0, 0, 1),
                    tertiary_theme_text_color='Custom'
                )
                item.bind(
                    on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
                self.ids.container13.add_widget(item)

    def icon_button_clicked(self, instance, loan_id):
        value = instance.text.split(':')
        value = value[-1][1:]
        data = app_tables.fin_extends_loan.search()
        sm = self.manager

        # Create a new instance of the LoginScreen
        disbursed = ViewProfileEXE(name='ViewProfileEXE')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(disbursed)

        # Switch to the LoginScreen
        sm.current = 'ViewProfileEXE'
        self.manager.get_screen('ViewProfileEXE').initialize_with_value(loan_id, data)

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
        self.manager.current = 'NewExtension'

    def refresh(self):
        self.ids.container13.clear_widgets()
        self.__init__()


class UnderProcessLoansEX(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        view = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        data = app_tables.fin_extends_loan.search()
        loan_id = []
        borrower_name = []
        loan_status = []
        cus_id = []
        s = 0
        for i in data:
            s += 1
            cus_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['status'])

        customer_id = []
        product_name = []
        for i in view:
            customer_id.append(i['borrower_customer_id'])
            product_name.append(i['product_name'])
        profile_customer_id = []
        profile_mobile_number = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[c] == 'under process':
                index_list.append(c)

        b = 1
        k = -1
        for i in reversed(index_list):
            b += 1
            k += 1
            if i < len(customer_id):
                print(customer_id[i])
                if customer_id[i] in profile_customer_id:
                    number = profile_customer_id.index(customer_id[i])
                else:
                    number = 0
                item = ThreeLineAvatarIconListItem(

                    IconLeftWidget(
                        icon="card-account-details-outline"
                    ),
                    text=f"Borrower Name : {borrower_name[i]}",
                    secondary_text=f"Borrower Mobile Number : {profile_mobile_number[number]}",
                    tertiary_text=f"Product Name : {product_name[i]}",
                    text_color=(0, 0, 0, 1),  # Black color
                    theme_text_color='Custom',
                    secondary_text_color=(0, 0, 0, 1),
                    secondary_theme_text_color='Custom',
                    tertiary_text_color=(0, 0, 0, 1),
                    tertiary_theme_text_color='Custom'
                )
                item.bind(
                    on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
                self.ids.container12.add_widget(item)

    def icon_button_clicked(self, instance, loan_id):
        value = instance.text.split(':')
        value = value[-1][1:]
        data = app_tables.fin_extends_loan.search()
        sm = self.manager

        # Create a new instance of the LoginScreen
        disbursed = ViewProfileE(name='ViewProfileE')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(disbursed)

        # Switch to the LoginScreen
        sm.current = 'ViewProfileE'
        self.manager.get_screen('ViewProfileE').initialize_with_value(loan_id, data)

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
        self.manager.current = 'NewExtension'

    def refresh(self):
        self.ids.container12.clear_widgets()
        self.__init__()


class ViewProfileEX(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialize_with_value(self, value, data):
        data = app_tables.fin_extends_loan.search()
        borrower_name = []
        loan_id = []
        loan_amount = []
        extension_fee = []
        extension_amount1 = []
        reason_for_extension = []
        remaining_amount = []
        new_emi = []

        for i in data:
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_amount.append(i['loan_amount'])
            extension_fee.append(i['extend_fee'])
            extension_amount1.append(i['extension_amount'])
            reason_for_extension.append(i['reason'])
            remaining_amount.append(i['final_repayment_amount'])
            new_emi.append(i['new_emi'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.name.text = str(borrower_name[index])
            self.ids.amount.text = str(loan_amount[index])
            self.ids.extension.text = str(extension_fee[index])
            self.ids.extension_amount.text = str(extension_amount1[index])
            self.ids.reason.text = str(reason_for_extension[index])
            self.ids.remaining_amount.text = str(remaining_amount[index])
            self.ids.interest.text = str(new_emi[index])

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def on_back_button_press(self):
        self.manager.current = 'NewExtension'

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True


class ViewProfileEXE(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialize_with_value(self, value, data):
        data = app_tables.fin_extends_loan.search()
        borrower_name = []
        loan_id = []
        loan_amount = []
        extension_fee = []
        extension_amount = []
        reason_for_extension = []
        remaining_amount = []
        new_emi = []

        for i in data:
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_amount.append(i['loan_amount'])
            extension_fee.append(i['extend_fee'])
            extension_amount.append(i['extension_amount'])
            reason_for_extension.append(i['reason'])
            remaining_amount.append(i['final_repayment_amount'])
            new_emi.append(i['new_emi'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.name.text = str(borrower_name[index])
            self.ids.amount.text = str(loan_amount[index])
            self.ids.extension.text = str(extension_fee[index])
            self.ids.extension_amount.text = str(extension_amount[index])
            self.ids.reason.text = str(reason_for_extension[index])
            self.ids.remaining_amount.text = str(remaining_amount[index])
            self.ids.interest.text = str(new_emi[index])

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_back_button_press(self):
        self.manager.current = 'NewExtension'


class ViewProfileE(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.check = None

    def checkbox_callback(self, checkbox, value):
        if value:
            self.check = True
        else:
            self.check = False

    def initialize_with_value(self, value, data):
        self.loan_id = value
        data = app_tables.fin_extends_loan.search()
        borrower_name = []
        loan_id = []
        loan_amount = []
        extension_fee = []
        extension_amount = []
        reason_for_extension = []
        remaining_amount = []
        new_emi = []

        for i in data:
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_amount.append(i['loan_amount'])
            extension_fee.append(i['extend_fee'])
            extension_amount.append(i['extension_amount'])
            reason_for_extension.append(i['reason'])
            remaining_amount.append(i['final_repayment_amount'])
            new_emi.append(i['new_emi'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.name.text = str(borrower_name[index])
            self.ids.amount.text = str(loan_amount[index])
            self.ids.extension.text = str(extension_fee[index])
            self.ids.extension_amount.text = str(extension_amount[index])
            self.ids.reason.text = str(reason_for_extension[index])
            self.ids.remaining_amount.text = str(remaining_amount[index])
            self.ids.interest.text = str(new_emi[index])

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"

    def on_back_button_press(self):
        self.manager.current = 'NewExtension'

    def accept_request(self):
        if self.check != True:
            self.show_validation_error('You need to select Terms and Conditions')
            return
        loan_id = self.loan_id
        approved_date = datetime.now()
        extends_loan_records = app_tables.fin_extends_loan.search(loan_id=loan_id)
        loan_details_records = app_tables.fin_loan_details.search(loan_id=loan_id)
        loan_records = app_tables.fin_loan_details.search(loan_id=loan_id)
        profile = app_tables.fin_user_profile.search()
        email_user = self.email_user()
        data = app_tables.fin_loan_details.search()
        lender_cos_id = []
        lender_email = []
        lender_name = []
        product_name = []
        for i in data:
            lender_cos_id.append(i['lender_customer_id'])
            lender_email.append(i['lender_email_id'])
            lender_name.append(i['lender_full_name'])
            product_name.append(i['product_name'])
        index1 = 0
        if loan_id in data:
            index1 = loan_id.index(loan_id)
        loan_idlist = [i['loan_id'] for i in data]
        profile_customer_id = []
        profile_email = []
        profile_name = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_email.append(i['email_user'])
            profile_name.append(i['full_name'])
        email_index = 0
        if email_user in profile_email:
            email_index = profile_email.index(email_user)
        else:
            print("no email found")
        if loan_id in loan_idlist:
            for i in data:
                if i['loan_id'] == loan_id:
                    borrower_name = i['borrower_full_name']
                    break
            extends_loan_records[index1]['status_timestamp'] = approved_date
            extends_loan_records[index1]['lender_customer_id'] = lender_cos_id[email_index]
            extends_loan_records[index1]['lender_full_name'] = lender_name[email_index]
            extends_loan_records[index1]['lender_email_id'] = lender_email[email_index]
            extends_loan_records[index1]['product_name'] = product_name[email_index]

        if extends_loan_records and loan_details_records:
            for extends_loan_record in extends_loan_records:
                extends_loan_record['status'] = 'approved'
                extends_loan_record.update()

            for record in loan_records:
                record['loan_updated_status'] = 'extension'
                record.update()

            # Switch to the 'NewExtension' screen
            self.manager.current = 'NewExtension'
        else:
            print("No data found for loan_id:", loan_id)

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

    def reject_request(self):
        if self.check != True:
            self.show_validation_error('You need to select Terms and Conditions')
            return
        data = app_tables.fin_extends_loan.search()
        loan_id = self.loan_id
        print(loan_id)
        loan_idlist = []
        for i in data:
            loan_idlist.append(i['loan_id'])
        print(loan_idlist)
        if self.check != True:
            self.show_validation_error('You need to select Terms and Conditions')
            return
        loan_id = self.loan_id
        extends_loan_records = app_tables.fin_extends_loan.search(loan_id=loan_id)
        approved_date = datetime.now()
        profile = app_tables.fin_user_profile.search()
        email_user = self.email_user()
        data1 = app_tables.fin_loan_details.search()
        lender_cos_id = []
        lender_email = []
        lender_name = []
        product_name = []
        for i in data1:
            lender_cos_id.append(i['lender_customer_id'])
            lender_email.append(i['lender_email_id'])
            lender_name.append(i['lender_full_name'])
            product_name.append(i['product_name'])
        index1 = 0
        if loan_id in data1:
            index1 = loan_id.index(loan_id)

        loan_idlist = [i['loan_id'] for i in data]
        profile_customer_id = []
        profile_email = []
        profile_name = []

        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_email.append(i['email_user'])
            profile_name.append(i['full_name'])
        email_index = 0
        if email_user in profile_email:
            email_index = profile_email.index(email_user)
        else:
            print("no email found")
        if loan_id in loan_idlist:
            index = loan_idlist.index(loan_id)
            data[index]['status'] = 'rejected'
            extends_loan_records[index1]['status_timestamp'] = approved_date
            extends_loan_records[index1]['lender_customer_id'] = lender_cos_id[email_index]
            extends_loan_records[index1]['lender_full_name'] = lender_name[email_index]
            extends_loan_records[index1]['lender_email_id'] = lender_email[email_index]
            extends_loan_records[index1]['product_name'] = product_name[email_index]
            self.manager.current = 'NewExtension'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def email_user(self):
        return anvil.server.call('another_method')

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.on_back_button_press()
            return True
        return False

    def on_back_button_press(self):
        self.manager.current = 'NewExtension'


class MyScreenManager(ScreenManager):
    pass
