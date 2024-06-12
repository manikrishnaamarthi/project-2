from anvil.tables import app_tables
from kivy.animation import Animation
from kivy.clock import Clock
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
from kivymd.uix.button import MDFlatButton
from kivymd.uix.snackbar import Snackbar

lost_opportunities = '''
<WindowManager>:
    LostOpportunitiesScreen:
    LostOpportunitiesProfileScreen:
<LostOpportunitiesScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Lost Opportunities"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container1


<LostOpportunitiesProfileScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Profile"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                BoxLayout:
                    id: box1
                    orientation: 'vertical'
                    size_hint_y: None
                    MDLabel:
                        text: "Borrower Full Loan details"
                        halign: "center"
                        bold: True
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(20)

                    BoxLayout:
                        id: box1
                        orientation: 'vertical'
                        size_hint_y: None
                        height: dp(500)

                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  # Blue color for the box
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]

                        GridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)

                            MDLabel:
                                text: "User ID:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: user1
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                            
                            MDLabel:
                                text: "Loan ID:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: loan_id
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                
                            MDLabel:
                                text: "Borrower Name:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: name
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                            MDLabel:
                                text: "Date Of Apply:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: date
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                
                            MDLabel:
                                text: "Loan Tenure:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True

                            MDLabel:
                                id: tenure
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                            
                            MDLabel:
                                text: "Interest Rate:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: interest
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                            MDLabel:
                                text: "Loan Amount:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: amount_applied
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                            
                            MDLabel:
                                text: "Loan Status:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: status
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
    '''

Builder.load_string(lost_opportunities)
conn = sqlite3.connect('fin_user.db')
cursor = conn.cursor()


class LostOpportunitiesScreen(Screen):
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
            if loan_status[c] == 'lost opportunities':
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
                secondary_text=f"Borrower Mobile Number : {profile_mobile_number[number]}",
                tertiary_text=f"Product Name : {product_name[i]}",
                text_color=(0, 0, 0, 1),  # Black color
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0, 0, 0, 1),
                tertiary_theme_text_color='Custom'
            )
            item.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
            self.ids.container1.add_widget(item)

    def icon_button_clicked(self, instance, loan_id):
        # Handle the on_release event here
        data = app_tables.fin_loan_details.search()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = LostOpportunitiesProfileScreen(name='LostOpportunitiesProfileScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'LostOpportunitiesProfileScreen'
        self.manager.get_screen('LostOpportunitiesProfileScreen').initialize_with_value(loan_id, data)

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
        self.manager.current = 'LenderDashboard'

    def refresh(self):
        self.ids.container1.clear_widgets()
        self.__init__()


class LostOpportunitiesProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_back_button_press(self):
        self.manager.current = 'LostOpportunitiesScreen'

    def initialize_with_value(self, value, data):
        customer_id = []
        loan_id = []
        loan_amount = []
        interest_rate = []
        tenure = []
        date_of_apply = []
        name = []
        status = []
        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            date_of_apply.append(i['lender_accepted_timestamp'])
            loan_amount.append(i['loan_amount'])
            name.append(i['borrower_full_name'])
            status.append(i['loan_updated_status'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.loan_id.text = str(loan_id[index])
            self.ids.user1.text = str(customer_id[index])
            self.ids.interest.text = str(interest_rate[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.amount_applied.text = str(loan_amount[index])
            self.ids.name.text = str(name[index])
            date = date_of_apply[index].date()
            self.ids.date.text = str(date)
            self.ids.status.text = str(status[index])

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
        self.manager.current = 'LostOpportunitiesScreen'


class MyScreenManager(ScreenManager):
    pass
