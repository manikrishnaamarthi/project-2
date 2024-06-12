from anvil.tables import app_tables
from kivy import platform
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
import sqlite3
from kivy.factory import Factory
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget
import anvil.server

application_tracker = """

<WindowManager>:
    ApplicationTrackerScreen:

<ALLLoansAPT>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Application Tracker "
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container 

<ApplicationTrackerScreen>
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDTopAppBar:
            title: "Application status"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.borrower_dashboard()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)

            MDLabel:
                text: 'Application Received'
                font_size: dp(20)
                bold: True
                size_hint_y: None
                height: 5

            MDLabel:
                text: "Congratulations! Your loan application with P2P has been received. Please wait while we process the loan. You can check the status here"
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
                    text: "Application for #product_name Product Loan sent"
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
                    text: "Loan is approved "
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
                    text: "Loan has been disbursed"
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
                    text: "Loan is credited to a/c: xxxxxxxxxxx"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height:dp(50)


"""
Builder.load_string(application_tracker)


class ApplicationTrackerScreen(Screen):
    def initialize_with_value(self, value, data):
        email = self.get_table()
        profile = app_tables.fin_user_profile.search()
        print(value)
        loan_id = []
        loan_amount = []
        loan_status = []
        product_name = []

        for i in data:
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            loan_status.append(i['loan_updated_status'])
            product_name.append(i['product_name'])
        profile_email_id = []
        profile_account_number = []

        for i in profile:
            profile_email_id.append(i['email_user'])
            profile_account_number.append(i['account_number'])

        index1 = -1  # Initialize index1 to a default value

        if email in profile_email_id:
            index1 = profile_email_id.index(email)

        if value in loan_id:
            index = loan_id.index(value)
            print(f"Loan Status: {loan_status[index]}")
            print(f"Processing loan with ID {value}")
            if loan_status[index] == 'under process':
                print('under process')
                self.ids.icon1.icon = 'circle-slice-8'
                self.ids.label1.theme_text_color = "Custom"
                self.ids.label1.text_color = 0, 0, 0, 1
                self.ids.label1.bold = True
                self.ids.icon3.icon = 'checkbox-blank-circle-outline'
                self.ids.label3.theme_text_color = "Custom"
                self.ids.label3.text_color = 0.043, 0.145, 0.278, 1
                self.ids.label3.bold = False
                self.ids.icon4.icon = 'checkbox-blank-circle-outline'
                self.ids.label4.theme_text_color = "Custom"
                self.ids.label4.text_color = 0.043, 0.145, 0.278, 1
                self.ids.label4.bold = False
                self.ids.icon5.icon = 'checkbox-blank-circle-outline'
                self.ids.label5.theme_text_color = "Custom"
                self.ids.label5.text_color = 0.043, 0.145, 0.278, 1
                self.ids.label5.bold = False
                self.ids.label1.text = f"Application for {product_name[index]} product loan sent"

            elif loan_status[index] == 'approved':
                self.ids.icon1.icon = 'circle-slice-8'
                self.ids.label1.theme_text_color = "Custom"
                self.ids.label1.text_color = 0, 0, 0, 1
                self.ids.label1.bold = True
                self.ids.label1.text = f"Application for {product_name[index]} product loan sent"
                self.ids.icon3.icon = 'circle-slice-8'
                self.ids.label3.theme_text_color = "Custom"
                self.ids.label3.text_color = 0, 0, 0, 1
                self.ids.label3.text = f'Loan is approved for ₹{loan_amount[index]:.2f}'
                self.ids.label3.bold = True
                self.ids.icon4.icon = 'checkbox-blank-circle-outline'
                self.ids.label4.theme_text_color = "Custom"
                self.ids.label4.text_color = 0.043, 0.145, 0.278, 1
                self.ids.label4.bold = False
                self.ids.icon5.icon = 'checkbox-blank-circle-outline'
                self.ids.label5.theme_text_color = "Custom"
                self.ids.label5.text_color = 0.043, 0.145, 0.278, 1
                self.ids.label5.bold = False
            elif loan_status[index] == 'disbursed':
                self.ids.icon1.icon = 'circle-slice-8'
                self.ids.label1.theme_text_color = "Custom"
                self.ids.label1.text_color = 0, 0, 0, 1
                self.ids.label1.bold = True
                self.ids.label1.text = f"Application for {product_name[index]} product loan sent"
                self.ids.icon3.icon = 'circle-slice-8'
                self.ids.label3.theme_text_color = "Custom"
                self.ids.label3.text_color = 0, 0, 0, 1
                self.ids.label3.text = f'Loan is approved for ₹{loan_amount[index]:.2f}'
                self.ids.label3.bold = True
                self.ids.icon4.icon = 'circle-slice-8'
                self.ids.label4.theme_text_color = "Custom"
                self.ids.label4.text_color = 0, 0, 0, 1
                self.ids.label4.text = f"{product_name[index]} product loan has been disbursed"
                self.ids.label4.bold = True
                self.ids.icon5.icon = 'circle-slice-8'
                self.ids.label5.text = f"Loan credited to a/c {profile_account_number[index1]}"
                self.ids.label5.theme_text_color = "Custom"
                self.ids.label5.text_color = 0, 0, 0, 1
                self.ids.label5.bold = True
            elif loan_status[index] == 'rejected':
                self.ids.icon1.icon = 'circle-slice-8'
                self.ids.label1.theme_text_color = "Custom"
                self.ids.label1.text_color = 0, 0, 0, 1
                self.ids.label1.bold = True
                self.ids.label1.text = f"Application Rejected"
                self.ids.icon3.icon = 'cancel'
                self.ids.label3.theme_text_color = "Custom"
                self.ids.label3.text_color = 0, 0, 0, 1
                self.ids.label3.text = f'Loan is Rejected ₹{loan_amount[index]:.2f}'
                self.ids.label3.bold = True
                self.ids.icon4.icon = 'checkbox-blank-circle-outline'
                self.ids.label4.theme_text_color = "Custom"
                self.ids.label4.text_color = 0.043, 0.145, 0.278, 1
                self.ids.label4.bold = False
                self.ids.icon5.icon = 'checkbox-blank-circle-outline'
                self.ids.label5.theme_text_color = "Custom"
                self.ids.label5.text_color = 0.043, 0.145, 0.278, 1
                self.ids.label5.bold = False

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

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
        self.manager.current = 'DashboardScreen'

    def borrower_dashboard(self):
        self.manager.current = 'ALLLoansAPT'


