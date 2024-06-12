from anvil.tables import app_tables
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.factory import Factory
from kivy.metrics import dp
from kivy.uix.modalview import ModalView
from kivymd.uix.label import MDLabel
from kivymd.uix.list import *
import anvil.server
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
import sqlite3
import anvil.server
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.app import MDApp
from datetime import datetime, timedelta, timezone
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDRaisedButton

from borrower_wallet import WalletScreen
from lender_view_loans import ViewLoansScreen
from lender_wallet import LenderWalletScreen

view_loans = """
<WindowManager>:
    ViewUnderProcess:
    ViewUnderScreen:
    ViewUnderScreenLR:
    ViewUnderScreenRL:

<ViewUnderProcess>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View UnderProcess Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            title_align: 'left'
        MDScrollView:

            MDList:
                id: container

<ViewUnderScreen>

    MDGridLayout:
        cols: 1
        MDTopAppBar:
            title: "Lender View Loan"
            elevation: 2
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            pos_hint: {'top': 1}

        BoxLayout:
            orientation: 'vertical'
            spacing: dp(40)
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
                    text: 'Amount:'
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

                MDLabel:
                    id: amount
                    bold: True
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1

            MDLabel:
                text: ''
                halign: 'left'
                size_hint_y: None
                height: dp(20)
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Product Name'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: pro_name
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Borrower Name'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: b_name
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Phone Number'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: phone_num
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    
                    
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Ascend Score'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: ascend
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    


            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Interest(%)'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: int_rate
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Duration(M)'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: tenure
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Credit Limit'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: limit
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    


            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Published Date'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: date
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Loan Status'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: status
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(30)
            padding: dp(15)
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
                text: ''
                halign: 'left'
                size_hint_y: None
                height: dp(5)
            MDGridLayout:
                cols: 3

                MDLabel:
                    text: 'Total'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1  
                    font_size: dp(25) 
                    bold: True
                MDIconButton:
                    icon: 'currency-inr'
                    halign: 'center' 
                    bold: True   

                MDLabel:
                    id: amount_1
                    bold: True
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1

        MDBoxLayout:
            orientation: 'horizontal'
            spacing: dp(30)
            padding: dp(20)
            size_hint: 1, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}    
            MDRaisedButton:
                text: "Reject"
                md_bg_color: 194/255, 2/255, 21/255, 1
                theme_text_color: 'Primary'
                on_release: root.rejected_click()
                text_color: 0, 0, 0, 1
                font_name: "Roboto-Bold.ttf"
                size_hint: 1, None

            MDRaisedButton:
                text: "Accept"
                md_bg_color: 5/255, 235/255, 77/255, 1
                on_release: root.approved_click()
                theme_text_color: 'Primary'
                font_name: "Roboto-Bold.ttf"
                text_color: 0, 0, 0, 1
                size_hint: 1, None



<ViewUnderScreenLR>
    MDGridLayout:
        cols: 1
        MDTopAppBar:
            title: "Approved Loan details"
            elevation: 2
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            pos_hint: {'top': 1}

        BoxLayout:
            orientation: 'vertical'
            spacing: dp(40)
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
                    text: 'Amount:'
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

                MDLabel:
                    id: amount
                    bold:True
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1

            MDLabel:
                text: ''
                halign: 'left'
                size_hint_y: None
                height: dp(20)
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Product Name'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: pro_name
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Borrower Name'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: b_name
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Phone Number'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: phone_num
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Ascend Score'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: ascend
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Interest(%)'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: int_rate
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Duration(M)'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: tenure
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Credit Limit'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: limit
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    


            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Published Date'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: date
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Loan Status'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: status
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    
            MDLabel:
                text: ''
                halign: 'left'
                size_hint_y: None
                height: dp(5)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(15)
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
                text: ''
                halign: 'left'
                size_hint_y: None
                height: dp(5)
            MDGridLayout:
                cols: 3

                MDLabel:
                    text: 'Total'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1  
                    font_size: dp(25) 
                    bold: True
                MDIconButton:
                    icon: 'currency-inr'
                    halign: 'center' 
                    bold: True   

                MDLabel:
                    id: amount_1
                    bold:True
                    halign: 'left'
        BoxLayout:
            orientation: 'horizontal'
            spacing: dp(30)
            padding: dp(20)
            size_hint: 1, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDRaisedButton:
                text: "Disburse this loan"
                md_bg_color: 0.043, 0.145, 0.278, 1
                font_name: "Roboto-Bold.ttf"
                size_hint: 1, None
                on_release: root.paynow()

<ViewUnderScreenRL>
    MDGridLayout:
        cols: 1
    
        MDTopAppBar:
            title: "View Loan details"
            elevation: 2
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            pos_hint: {'top': 1}

        BoxLayout:
            orientation: 'vertical'
            spacing: dp(40)
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
                    text: 'Amount:'
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

                MDLabel:
                    id: amount
                    bold: True
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1
                    

            MDLabel:
                text: ''
                halign: 'left'
                size_hint_y: None
                height: dp(20)
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Product Name'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: pro_name
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Borrower Name'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: b_name
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Phone Number'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: phone_num
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Ascend Score'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: ascend
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    


            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Interest(%)'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: int_rate
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Duration(M)'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: tenure
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Credit Limit'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: limit
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
                    


            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Published Date'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: date
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Loan Status'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: status
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold : True
            MDLabel:
                text: ''
                halign: 'left'
                size_hint_y: None
                height: dp(5)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(15)
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
                text: ''
                halign: 'left'
                size_hint_y: None
                height: dp(5)
            MDGridLayout:
                cols: 3

                MDLabel:
                    text: 'Total'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1  
                    font_size: dp(25) 
                    bold: True
                MDIconButton:
                    icon: 'currency-inr'
                    halign: 'center' 
                    bold: True   

                MDLabel:
                    id: amount_1
                    bold: True
                    halign: 'left'

        MDBoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: dp(50)
            MDLabel:
                text: "Your Loan request is Rejected"    
                bold: True  
                halign: "center"
                size_hint_y: None
                height: dp(50)    
"""
Builder.load_string(view_loans)


