import json
import sqlite3
import threading
from anvil.tables import app_tables
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.lang import Builder
from datetime import datetime
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivy.properties import ListProperty
from kivymd.uix.textfield import MDTextField
import anvil.server
from dashboard import DashScreen
from lender_dashboard import LenderDashboard
from borrower_dashboard import DashboardScreen
from kivy.factory import Factory
import bcrypt
# anvil.server.connect("server_VRGEXX5AO24374UMBBQ24XN6-ZAWBX57M6ZDN6TBV")
import server

KV = """
<WindowManager>:
    LoginScreen:

<LoginScreen>:
    MDFloatLayout:
        id: login_screen
        md_bg_color:1,1,1,1
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_y": .95}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: rgba(26, 24, 58, 255)
            on_release: root.go_back()

        Image:
            source: "LOGO.png"
            pos_hint: {'center_x': 0.5, 'center_y': 0.93}
            size_hint: None, None
            size: "100dp", "100dp"

        MDLabel:
            id: label1
            text: 'Welcome,'
            font_size:dp(23)

            halign: 'center'
            font_name:"Roboto-Bold"
            underline:"True"
            pos_hint: {'center_x': 0.5, 'center_y': 0.81}
        MDLabel:

            text: 'Sign in to continue'
            color:6/255, 143/255, 236/255, 1
            font_size:dp(16)
            halign: 'center'

            pos_hint: {'center_x': 0.5, 'center_y': 0.77}
        BoxLayout:
            id: float1
            orientation: 'vertical'
            size_hint: 0.8, None
            height: "80dp"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Line:
                    rectangle: self.x, self.y, self.width, self.height
            MDTextField:
                id: email      
                hint_text: "Email"
                hint_text_color: 0.043, 0.145, 0.278, 1  # Indigo color for hint text
                helper_text_mode: "on_focus"
                icon_right: "account"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_name: "Roboto-Bold"
                pos_hint: {'center_x': 0.5, 'center_y': 0.57}
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Change the text color here (black in this example)

            MDTextField:
                id: password
                hint_text: "Password"
                hint_text_color: 0.043, 0.145, 0.278, 1  # Indigo color for hint text
                color_mode: 'custom'
                line_color_normal: 0.043, 0.145, 0.278, 1
                helper_text: "Enter your password"
                helper_text_mode: "on_focus"
                icon_right: "lock"
                password: not password_visibility.active
                size_hint_y: None
                height: "30dp"
                width: dp(200)
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                pos_hint: {'center_x': 0.5, 'center_y': 0.46}
                on_text_validate: app.validate_password()
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Change the text color here (black in this example)

        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: "29dp"
            spacing:dp(5)
            pos_hint: {'center_x': 0.6, 'center_y': 0.4}
            MDCheckbox:
                id: password_visibility
                size_hint: None, None
                size: "30dp", "30dp"
                active: False
                on_active: root.on_checkbox_active(self, self.active)

            MDLabel:
                text: "Show Password"
                font_size:dp(14)
                size: "30dp", "30dp"
                theme_text_color: "Secondary"
                halign: "left"
                valign: "center"      
        GridLayout:
            id:grid1
            cols: 2
            spacing:dp(20)
            padding:dp(20)
            pos_hint: {'center_x': 0.5, 'center_y': 0.32}
            size_hint: 1, None
            height: "50dp"
            MDRaisedButton:
                text: "Login"
                on_release: root.go_to_dashboard()
                md_bg_color:0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"
        MDLabel:
            id: error_text
            text: ""
        MDSpinner:
            id: loading_spinner
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint_x: None
            size_hint_y: None
            size_hint: None, None
            size: "70dp", "70dp"
            opacity: 0
            anim_delay: 0.05       
    BoxLayout:
        id:box1
        orientation: 'horizontal'
        size_hint: None, None
        width: "190dp"
        height: "15dp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}

        MDTextButton:
            text: "Already have an account? [color=#0699FF]Sign In[/color]"
            font_name: "Roboto"
            font_size: dp(14)
            markup: True
            theme_text_color: 'Secondary'
            halign: 'left'
            height: "50dp"
            text_color: 0.043, 0.145, 0.278, 1
            on_release: root.go_to_signup()

"""
Builder.load_string(KV)


