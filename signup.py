import re
import bcrypt
from anvil.tables import app_tables
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivymd.app import MDApp
import sqlite3
from kivymd.uix.label import MDLabel
from tables import create_user_table, create_registration_table
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from dashboard import DashScreen
import anvil.server
from datetime import datetime, timedelta, timezone
from kivymd.uix.spinner import MDSpinner
from kivy.factory import Factory
from login import LoginScreen

KV = """
<WindowManager>:
    SignupScreen:

<SignupScreen>:
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_y": .95}
        user_font_size: "30sp"
        theme_text_color: "Custom"
        text_color: rgba(26, 24, 58, 255)
        on_release: root.go_back()

    BoxLayout:
        orientation: "vertical"
        padding: dp(45)
        spacing: dp(5)

        MDLabel:
            text: "Create new account"
            font_name: "Roboto"
            font_size: "18sp"
            color: rgba(0, 0, 0, 255)
            halign: 'center'
            bold: True

        MDTextField:
            id: name
            hint_text: 'Enter full name'
            multiline: False
            helper_text: 'Enter a valid name'
            helper_text_mode: 'on_focus'
            icon_left: 'account'
            hint_text_color: 0, 0, 0, 1
            hint_text_color_normal: "black"
            text_color_normal: "black"
            helper_text_color_normal: "black"
            font_name: "Roboto-Bold"
            pos_hint: {'center_y': 0.1}

        MDTextField:
            id: mobile
            hint_text: 'Enter mobile number'
            multiline: False
            helper_text: 'Enter a valid number'
            helper_text_mode: 'on_focus'
            icon_left: 'cellphone'
            font_name: "Roboto-Bold"
            hint_text_color: 0, 0, 0, 1
            hint_text_color_normal: "black"
            text_color_normal: "black"
            helper_text_color_normal: "black"
            input_type: 'number'  
            on_touch_down: root.on_mobile_number_touch_down()

        MDTextField:
            id: email
            hint_text: 'Enter your email'
            multiline: False
            helper_text: 'Enter a valid email'
            helper_text_mode: 'on_focus'
            icon_left: 'email'
            hint_text_color: 0, 0, 0, 1
            hint_text_color_normal: "black"
            text_color_normal: "black"
            helper_text_color_normal: "black"
            font_name: "Roboto-Bold"

        MDTextField:
            id: password
            hint_text: "Enter Your Password"
            icon_left: 'lock-outline'
            helper_text_mode: 'on_focus'
            hint_text_color: 0, 0, 0, 1
            hint_text_color_normal: "black"
            text_color_normal: "black"
            helper_text_color_normal: "black"
            multiline: False
            helper_text: "Password must be greater than 8 characters"
            password: True
            font_name: "Roboto-Bold"

        MDTextField:
            id: password2
            hint_text: "Re-Enter Your Password"
            helper_text: "Password does not match"
            helper_text_mode: 'on_focus'
            icon_left: 'lock-outline'
            password: True
            hint_text_color: 0, 0, 0, 1
            hint_text_color_normal: "black"
            text_color_normal: "black"
            helper_text_color_normal: "black"
            font_name: "Roboto-Bold"

        BoxLayout:
            orientation: 'horizontal'
            width: "260dp"
            height: "10dp"
            MDCheckbox:
                id: terms_checkbox
                size_hint_x: None
                width: "20dp"
            MDLabel:
                text: "Terms and Conditions"
                theme_text_color: 'Custom'
                text_color: 6/255, 143/255, 236/255, 1
                halign: 'left'
                font_size: dp(10)
                valign: 'center'
                on_touch_down: app.root.get_screen("SignupScreen").show_terms_dialog() if self.collide_point(*args[1].pos) else None

        BoxLayout:
            orientation: 'horizontal'
            width: "260dp"
            height: "10dp"
            MDCheckbox:
                id: kyc_checkbox
                size_hint_x: None
                width: "20dp"
            MDLabel:
                text: "I authorize the company to fetch my KYC details via the Central KYC(CKYC) Registry"
                theme_text_color: 'Primary'
                font_size: dp(10)
                halign: 'left'
                valign: 'center'


        GridLayout:
            cols: 1
            spacing: dp(30)
            padding: dp(20)
            size_hint: 1, None
            height: "50dp"  # Adjust the height to accommodate both sections
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDRaisedButton:
                text: "Signup"
                on_release: root.go_to_login()
                md_bg_color: 0.043, 0.145, 0.278, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"
        
        MDLabel:
            text: ""  # Add an empty label for spacing
        
        BoxLayout:
            id:box1
            orientation: 'horizontal'
            size_hint: None, None
            width: "190dp"
            height: "15dp"
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}
    
            MDFlatButton:
                text: "Already have an account? [color=#0699FF]Sign In[/color]"
                font_name: "Roboto"
                font_size: dp(14)
                markup: True
                theme_text_color: 'Secondary'
                halign: 'left'
                height: "50dp"
                text_color: 0.043, 0.145, 0.278, 1
                on_release: root.go_to_signin()
                

"""