class ViewUnderProcess(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        product_name = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])
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
            if customer_id[i] in profile_customer_id:
                number = profile_customer_id.index(customer_id[i])
            else:
                number = 0
            item = ThreeLineAvatarIconListItem(

                IconLeftWidget(
                    icon="card-account-details-outline"
                ),
                text=f"Borrower Name : {borrower_name[i]}",
                secondary_text=f"Borrower Number : {profile_mobile_number[number]}",
                tertiary_text=f"Product Name : {product_name[i]}",
                text_color=(0, 0, 0, 1),  # Black color
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0, 0, 0, 1),
                tertiary_theme_text_color='Custom'
            )
            item.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
            self.ids.container.add_widget(item)

    def icon_button_clicked(self, instance, loan_id):
        # Handle the on_release event here
        print(loan_id)
        data = app_tables.fin_loan_details.search()  # Fetch data here
        loan_status = None
        for loan in data:
            if loan['loan_id'] == loan_id:
                loan_status = loan['loan_updated_status']
                break

        if loan_status == 'approved':
            # Open the screen for approved loans

            sm = self.manager

            # Create a new instance of the LoginScreen
            approved = ViewUnderScreenLR(name='ViewUnderScreenLR')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(approved)

            # Switch to the LoginScreen
            sm.current = 'ViewUnderScreenLR'
            self.manager.get_screen('ViewUnderScreenLR').initialize_with_value(loan_id, data)

        elif loan_status == 'under process':
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            under_process = ViewUnderScreen(name='ViewUnderScreen')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(under_process)

            # Switch to the LoginScreen
            sm.current = 'ViewUnderScreen'
            self.manager.get_screen('ViewUnderScreen').initialize_with_value(loan_id, data)
        elif loan_status == 'rejected':
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            rejected = ViewUnderScreenRL(name='ViewUnderScreenRL')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(rejected)

            # Switch to the LoginScreen
            sm.current = 'ViewUnderScreenRL'
            self.manager.get_screen('ViewUnderScreenLR').initialize_with_value(loan_id, data)
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
        # Navigate to the previous screen with a slide transition
        from lender_dashboard import LenderDashboard
        self.manager.transition = SlideTransition(direction='right')

        type = self.manager.get_screen('LenderDashboard').type()
        print(type)
        if type == 'dashboard':
            self.manager.transition = SlideTransition(direction='right')
            sm = self.manager

            # Create a new instance of the LoginScreen
            profile = LenderDashboard(name='LenderDashboard')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(profile)

            # Switch to the LoginScreen
            sm.current = 'LenderDashboard'
        else:
            sm = self.manager
            profile = ViewLoansScreen(name='ViewLoansScreen')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(profile)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansScreen'

    def refresh(self):
        self.ids.container.clear_widgets()
        self.__init__()


class ViewUnderScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.loan_id = None

    def on_back_button_press(self):
        self.manager.current = 'ViewUnderProcess'

    def initialize_with_value(self, value, data):
        profile = app_tables.fin_user_profile.search()
        self.loan_id = value
        customer_id = []
        loan_id = []
        product_name = []
        borrower_name = []
        tenure = []
        interest_rate = []
        loan_amount = []
        loan_amount1 = []
        credit_limit = []
        date_of_apply = []
        status = []
        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            product_name.append(i['product_name'])
            borrower_name.append(i['borrower_full_name'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            loan_amount.append(i['loan_amount'])
            loan_amount1.append(i['loan_amount'])
            credit_limit.append(i['credit_limit'])
            date_of_apply.append(i['borrower_loan_created_timestamp'])
            status.append(i['loan_updated_status'])
        profile_customer_id = []
        profile_mobile_number = []
        ascend_score=[]
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            ascend_score.append(i['ascend_value'])
        index = 0

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.pro_name.text = str(product_name[index])
            self.ids.b_name.text = str(borrower_name[index])
            self.ids.int_rate.text = str(interest_rate[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.amount.text = str(loan_amount[index])
            self.ids.amount_1.text = str(loan_amount1[index])
            self.ids.limit.text = str(credit_limit[index])
            self.ids.date.text = str(date_of_apply[index])
            self.ids.status.text = str(status[index])

        if customer_id[index] in profile_customer_id:
            index2 = profile_customer_id.index(customer_id[index])

            self.ids.phone_num.text = str(profile_mobile_number[index2])
            self.ids.ascend.text = str(ascend_score[index2])

    def email_user(self):
        return anvil.server.call('another_method')

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

    def approved_click(self):
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
        Clock.schedule_once(lambda dt: self.perform_approved_click(modal_view), 2)

    def perform_approved_click(self, modal_view):

        # Cancel the animation
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        profile = app_tables.fin_user_profile.search()
        email_user = self.email_user()
        profile_customer_id = []
        profile_email = []
        profile_name = []
        email_index = 0
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_email.append(i['email_user'])
            profile_name.append(i['full_name'])

        if email_user in profile_email:
            email_index = profile_email.index(email_user)
        else:
            print("no email found")

        approved_date = datetime.now()
        data = app_tables.fin_loan_details.search()
        loan_id = self.loan_id
        print(loan_id)

        loan_idlist = []
        for i in data:
            loan_idlist.append(i['loan_id'])
        print(loan_idlist)
        if loan_id in loan_idlist:
            index = loan_idlist.index(loan_id)
            data[index]['loan_updated_status'] = 'approved'
            data[index]['lender_accepted_timestamp'] = approved_date
            data[index]['lender_customer_id'] = profile_customer_id[email_index]
            data[index]['lender_full_name'] = profile_name[email_index]
            data[index]['lender_email_id'] = profile_email[email_index]
            sm = self.manager
            disbursed = ViewUnderScreenLR(name='ViewUnderScreenLR')
            sm.add_widget(disbursed)
            sm.current = 'ViewUnderScreenLR'
            self.manager.get_screen('ViewUnderScreenLR').initialize_with_value(loan_id, data)
            self.show_validation_error(f"Your requested Loan is Approved")
            return
        else:
            pass

    def rejected_click(self):
        data = app_tables.fin_loan_details.search()
        loan_id = self.loan_id
        print(loan_id)

        loan_idlist = []
        for i in data:
            loan_idlist.append(i['loan_id'])
        print(loan_idlist)
        if loan_id in loan_idlist:
            index = loan_idlist.index(loan_id)
            data[index]['loan_updated_status'] = 'rejected'
            sm = self.manager
            disbursed = ViewUnderScreenRL(name='ViewUnderScreenRL')
            sm.add_widget(disbursed)
            sm.current = 'ViewUnderScreenRL'
            self.manager.get_screen('ViewUnderScreenRL').initialize_with_value(loan_id, data)
            self.show_validation_error(f"Your requested Loan is Rejected")
            return
        else:
            pass

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation",
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

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ViewUnderProcess'


class ViewUnderScreenLR(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.loan_id = None

    def show_alert_dialog(self, alert_text):
        if not hasattr(self, 'dialog') or not self.dialog:
            self.dialog = MDDialog(
                text=alert_text,
                buttons=[
                    MDFlatButton(
                        text="OK", on_release=self.close_dialog
                    ),
                ],
            )

        self.dialog.text = alert_text
        self.dialog.open()

    # Click Cancel Button
    def close_dialog(self, obj):
        # Close alert box
        self.dialog.dismiss()

    def initialize_with_value(self, value, data):
        profile = app_tables.fin_user_profile.search()
        self.loan_id = value
        customer_id = []
        loan_id = []
        product_name = []
        borrower_name = []
        tenure = []
        interest_rate = []
        loan_amount = []
        loan_amount1 = []
        credit_limit = []
        date_of_apply = []
        status = []
        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            product_name.append(i['product_name'])
            borrower_name.append(i['borrower_full_name'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            loan_amount.append(i['loan_amount'])
            loan_amount1.append(i['loan_amount'])
            credit_limit.append(i['credit_limit'])
            date_of_apply.append(i['borrower_loan_created_timestamp'])
            status.append(i['loan_updated_status'])
        profile_customer_id = []
        profile_mobile_number = []
        ascend_score=[]

        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            ascend_score.append(i['ascend_value'])

        index = 0

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.pro_name.text = str(product_name[index])
            self.ids.b_name.text = str(borrower_name[index])
            self.ids.int_rate.text = str(interest_rate[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.amount.text = str(loan_amount[index])
            self.ids.amount_1.text = str(loan_amount1[index])
            self.ids.limit.text = str(credit_limit[index])
            self.ids.date.text = str(date_of_apply[index])
            self.ids.status.text = str(status[index])


        if customer_id[index] in profile_customer_id:
            index2 = profile_customer_id.index(customer_id[index])

            self.ids.phone_num.text = str(profile_mobile_number[index2])
            self.ids.ascend.text = str(ascend_score[index2])

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            # self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    '''def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ViewLoansRequest'
        '''

    def on_back_button_press(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ViewUnderScreen'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation",
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

    def paynow(self):
        data = app_tables.fin_loan_details.search()
        disbursed_time = datetime.now()
        paid_time = datetime.now()
        loan_id = self.loan_id
        print(loan_id)
        loan_id_list = []
        disbursed = []
        credit_limit = []
        loan_amount = []
        bow_customer_id = []

        wallet = app_tables.fin_wallet.search()
        wallet_customer_id = []
        wallet_amount = []
        wallet_email = []
        wallet_id = []
        for i in wallet:
            wallet_customer_id.append(i['customer_id'])
            wallet_amount.append(i['wallet_amount'])
            wallet_email.append(i['user_email'])
            wallet_id.append(i['wallet_id'])

        lender_customer_id = []
        processing_fee = []
        for i in data:
            loan_id_list.append(i['loan_id'])
            disbursed.append(i['lender_accepted_timestamp'])
            credit_limit.append(i['credit_limit'])
            bow_customer_id.append(i['borrower_customer_id'])
            loan_amount.append(i['loan_amount'])
            lender_customer_id.append(i['lender_customer_id'])
            processing_fee.append(i['total_processing_fee_amount'])

        if loan_id in loan_id_list:
            index = loan_id_list.index(loan_id)

        loan_amount_text = float(self.ids.amount.text) - processing_fee[index]

        b_index = -1
        l_index = -1
        if lender_customer_id[index] in wallet_customer_id and int(bow_customer_id[index]) in wallet_customer_id:
            b_index = wallet_customer_id.index(int(bow_customer_id[index]))
            l_index = wallet_customer_id.index(lender_customer_id[index])
        else:
            print("no customer id found")

        print(loan_amount_text)
        datetime1 = datetime.fromisoformat(str(disbursed_time)).replace(tzinfo=timezone.utc)
        datetime2 = datetime.fromisoformat(str(disbursed[index])).replace(tzinfo=timezone.utc)

        # Calculate the time difference
        time_difference = datetime1 - datetime2

        # Extract minutes from the timedelta
        minutes_difference = round(time_difference.total_seconds() / 60)

        print(f"The difference in minutes is: {minutes_difference} minutes")

        transaction = app_tables.fin_wallet_transactions.search()
        t_id = []
        for i in transaction:
            t_id.append(i['transaction_id'])

        if len(t_id) >= 1:
            transaction_id = 'TA' + str(int(t_id[-1][2:]) + 1).zfill(4)
        else:
            transaction_id = 'TA0001'
        transaction_date_time = datetime.today()
        if minutes_difference < 30 and wallet_amount[l_index] >= float(loan_amount_text):
            self.show_success_dialog(
                f"Amount paid successfully {loan_amount_text} to this Loan ID {loan_id_list[index]}")
            data[index]['loan_updated_status'] = 'disbursed'
            data[index]['loan_disbursed_timestamp'] = paid_time
            wallet[b_index]['wallet_amount'] += float(loan_amount_text)
            wallet[l_index]['wallet_amount'] -= float(loan_amount_text)
            app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                       customer_id=wallet_customer_id[l_index],
                                                       user_email=wallet_email[l_index],
                                                       transaction_type="amount transferred",
                                                       amount=float(loan_amount_text),
                                                       status='success', wallet_id=wallet_id[l_index],
                                                       transaction_time_stamp=transaction_date_time,
                                                       receiver_customer_id=wallet_customer_id[b_index],
                                                       receiver_email=wallet_email[b_index])
            app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                       customer_id=wallet_customer_id[b_index],
                                                       user_email=wallet_email[b_index],
                                                       transaction_type="amount received",
                                                       amount=float(loan_amount_text),
                                                       status='success', wallet_id=wallet_id[b_index],
                                                       transaction_time_stamp=transaction_date_time,
                                                       receiver_customer_id=wallet_customer_id[l_index],
                                                       receiver_email=wallet_email[l_index])
            anvil.server.call('loan_text', None)
            anvil.server.call('view_loan', None)
            self.manager.current = "LenderDashboard"
            return

        elif minutes_difference < 30 and wallet_amount[l_index] < float(loan_amount_text):

            self.show_success_dialog2(f"Insufficient Balance Please Deposit {float(loan_amount_text)}")
            anvil.server.call('loan_text', loan_amount_text)
            anvil.server.call('view_loan', "view_loan_text")

            sm = self.manager
            # Create a new instance of the LenderWalletScreen
            wallet_screen = LenderWalletScreen(name='LenderWalletScreen', loan_amount_text=float(loan_amount_text))
            # Add the LenderWalletScreen to the existing ScreenManager
            sm.add_widget(wallet_screen)
            # Switch to the LenderWalletScreen
            sm.current = 'LenderWalletScreen'

        elif minutes_difference > 30:
            self.show_success_dialog3(f"Time Out You Must Finish Before 30 Minutes")
            data[index]['loan_updated_status'] = 'lost opportunities'
            self.manager.current = 'ViewLoansRequest'
            return

    def show_success_dialog(self, text):
        dialog = MDDialog(
            text=text,
            size_hint=(0.8, 0.3),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *args: self.open_dashboard_screen(dialog),
                    theme_text_color="Custom",
                    text_color=(0.043, 0.145, 0.278, 1),
                )
            ]
        )
        dialog.open()

    def show_success_dialog2(self, text):
        dialog = MDDialog(
            text=text,
            size_hint=(0.8, 0.3),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *args: self.open_dashboard_screen2(dialog),
                    theme_text_color="Custom",
                    text_color=(0.043, 0.145, 0.278, 1),
                )
            ]
        )
        dialog.open()

    def show_success_dialog3(self, text):
        dialog = MDDialog(
            text=text,
            size_hint=(0.8, 0.3),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *args: self.open_dashboard_screen3(dialog),
                    theme_text_color="Custom",
                    text_color=(0.043, 0.145, 0.278, 1),
                )
            ]
        )
        dialog.open()

    def open_dashboard_screen(self, dialog):

        dialog.dismiss()
        self.manager.current = 'LenderDashboard'

    def open_dashboard_screen2(self, dialog):

        dialog.dismiss()
        self.manager.current = 'LenderWalletScreen'

    def open_dashboard_screen3(self, dialog):

        dialog.dismiss()
        self.manager.current = 'ViewLoansRequest'


class ViewUnderScreenRL(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_back_button_press(self):
        self.manager.current = 'ViewUnderProcess'

    def initialize_with_value(self, value, data):
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        loan_id = []
        product_name = []
        borrower_name = []
        tenure = []
        interest_rate = []
        loan_amount = []
        loan_amount1 = []
        credit_limit = []
        date_of_apply = []
        status = []
        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            product_name.append(i['product_name'])
            borrower_name.append(i['borrower_full_name'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            loan_amount.append(i['loan_amount'])
            loan_amount1.append(i['loan_amount'])
            credit_limit.append(i['credit_limit'])
            date_of_apply.append(i['borrower_loan_created_timestamp'])
            status.append(i['loan_updated_status'])
        profile_customer_id = []
        profile_mobile_number = []
        ascend_score = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            ascend_score.append(i['ascend_value'])
        index = 0

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.pro_name.text = str(product_name[index])
            self.ids.b_name.text = str(borrower_name[index])
            self.ids.int_rate.text = str(interest_rate[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.amount.text = str(loan_amount[index])
            self.ids.amount_1.text = str(loan_amount1[index])
            self.ids.limit.text = str(credit_limit[index])
            self.ids.date.text = str(date_of_apply[index])
            self.ids.status.text = str(status[index])

        if customer_id[index] in profile_customer_id:
            index2 = profile_customer_id.index(customer_id[index])

            self.ids.phone_num.text = str(profile_mobile_number[index2])
            self.ids.ascend.text = str(ascend_score[index])

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
        self.manager.current = 'ViewUnderProcess'


class MyScreenManager(ScreenManager):
    pass