class LoginScreen(Screen):

    def on_checkbox_active(self, checkbox, value):
        # Handle checkbox state change
        # Update password visibility based on the checkbox state
        if hasattr(self, 'login_screen'):
            self.login_screen.ids.password.password = not value
            print(value)

    def show_error_dialog(self, message):
        Clock.schedule_once(lambda dt: self._show_error_dialog(message), 0)

    def _show_error_dialog(self, message):
        dialog = MDDialog(
            text=message,
            size_hint=(0.8, 0.3),
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda *args: dialog.dismiss()
                )
            ]
        )
        dialog.open()
        self.hide_loading_spinner()

    def go_to_dashboard(self):
        entered_email = self.ids.email.text
        # Show loading spinner
        self.ids.error_text.text = ""
        self.show_loading_spinner()
        self.dim_screen()  # Dim the screen

        # Start a separate thread for background validation
        self.background_validation()
        last_login = datetime.now()
        user_profiles = app_tables.users.search(email=entered_email)
        user_profile = user_profiles[0]
        user_profile.update(last_login=last_login)

    def show_loading_spinner(self):
        self.ids.loading_spinner.opacity = 1

    def hide_loading_spinner(self):
        Clock.schedule_once(self._hide_loading_spinner, 0)

    def _hide_loading_spinner(self, *args):
        self.ids.loading_spinner.opacity = 0
        self.undim_screen()

    def dim_screen(self):
        # Dim other UI elements while loading
        self.ids.float1.opacity = 0.5
        self.ids.grid1.disabled = True
        self.ids.box1.opacity = 0.5

    def undim_screen(self):
        # Restore opacity of UI elements after loading
        self.ids.float1.opacity = 1
        self.ids.grid1.disabled = False
        self.ids.box1.opacity = 1

    def background_validation(self):
        entered_email = self.ids.email.text
        entered_password = self.ids.password.text

        if not entered_email or "@" not in entered_email or "." not in entered_email:
            Clock.schedule_once(lambda dt: self.show_error_dialog("Invalid email address"), 0)
            self.hide_loading_spinner()  # Hide spinner in case of error
            return

        if not entered_password:
            self.show_error_dialog("Please enter password")
            self.hide_loading_spinner()
            # Hide spinner in case of error
            return

        # Start another thread for SQLite operations
        threading.Thread(target=self.perform_database_operations, args=(entered_email, entered_password)).start()

    def perform_database_operations(self, entered_email, entered_password):
        conn = sqlite3.connect("fin_user.db")
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM fin_users
            WHERE email = ?
        ''', (entered_email,))

        user_data = cursor.fetchone()
        data = app_tables.users.search()
        profile = app_tables.fin_user_profile.search()
        email_list = []
        password_list = []
        registartion_approve = []
        user_type = []
        email_user = []
        a = 0
        for i in data:
            a += 1
            email_list.append(i['email'])
            password_list.append(i['password_hash'])
        for i in profile:
            registartion_approve.append(i['registration_approve'])
            user_type.append(i['usertype'])
            email_user.append(i['email_user'])

        if entered_email in email_list:
            i = email_list.index(entered_email)
            if entered_email in email_user:
                index = email_user.index(entered_email)
            else:
                print('no email found')

            if entered_email in email_list:
                i = email_list.index(entered_email)
                password_value = bcrypt.checkpw(entered_password.encode('utf-8'), password_list[i].encode('utf-8'))
                if entered_email in email_user:
                    index = email_user.index(entered_email)
                else:
                    print('no email found')

                if (email_list[i] == entered_email) and (password_value) and (
                        registartion_approve[index] == True) and (user_type[index] == 'borrower'):
                    self.share_email_with_anvil(email_list[i])
                    self.save_user_info(entered_email, user_type[index])  # Save user info to email.json
                    # Schedule the creation of borrower DashboardScreen on the main thread
                    Clock.schedule_once(lambda dt: self.show_dashboard('DashboardScreen'), 0)
                    self.hide_loading_spinner()
                    return  # Added to exit the method after successful login as borrower
                elif (email_list[i] == entered_email) and (password_value) and (
                        registartion_approve[index] == True) and (user_type[index] == 'lender'):
                    self.share_email_with_anvil(email_list[i])
                    self.save_user_info(entered_email, user_type[index])  # Save user info to email.json
                    # Schedule the creation of lender DashboardScreen on the main thread
                    Clock.schedule_once(lambda dt: self.show_dashboard('LenderDashboard'), 0)
                    self.hide_loading_spinner()
                    return  # Added to exit the method after successful login as lender
                elif (email_list[i] == entered_email) and (password_value):
                    self.share_email_with_anvil(email_list[i])
                    self.save_user_info(entered_email, "default")  # Save user info to email.json
                    # Schedule the creation of default DashboardScreen on the main thread
                    Clock.schedule_once(lambda dt: self.show_dashboard('DashScreen'), 0)
                    self.hide_loading_spinner()
                    return  # Added to exit the method after successful login with no specific user type
                else:
                    # Schedule the error dialog on the main thread
                    Clock.schedule_once(lambda dt: self.show_error_dialog("Incorrect email/password"), 0)
                    self.hide_loading_spinner()
                    return  # Added to exit the method after showing error dialog

        if user_data:
            password_value2 = bcrypt.checkpw(entered_password.encode('utf-8'), user_data[4].encode('utf-8'))
            print(password_value2)
            if password_value2:  # Fix index to 4 for the password field

                users = cursor.execute('''SELECT * FROM fin_users''')
                id_list = []
                for i in users:
                    id_list.append(i[0])

                for i in id_list:
                    if i == user_data[0]:

                        cursor.execute('''
                                        UPDATE fin_users SET customer_status = 'logged'
                                        WHERE user_id = ?
                                    ''', (user_data[0],))
                        conn.commit()
                    else:
                        cursor.execute('''
                                        UPDATE fin_users SET customer_status = ''
                                        WHERE user_id = ?
                                    ''', (i,))
                        conn.commit()

                conn.close()

                # Clock.schedule_once(lambda dt: self.show_dashboard(), 0)

            else:

                Clock.schedule_once(lambda dt: self.show_error_dialog("Incorrect password"), 0)
                # Clock.schedule_once(lambda dt: self.hide_loading_spinner(), 0)
        elif entered_email not in email_list and not user_data:

            Clock.schedule_once(lambda dt: self.show_error_dialog("Enter valid Email and password"), 0)
            # Clock.schedule_once(lambda dt: self.hide_loading_spinner(), 0)

    def save_user_info(self, email, user_type):
        # Read existing email.json data
        with open("emails.json", "r") as file:
            data = json.load(file)

        # Update or create entry for the current user
        data[email] = {"user_type": user_type, "logged_status": True}

        # Write updated data back to the file
        with open("emails.json", "w") as file:
            json.dump(data, file)
    def show_dashboard(self, screen_name):
        def switch_screen(dt):

            if screen_name == 'DashboardScreen':
                self.manager.add_widget(Factory.DashboardScreen(name='DashboardScreen'))
                self.manager.current = 'DashboardScreen'

            elif screen_name == 'LenderDashboard':
                self.manager.add_widget(Factory.LenderDashboard(name='LenderDashboard'))
                self.manager.current = 'LenderDashboard'

            elif screen_name == 'DashScreen':
                self.manager.add_widget(Factory.DashScreen(name='DashScreen'))
                self.manager.current = 'DashScreen'

        Clock.schedule_once(switch_screen, 0)

    def share_email_with_anvil(self, email):
        # Make an API call to Anvil server to share the email
        anvil.server.call('share_email', email)

    def show_error_dialog(self, message):

        dialog = MDDialog(
            text=message,
            size_hint=(0.8, 0.3),
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda *args: dialog.dismiss()
                )
            ]
        )
        dialog.open()
        self.hide_loading_spinner()

    def go_to_signup(self):
        from signup import SignupScreen
        self.manager.add_widget(Factory.SignupScreen(name='SignupScreen'))
        self.manager.current = 'SignupScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)
        # Clear input fields when navigating back to the login page
        self.ids.email.text = ""
        self.ids.password.text = ""

    def on_pre_leave(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def on_start(self):
        Window.softinput_mode = "below_target"

    def go_back(self):

        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'MainScreen'


class MyScreenManager(ScreenManager):
    pass