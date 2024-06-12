from datetime import datetime, timezone

import anvil
from anvil.tables import app_tables
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.filechooser import platform
from kivy.uix.screenmanager import Screen, ScreenManager
import anvil.server
from kivy.lang import Builder
import anvil.server
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission)

lender_foreclouser = '''

<WindowManager>:
    DashboardScreenLF:
    ApprovedLoansLF:
    ViewAllLoansLF:
    RejectedLoansLF:
    UnderProcessLoansLF:
    ClosedLoansLF:
    ViewProfileScreenLF:
    ViewProfileScreenLFL:
    ViewProfileScreenFLF:

<DashboardScreenLF>:
    MDFloatLayout:
        md_bg_color:1,1,1,1
        size_hint: 1, 1 

        MDTopAppBar:
            title: "Foreclose Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'left'
            pos_hint: {'top': 1}
            md_bg_color: 0.043, 0.145, 0.278, 1
            MDList:
                id: container

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
                on_release: root.go_to_open_loans()
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
                on_release: root.go_to_under_loans()
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
                on_release: root.go_to_reject_loans()
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

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.043, 0.145, 0.278, 1

                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)
                on_release: root.go_to_app_tracker()
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "Closed Loans"
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
                on_release: root.all_loanscreen()
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

<ApprovedLoansLF>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Approved Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back_screen()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container1

<UnderProcessLoansLF>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "UnderProcess Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back_screen()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container2
<ClosedLoansLF>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Closed Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back_screen()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container3
<RejectedLoansLF>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Rejected Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back_screen()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container4
<ViewAllLoansLF>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "All Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back_screen()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container5


<ViewProfileScreenLF>:
    GridLayout:
        cols: 1
        MDTopAppBar:
            title: "Lender Foreclose"
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
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                            bold: True
                    MDGridLayout:
                        cols: 2
                        MDIconButton:
                            icon: 'currency-inr'
                            halign: 'left'
                            size_hint_y: None
                            height: dp(1)
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0,0,0,1

                        MDLabel:
                            id: amount
                            halign: 'left'
                            theme_text_color: 'Custom'  
                            text_color: 0,0,0,1
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
                            bold: True

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Interest Rate" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: rate
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Foreclosure Fee" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: fee
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Foreclosure Amount" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: famount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Total Paid Amount" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: total_paid
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True


                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Outstanding Amount" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: samount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Reason For Foreclosure"
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: reason
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1 
                            bold: True          


                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Total Due Amount"
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: due_amount
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
                        on_release: root.rejected_click()
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1, 1
                        size_hint: 1, 1

                    MDRaisedButton:
                        text: "Approve"
                        theme_text_color: 'Custom'
                        on_release: root.approved_click() 
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        size_hint: 1, 1

<ViewProfileScreenFLF>:
    GridLayout:
        cols: 1
        MDTopAppBar:
            title: "Lender Foreclose"
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
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                            bold: True
                    MDGridLayout:
                        cols: 2
                        MDIconButton:
                            icon: 'currency-inr'
                            halign: 'left'
                            size_hint_y: None
                            height: dp(1)
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0,0,0,1

                        MDLabel:
                            id: amount
                            halign: 'left'
                            theme_text_color: 'Custom'  
                            text_color: 0,0,0,1
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
                            bold: True

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Interest Rate"
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: rate
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Foreclosure Fee"
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: fee
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Foreclosure Amount"
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: famount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Total Paid Amount"
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: total_paid
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True


                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Outstanding Amount" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: samount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Reason For Foreclosure" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: reason
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1   
                            bold: True       


                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Total Due Amount" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: due_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

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
                        text: "Your Requested Loan has been Approved" 
                        halign: "center"
                        bold: True

<ViewProfileScreenLFL>:
    GridLayout:
        cols: 1
        MDTopAppBar:
            title: "Lender Foreclose"
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
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                            bold: True
                    MDGridLayout:
                        cols: 2
                        MDIconButton:
                            icon: 'currency-inr'
                            halign: 'left'
                            size_hint_y: None
                            height: dp(1)
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0,0,0,1

                        MDLabel:
                            id: amount
                            halign: 'left'
                            theme_text_color: 'Custom'  
                            text_color: 0,0,0,1
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
                            bold: True


                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Interest Rate:" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: rate
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True 

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Foreclosure Fee"
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: fee
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True 

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Foreclosure Amount" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: famount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True 

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Total Paid Amount" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: total_paid
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True 

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Outstanding Amount" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: samount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True 

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Reason For Foreclosure" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: reason
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1     
                            bold: True      


                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Total Due Amount" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: due_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 0,0,0,1
                            bold: True 

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
                        text: "Your Requested Loan has been Rejected"
                        halign: "center"
                        bold: True  
                        theme_text_color: 'Custom'  
                        text_color: 0,0,0,1                             

'''

