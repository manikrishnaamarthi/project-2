from datetime import datetime
import anvil.server
import json

from kivy.clock import mainthread, Clock
from kivy.config import value
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.uix.popup import Popup
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import *
from kivy.lang import Builder
from datetime import datetime
from kivy.core.window import Window
import anvil.users
from pytz import utc

import server
from anvil.tables import app_tables
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager

from borrower_dues import BorrowerDuesScreen

extension_loan_request = """
<WindowManager>:
    NotificationScreen:
    ExtensionLoansProfileScreen:
    ExtendLoansScreen:

<NotificationScreen> 
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Notifications"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            title_align: 'center'
        MDScrollView:

            MDList:
                id: container1

<NotificationViewScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Details"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            title_align: 'center'

        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height

                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    width:self.minimum_width
                    padding: dp(20)
                    spacing:dp(10)
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
                                width:0.7
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]



                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Lender Name" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: name
                                text: "" 
                                height:dp(50)
                                size_hint_y:None
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Lender Phone Number" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: number
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Product Name" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: product_name
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"   
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Loan Amount" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: loan_amount
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"


                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Loan Tenure(Months)" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: tenure
                                text: "" 
                                height:dp(50)
                                size_hint_y:None
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Interest Rate (%)" 
                                size_hint_y:None
                                bold: True
                                height:dp(50)
                                halign: "left"

                            MDLabel:
                                id: interest
                                text: "" 
                                height:dp(50)
                                size_hint_y:None
                                halign: "left"
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: dp(100)
                            padding: dp(1)
                            spacing: dp(1)

                            MDLabel:
                                id: loan_status_label
                                size_hint_y: None
                                bold: True
                                height: dp(10)
                                halign: "center"
                            MDLabel:
                                id: extension_status_label
                                size_hint_y: None
                                bold: True
                                height: dp(10)
                                halign: "center"
                            MDLabel:
                                id: foreclosure_status_label
                                size_hint_y: None
                                bold: True
                                height: dp(10)
                                halign: "center"       
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)

                            MDLabel:
                                id: user1
                                color:1,1,1,1      
                                font_size:dp(1)
                                text: "" 
                                height:dp(1)
                            MDLabel:
                                id: loan_id
                                color:1,1,1,1      
                                font_size:dp(1)
                                text: "" 
                                height:dp(1)
                            MDLabel:
                                id: total_payment
                                color:1,1,1,1      
                                font_size:dp(1)
                                text: "" 
                                height:dp(1)




<ExtendLoansScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Extension Loan Request"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            title_align: 'center'

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
                        text: " Borrower Extension Details"
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
                        height: dp(700)
                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  # Blue color for the box
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Loan Amount" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: loan_amount
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                            MDLabel:
                                id: loan_id
                                color:1,1,1,1      
                                font_size:dp(1)
                                text: "" 
                                height:dp(1)

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Extension Fee(%) :" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: extension_fee
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Extension Amount :" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: extension_amount
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Finial Repayment Amount :" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: finial_repayment_amount
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "New EMI :" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: new_emi
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 1
                            spacing: dp(5)
                            padding: dp(10)
                            MDLabel:
                                text: "Reason For Extended Loan :" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                            MDTextField:
                                hint_text: ""
                                id: reason
                                size_hint_y:None
                                height:dp(50)
                        MDLabel:
                            text: " " 
                            size_hint_y:None

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDCheckbox:
                                id: check
                                size_hint: None, None
                                width: "20dp"
                                active: False
                                on_active: root.on_checkbox_active(self, self.active)
                            MDLabel:
                                text: "I Agree Terms and Conditions"
                                multiline: False
                                theme_text_color: 'Primary'
                                halign: 'left'
                                valign: 'center'
                                bold: True
                                on_touch_down: app.root.get_screen("ExtendLoansScreen").show_terms_dialog() if self.collide_point(*args[1].pos) else None

                        MDFloatLayout:
                            MDRaisedButton:
                                text: "Submit"
                                md_bg_color: 0.043, 0.145, 0.278, 1
                                font_name: "Roboto-Bold"
                                size_hint: 0.4, None
                                height: dp(50)
                                on_release:root.add_data()
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                font_size:dp(15)
"""
Builder.load_string(extension_loan_request)
date = datetime.today()
print(date)

