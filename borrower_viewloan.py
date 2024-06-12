from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.material_resources import dp
from kivymd.uix.button import MDRaisedButton, MDRoundFlatIconButton, MDRoundFlatButton, MDFillRoundFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.list import *
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.utils import platform
from kivy.clock import mainthread
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.spinner import MDSpinner
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from kivy.animation import Animation
from kivymd.uix.label import MDLabel
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget
import anvil.users
from anvil.tables import app_tables

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission)

import anvil.server

borrower_view_loan = '''
<WindowManager>:
    DashboardScreenVLB:
    OpenLoanVLB:
    UnderProcessLoanVLB:
    RejectedLoanVLB:
    ViewLoansScreenVLB:



<DashboardScreenVLB>:
    MDFloatLayout:
        md_bg_color:1,1,1,1
        size_hint: 1, 1 

        MDTopAppBar:
            title: "Borrower View Loan"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
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
                on_release: root.go_to_open_loans()
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "Open Loans"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1, 1
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
                        text: "Under process Loans"
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

<OpenLoanVLB>
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "View All Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        MDScrollView:
            
            MDBoxLayout:
                id: container
                orientation: 'vertical'
                padding: dp(30)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height
                width: self.minimum_width
                adaptive_size: True
                
                pos_hint: {"center_x": 0, "center_y":  0}
                

            # MDList:
            #     
            #     id: container                 




<UnderProcessLoanVLB>
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "UnderProcess Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'left'
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container1
                
                
<RejectedLoanVLB>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Rejected Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'left'
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container2
<ClosedLoanVLB>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Close Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'left'
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container3
<ViewLoansScreenVLB>
    MDGridLayout:
        cols: 1
        MDTopAppBar:
            title: "View Loan details"
            elevation: 2
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            halign: 'left'
            pos_hint: {'top': 1}

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
                    text: 'Required amount:'
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
                    halign: 'left'
                    bold: True

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
                    theme_text_color: 'Custom'  
                    bold: True


                MDLabel:
                    id: pro_name
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold: True

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Borrower Name'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    bold: True

                MDLabel:
                    id: b_name
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold: True

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Phone Number'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    bold: True

                MDLabel:
                    id: phone_num
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold: True
                    
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Ascend Score'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    bold: True

                MDLabel:
                    id: asc_score
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold: True

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
                    bold: True

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
                    bold: True

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
                    bold: True

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Loan Status'
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: updated_status
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
                    bold: True

        BoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
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
                    bold: True
                MDIconButton:
                    icon: 'currency-inr'
                    halign: 'center' 
                    bold: True   

                MDLabel:
                    id: amount_1
                    halign: 'left'
                    bold: True




'''
Builder.load_string(borrower_view_loan)