class SignupScreen(Screen):
    Builder.load_string(KV)
    create_user_table()
    create_registration_table()

    def go_to_signin(self):
        self.manager.add_widget(Factory.LoginScreen(name='LoginScreen'))
        self.manager.current = 'LoginScreen'
    def on_mobile_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mobile.input_type = 'number'

    def save_to_database(self):

        try:
            # Connect to the SQLite database
            conn = sqlite3.connect("fin_user.db")
            cursor = conn.cursor()

            cursor.execute('SELECT user_id FROM fin_users ORDER BY user_id DESC LIMIT 1')
            latest_user_id = cursor.fetchone()

            c_id = app_tables.fin_user_profile.search()
            id_c = []

            for i in c_id:
                id_c.append(i['customer_id'])

            if id_c:
                last_customer_id = id_c[-1]
                if isinstance(last_customer_id, dict) and 'customer_id' in last_customer_id:
                    user_id = last_customer_id['customer_id'] + 1
                else:
                    user_id = 100000 + len(id_c)
            else:
                user_id = 100000

            if latest_user_id is not None:
                next_user_id = latest_user_id[0] + 1
            else:
                next_user_id = user_id

            hash_pashword = bcrypt.hashpw(self.ids.password.text.encode('utf-8'), bcrypt.gensalt())
            hash_pashword = hash_pashword.decode('utf-8')

            cursor.execute('''
                INSERT INTO fin_users (
                    user_id, fullname, email, mobile_number, password, confirm_password,
                    accept_terms, authorize_kyc
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                next_user_id,
                self.ids.name.text, self.ids.email.text, self.ids.mobile.text,
                hash_pashword, hash_pashword,
                "Accepted" if self.ids.terms_checkbox.active else "Rejected",
                "Accepted" if self.ids.kyc_checkbox.active else "Rejected"
            ))

            conn.commit()
            cursor.execute('''INSERT INTO fin_registration_table (customer_id) VALUES (?)''', (next_user_id,))

            self.add_data(user_id=user_id, email=self.ids.email.text, password=hash_pashword,
                          name=self.ids.name.text, number=self.ids.mobile.text, enable=True)
            self.wallet_generator(self.ids.email.text, self.ids.name.text, user_id)
            conn.commit()
        except sqlite3.Error as e:

            print(f"SQLite error: {e}")

    def add_data(self, user_id, email, password, name, number, enable):
        approved_date = datetime.now()
        # Ensure 'YOUR_ANVIL_UPLINK_KEY' is replaced with your actual Anvil Uplink key
        app_tables.users.add_row(email=email, password_hash=password, enabled=enable, signed_up=approved_date)
        app_tables.fin_user_profile.add_row(customer_id=user_id, email_user=email, full_name=name,
                                            mobile=number)
        app_tables.fin_guarantor_details.add_row(customer_id=user_id)

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

    def go_to_login(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="25sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_signup_action(modal_view), 2)

    def perform_signup_action(self, modal_view):
        # Close the modal view after
        modal_view.dismiss()
        name = self.ids.name.text
        mobile = self.ids.mobile.text
        email = self.ids.email.text
        password = self.ids.password.text
        password2 = self.ids.password2.text
        terms_checkbox = self.ids.terms_checkbox
        kyc_checkbox = self.ids.kyc_checkbox
        # Validation errors list
        validation_errors = []

        # Regular expression for email validation
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        # Check for existing email in the database
        conn = sqlite3.connect("fin_user.db")
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM fin_users
            WHERE email = ?
        ''', (email,))
        existing_user = cursor.fetchone()

        # Check if the email already exists in the database
        c_id = app_tables.fin_user_profile.search()

        anvil_email = []
        for i in c_id:
            anvil_email.append(i['email_user'])

        # Other input validations
        if not name or len(name.split()) < 2 or not re.match(r'^[a-zA-Z\s]+$', name):
            validation_errors.append(
                (self.ids.name, "Please enter a valid first name and last name"))
        else:
            self.ids.name.helper_text = ''

        # Mobile number validation
        if not mobile or not (len(mobile) == 10 or len(mobile) == 12) or not mobile.startswith(('6', '7', '8', '9')):
            validation_errors.append((self.ids.mobile, "Invalid mobile number"))
        else:
            self.ids.mobile.helper_text = ''

        # Email validation
        if not email or not re.match(email_regex, email):
            validation_errors.append((self.ids.email, "Invalid email address"))
        elif email in anvil_email:
            validation_errors.append((self.ids.email, "Email already exists"))
        elif existing_user:
            validation_errors.append((self.ids.email, "Email already exists"))
        else:
            self.ids.email.helper_text = ''

        # Password validation
        if not password or not self.is_strong_password(password):
            validation_errors.append((self.ids.password, "Please set a strong password"))
        else:
            self.ids.password.helper_text = ''

        # Confirm password validation
        if not password2 or password != password2:
            validation_errors.append((self.ids.password2, "Passwords do not match"))
        else:
            self.ids.password2.helper_text = ''

        # Terms and Conditions checkbox validation
        if not terms_checkbox.active:
            validation_errors.append((terms_checkbox, "Please accept the Terms and Conditions"))

        # KYC checkbox validation
        if not kyc_checkbox.active:
            validation_errors.append((kyc_checkbox, "Please authorize KYC details"))

        # Show validation errors if any
        for widget, error_text in validation_errors:
            self.show_validation_error(widget, error_text)

        if validation_errors:
            return

        # If no validation errors, proceed with saving to the database
        self.save_to_database()

        # Reset input fields
        self.ids.name.text = ""
        self.ids.mobile.text = ""
        self.ids.email.text = ""
        self.ids.password.text = ""
        self.ids.password2.text = ""
        self.ids.terms_checkbox.active = False
        self.ids.kyc_checkbox.active = False

        # self.share_email_with_anvil(email)
        # self.manager.current = 'LoginScreen'
        sm = self.manager
        lender_screen = LoginScreen(name='LoginScreen')
        sm.add_widget(lender_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LoginScreen'

    def wallet_generator(self, email_user, name, customer_id1):
        wallet = app_tables.fin_wallet.search()
        wallet_amount = 0
        id_w = []
        acc_id = []
        for i in wallet:
            id_w.append(i['wallet_id'])
            acc_id.append(i['account_id'])

        if len(id_w) >= 1:
            wallet_id = 'WA' + str(int(id_w[-1][2:]) + 1).zfill(4)
        else:
            wallet_id = 'WA0001'

        if acc_id and acc_id[-1]:
            account_id = 'AC' + str(int(acc_id[-1][2:]) + 1).zfill(4)
        else:
            account_id = 'AC0001'
        data = app_tables.fin_user_profile.search()
        email = []
        customer_id = []
        acc_number = []
        acc_name = []
        acc_type = []
        branch_name = []
        bank_name = []
        user_type = []
        for i in data:
            email.append(i['email_user'])
            customer_id.append(i['customer_id'])
            acc_number.append(i['account_number'])
            acc_name.append(i['account_name'])
            acc_type.append(i['account_type'])
            branch_name.append(i['account_bank_branch'])
            bank_name.append(i['bank_name'])
            user_type.append(i['usertype'])

        if customer_id1 in customer_id:
            index = email.index(email_user)
            app_tables.fin_wallet.add_row(account_id=account_id, wallet_id=wallet_id,
                                          wallet_amount=wallet_amount, customer_id=customer_id1,
                                          user_name=name, user_email=email_user,
                                          user_type=user_type[index])
        else:
            print("customer ID not defined")

    def show_validation_error(self, widget, error_text):
        widget.error = True
        widget.helper_text_color = (1, 0, 0, 1)
        widget.helper_text = error_text
        widget.helper_text_mode = "on_error"
        if isinstance(widget, MDCheckbox):
            widget.theme_text_color = 'Error'

    def show_terms_dialog(self):
        dialog = MDDialog(
            title="Terms and Conditions",
            text="I agree with terms and conditions",
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda *args: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def is_strong_password(self, password):
        # Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter,
        # one digit, and one special character
        return len(password) >= 8 and bool(
            re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+=-])[A-Za-z\d!@#$%^&*()_+=-]+$', password))

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)


    def on_pre_leave(self):
        Window.bind(on_keyboard=self.on_keyboard)
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

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'MainScreen'


class MyScreenManager(ScreenManager):
    pass