from datetime import datetime


class NotificationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.clicked_notifications = set()  # Set to store clicked notifications
        self.load_notifications()
        Clock.schedule_interval(self.refresh_wrapper, 15)  # Schedule refresh every 10 seconds

    @mainthread
    def refresh_wrapper(self, dt):
        self.refresh()

    def refresh(self):
        self.load_notifications()

    def load_notifications(self):
        self.ids.container1.clear_widgets()

        # Fetch data from fin_loan_details table
        loan_data = app_tables.fin_loan_details.search()
        email = anvil.server.call('another_method')
        profile = app_tables.fin_user_profile.search(email_user=email)

        # Lists to store details
        customer_id, loan_id, loan_amount, borrower_name, loan_status, tenure, product_name, email1 = ([] for _ in range(8))
        status_timestamp = []  # Initialize status_timestamp as an empty list

        today = datetime.today().date()

        for i in loan_data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            borrower_name.append(i['lender_full_name'])
            loan_status.append(i['loan_updated_status'])
            tenure.append(i['tenure'])
            product_name.append(i['product_name'])
            email1.append(i['borrower_email_id'])

            # Determine and fetch the appropriate timestamp based on loan status and append it to status_timestamp list
            if i['loan_updated_status'] == 'disbursed':
                status_timestamp.append(i['loan_disbursed_timestamp'])
            elif i['loan_updated_status'] == 'approved':
                status_timestamp.append(i['lender_accepted_timestamp'])
            elif i['loan_updated_status'] == 'rejected':
                status_timestamp.append(i['lender_rejected_timestamp'])
            else:
                status_timestamp.append(None)

            # Check for overdue payments
            first_emi_payment_due_date = i['first_emi_payment_due_date'].date() if isinstance(i['first_emi_payment_due_date'], datetime) else i['first_emi_payment_due_date']
            if first_emi_payment_due_date is not None and i['loan_updated_status'] in ['disbursed', 'foreclosure', 'extension'] and first_emi_payment_due_date <= today:
                self.add_due_notification_item(i['lender_full_name'], i['loan_id'], i['loan_updated_status'], i['loan_amount'], i['product_name'], first_emi_payment_due_date)

        profile_customer_id, profile_mobile_number = [], []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])

        cos_id = None
        if email in email1:
            index = email1.index(email)
            cos_id = customer_id[index]

        if cos_id is not None:
            c = -1
            index_list = []
            for i in range(len(loan_data)):
                c += 1
                if loan_status[c] in ('approved', 'disbursed', 'rejected') and customer_id[c] == cos_id:
                    index_list.append(c)

            self.display_notifications(index_list, loan_id, borrower_name, loan_status, loan_amount, product_name, loan_data, status_timestamp)

        # Fetch data from fin_extend_loans table
        extension_data = app_tables.fin_extends_loan.search()
        for item in extension_data:
            if item['status'] in ('approved', 'rejected'):
                self.add_notification_item(item['lender_full_name'], item['loan_id'], item['status'], 'extension', item['loan_amount'], item['product_name'], item['status_timestamp'])

        # Fetch data from fin_foreclosure table
        foreclosure_data = app_tables.fin_foreclosure.search()
        for item in foreclosure_data:
            if item['status'] in ('approved', 'rejected'):
                self.add_notification_item(item['lender_full_name'], item['loan_id'], item['status'], 'foreclosure', item['loan_amount'], item['product_name'], item['status_timestamp'])
        self.print_container1_items()

    def print_container1_items(self):
        false_count = 0
        for item in self.ids.container1.children:
            loan_id = getattr(item, 'loan_id', 'No loan ID')
            clicked_status = self.is_notification_clicked(loan_id)
            print(f"Loan ID: {loan_id}, Clicked Status: {clicked_status}")
            if not clicked_status:
                false_count += 1

        # Store the count of false in a JSON file
        count_data = {"false_count": false_count}
        with open("false_count.json", "w") as json_file:
            json.dump(count_data, json_file)

        print("Count of 'Clicked Status: False' stored in false_count.json:", false_count)
    def add_due_notification_item(self, borrower_name, loan_id, loan_status, loan_amount, product_name, shedule_date):
        self.ids.container1.clear_widgets()  # Clear existing items from the container

        today_date = datetime.now(tz=utc).date()
        data = app_tables.fin_loan_details.search()
        emi_data = app_tables.fin_emi_table.search()
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        loan_id = []
        loan_status = []
        borrower_id = []
        borrower_name = []
        schedule_date = []

        s = 0

        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            customer_id.append(i['borrower_customer_id'])
            loan_status.append(i['loan_updated_status'])
            borrower_id.append(i['borrower_customer_id'])
            borrower_name.append(i['borrower_full_name'])
            schedule_date.append(i['first_emi_payment_due_date'])

        emi_loan_id = []
        emi_num = []
        next_payment = []
        part_payment_type = []
        part_payment_done = []
        for i in emi_data:
            emi_loan_id.append(i['loan_id'])
            emi_num.append(i['emi_number'])
            next_payment.append(i['next_payment'])
            part_payment_type.append((i['payment_type']))
            part_payment_done.append(i['part_payment_done'])
        profile_customer_id = []
        profile_mobile_number = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
        index_list = []
        a = -1
        shedule_date = {}
        for i in range(s):
            a += 1

            if loan_status[i] == "disbursed" or loan_status[i] == "extension" or loan_status[i] == "foreclosure":
                if loan_id[i] not in emi_loan_id and schedule_date[i] is not None and today_date >= schedule_date[i]:
                    index_list.append(i)
                    shedule_date[loan_id[i]] = schedule_date[i]
                elif loan_id[i] in emi_loan_id:
                    last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(loan_id[i])
                    if next_payment[last_index] is not None and today_date >= next_payment[last_index]:
                        index_list.append(i)
                        shedule_date[loan_id[i]] = next_payment[last_index]

        today_date = datetime.now(tz=utc).date()
        b = 1
        k = -1
        for i in reversed(index_list):
            b += 1
            k += 1
            if customer_id[i] in profile_customer_id:
                number = profile_customer_id.index(customer_id[i])
            else:
                number = 0

            # Retrieve loan amount and product name based on loan_id
            loan_amount_for_id = None
            product_name_for_id = None
            for loan_record in data:
                if loan_record['loan_id'] == loan_id[i]:
                    loan_amount_for_id = loan_record['loan_amount']
                    product_name_for_id = loan_record['product_name']
                    break

            pay_now_button = Button(
                text="Pay Now",
                size_hint=(None, None),
                size=(dp(100), dp(28)),  # Adjust button size
                background_color=(0, 1, 0, 1),  # green background
                color=(1, 1, 1, 1)  # White text color
            )
            pay_now_button.bind(
                on_release=lambda instance, loan_id=loan_id[i]: self.pay_now_button(instance, loan_id, shedule_date))

            # Create a BoxLayout for the button
            button_layout = BoxLayout(
                orientation='horizontal',
                size_hint=(None, None),
                size=(dp(100), dp(28)),  # Adjust size of button layout
                spacing=dp(10),  # Adjust spacing if needed
                pos_hint={'center_x': 0.5, 'center_y': 0.2}  # Center the button layout
            )

            button_layout.add_widget(pay_now_button)

            # Create the ThreeLineAvatarIconListItem without tertiary text
            item = ThreeLineAvatarIconListItem(
                IconLeftWidget(icon="calendar-check"),
                IconRightWidget(icon="chevron-right"),
                text=f"Dear {borrower_name[i]}, your loan payment is currently",
                secondary_text=f"overdue for {loan_amount_for_id} loan amount in {product_name_for_id} product",
                tertiary_text=" ",
                text_color=(0, 0, 0, 1),
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0, 0, 0, 1),
                tertiary_theme_text_color='Custom'
            )
            item.loan_id = loan_id[i]

            # Add the button layout as a widget to the item
            item.add_widget(Label(size_hint_y=None, height=dp(5)))  # Spacer to position button correctly
            item.add_widget(button_layout)  # Add the button layout below the list item

            self.ids.container1.add_widget(item)

    def pay_now_button(self,instance, loan_id, schedule_date):
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = BorrowerDuesScreen(name='BorrowerDuesScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'BorrowerDuesScreen'
        self.manager.get_screen('BorrowerDuesScreen').initialize_with_value(loan_id, schedule_date)

    def display_notifications(self, index_list, loan_id, borrower_name, loan_status, loan_amount, product_name,
                              loan_data, status_timestamp):
        for i in reversed(index_list):
            status_color = "008000" if loan_status[i] == "approved" else ("FF0000" if loan_status[i] == "rejected" else "000000")


            # Embed the color tag in the status message
            status_message = f"{borrower_name[i]}, has [color=#{status_color}]{loan_status[i]}[/color] your loan request"
            secondary_message = f"for {loan_amount[i]} loan amount in {product_name[i]} product"
            tertiary_message = status_timestamp[i].strftime("%Y-%m-%d, %A")

            if self.is_notification_clicked(loan_id[i]):
                formatted_status_message = status_message
                formatted_secondary_message = secondary_message
                formatted_tertiary_message = tertiary_message
            else:
                formatted_status_message = f"[b]{status_message}[/b]"
                formatted_secondary_message = f"[b]{secondary_message}[/b]"
                formatted_tertiary_message = f"[b]{tertiary_message}[/b]"

            item = ThreeLineAvatarIconListItem(
                IconLeftWidget(icon="card-account-details-outline"),
                IconRightWidget(icon="chevron-right"),
                text=formatted_status_message,
                secondary_text=formatted_secondary_message,
                tertiary_text=formatted_tertiary_message,
                text_color=(0, 0, 0, 1),  # Black color
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0.6, 0.6, 0.6, 1),
                tertiary_theme_text_color='Custom'
            )
            item.loan_id = loan_id[i]
            item.bind(
                on_release=lambda instance, loan_id=loan_id[i], loan_type='regular': self.icon_button_clicked(instance,
                                                                                                              loan_id,
                                                                                                              loan_type))
            self.ids.container1.add_widget(item)

    def is_notification_clicked(self, loan_id):
        try:
            with open("notification_status.json", "r") as json_file:
                data = json.load(json_file)
            status = data.get(str(loan_id))
            if isinstance(status, bool):
                return status
            return status.get("clicked", False) if status else False
        except FileNotFoundError:
            return False

    def icon_button_clicked(self, instance, loan_id, loan_type):
        print(f"Clicked loan ID: {loan_id} of type {loan_type}")

        # Update the status in the JSON file
        self.update_json_status(loan_id, loan_type)

        # Remove bold formatting from the clicked item
        instance.text = instance.text.replace("[b]", "").replace("[/b]", "")
        instance.secondary_text = instance.secondary_text.replace("[b]", "").replace("[/b]", "")
        instance.tertiary_text = instance.tertiary_text.replace("[b]", "").replace("[/b]", "")

        # Refresh the notification list to reflect the changes
        self.refresh()

        data = app_tables.fin_loan_details.search()  # Fetch data here
        loan_status = None
        for loan in data:
            if loan['loan_id'] == loan_id:
                loan_status = loan['loan_updated_status']
                break

        sm = self.manager
        if loan_type == 'extension':
            view_screen = NotificationViewScreen(name='ExtensionViewScreen')
        elif loan_type == 'foreclosure':
            view_screen = NotificationViewScreen(name='ForeclosureViewScreen')
        else:
            view_screen = NotificationViewScreen(name='NotificationViewScreen')

        sm.add_widget(view_screen)
        sm.current = view_screen.name
        self.manager.get_screen(view_screen.name).initialize_with_value(loan_id, data, notification_type=loan_type)

    def refresh(self):
        self.load_notifications()

    def update_json_status(self, loan_id, loan_type):
        try:
            with open("notification_status.json", "r") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = {}

        # Update the JSON data with loan type and clicked status
        data[str(loan_id)] = {
            "loan_type": loan_type,
            "clicked": True
        }

        with open("notification_status.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

    def recreate_notification_item(self, instance, loan_id, loan_type):
        text = instance.text.replace("[b]", "").replace("[/b]", "")
        secondary_text = instance.secondary_text.replace("[b]", "").replace("[/b]", "")
        tertiary_text = instance.tertiary_text.replace("[b]", "").replace("[/b]", "")

        item = ThreeLineAvatarIconListItem(
            IconLeftWidget(icon="card-account-details-outline"),
            IconRightWidget(icon="chevron-right"),
            text=text,
            secondary_text=secondary_text,
            tertiary_text=tertiary_text,
            text_color=(0, 0, 0, 1),  # Black color
            theme_text_color='Custom',
            secondary_text_color=(0, 0, 0, 1),
            secondary_theme_text_color='Custom',
            tertiary_text_color=(0.6, 0.6, 0.6, 1),
            tertiary_theme_text_color='Custom'
        )
        item.loan_id = loan_id
        item.bind(
            on_release=lambda instance, loan_id=loan_id, loan_type=loan_type: self.icon_button_clicked(instance,
                                                                                                       loan_id,
                                                                                                       loan_type))
        self.ids.container1.add_widget(item)

    def add_notification_item(self, borrower_name, loan_id, status, notification_type, loan_amount, product_name,
                              status_timestamp):
        status_color = "008000" if status == "approved" else (
            "FF0000" if status == "rejected" else "000000")



        formatted_status_text =f"{borrower_name}, has [color=#{status_color}]{status}[/color] your {notification_type} request"
        secondary_message = f"for {loan_amount} loan amount in {product_name} product"

        if status_timestamp:
            tertiary_message = status_timestamp.strftime("%Y-%m-%d, %A")
        else:
            tertiary_message = "No timestamp available"

        if self.is_notification_clicked(loan_id):
            formatted_text = formatted_status_text
            formatted_secondary_message = secondary_message
            formatted_tertiary_message = tertiary_message
        else:
            formatted_text = f"[b]{formatted_status_text}[/b]"
            formatted_secondary_message = f"[b]{secondary_message}[/b]"
            formatted_tertiary_message = f"[b]{tertiary_message}[/b]"



        item = ThreeLineAvatarIconListItem(
            IconLeftWidget(icon="card-account-details-outline"),
            IconRightWidget(icon="chevron-right"),
            text=formatted_text,
            secondary_text=formatted_secondary_message,
            tertiary_text=formatted_tertiary_message,
            text_color=(0, 0, 0, 1),  # Black color
            theme_text_color='Custom',
            secondary_text_color=(0, 0, 0, 1),
            secondary_theme_text_color='Custom',
            tertiary_text_color=(0.6, 0.6, 0.6, 1),
            tertiary_theme_text_color='Custom'
        )
        item.loan_id = loan_id
        item.bind(
            on_release=lambda instance, loan_id=loan_id, loan_type=notification_type: self.icon_button_clicked(instance,
                                                                                                               loan_id,
                                                                                                               notification_type))
        self.ids.container1.add_widget(item)
    def on_back_button_press(self):
        self.manager.current = 'DashboardScreen'

    def refresh(self):
        self.load_notifications()

    def on_pre_enter(self):
        self.refresh()
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Create a modal view for the loading animation
        modal_view = ModalView(size_hint=(None, None), size=(300, 150), background_color=[0, 0, 0, 0])

        # Create a BoxLayout to hold the loading text
        box_layout = BoxLayout(orientation='vertical')

        # Create a label for the loading text
        loading_label = MDLabel(
            text="Loading...",
            halign="center",
            valign="center",
            theme_text_color="Custom",
            text_color=[1, 1, 1, 1],
            font_size="20sp",
            bold=True
        )

        # Add the label to the box layout
        box_layout.add_widget(loading_label)

        # Add the box layout to the modal view
        modal_view.add_widget(box_layout)

        # Open the modal view
        modal_view.open()

        # Perform the actual action (e.g., checking account details and navigating)
        Clock.schedule_once(lambda dt: self.show_transfer_screen(modal_view), 1)

    def show_transfer_screen(self, modal_view):
        # Dismiss the loading animation modal view
        modal_view.dismiss()
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreen'



    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            self.screen_manager.y = 0
        return True


class NotificationViewScreen(Screen):
    def initialize_with_value(self, value, data, notification_type=None):
        print(f"Initializing with value: {value}")
        emi1 = app_tables.fin_emi_table.search()
        profile = app_tables.fin_user_profile.search()
        profile_customer_id = [i['customer_id'] for i in profile]
        profile_mobile_number = [i['mobile'] for i in profile]
        loan_id = [i['loan_id'] for i in data]
        loan_details = {i['loan_id']: (
            i['borrower_customer_id'], i['loan_amount'], i['tenure'], i['product_name'], i['interest_rate'],
            i['lender_full_name']) for i in data}

        if value in loan_details:
            borrower_customer_id, loan_amount, tenure, product_name, interest_rate, lender_name = loan_details[value]

            if borrower_customer_id in profile_customer_id:
                number = profile_customer_id.index(borrower_customer_id)
                self.ids.number.text = str(profile_mobile_number[number])
            else:
                self.ids.number.text = "N/A"

            self.ids.loan_id.text = str(value)
            self.ids.loan_amount.text = str(loan_amount)
            self.ids.user1.text = str(borrower_customer_id)
            try:
                interest_rate = float(interest_rate)
            except ValueError:
                interest_rate = 0
            self.ids.interest.text = str(interest_rate)
            self.ids.tenure.text = str(tenure)
            self.ids.product_name.text = str(product_name)
            self.ids.name.text = str(lender_name)

        loan_status = None
        for loan in data:
            if loan['loan_id'] == value:
                loan_status = loan['loan_updated_status']
                break

        # Clear all status labels initially
        self.ids.loan_status_label.text = ""
        self.ids.extension_status_label.text = ""
        self.ids.foreclosure_status_label.text = ""

        if notification_type == 'extension':
            extension_data = app_tables.fin_extends_loan.search(loan_id=value)
            if extension_data and len(extension_data) > 0:
                extension_status = extension_data[0]['status']
                self.ids.extension_status_label.text = f"Your application for extending the loan term has been {extension_status}."
            else:
                self.ids.extension_status_label.text = "Extension status not available"

        elif notification_type == 'foreclosure':
            foreclosure_data = app_tables.fin_foreclosure.search(loan_id=value)
            if foreclosure_data and len(foreclosure_data) > 0:
                foreclosure_status = foreclosure_data[0]['status']
                self.ids.foreclosure_status_label.text = f"Your application for foreclosure has been {foreclosure_status}."
            else:
                self.ids.foreclosure_status_label.text = "Foreclosure status not available"

        else:
            if loan_status is not None:
                self.ids.loan_status_label.text = f"The processing of your loan request is complete, and it has been {loan_status}."
            else:
                self.ids.loan_status_label.text = "N/A"

    def on_back_button_press(self):
        self.manager.current = 'NotificationScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'NotificationScreen'

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"


class ExtendLoansScreen(Screen):
    loan_id = ""
    loan_amount = ""
    extension_fee = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.check = None

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.check = True
        else:
            self.check = False

    def on_back_button_press(self):
        self.manager.current = 'ExtensionLoansProfileScreen'
        # Assuming you have these labels in your Kivy app

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)
        self.root_screen = self.manager.get_screen('ExtensionLoansProfileScreen')
        loan_id = str(self.root_screen.ids.loan_id.text)
        self.ids.loan_id.text = str(loan_id)

        loan_amount = str(self.root_screen.ids.loan_amount.text)
        self.ids.loan_amount.text = str(loan_amount)

        extension_fee = str(self.root_screen.ids.extension_fee.text)
        self.ids.extension_fee.text = str(extension_fee)

        tenure = str(self.root_screen.ids.tenure.text)
        loan_extension_months = str(self.root_screen.ids.extension_months.text)
        extension_amount = float(extension_fee) * float(loan_amount) / 100
        self.ids.extension_amount.text = str(extension_amount)

        emi = app_tables.fin_product_details.search()
        if emi:
            roi = emi[0]['roi']
            roi = float(roi)
        else:
            self.show_validation_error("ROI not found for the selected category")
            return

        monthly_interest_rate = (roi / 100) / 12
        total_tenure = app_tables.fin_emi_table.search(loan_id=loan_id)
        try:
            total_tenure = total_tenure[0]['emi_number']
        except IndexError:
            self.show_validation_error("EMI number not found for the loan")
            return

        remaining_tenure = (float(tenure) - float(total_tenure)) + float(loan_extension_months)
        loan_extension = (float(loan_amount) * monthly_interest_rate * pow(1 + monthly_interest_rate,
                                                                           float(remaining_tenure))) / \
                         (pow(1 + monthly_interest_rate, float(remaining_tenure)) - 1)
        emi = loan_extension
        self.ids.new_emi.text = f"{float(emi):.2f}"

        payment = app_tables.fin_emi_table.search()
        if payment:
            total_payment = payment[0]['emi_number']
            if total_payment is not None:
                total_payment = float(total_payment)
            else:
                self.show_validation_error("Invalid total payment EMI number")
                return

            emi_paid = total_payment * emi
            remaining_loan_amount = (float(loan_amount) - emi_paid) + float(extension_amount)
            self.ids.finial_repayment_amount.text = f"{remaining_loan_amount:.2f}"
        else:
            self.show_validation_error("No payment data found")

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def show_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    date = datetime.today()

    def add_data(self):
        loan_id = str(self.root_screen.ids.loan_id.text)
        extension_fee = float(self.root_screen.ids.extension_fee.text)
        loan_extension_months = float(self.root_screen.ids.extension_months.text)
        loan_amount = float(self.root_screen.ids.loan_amount.text)
        extension_amount = float(self.ids.extension_amount.text)
        finial_repayment = float(self.ids.finial_repayment_amount.text)
        new_emi = float(self.ids.new_emi.text)
        reason = str(self.ids.reason.text)
        borrower_name = ''
        customer_id = ''
        email = ''
        emi_number = ''
        data = app_tables.fin_loan_details.search(loan_id=loan_id)
        if data:
            borrower_name = data[0]['borrower_full_name']
            customer_id = data[0]['borrower_customer_id']
            email = data[0]['borrower_email_id']
            lender_id = data[0]['lender_customer_id']
            lender_email = data[0]['lender_email_id']
            lender_name = data[0]['lender_full_name']
        emi = app_tables.fin_emi_table.search(loan_id=loan_id)
        if emi:
            emi_number = emi[0]['emi_number']

        # Validate reason field
        if not reason:
            self.show_validation_error("Reason is required.")
            return

        if self.check != True:
            self.show_validation_error(' Please Read and Accept the  Terms and Conditions')
            return

        # Check if all required fields are filled
        if loan_id and lender_name and lender_id and lender_email and email and emi_number and loan_amount and customer_id and extension_fee and loan_extension_months and extension_amount and finial_repayment and borrower_name and new_emi:
            # Add data to the table
            app_tables.fin_extends_loan.add_row(
                lender_email_id=lender_email,
                lender_customer_id=lender_id,
                lender_full_name=lender_name,
                loan_id=loan_id,
                borrower_full_name=borrower_name,
                loan_amount=loan_amount,
                borrower_customer_id=customer_id,
                borrower_email_id=email,
                extend_fee=extension_fee,
                emi_number=emi_number,
                final_repayment_amount=finial_repayment,
                extension_amount=extension_amount,
                new_emi=new_emi,
                total_extension_months=loan_extension_months,
                reason=reason,
                status="under process",
                extension_request_date=date
            )
            data[0]['loan_updated_status'] = 'extension'
            # Clear the data after submitting

            self.root_screen.ids.extension_months.text = ""
            self.ids.reason.text = ""
            self.show_validation_errors(
                "Your extension request has been successfully submitted. You will receive a notification once it is approved.")
            # Navigate to DashboardScreen after adding data
            sm = self.manager
            profile = ExtendLoansScreen(name='DashboardScreen')
            sm.add_widget(profile)  # Add the screen to the ScreenManager
            sm.current = 'DashboardScreen'
        else:
            self.show_validation_error("Please fill all the required fields.")

    def show_validation_errors(self, error_message):
        dialog = MDDialog(
            title="Sucessfully Submitted",
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

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Warning",
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

    def on_start(self):
        Window.softinput_mode = "below_target"

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ExtensionLoansProfileScreen'

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


class MyScreenManager(ScreenManager):
    pass