class DashboardScreenVLB(Screen):
    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=5)
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label,
                                                                      modal_height))  # Bind to the completion event to repeat the animation
        anim.start(loading_label)

    def go_to_open_loans(self):
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
        Clock.schedule_once(lambda dt: self.performance_go_to_open_loans(modal_view), 2)

    def performance_go_to_open_loans(self, modal_view):
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = OpenLoanVLB(name='OpenLoanVLB')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'OpenLoanVLB'

    def go_to_under_loans(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

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
        Clock.schedule_once(lambda dt: self.performance_go_to_under_loans(modal_view), 2)

    def performance_go_to_under_loans(self, modal_view):
        # Perform the actual action here (e.g., fetching loan requests)
        # For demonstration purposes, let's simulate a delay of 2 seconds
        # Replace this with your actual logic

        # Dismiss the modal view once the action is complete
        modal_view.dismiss()

        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = UnderProcessLoanVLB(name='UnderProcessLoanVLB')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'UnderProcessLoanVLB'

    def go_to_reject_loans(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

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
        Clock.schedule_once(lambda dt: self.performance_go_to_reject_loans(modal_view), 2)

    def performance_go_to_reject_loans(self, modal_view):
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = RejectedLoanVLB(name='RejectedLoanVLB')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'RejectedLoanVLB'

    def go_to_app_tracker(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

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
        Clock.schedule_once(lambda dt: self.performance_go_to_app_tracker(modal_view), 2)

    def performance_go_to_app_tracker(self, modal_view):
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = ClosedLoanVLB(name='ClosedLoanVLB')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'ClosedLoanVLB'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.on_back_button_press()
            return True
        return False

    def on_back_button_press(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreen'

    def logout(self):
        self.manager.current = 'MainScreen'

    def refresh(self):
        pass


class ViewLoansScreenVLB(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialize_with_value(self, value, data):
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        loan_id = []
        product_name = []
        borrower_name = []
        loan_amount = []
        loan_amount1 = []
        interest_rate = []
        tenure = []
        date_of_apply = []
        status = []
        print(loan_id)
        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            product_name.append(i['product_name'])
            loan_amount.append(i['loan_amount'])
            loan_amount1.append(i['loan_amount'])
            borrower_name.append(i['borrower_full_name'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            date_of_apply.append(i['borrower_loan_created_timestamp'])
            status.append(i['loan_updated_status'])
        profile_customer_id = []
        profile_mobile_number = []
        ascend_value = []

        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            ascend_value.append(i['ascend_value'])

        index = 0
        if value in loan_id:
            index = loan_id.index(value)
            self.ids.pro_name.text = str(product_name[index])
            self.ids.b_name.text = str(borrower_name[index])
            self.ids.amount.text = str(loan_amount[index])
            self.ids.amount_1.text = str(loan_amount1[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.int_rate.text = str(interest_rate[index])
            self.ids.date.text = str(date_of_apply[index])
            self.ids.updated_status.text = str(status[index])

        if customer_id[index] in profile_customer_id:
            index2 = profile_customer_id.index(customer_id[index])

            self.ids.phone_num.text = str(profile_mobile_number[index2])
            self.ids.asc_score.text = str(ascend_value[index2])

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

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ViewLoansRequest'

    def on_back_button_press(self):
        self.manager.current = 'OpenLoanVLB'


class OpenLoanVLB(Screen):
    def __init__(self, instance=None, **kwargs):
        super().__init__(**kwargs)
        self.selected_item = None  # Track the selected item

        data = app_tables.fin_loan_details.search()
        email = anvil.server.call('another_method')
        profile = app_tables.fin_user_profile.search(email_user=email)
        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        product_name = []
        email1 = []
        loan_amount = []
        tenure = []
        interest_rate = []
        #ascend_value = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])
            product_name.append(i['product_name'])
            email1.append(i['borrower_email_id'])
            loan_amount.append(i['loan_amount'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            #ascend_value.append(i['ascend_value'])

        profile_customer_id = []
        profile_mobile_number = []
        ascend_value = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            ascend_value.append(i['ascend_value'])
        cos_id = None
        if email in email1:
            index = email1.index(email)
            cos_id = customer_id[index]
        if cos_id is not None:

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
                if customer_id[i] in profile_customer_id:
                    number = profile_customer_id.index(customer_id[i])
                else:
                    number = 0
                # Card to display the list of details
                card = MDCard(
                    orientation='vertical',
                    size_hint=(None, None),
                    size=("280dp", "190dp"),
                    padding="10dp",
                    spacing="3dp",
                    elevation=3,
                )
                # Horizontal layout to keep the text and image in to the card
                horizontal_layout = BoxLayout(orientation='horizontal')
                image = Image(
                    source="img.png",  # Assuming you want to use the same image for now
                    size_hint_x=None,
                    height="10dp",
                )
                horizontal_layout.add_widget(image)

                # Text Layout to keep the text on card
                text_layout = BoxLayout(orientation='vertical')
                text_layout.add_widget(MDLabel(
                    text=f" [b]{borrower_name[i]}\n {profile_mobile_number[number]}[/b]",
                    theme_text_color='Custom',
                    text_color=(0, 0, 0, 1),
                    halign='left',
                    markup=True,
                    font_size='10sp',
                    bold = True
                ))
                text_layout.add_widget(MDLabel(
                    text=f" [b]Loan Amount:[/b] {loan_amount[i]}",
                    theme_text_color='Custom',
                    text_color=(0, 0, 0, 1),
                    halign='left',
                    markup=True,
                    # font_size='10sp'
                ))
                text_layout.add_widget(MDLabel(
                    text=f" [b]Ascend Score :[/b]{ascend_value[number]}",
                    theme_text_color='Custom',
                    text_color=(0, 0, 0, 1),
                    halign='left',
                    markup=True,
                    # font_size='10sp'
                ))
                text_layout.add_widget(MDLabel(
                    text=f" [b]Interest Rate :[/b]{interest_rate[i]}",
                    theme_text_color='Custom',
                    text_color=(0, 0, 0, 1),
                    halign='left',
                    markup=True,
                    # font_size='10sp'
                ))
                horizontal_layout.add_widget(text_layout)
                card.add_widget(horizontal_layout)

                horizontal_layout1 = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(45))
                # Button layout to align the Buttons
                button_layout2 = BoxLayout(
                    size_hint_y=None,
                    height="40dp",
                    padding="10dp",
                    spacing=30
                )

                #this colors for loan status button colors based on loan status

                status_color = (0.545, 0.765, 0.290, 1)  # default color
                if loan_status[i] == "under process" or loan_status[i] == "Under Process" or loan_status[
                    i] == "UnderProcess" or loan_status[i] == "underprocess":
                    status_color = (0.9804, 0.9804, 0.8235, 1.0)
                elif loan_status[i] == "disbursed loan" or loan_status[i] == "disbursed":
                    status_color = (0.8588, 0.4392, 0.5765, 1.0)
                elif loan_status[i] == "closed loan" or loan_status[i] == "Closed Loan" or loan_status[
                    i] == "closedloan" or loan_status[i] == "ClosedLoan":
                    status_color = (0.4235, 0.5569, 0.1373, 1.0)
                elif loan_status[i] == "extension" or loan_status[i] == "Extension":
                    status_color = (1.0, 0.6275, 0.4824, 1.0)
                elif loan_status[i] == "foreclosure" or loan_status[i] == "Foreclosure":
                    status_color = (0.0, 0.749, 1.0, 1.0)
                elif loan_status[i] == "accepted" or loan_status[i] == "Accepted":
                    status_color = (0.2353, 0.7019, 0.4431, 1.0)
                elif loan_status[i] == "rejected" or loan_status[i] == "Rejected" or loan_status[
                    i] == "Rejected Loan" or loan_status[i] == "rejected loan":
                    status_color = (0.902, 0.141, 0.141, 1)
                elif loan_status[i] == "approved" or loan_status[i] == "Approved" or loan_status[
                    i] == "approved loans" or loan_status[i] == "Approved Loans":
                    status_color = (0.2353, 0.7019, 0.4431, 1.0)
                elif loan_status[i] == "decline" or loan_status[i] == "Decline" or loan_status[i] == "declined" or \
                        loan_status[i] == "Declined":
                    status_color = (0.902, 0.141, 0.141, 1)
                button2 = MDFillRoundFlatButton(
                    text="  View Details  ",
                    # size_hint=(None, None),
                    height="40dp",
                    width="250dp",
                    pos_hint={"center_x": 1},
                    md_bg_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id),
                    text_color=(1, 1, 1, 1)
                )
                button_layout1 = BoxLayout(
                    size_hint_y=None,
                    height="40dp",
                    padding="10dp",
                    spacing=30
                )
                #this status_text for status text to keep button
                status_text = {
                    "under process":    "Under Process",
                    "disbursed loan":   "Disburse Loan",
                    "closed loan":      "  Closed Loan  ",
                    "extension":        " Extension Loan ",
                    "foreclosure":      "   Foreclosure   ",
                    "accepted":         "Accepted Loan",
                    "rejected":         "Rejected Loan",
                    "approved":         "Approved Loan",
                    "decline":          " Declined Loan"
                }
                button1 = MDFillRoundFlatButton(
                    text=status_text.get(loan_status[i], loan_status[i]),
                    height=dp(40),
                    pos_hint={"center_x": 0},
                    md_bg_color=status_color,
                    text_color=(1, 1, 1, 1),
                )
                button_layout1.add_widget(button1)
                button_layout2.add_widget(button2)

                # Adding the Buttons to the card
                horizontal_layout1.add_widget(button_layout1)
                horizontal_layout1.add_widget(button_layout2)
                card.add_widget(horizontal_layout1)

                self.ids.container.add_widget(card)

                # Actual code for the future referance incase of failures
                # item = ThreeLineAvatarIconListItem(
                #
                #     IconLeftWidget(
                #         icon="icon1.jpg", size_hint_x=None, width=50
                #         # icon = f"{customer_id}"
                #     ),
                #
                #     text=f"User Name :{borrower_name[i]},       Product Name :{product_name[i]}",
                #     secondary_text=f"Mobile Number :{profile_mobile_number[number]},            Loan Amount :{loan_amount[i]}",
                #     tertiary_text=f"Interest Rate :{interest_rate[i]},      Tenure: {tenure[i]},        Loan Status: {loan_status[i]}",
                #     text_color=(0, 0, 0, 1),  # Black color
                #     theme_text_color='Custom',
                #     secondary_text_color=(0, 0, 0, 1),
                #     secondary_theme_text_color='Custom',
                #     tertiary_text_color=(0, 0, 0, 1),
                #     tertiary_theme_text_color='Custom',
                #
                # )
                # item.ids._lbl_primary.halign = 'center'
                # item.ids._lbl_primary.valign = 'top'
                # item.ids._lbl_secondary.halign = 'center'
                # item.ids._lbl_primary.valign = 'middle'
                # item.ids._lbl_tertiary.halign = 'center'
                # item.ids._lbl_primary.valign = 'bottom'
                #
                # button = MDRaisedButton(
                #     text="Close Loan",
                #     size_hint=(None, None),
                #     height=30,
                #     width=20,
                #     #pos_hint={"center_x": 1, "center_y": 0},
                #     pos_hint={"right": 1, "bottom": 0}
                #
                #     # on_release=lambda x, i=i: self.close_loan(i)
                # )
                #
                # # Add the button to the item
                # right_icon = IconRightWidget()
                # right_icon.add_widget(button)
                # item.add_widget(right_icon)
                #
                #
                # card.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
                # self.ids.container.add_widget(card)

    def icon_button_clicked(self, instance, loan_id):
        # Deselect all other items
        self.deselect_items()

        # Change the background color of the clicked item to indicate selection
        # instance.bg_color = (0.5, 0.5, 0.5, 1)  # Change color as desired
        self.selected_item = instance

        data = app_tables.fin_loan_details.search()
        loan_status = None
        for loan in data:
            if loan['loan_id'] == loan_id:
                loan_status = loan['loan_updated_status']
                break
        #if loan_status == 'under process' or loan_status == 'disbursed loan' or loan_status == 'foreclosure':
            # Open the screen for approved loans

        sm = self.manager

        # Create a new instance of the LoginScreen
        under_process = ViewLoansScreenVLB(name='ViewLoansScreenVLB')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(under_process)

        # Switch to the LoginScreen
        sm.current = 'ViewLoansScreenVLB'
        self.manager.get_screen('ViewLoansScreenVLB').initialize_with_value(loan_id, data)

        # else:
        #     # Handle other loan statuses or show an error message
        #     pass

    def deselect_items(self):
        # Deselect all items in the list
        for item in self.ids.container.children:
            if isinstance(item, ThreeLineAvatarIconListItem):
                item.bg_color = (1, 1, 1, 1)  # Reset background color for all items

    def on_pre_enter(self):
        self.deselect_items()  # Deselect items when entering the screen
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

    def refresh(self):
        self.ids.container.clear_widgets()
        self.__init__()


class UnderProcessLoanVLB(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = app_tables.fin_loan_details.search()
        email = anvil.server.call('another_method')
        profile = app_tables.fin_user_profile.search(email_user=email)
        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        product_name = []
        email1 = []
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
                if loan_status[c] == 'under process' and customer_id[c] == cos_id:
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

        data = app_tables.fin_loan_details.search()  # Fetch data here
        loan_status = None
        for loan in data:
            if loan['loan_id'] == loan_id:
                loan_status = loan['loan_updated_status']
                break

        if loan_status == 'under process':
            # Open the screen for approved loans

            sm = self.manager

            # Create a new instance of the LoginScreen
            under_process = ViewLoansScreenVLB(name='ViewLoansScreenVLB')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(under_process)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansScreenVLB'
            self.manager.get_screen('ViewLoansScreenVLB').initialize_with_value(loan_id, data)

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreenVLB'

    def refresh(self):
        self.ids.container1.clear_widgets()
        self.__init__()


class RejectedLoanVLB(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = app_tables.fin_loan_details.search()
        email = anvil.server.call('another_method')
        profile = app_tables.fin_user_profile.search(email_user=email)
        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        product_name = []
        email1 = []
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
                if loan_status[c] == 'rejected' and customer_id[c] == cos_id:
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
                self.ids.container2.add_widget(item)

    def icon_button_clicked(self, instance, loan_id):
        # Handle the on_release event here
        data = app_tables.fin_loan_details.search()  # Fetch data here
        loan_status = None
        for loan in data:
            if loan['loan_id'] == loan_id:
                loan_status = loan['loan_updated_status']
                break

        if loan_status == 'rejected':
            # Open the screen for approved loans

            sm = self.manager

            # Create a new instance of the LoginScreen
            rejected = ViewLoansScreenVLB(name='ViewLoansScreenVLB')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(rejected)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansScreenVLB'
            self.manager.get_screen('ViewLoansScreenVLB').initialize_with_value(loan_id, data)

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreenVLB'

    def refresh(self):
        self.ids.container2.clear_widgets()
        self.__init__()


class ClosedLoanVLB(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = app_tables.fin_loan_details.search()
        email = anvil.server.call('another_method')
        profile = app_tables.fin_user_profile.search(email_user=email)
        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        product_name = []
        email1 = []
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
                if loan_status[c] == 'closed' and customer_id[c] == cos_id:
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
                item.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance,
                                                                                                   loan_id))  # Corrected the binding
                self.ids.container3.add_widget(item)

    def icon_button_clicked(self, instance, loan_id):
        # Handle the on_release event here
        data = app_tables.fin_loan_details.search()  # Fetch data here
        loan_status = None
        for loan in data:
            if loan['loan_id'] == loan_id:
                loan_status = loan['loan_updated_status']
                break

        if loan_status == 'closed':
            # Open the screen for approved loans

            sm = self.manager

            # Create a new instance of the LoginScreen
            disbursed = ViewLoansScreenVLB(name='ViewLoansScreenVLB')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(disbursed)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansScreenVLB'
            self.manager.get_screen('ViewLoansScreenVLB').initialize_with_value(loan_id, data)

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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreenVLB'

    def refresh(self):
        self.ids.container3.clear_widgets()
        self.__init__()


class MyScreenManager(ScreenManager):
    pass