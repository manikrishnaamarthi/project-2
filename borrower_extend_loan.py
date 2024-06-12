from datetime import datetime, timezone
import anvil.server
from kivy.config import value
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import *
from kivy.lang import Builder
from datetime import datetime
from kivy.core.window import Window
import anvil.users
import server
from anvil.tables import app_tables
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager

extension_loan_request = """
<WindowManager>:
    ExtensionLoansRequest:
    ExtensionLoansProfileScreen:
    ExtendLoansScreen:

<ExtensionLoansRequest> 
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Extension Loan Request"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            title_align: 'center'
        MDScrollView:

            MDList:
                id: container1

<ExtensionLoansProfileScreen>
    GridLayout:
        cols: 1
        MDTopAppBar:
            title: "Extension Loan Request"
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
                        cols: 1
        
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
        
                        MDLabel:
                            id: loan_amount
                            halign: 'left'
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True
                    MDLabel:
                        text: ''
                        halign: 'left'
                        size_hint_y: None
                        height: dp(20)

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
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Phone Number" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: number
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Product Name" 
                            halign: "left"
                            bold: True
                        MDLabel:
                            id: product_name
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Loan Tenure" 
                            bold: True
                            halign: "left"
                        MDLabel:
                            id: tenure
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Interest Rate (%)" 
                            bold: True
                            halign: "left"
                        MDLabel:
                            id: interest
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Extension Fee(%)" 
                            bold: True
                            halign: "left"
                        MDLabel:
                            id: extension_fee
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Extension Allowed"
                            bold: True
                            halign: "left"
                        MDLabel:
                            id: extension_allowed
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
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
                    
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Extension Months" 
                            bold: True
                            halign: "left"
                        MDTextField:
                            hint_text: ""
                            id: extension_months
                            halign: "left"
                            input_type: 'number'
                            on_touch_down: root.on_extension_months()
                    MDLabel:
                        text: ''
                        halign: 'left'
                        size_hint_y: None
                        height: dp(25)
                MDLabel:
                    text: ''
                    halign: 'left'
                    size_hint_y: None
                    height: dp(5)
                BoxLayout:
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
                        id:extension_request
                        text: "Extension Request"
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        font_name: "Roboto-Bold"
                        size_hint: 0.4, None
                        height: dp(50)
                        on_release:root.on_extend()
                        text: "Next"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        font_size:dp(15)


<ExtendLoansScreen>
    GridLayout:
        cols: 1
        MDTopAppBar:
            title: "Extension Loan Request"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            title_align: 'center'

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
                        cols: 3
                        MDIconButton:
                            icon: 'currency-inr'
                            halign: 'left'
                            size_hint_y: None
                            height: dp(1)
                            bold: True

                        MDLabel:
                            id: loan_amount
                            halign: 'left'
                            text_color: 0,0,0,1
                            bold: True
                        MDLabel:
                            id: loan_id
                            color:1,1,1,1      
                            font_size:dp(1)
                            text: "" 
                            height:dp(1)
                    MDLabel:
                        text: ''
                        halign: 'left'
                        size_hint_y: None
                        height: dp(2)
                            
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Extension Fee(%)" 
                            bold: True
                            halign: "left"
                        MDLabel:
                            id: extension_fee
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDLabel:
                        text: ''
                        halign: 'left'
                        size_hint_y: None
                        height: dp(2)
                            
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Extension Amount" 
                            bold: True
                            halign: "left"
                        MDLabel:
                            id: extension_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            
                    MDLabel:
                        text: ''
                        halign: 'left'
                        size_hint_y: None
                        height: dp(2)
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Finial Repayment Amount" 
                            bold: True
                            halign: "left"
                        MDLabel:
                            id: finial_repayment_amount
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                    MDLabel:
                        text: ''
                        halign: 'left'
                        size_hint_y: None
                        height: dp(2)        
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "New EMI"
                            bold: True
                            halign: "left"
                        MDLabel:
                            id: new_emi
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1
                            
                MDLabel:
                    text: ""
                    size_hint_y: None
                    height: dp(65)
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: "75dp"
                    spacing:dp(15)
                    padding: dp(20)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    MDLabel:
                        text: "Reason For Extended Loan" 
                        bold: True
                        halign: 'left'
                    MDTextField:
                        id : reason
                        hint_text: ""
                        halign: 'left' 
                        theme_text_color: 'Custom'  
                        text_color: 140/255, 140/255, 140/255, 1

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: "68dp"
                    spacing:dp(15)
                    padding: dp(20)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    MDCheckbox:
                        id: check
                        size_hint: None, None
                        size: "30dp", "30dp"
                        bold: True
                        active: False
                        on_active: root.on_checkbox_active(self, self.active)
                    MDLabel:
                        text: "I Agree Terms and Conditions"
                        multiline: False  
                        size: "30dp", "30dp"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1
                        halign: "left"
                        valign: "center" 
                        on_touch_down: app.root.get_screen("ExtendLoansScreen").show_terms_dialog() if self.collide_point(*args[1].pos) else None   
                                                
                BoxLayout:
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

class ExtensionLoansRequest(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = app_tables.fin_loan_details.search()
        email = anvil.server.call('another_method')
        profile = app_tables.fin_user_profile.search(email_user=email)
        customer_id = []
        loan_id = []
        loan_amount = []
        borrower_name = []
        loan_status = []
        tenure = []
        product_name = []
        email1 = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])
            tenure.append(i['tenure'])
            product_name.append(i['product_name'])
            email1.append(i['borrower_email_id'])
        product = app_tables.fin_product_details.search()
        extension_allowed = []
        extension_fee = []
        for i in product:
            extension_allowed.append(i['extension_allowed'])
            extension_fee.append(i['extension_fee'])
        profile_customer_id = []
        profile_mobile_number = []
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
            for i in range(s):
                c += 1
                if loan_status[c] == 'disbursed' and customer_id[c] == cos_id :
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

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreen'

    def refresh(self):
        self.ids.container1.clear_widgets()
        self.__init__()

    def icon_button_clicked(self, instance, loan_id):
        print(loan_id)
        data = app_tables.fin_loan_details.search()  # Fetch data here
        loan_status = None
        for loan in data:
            if loan['loan_id'] == loan_id:
                loan_status = loan['loan_updated_status']
                break

        if loan_status == 'disbursed':
            # Open the screen for approved loans
            sm = self.manager
            disbursed = ExtensionLoansProfileScreen(name='ExtensionLoansProfileScreen')
            sm.add_widget(disbursed)
            sm.current = 'ExtensionLoansProfileScreen'
            self.manager.get_screen('ExtensionLoansProfileScreen').initialize_with_value(loan_id, data)
        else:
            pass

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreen'

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"


class ExtensionLoansProfileScreen(Screen):
    def initialize_with_value(self, value, data):
        emi1 = app_tables.fin_emi_table.search()
        profile = app_tables.fin_user_profile.search()
        extension_months = ''
        profile_customer_id = [i['customer_id'] for i in profile]
        profile_mobile_number = [i['mobile'] for i in profile]
        loan_id = [i['loan_id'] for i in data]
        product = app_tables.fin_product_details.search()
        extension_details = {i['product_name']: (i['extension_allowed'], i['extension_fee'], i['min_extension_months'])
                             for i in product}

        loan_details = {i['loan_id']: (
            i['borrower_customer_id'], i['loan_amount'], i['tenure'], i['product_name'], i['interest_rate'],
            i['borrower_full_name']) for i in data}
        if value in loan_details:
            borrower_customer_id, loan_amount, tenure, product_name, interest_rate, borrower_name = loan_details[value]
            extension_allowed, extension_fee, product_id = extension_details.get(product_name, ('No', 0, None))

            # Check if the borrower's customer ID is in the profile customer ID list
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
            self.ids.extension_allowed.text = str(extension_allowed)
            try:
                extension_fee = float(extension_fee)
            except ValueError:
                extension_fee = 0
                # Now you can assign extension_fee_display to the corresponding text field in your UI
            self.ids.extension_fee.text = str(extension_fee)
            self.ids.name.text = str(borrower_name)
            self.ids.extension_months.text = str(extension_months)

            # Check if the button exists in ids before accessing its attributes
            if extension_allowed == 'Yes':
                self.ids.extension_request.disabled = False
            else:
                self.show_popup("Your extension is not allowed")
                self.ids.extension_request.disabled = True

            emi_loan = [i for i in emi1 if i['loan_id'] == value]
            print(emi_loan)

            # Sort the emi_loan list based on the payment date in descending order
            if emi_loan:
                sorted_emi_loan = sorted(emi_loan,
                                         key=lambda x: datetime.strptime(x['next_payment'].isoformat(), '%Y-%m-%d') if
                                         x['next_payment'] is not None else datetime.min, reverse=True)
            else:
                sorted_emi_loan = []

            if sorted_emi_loan:
                latest_emi_number = sorted_emi_loan[0]['emi_number']
                minimum_months = [i['min_extension_months'] for i in product if i['product_name'] == product_name]
                print(minimum_months)
                if minimum_months:
                    minimum_months = minimum_months[0]
                    if latest_emi_number >= minimum_months:
                        self.ids.extension_request.disabled = False
                    else:
                        self.ids.extension_request.disabled = True
                else:
                    self.ids.extension_request.disabled = True
                    print("Minimum extension months not found.")
                # Display the total payment
                self.ids.total_payment.text = str(latest_emi_number)
            else:
                # Handle the case where sorted_emi_loan is empty
                self.ids.extension_request.disabled = True
                print("No emi_loan found.")

    def show_popup(self, error_message):
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

    def on_extension_months(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.extension_months.input_type = 'number'

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ExtensionLoansRequest'

    def on_back_button_press(self):
        self.manager.current = 'ExtensionLoansRequest'

    def on_extend(self):
        extension_months = self.ids.extension_months.text
        if extension_months.isdigit():
            extension_months = int(extension_months)
            if 1 < extension_months <= 6:
                # Proceed to the next screen
                loan_id = self.ids.loan_id.text
                extension_fee = self.ids.extension_fee.text
                sm = self.manager
                profile = ExtendLoansScreen(name='ExtendLoansScreen')
                sm.add_widget(profile)  # Add the screen to the ScreenManager
                sm.current = 'ExtendLoansScreen'
            else:
                # Show error message if extension months are not between 0 and 6
                self.show_popup( "Please enter a number between 1 and 6.")
        else:
            # Show error message if extension months is not a valid positive integer
            self.show_popup( "Please enter extension months.")

    def on_text_validate(self, instance):
        extension_months = instance.text
        if not extension_months.isdigit() or int(extension_months) <= 1:
            self.show_popup( "Please enter a valid number of extension months.")
            # Clear the invalid value from the field
            instance.text = ''

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
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
            self.show_validation_error( "EMI number not found for the loan")
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
            lender_id=data[0]['lender_customer_id']
            lender_email=data[0]['lender_email_id']
            lender_name=data[0]['lender_full_name']
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
            data[0]['loan_updated_status']='extension'
            # Clear the data after submitting

            self.root_screen.ids.extension_months.text = ""
            self.ids.reason.text = ""
            self.show_validation_errors("Your extension request has been successfully submitted. You will receive a notification once it is approved.")
            # Navigate to DashboardScreen after adding data
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
            sm = self.manager
            profile = ExtendLoansScreen(name='DashboardScreen')
            sm.add_widget(profile)  # Add the screen to the ScreenManager
            sm.current = 'DashboardScreen'
        else:
            self.show_validation_error("Please fill all the required fields.")
    def show_validation_errors(self,error_message):
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