class ALLLoansAPT(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = app_tables.fin_loan_details.search()
        email = self.get_table()
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        loan_id = []
        email1 = []
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
            email1.append(i['borrower_email_id'])

        profile_customer_id = []
        profile_mobile_number = []
        profile_email_id = []
        profile_account_number = []

        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            profile_email_id.append('email_user')
            profile_account_number.append('account_number')
        cos_id = None
        index = -1
        if email in profile_email_id:
            index = profile_email_id.index(email)

        if email in email1:
            index = email1.index(email)
            cos_id = customer_id[index]

        if cos_id is not None:
            print(cos_id, type(cos_id))
            print(customer_id[-1], type(customer_id[-1]))
            c = -1
            index_list = []
            for i in range(s):
                c += 1
                if customer_id[c] == cos_id:
                    index_list.append(c)

            b = 1
            k = -1
            for i in reversed(index_list):
                b += 1
                k += 1
                number = profile_customer_id.index(customer_id[i])
                item = ThreeLineAvatarIconListItem(

                    IconLeftWidget(
                        icon="card-account-details-outline"
                    ),
                    text=f"Borrower Name : {borrower_name[i]}",
                    secondary_text=f"Mobile Number : {profile_mobile_number[number]}",
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
        # Highlight the selected item
        self.highlight_item(instance)

        data = app_tables.fin_loan_details.search()  # Fetch data here
        loan_status = None
        for loan in data:
            if loan['loan_id'] == loan_id:
                loan_status = loan['loan_updated_status']
                break

        sm = self.manager

        # Create a new instance of the ApplicationTrackerScreen
        approved = ApplicationTrackerScreen(name='ApplicationTrackerScreen')

        # Add the ApplicationTrackerScreen to the existing ScreenManager
        sm.add_widget(approved)

        # Switch to the ApplicationTrackerScreen
        sm.current = 'ApplicationTrackerScreen'
        self.manager.get_screen('ApplicationTrackerScreen').initialize_with_value(loan_id, data)

    def highlight_item(self, item):
        # Deselect all other items
        self.deselect_items()

        # Change the background color of the clicked item to indicate selection
        item.bg_color = (0.5, 0.5, 0.5, 1)  # Change color as desired
        self.selected_item = item

    def deselect_items(self):
        # Deselect all items in the list
        for item in self.ids.container.children:
            if isinstance(item, ThreeLineAvatarIconListItem):
                item.bg_color = (1, 1, 1, 1)  # Reset background color for all items

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def refresh(self):
        self.ids.container.clear_widgets()
        self.__init__()

    def go_back(self):
        self.manager.current = 'DashboardScreen'


class WindowManager(ScreenManager):
    pass