Builder.load_string(lender_foreclouser)


class DashboardScreenLF(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = app_tables.fin_foreclosure.search()
        loan = app_tables.fin_loan_details.search()
        today_date = datetime.now(timezone.utc).date()
        loan_id = []
        request_time = []
        loan_status = []
        a = 0
        for i in data:
            a += 1  # how much data was available in data it will print all data
            loan_id.append(i['loan_id'])
            request_time.append(i['requested_on'])
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
                    loan[i]["loan_updated_status"] = "foreclosure"
            print(day_left)

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.on_back_button_press()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def on_back_button_press(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderDashboard'

    def go_to_open_loans(self):
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = ApprovedLoansLF(name='ApprovedLoansLF')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'ApprovedLoansLF'

    def go_to_under_loans(self):
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = UnderProcessLoansLF(name='UnderProcessLoansLF')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'UnderProcessLoansLF'

    def go_to_app_tracker(self):
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = ClosedLoansLF(name='ClosedLoansLF')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'ClosedLoansLF'

    def go_to_reject_loans(self):
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = RejectedLoansLF(name='RejectedLoansLF')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'RejectedLoansLF'

    def all_loanscreen(self):
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = ViewAllLoansLF(name='ViewAllLoansLF')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'ViewAllLoansLF'

    def refresh(self):
        self.ids.container.clear_widgets()
        self.__init__()


class ApprovedLoansLF(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        view = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        data = app_tables.fin_foreclosure.search()

        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_name'])
            loan_status.append(i['status'])

        c = -1
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
        print(profile_customer_id)
        for i in reversed(index_list):
            b += 1
            k += 1
            print(i)
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
                self.ids.container1.add_widget(item)
            else:
                print("Index out of range!")

    def icon_button_clicked(self, instance, loan_id):
        # Handle the on_release event here
        value = instance.text.split(':')
        value = value[-1][1:]
        data = app_tables.fin_foreclosure.search()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = ViewProfileScreenFLF(name='ViewProfileScreenFLF')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ViewProfileScreenFLF'
        self.manager.get_screen('ViewProfileScreenFLF').initialize_with_value(loan_id, data)

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back_screen()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back_screen(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreenLF'

    def refresh(self):
        self.ids.container1.clear_widgets()
        self.__init__()

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreenLF'


class ClosedLoansLF(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        view = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        data = app_tables.fin_foreclosure.search()

        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_name'])
            loan_status.append(i['status'])

        c = -1
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
            if loan_status[c] == 'closed':
                index_list.append(c)
        b = 1
        k = -1
        print(profile_customer_id)
        for i in reversed(index_list):
            b += 1
            k += 1
            print(i)
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
                self.ids.container3.add_widget(item)
            else:
                print("Index out of range!")

    def icon_button_clicked(self, instance, loan_id):
        value = instance.text.split(':')
        value = value[-1][1:]
        data = app_tables.fin_foreclosure.search()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = ViewProfileScreenLF(name='ViewProfileScreenLF')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ViewProfileScreenLF'
        self.manager.get_screen('ViewProfileScreenLF').initialize_with_value(loan_id, data)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back_screen()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back_screen(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreenLF'

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def refresh(self):
        self.ids.container3.clear_widgets()
        self.__init__()


class RejectedLoansLF(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        view = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        data = app_tables.fin_foreclosure.search()

        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_name'])
            loan_status.append(i['status'])

        c = -1
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
        print(profile_customer_id)
        for i in reversed(index_list):
            b += 1
            k += 1
            print(i)
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
                self.ids.container4.add_widget(item)
            else:
                print("Index out of range!")

    def icon_button_clicked(self, instance, loan_id):
        # Handle the on_release event here
        value = instance.text.split(':')
        value = value[-1][1:]
        data = app_tables.fin_foreclosure.search()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = ViewProfileScreenLFL(name='ViewProfileScreenLFL')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ViewProfileScreenLFL'
        self.manager.get_screen('ViewProfileScreenLFL').initialize_with_value(loan_id, data)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back_screen()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def refresh(self):
        self.ids.container4.clear_widgets()
        self.__init__()

    def go_back_screen(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreenLF'

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreenLF'


class UnderProcessLoansLF(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        view = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        data = app_tables.fin_foreclosure.search()

        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_name'])
            loan_status.append(i['status'])

        c = -1
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
        print(profile_customer_id)
        for i in reversed(index_list):
            b += 1
            k += 1
            print(i)
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
                self.ids.container2.add_widget(item)
            else:
                print("Index out of range!")

    def icon_button_clicked(self, instance, loan_id):
        # Handle the on_release event here
        value = instance.text.split(':')
        value = value[-1][1:]
        data = app_tables.fin_foreclosure.search()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = ViewProfileScreenLF(name='ViewProfileScreenLF')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ViewProfileScreenLF'
        self.manager.get_screen('ViewProfileScreenLF').initialize_with_value(loan_id, data)

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back_screen()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def refresh(self):
        self.ids.container2.clear_widgets()
        self.__init__()

    def go_back_screen(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreenLF'

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreenLF'


class ViewAllLoansLF(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        view = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        data = app_tables.fin_foreclosure.search()

        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_name'])
            loan_status.append(i['status'])
        print(loan_id)
        c = -1
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
            index_list.append(c)
        b = 1
        k = -1
        print(profile_customer_id)
        for i in reversed(index_list):
            b += 1
            k += 1
            print(i)
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
                self.ids.container5.add_widget(item)
            else:
                print("Index out of range!")

    def icon_button_clicked(self, instance, loan_id):
        # Handle the on_release event here
        value = instance.text.split(':')
        value = value[-1][1:]
        data = app_tables.fin_foreclosure.search()
        loan_status = None
        for loan in data:
            if loan['loan_id'] == loan_id:
                loan_status = loan['status']
                break

        if loan_status == 'approved':
            # Open the screen for approved loans

            sm = self.manager

            # Create a new instance of the LoginScreen
            approved = ViewProfileScreenFLF(name='ViewProfileScreenFLF')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(approved)

            # Switch to the LoginScreen
            sm.current = 'ViewProfileScreenFLF'
            self.manager.get_screen('ViewProfileScreenFLF').initialize_with_value(loan_id, data)

        elif loan_status == 'under process':
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            under_process = ViewProfileScreenLF(name='ViewProfileScreenLF')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(under_process)

            # Switch to the LoginScreen
            sm.current = 'ViewProfileScreenLF'
            self.manager.get_screen('ViewProfileScreenLF').initialize_with_value(loan_id, data)

        elif loan_status == 'rejected':
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            rejected = ViewProfileScreenLFL(name='ViewProfileScreenLFL')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(rejected)

            # Switch to the LoginScreen
            sm.current = 'ViewProfileScreenLFL'
            self.manager.get_screen('ViewProfileScreenLF').initialize_with_value(loan_id, data)
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
            self.go_back_screen()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back_screen(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreenLF'

    def refresh(self):
        self.ids.container5.clear_widgets()
        self.__init__()


class ViewProfileScreenLFL(Screen):
    def initialize_with_value(self, value, data):
        data = app_tables.fin_foreclosure.search()
        loan_id = []
        borrower_name = []
        loan_amount = []
        interest = []
        forecloser_fee = []
        forecloser_amount = []
        total_amount = []
        outstanding_amount = []
        reason_foreclose = []
        total_due_amount = []

        for i in data:
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_name'])
            loan_amount.append(i['loan_amount'])
            forecloser_fee.append(i['foreclose_fee'])
            forecloser_amount.append(i['foreclose_amount'])
            interest.append(i['interest_rate'])
            total_amount.append(i['paid_amount'])
            outstanding_amount.append(i['outstanding_amount'])
            reason_foreclose.append(i['reason'])
            total_due_amount.append(i['total_due_amount'])
        if value in loan_id:
            index1 = loan_id.index(value)
            self.ids.amount.text = str(loan_amount[index1])
            self.ids.name.text = str(borrower_name[index1])
            self.ids.fee.text = str(forecloser_fee[index1])
            self.ids.famount.text = str(forecloser_amount[index1])
            self.ids.rate.text = str(interest[index1])
            self.ids.total_paid.text = str(total_amount[index1])
            self.ids.samount.text = str(outstanding_amount[index1])
            self.ids.reason.text = str(reason_foreclose[index1])
            self.ids.due_amount.text = str(total_due_amount[index1])

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.on_back_button_press()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreenLF'


class ViewProfileScreenFLF(Screen):
    def initialize_with_value(self, value, data):
        data = app_tables.fin_foreclosure.search()
        loan_id = []
        borrower_name = []
        loan_amount = []
        interest = []
        forecloser_fee = []
        forecloser_amount = []
        total_amount = []
        outstanding_amount = []
        reason_foreclose = []
        total_due_amount = []

        for i in data:
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_name'])
            loan_amount.append(i['loan_amount'])
            forecloser_fee.append(i['foreclose_fee'])
            forecloser_amount.append(i['foreclose_amount'])
            interest.append(i['interest_rate'])
            total_amount.append(i['paid_amount'])
            outstanding_amount.append(i['outstanding_amount'])
            reason_foreclose.append(i['reason'])
            total_due_amount.append(i['total_due_amount'])
        if value in loan_id:
            index2 = loan_id.index(value)
            self.ids.amount.text = str(loan_amount[index2])
            self.ids.name.text = str(borrower_name[index2])
            self.ids.fee.text = str(forecloser_fee[index2])
            self.ids.famount.text = str(forecloser_amount[index2])
            self.ids.rate.text = str(interest[index2])
            self.ids.total_paid.text = str(total_amount[index2])
            self.ids.samount.text = str(outstanding_amount[index2])
            self.ids.reason.text = str(reason_foreclose[index2])
            self.ids.due_amount.text = str(total_due_amount[index2])

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.on_back_button_press()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreenLF'


class ViewProfileScreenLF(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.check = None

    def checkbox_callback(self, checkbox, value):
        if value:
            self.check = True
        else:
            self.check = False

    def initialize_with_value(self, value, data):
        data = app_tables.fin_foreclosure.search()
        today_date = datetime.now(timezone.utc).date()
        index = 0
        self.loan_id = value
        loan_id = []
        borrower_name = []
        loan_amount = []
        interest = []
        forecloser_fee = []
        forecloser_amount = []
        total_amount = []
        request_time = []
        loan_status = []
        outstanding_amount = []
        reason_foreclose = []
        total_due_amount = []

        for i in data:
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_name'])
            request_time.append(i['requested_on'])
            loan_amount.append(i['loan_amount'])
            forecloser_fee.append(i['foreclose_fee'])
            forecloser_amount.append(i['foreclose_amount'])
            interest.append(i['interest_rate'])
            loan_status.append(i['status'])
            total_amount.append(i['paid_amount'])
            outstanding_amount.append(i['outstanding_amount'])
            reason_foreclose.append(i['reason'])
            total_due_amount.append(i['total_due_amount'])

        print(value)
        if value in loan_id:
            index = loan_id.index(value)
            self.ids.amount.text = str(loan_amount[index])
            self.ids.name.text = str(borrower_name[index])
            self.ids.fee.text = str(forecloser_fee[index])
            self.ids.famount.text = str(forecloser_amount[index])
            self.ids.rate.text = str(interest[index])
            self.ids.total_paid.text = str(total_amount[index])
            self.ids.samount.text = str(outstanding_amount[index])
            self.ids.reason.text = str(reason_foreclose[index])
            self.ids.due_amount.text = str(total_due_amount[index])

    def approved_click(self):
        if self.check != True:
            self.show_validation_error('You need to select Terms and Conditions')
            return
        loan_id = self.loan_id
        approved_date = datetime.now()
        foreclosure_records = app_tables.fin_foreclosure.search(loan_id=loan_id)
        loan_records = app_tables.fin_loan_details.search(loan_id=loan_id)
        profile = app_tables.fin_user_profile.search()
        email_user = self.email_user()
        data = app_tables.fin_loan_details.search()
        lender_loan_id = []
        lender_cos_id = []
        lender_email = []
        lender_name = []
        product_name = []
        for i in data:
            lender_loan_id.append(i['loan_id'])
            lender_cos_id.append(i['lender_customer_id'])
            lender_email.append(i['lender_email_id'])
            lender_name.append(i['lender_full_name'])
            product_name.append(i['product_name'])
        index1 = 0
        if loan_id in lender_loan_id:
            index1 = lender_loan_id.index(loan_id)
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
            foreclosure_records[index1]['status_timestamp'] = approved_date
            foreclosure_records[index1]['lender_customer_id'] = lender_cos_id[email_index]
            foreclosure_records[index1]['lender_full_name'] = lender_name[email_index]
            foreclosure_records[index1]['lender_email_id'] = lender_email[email_index]
            foreclosure_records[index1]['product_name'] = product_name[email_index]

        if foreclosure_records and loan_records:
            for record in foreclosure_records:
                record['status'] = 'approved'
                record.update()
            for record in loan_records:
                record['loan_updated_status'] = 'foreclosure'
                record.update()

            self.manager.current = 'DashboardScreenLF'
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

    def rejected_click(self):
        if self.check != True:
            self.show_validation_error('You need to select Terms and Conditions')
            return
        loan_id = self.loan_id
        foreclosure_records = app_tables.fin_foreclosure.search(loan_id=loan_id)
        approved_date = datetime.now()
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
            index = loan_idlist.index(loan_id)
            foreclosure_records[index1]['status'] = 'rejected'
            foreclosure_records[index1]['status_timestamp'] = approved_date
            foreclosure_records[index1]['lender_customer_id'] = lender_cos_id[email_index]
            foreclosure_records[index1]['lender_full_name'] = lender_name[email_index]
            foreclosure_records[index1]['lender_email_id'] = lender_email[email_index]
            foreclosure_records[index1]['product_name'] = product_name[email_index]
            self.manager.current = 'DashboardScreenLF'

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
        self.manager.current = 'DashboardScreenLF'


class MyScreenManager(ScreenManager):
    pass