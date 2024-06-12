import json
import threading
from datetime import datetime, timezone
import anvil.server
from kivy.app import App
from kivy.clock import Clock, mainthread
from kivy.config import value

from kivy.factory import Factory
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import BooleanProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.uix.popup import Popup
from kivy.utils import get_color_from_hex
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDRaisedButton
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

from lender_foreclosure_request import ViewProfileScreenLF
from lender_today_due import ViewProfileTD
from lender_view_extension_request import ViewProfileE, ViewProfileEX
from lender_view_loans_request import ViewLoansProfileScreenRL, ViewLoansProfileScreen, ViewLoansProfileScreenLR

extension_loan_request = """
<WindowManager>:
    Lend_NotificationScreen:
    ExtensionLoansProfileScreen:
    ExtendLoansScreen:

<Lend_NotificationScreen> 
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Notifications"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            title_align: 'center'
        MDScrollView:

            MDList:
                id: container1

<Lend_NotificationViewScreen>
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
                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(30)
                            padding: dp(20)
                            size_hint: 1, 1
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}    
                            MDRaisedButton:
                                text: "Reject"
                                md_bg_color: 194/255, 2/255, 21/255, 1
                                theme_text_color: 'Primary'
                                on_release: app.root.rejected_click(loan_id)
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


class Lend_NotificationScreen(Screen):
    new_notifications = NumericProperty(0)  # Change BooleanProperty to NumericProperty

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.refresh()
        Clock.schedule_interval(self.refresh, 40)

    def refresh(self, *args):
        threading.Thread(target=self.fetch_data).start()

    def fetch_data(self):
        data = app_tables.fin_loan_details.search()
        email = anvil.server.call('another_method')
        profile = app_tables.fin_user_profile.search(email_user=email)

        under_process_loans = []
        approved_loans = []
        under_process_extensions = []
        under_process_foreclosures = []

        for loan in data:
            if loan['loan_updated_status'] == 'under process':
                under_process_loans.append(loan)
            elif loan['loan_updated_status'] == 'approved':
                approved_loans.append(loan)

        extension_data = app_tables.fin_extends_loan.search()
        for extension in extension_data:
            if extension['status'] == 'under process':
                under_process_extensions.append(extension)

        foreclosure_data = app_tables.fin_foreclosure.search()
        for foreclosure in foreclosure_data:
            if foreclosure['status'] == 'under process':
                under_process_foreclosures.append(foreclosure)

        # Schedule UI update on the main thread
        Clock.schedule_once(lambda dt: self.update_ui(under_process_loans, approved_loans, under_process_extensions, under_process_foreclosures))

    @mainthread
    def update_ui(self, under_process_loans, approved_loans, under_process_extensions, under_process_foreclosures):
        self.ids.container1.clear_widgets()

        self.add_loans_to_container(under_process_loans, "")
        self.add_loans_to_container(approved_loans, "is waiting for your loan [b]disbursement[/b].")
        self.add_extensions_to_container(under_process_extensions, "is waiting for loan [b]extension request[/b]")
        self.add_foreclosures_to_container(under_process_foreclosures, "is waiting for loan [b]forclosure[/b] request")

        # Get the count of today's dues
        todays_dues_count = self.add_todays_dues_to_container()

        notification_count = (len(under_process_loans) + len(approved_loans) +
                              len(under_process_extensions) + len(under_process_foreclosures) +
                              todays_dues_count)
        self.new_notifications = notification_count

        # Update notification count on LenderDashBoard screen if it exists
        if self.lender_dashboard:
            self.lender_dashboard.update_notification_count(notification_count)
    def add_loans_to_container(self, loans, message):
        for loan in loans:
            borrower_name = loan['borrower_full_name']
            loan_id = loan['loan_id']
            loan_amount = loan['loan_amount']

            item = TwoLineAvatarIconListItem(
                IconLeftWidget(
                    icon="account"
                ),
                IconRightWidget(
                    icon="chevron-right"
                ),
                text=f"[b]{borrower_name}[/b]",
                secondary_text=message,
                text_color=(0, 0, 0, 1),
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                height=dp(80),
            )

            item.bind(on_release=lambda instance, loan_id=loan_id: self.loan_item_clicked(instance, loan_id))
            self.ids.container1.add_widget(item)

    def add_todays_dues_to_container(self):

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


        today_date = datetime.now(timezone.utc).date()

        b = 1
        k = -1
        due_count = 0
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

            item = ThreeLineAvatarIconListItem(

                IconLeftWidget(
                    icon="calendar-clock"
                ),
                IconRightWidget(
                    icon="chevron-right"
                ),
                text=f"{borrower_name[i]} has an [b]overdue[/b] payment",  # Corrected line
                secondary_text=f"for Rs:{loan_amount_for_id} loan amount in {product_name_for_id} product",
                tertiary_text=f"Day Passed Due Date : {(today_date - shedule_date[loan_id[i]]).days}",
                text_color=(0, 0, 0, 1),  # Black color
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0, 0, 0, 1),
                tertiary_theme_text_color='Custom'
            )
            item.bind(on_release=lambda instance, loan_id=loan_id[i],: self.icon_button_clicked1(instance, loan_id,
                                                                                                shedule_date))
            self.ids.container1.add_widget(item)
            due_count += 1

        return due_count

    def icon_button_clicked1(self, instance, loan_id, shedule_date):
        sm = self.manager

        # Create a new instance of the LoginScreen
        lender_today_due = ViewProfileTD(name='ViewProfileTD')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(lender_today_due)

        # Switch to the LoginScreen
        sm.current = 'ViewProfileTD'
        self.manager.get_screen('ViewProfileTD').initialize_with_value(loan_id, shedule_date)

    def add_foreclosures_to_container(self, foreclosures, message):
        for foreclosure in foreclosures:
            borrower_name = foreclosure['borrower_name']
            loan_id = foreclosure['loan_id']
            now = datetime.now()
            formatted_date = now.strftime("%Y-%m-%d")
            formatted_day = now.strftime("%A")
            loan_status = foreclosure['status']
            loan_amount = foreclosure['loan_amount']
            product_name = foreclosure['product_name']

            message = f"for {loan_amount} loan amount in {product_name} product"
            button_layout = BoxLayout(
                orientation='horizontal',
                size_hint=(None, None),
                size=(dp(200), dp(30)),
                spacing=dp(10),
                pos_hint={'center_x': 0.5, 'center_y': 0.2}
            )

            accept_button = Button(
                text="Accept",
                size_hint=(None, None),
                size=(dp(100), dp(28)),
                background_color=(0, 1, 0, 1),
                color=(1, 1, 1, 1)
            )
            accept_button.bind(on_release=lambda instance, loan_id=loan_id: self.on_accept(loan_id))

            reject_button = Button(
                text="Reject",
                size_hint=(None, None),
                size=(dp(100), dp(28)),
                background_color=(1, 0, 0, 1),
                color=(1, 1, 1, 1)
            )
            reject_button.bind(on_release=lambda instance, loan_id=loan_id: self.on_reject(loan_id))

            button_layout.add_widget(accept_button)
            button_layout.add_widget(reject_button)

            item = ThreeLineAvatarIconListItem(
                IconLeftWidget(
                    icon="account-remove"
                ),
                IconRightWidget(
                    icon="chevron-right"
                ),
                text=f"{borrower_name} has sent a [b]foreclose[/b] request",
                secondary_text=f"for Rs:{loan_amount} loan amount in {product_name} product",
                tertiary_text=" ",
                text_color=(0, 0, 0, 1),
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0.6, 0.6, 0.6, 1),
                tertiary_theme_text_color='Custom',
                height=dp(100),
            )

            item.add_widget(Label())
            item.add_widget(button_layout)
            # Add the buttons layout below the list item

            item.bind(on_release=lambda instance, loan_id=loan_id: self.foreclosure_button_clicked(instance, loan_id))
            self.ids.container1.add_widget(item)

    def on_accept(self, loan_id):
        # Fetch data from both tables
        foreclosure_records = app_tables.fin_foreclosure.search(loan_id=loan_id)
        loan_records = app_tables.fin_loan_details.search(loan_id=loan_id)

        # Check if records exist for the given loan_id in both tables
        if foreclosure_records and loan_records:
            # Extract lender and product data from the first loan record (assuming there's only one matching record)
            lender_customer_id = loan_records[0]['lender_customer_id']
            lender_email_id = loan_records[0]['lender_email_id']
            lender_full_name = loan_records[0]['lender_full_name']
            product_name = loan_records[0]['product_name']

            # Update 'status', 'status_timestamp', lender data, and product name in fin_foreclosure table for each record
            for record in foreclosure_records:
                record['status'] = 'approved'
                record['status_timestamp'] = datetime.now()
                record['lender_customer_id'] = lender_customer_id
                record['lender_email_id'] = lender_email_id
                record['lender_full_name'] = lender_full_name
                record['product_name'] = product_name
                record.update()

            # Update 'loan_updated_status' in fin_loan_details table for each record
            for record in loan_records:
                record['loan_updated_status'] = 'foreclosure'
                record.update()

            self.show_success_dialog('The foreclosure request has been approved successfully.')
            self.manager.add_widget(Factory.DashboardScreenLF(name='DashboardScreenLF'))
            # Switch to the 'DashboardScreenLF' screen
            self.manager.current = 'DashboardScreenLF'
        else:
            print("No data found for loan_id:", loan_id)

    def on_reject(self, loan_id):
        foreclosure_records = app_tables.fin_foreclosure.search(loan_id=loan_id)
        loan_records = app_tables.fin_loan_details.search(loan_id=loan_id)

        if foreclosure_records and loan_records:
            # Extract lender and product data from the first loan record (assuming there's only one matching record)
            lender_customer_id = loan_records[0]['lender_customer_id']
            lender_email_id = loan_records[0]['lender_email_id']
            lender_full_name = loan_records[0]['lender_full_name']
            product_name = loan_records[0]['product_name']

            # Update 'status', 'status_timestamp', lender data, and product name in fin_foreclosure table for each record
            for record in foreclosure_records:
                record['status'] = 'rejected'
                record['status_timestamp'] = datetime.now()
                record['lender_customer_id'] = lender_customer_id
                record['lender_email_id'] = lender_email_id
                record['lender_full_name'] = lender_full_name
                record['product_name'] = product_name
                record.update()

            self.show_reject_dialog('The foreclosure request has been rejected.')
            self.manager.add_widget(Factory.DashboardScreenLF(name='DashboardScreenLF'))
            # Switch to the 'DashboardScreenLF' screen
            self.manager.current = 'DashboardScreenLF'
        else:
            print("No data found for loan_id:", loan_id)

    def show_success_dialog(self, message):
        dialog = MDDialog(
            title="Success",
            text=message,
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

    def show_reject_dialog(self, message):
        dialog = MDDialog(
            title="Rejection",
            text=message,
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

    def foreclosure_button_clicked(self, instance, loan_id):
        # Create an instance of ViewProfileLF screen
        screen = ViewProfileScreenLF(name='ViewProfileScreenLF')
        # Initialize the screen with the loan_id
        screen.initialize_with_value(loan_id, value)

        # Add the screen to the screen manager
        self.manager.add_widget(screen)
        # Switch to the ViewProfileLF screen
        self.manager.current = 'ViewProfileScreenLF'

    def add_extensions_to_container(self, extensions, message):
        for extension in extensions:
            borrower_name = extension['borrower_full_name']
            loan_id = extension['loan_id']
            loan_status = extension['status']
            loan_amount = extension['extension_amount']
            product_name = extension['product_name']


            message = f"for Rs:{loan_amount} loan amount in {product_name} product"
            # Create accept and reject buttons
            accept_button = Button(
                text="Accept",
                size_hint=(None, None),
                size=(dp(100), dp(28)),  # Adjust button size
                background_color=(0, 1, 0, 1),  # Green background
                color=(1, 1, 1, 1)  # White text color
            )
            accept_button.bind(on_release=lambda instance, loan_id=loan_id: self.accept_request(loan_id))

            reject_button = Button(
                text="Reject",
                size_hint=(None, None),
                size=(dp(100), dp(28)),  # Adjust button size
                background_color=(1, 0, 0, 1),  # Red background
                color=(1, 1, 1, 1)  # White text color
            )
            reject_button.bind(on_release=lambda instance, loan_id=loan_id: self.reject_request(loan_id))

            # Create a BoxLayout for buttons
            button_layout = BoxLayout(
                orientation='horizontal',  # Change orientation to horizontal
                size_hint=(None, None),
                size=(dp(200), dp(30)),  # Adjust size of button layout
                spacing=dp(10),  # Adjust spacing between buttons
                pos_hint={'center_x': 0.5, 'center_y': 0.2}  # Position the layout in the middle
            )

            button_layout.add_widget(accept_button)
            button_layout.add_widget(reject_button)

            # Create the ThreeLineAvatarIconListItem with the button layout instead of tertiary text
            item = ThreeLineAvatarIconListItem(
                IconLeftWidget(
                    icon="clock-outline"
                ),
                IconRightWidget(
                    icon="chevron-right"
                ),
                text=f"{borrower_name} has sent a [b]extension[/b] request",
                secondary_text=message,
                tertiary_text=" ",
                text_color=(0, 0, 0, 1),  # Black color
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0.6, 0.6, 0.6, 1),
                tertiary_theme_text_color='Custom',
                height=dp(100),  # Adjust the height of the list item
            )

            # Add the buttons layout and a spacer below the list item
            item.add_widget(Label())  # Add a spacer to separate buttons from secondary text
            item.add_widget(button_layout)  # Add the buttons layout below the list item

            item.bind(on_release=lambda instance, loan_id=loan_id: self.extension_button_clicked(instance, loan_id))
            self.ids.container1.add_widget(item)

    def accept_request(self, loan_id):
        extends_loan_records = app_tables.fin_extends_loan.search(loan_id=loan_id)
        loan_details_records = app_tables.fin_loan_details.search(loan_id=loan_id)

        if extends_loan_records and loan_details_records:
            for extends_loan_record in extends_loan_records:
                extends_loan_record['status'] = 'approved'
                extends_loan_record['status_timestamp'] = datetime.now()  # Store current timestamp
                extends_loan_record['product_name'] = loan_details_records[0]['product_name']  # Retrieve product_name
                extends_loan_record['lender_customer_id'] = (
                    loan_details_records[0]['lender_customer_id'])  # Ensure the value is a string
                extends_loan_record.update()

            for loan_details_record in loan_details_records:
                loan_details_record['loan_updated_status'] = 'extension'
                loan_details_record.update()

            # Show success dialog
            self.show_dialog('Success', 'Request approved successfully!', 'OK', 'NewExtension')
        else:
            print("No data found for loan_id:", loan_id)

    def reject_request(self, loan_id):
        extends_loan_records = app_tables.fin_extends_loan.search(loan_id=loan_id)

        if extends_loan_records:
            for extends_loan_record in extends_loan_records:
                extends_loan_record['status'] = 'rejected'
                extends_loan_record['status_timestamp'] = datetime.now()  # Store current timestamp
                extends_loan_record['product_name'] = extends_loan_records[0]['product_name']  # Retrieve product_name
                extends_loan_record['lender_customer_id'] = (extends_loan_records[0]['lender_customer_id'])
                extends_loan_record.update()

            # Show reject dialog
            self.show_dialog('Reject', 'Request rejected!', 'OK', 'NewExtension')
        else:
            print("No data found for loan_id:", loan_id)

    def show_dialog(self, title, message, button_text, next_screen):
        dialog = MDDialog(
            title=title,
            text=message,
            buttons=[
                MDFlatButton(
                    text=button_text,
                    on_release=lambda x: self.on_dialog_dismiss(dialog, next_screen)
                )
            ]
        )
        dialog.open()

    def on_dialog_dismiss(self, dialog, next_screen):
        dialog.dismiss()
        self.manager.add_widget(Factory.NewExtension(name=next_screen))
        self.manager.current = next_screen

    def on_accept_loan(self, loan_id):
        data = app_tables.fin_loan_details.search()

        borrower_name = None
        loan_entry = None
        for i in data:
            if i['loan_id'] == loan_id:
                borrower_name = i['borrower_full_name']
                loan_entry = i  # Store the loan entry to update

        if loan_entry:  # Check if the loan entry was found
            loan_entry['loan_updated_status'] = 'approved'
            loan_entry['lender_accepted_timestamp'] = datetime.now()  # Store the current date and time

            # Load the email from emails.json
            with open('emails.json') as f:
                emails = json.load(f)
                email = emails.get('email_user')

            # Search for user details in fin_user_profile table
            user_profile = app_tables.fin_user_profile.get(email_user=email)
            if user_profile:
                # Update lender details within the same row
                loan_entry['lender_customer_id'] = user_profile['customer_id']
                loan_entry['lender_full_name'] = user_profile['full_name']
                loan_entry['lender_email_id'] = user_profile['email_user']

            # Perform additional actions if needed

            # Show success dialogue
            self.show_success_dialog(f"{borrower_name} loan approved successfully")
            self.manager.add_widget(Factory.ViewLoansScreen(name='ViewLoansScreen'))
            self.manager.current = 'ViewLoansScreen'
        else:
            # Handle the case where loan_id is not found if necessary
            pass

    def on_reject_loan(self, loan_id):
        data = app_tables.fin_loan_details.search()

        borrower_name = None
        loan_entry = None
        for i in data:
            if i['loan_id'] == loan_id:
                borrower_name = i['borrower_full_name']
                loan_entry = i  # Store the loan entry to update

        if loan_entry:  # Check if the loan entry was found
            loan_entry['loan_updated_status'] = 'rejected'
            loan_entry['lender_rejected_timestamp'] = datetime.now()  # Store the current date and time

            # Load the email from emails.json
            with open('emails.json') as f:
                emails = json.load(f)
                email = emails.get('email_user')

            # Search for user details in fin_user_profile table
            user_profile = app_tables.fin_user_profile.get(email_user=email)
            if user_profile:
                # Update lender details within the same row
                loan_entry['lender_customer_id'] = user_profile['customer_id']
                loan_entry['lender_full_name'] = user_profile['full_name']
                loan_entry['lender_email_id'] = user_profile['email_user']

            # Perform additional actions if needed
            self.show_success_dialog(f"{borrower_name} loan rejected successfully")
            self.manager.add_widget(Factory.ViewLoansScreen(name='ViewLoansScreen'))
            self.manager.current = 'ViewLoansScreen'
        else:
            # Handle the case where loan_id is not found if necessary
            pass

    def show_success_dialog(self, message):
        dialog = MDDialog(
            text=message,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def add_loans_to_container(self, loans, message):
        for loan in loans:
            borrower_name = loan['borrower_full_name']
            loan_id = loan['loan_id']
            loan_status = loan['loan_updated_status']
            loan_amount = loan['loan_amount']
            product_name = loan['product_name']

            if loan_status != 'approved':
                message = f"for Rs:{loan_amount} loan amount in {product_name} product"
                # Design for under process loans
                item = ThreeLineAvatarIconListItem(
                    IconLeftWidget(
                        icon="card-account-details-outline"
                    ),
                    IconRightWidget(
                        icon="chevron-right"
                    ),
                    text=f"{borrower_name} has sent you [b]loan request[/b]",
                    secondary_text=message,
                    tertiary_text=" ",
                    text_color=(0, 0, 0, 1),  # Black color
                    theme_text_color='Custom',
                    secondary_text_color=(0, 0, 0, 1),  # Red color for under process loans
                    secondary_theme_text_color='Custom',
                    tertiary_text_color=(0.6, 0.6, 0.6, 1),
                    tertiary_theme_text_color='Custom',
                    height=dp(100),  # Adjust the height of the list item
                )
            else:
                if loan_status != 'under process':
                    message = f"{borrower_name} is waiting for"
                # Design for approved loans
                item = ThreeLineAvatarIconListItem(
                    IconLeftWidget(
                        icon="card-account-details-outline"
                    ),
                    IconRightWidget(
                        icon="chevron-right"
                    ),
                    text=f"{borrower_name} is waiting for [b]loan disbursement[/b],",
                    secondary_text=f"with an amount of Rs {loan_amount} loan,",
                    tertiary_text=f"intended for {product_name} loan product.",
                    text_color=(0, 0, 0, 1),
                    theme_text_color='Custom',
                    secondary_text_color=(0, 0, 0, 1),
                    secondary_theme_text_color='Custom',
                    tertiary_text_color=(0, 0, 0, 1),
                    tertiary_theme_text_color='Custom',
                    height=dp(100),
                )

            # Create a BoxLayout for buttons only if loan status is not 'approved'
            if loan_status != 'approved':
                button_layout = BoxLayout(
                    orientation='horizontal',  # Change orientation to horizontal
                    size_hint=(None, None),
                    size=(dp(200), dp(30)),  # Adjust size of button layout
                    spacing=dp(10),  # Adjust spacing between buttons
                    pos_hint={'center_x': 0.5, 'center_y': 0.2}  # Position the layout in the middle
                )

                accept_button = Button(
                    text="Accept",
                    size_hint=(None, None),
                    size=(dp(100), dp(28)),  # Adjust button size
                    background_color=(0, 1, 0, 1),  # Green background
                    color=(1, 1, 1, 1)  # White text color
                )
                accept_button.bind(on_release=lambda instance, loan_id=loan_id: self.on_accept_loan(loan_id))

                reject_button = Button(
                    text="Reject",
                    size_hint=(None, None),
                    size=(dp(100), dp(28)),  # Adjust button size
                    background_color=(1, 0, 0, 1),  # Red background
                    color=(1, 1, 1, 1)  # White text color
                )
                reject_button.bind(on_release=lambda instance, loan_id=loan_id: self.on_reject_loan(loan_id))

                button_layout.add_widget(accept_button)
                button_layout.add_widget(reject_button)

                item.add_widget(Label())  # Add a spacer to separate buttons from secondary text
                item.add_widget(button_layout)  # Add the buttons layout below the list item

            item.bind(
                on_release=lambda instance, loan_id=loan_id, loan_status=loan_status: self.icon_button_clicked(instance,
                                                                                                               loan_id,
                                                                                                               loan_status))
            self.ids.container1.add_widget(item)

    def icon_button_clicked(self, instance, loan_id, loan_status):
        data = app_tables.fin_loan_details.search()
        loan_status = None
        for loan in data:
            if loan['loan_id'] == loan_id:
                loan_status = loan['loan_updated_status']
                break

        sm = self.manager
        if loan_status == 'under process':
            screen = ViewLoansProfileScreen(name='ViewLoansProfileScreen')
            sm.add_widget(screen)
            sm.current = 'ViewLoansProfileScreen'
            self.manager.get_screen('ViewLoansProfileScreen').initialize_with_value(loan_id, data)
        elif loan_status == 'approved':
            self.manager.add_widget(Factory.ViewLoansProfileScreenLR(name='ViewLoansProfileScreenLR'))
            sm.current = 'ViewLoansProfileScreenLR'
            self.manager.get_screen('ViewLoansProfileScreenLR').initialize_with_value(loan_id, data)

    def extension_button_clicked(self, instance, loan_id):
        # Create an instance of ViewProfileE screen
        screen = ViewProfileE(name='ViewProfileE')
        # Initialize the screen with the loan_id
        screen.initialize_with_value(loan_id)
        # Add the screen to the screen manager
        self.manager.add_widget(screen)
        # Switch to the ViewProfileE screen
        self.manager.current = 'ViewProfileE'

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
        self.manager.current = 'LenderDashboard'

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"


class Lend_NotificationViewScreen(Screen):
    def initialize_with_value(self, value, data):
        emi1 = app_tables.fin_emi_table.search()
        profile = app_tables.fin_user_profile.search()
        profile_customer_id = [i['customer_id'] for i in profile]
        profile_mobile_number = [i['mobile'] for i in profile]
        loan_id = [i['loan_id'] for i in data]
        product = app_tables.fin_product_details.search()
        loan_details = {i['loan_id']: (
            i['borrower_customer_id'], i['loan_amount'], i['tenure'], i['product_name'], i['interest_rate'],
            i['lender_full_name']) for i in data}
        if value in loan_details:
            borrower_customer_id, loan_amount, tenure, product_name, interest_rate, lender_name = loan_details[value]

            if borrower_customer_id in profile_customer_id:
                number = profile_customer_id.index(borrower_customer_id)
                self.ids.number.text = str(profile_mobile_number[number])
            else:
                number = 0
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

    def rejected_click(self, loan_id):
        data = app_tables.fin_loan_details.search()
        borrower_name = None  # Initialize borrower_name to None
        print(loan_id)
        print(borrower_name)
        loan_idlist = [i['loan_id'] for i in data]  # Create a list of loan IDs from the data

        if loan_id in loan_idlist:  # Check if the loan ID exists in loan_idlist
            for i in data:
                if i['loan_id'] == loan_id:
                    borrower_name = i['borrower_full_name']  # Get borrower name for this loan ID
            index = loan_idlist.index(loan_id)
            data[index]['loan_updated_status'] = 'rejected'
            sm = self.manager
            disbursed = ViewLoansProfileScreenRL(name='ViewLoansProfileScreenRL')
            sm.add_widget(disbursed)
            sm.current = 'ViewLoansProfileScreenRL'
            self.manager.get_screen('ViewLoansProfileScreenRL').initialize_with_value(loan_id, data)
            self.show_success_dialog(f"{borrower_name} Loan is Rejected")
            return
        else:
            pass

    def approved_click(self, loan_id):
        data = app_tables.fin_loan_details.search()
        borrower_name = None  # Initialize borrower_name to None
        print(loan_id)
        print(borrower_name)
        loan_idlist = [i['loan_id'] for i in data]  # Create a list of loan IDs from the data

        if loan_id in loan_idlist:  # Check if the loan ID exists in loan_idlist
            for i in data:
                if i['loan_id'] == loan_id:
                    borrower_name = i['borrower_full_name']  # Get borrower name for this loan ID
            index = loan_idlist.index(loan_id)
            data[index]['loan_updated_status'] = 'approved'
            sm = self.manager
            disbursed = ViewLoansProfileScreenRL(name='ViewLoansProfileScreenRL')
            sm.add_widget(disbursed)
            sm.current = 'ViewLoansProfileScreenRL'
            self.manager.get_screen('ViewLoansProfileScreenRL').initialize_with_value(loan_id, data)
            self.show_success_dialog(f"{borrower_name} Loan is Approved")
        else:
            pass

    def show_success_dialog(self, text, loan_id):
        dialog = MDDialog(
            text=text,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *args: self.rejected_screen(dialog, loan_id),
                    theme_text_color="Custom",
                    text_color=(0.043, 0.145, 0.278, 1),
                )
            ]
        )
        dialog.open()

    def show_success_dialog1(self, text, loan_id):
        dialog = MDDialog(
            text=text,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *args: self.approved_screen(dialog, loan_id),
                    theme_text_color="Custom",
                    text_color=(0.043, 0.145, 0.278, 1),
                )
            ]
        )
        dialog.open()

    def approved_screen(self, dialog, loan_id):
        dialog.dismiss()
        self.manager.current = 'ViewLoansProfileScreenLR'
        self.approved_click(loan_id)

    def rejected_screen(self, dialog, loan_id):
        dialog.dismiss()
        self.manager.current = 'ViewLoansRequest'
        self.rejected_click(loan_id)

    def on_back_button_press(self):
        self.manager.current = 'Lend_NotificationScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'NotificationScreen'

    def on_text_validate(self, instance):
        extension_months = instance.text
        if not extension_months.isdigit() or int(extension_months) <= 1:
            self.show_popup("Please enter a valid number of extension months.")
            instance.text = ''

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

