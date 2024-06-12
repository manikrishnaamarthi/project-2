from datetime import datetime

from anvil.tables import app_tables
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDRoundFlatButton, MDRectangleFlatButton
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
import anvil
from kivymd.uix.dialog import MDDialog
from lender_view_transaction_history import TransactionLH

Builder.load_string(
    """
<WindowManager>:
    LenderWalletScreen:


<LenderWalletScreen>:
    MDTopAppBar:
        title: "Ascends P2P Wallet"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left',lambda x: root.go_back()]]
        right_action_items: [['refresh', lambda x: root.refresh()]]
        title_align: 'center'
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        id: box1
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)
        MDLabel:
            text: 'Available Balance'
            halign: 'center'
            size_hint_y: None
            height: dp(30)

        GridLayout:
            cols: 2
            spacing: dp(20)
            pos_hint: {'center_x': 0.7, 'center_y':0.3}
            size_hint_y: None
            height: dp(30)
            MDIcon:
                icon: 'currency-inr'
                halign: 'center'
            MDLabel:
                id: total_amount
                halign: 'left'
                font_size: dp(25)
                bold: True

        GridLayout:
            cols: 2
            spacing: dp(20)
            size_hint_y: None
            height: dp(50)
            pos_hint: {'center_x': 0.6}
            MDRectangleFlatIconButton:
                text: "Deposit"
                id: deposit_button_grid
                line_color: 0, 0, 0, 0
                icon: "cash"
                text_color: 0, 0, 0, 1
                md_bg_color:1,1,1,1
                font_name:"Roboto-Bold"
                on_release: root.highlight_button('deposit')
            MDRectangleFlatIconButton:
                id: withdraw_button_grid
                text: "Withdraw"
                icon: "cash"
                line_color: 0, 0, 0, 0
                text_color: 0, 0, 0, 1
                md_bg_color: 1,1,1,1
                font_name:"Roboto-Bold"
                on_release: root.highlight_button('withdraw')
        MDLabel:
            text: 'Enter Amount'
            bold: True
            size_hint_y: None
            height: dp(5)
        MDTextField:
            id: enter_amount
            multiline: False
            helper_text: 'Enter valid Amount'
            helper_text_mode: 'on_focus'
            size_hint_y:None
            font_size: "15dp"
            theme_text_color: "Custom"
            hint_text_color: 0, 0, 0, 1
            hint_text_color_normal: "black"
            text_color_normal: "black"
            helper_text_color_normal: "black"
            on_touch_down: root.on_amount_touch_down()

        MDFlatButton:
            text: "View Transaction History >"
            theme_text_color: "Custom"
            text_color: "black"
            pos_hint: {'center_x': 0.5}
            padding: dp(10)
            md_bg_color: 140/255, 140/255, 140/255, 1
            on_release: root.view_transaction_history()
        GridLayout:
            id: box
            cols: 1
            spacing: dp(20)
            size_hint_y: None
            height: dp(50)
            pos_hint: {'center_x': 0.65}


        MDRoundFlatButton:
            text: "Submit"
            md_bg_color: 0.043, 0.145, 0.278, 1
            theme_text_color: 'Custom'
            font_name: "Roboto-Bold" 
            text_color: 1, 1, 1, 1
            size_hint: 0.7, None
            height: "40dp"
            pos_hint: {'center_x': 0.5}
            on_release: root.submit()
        MDLabel:
			text:''
            size_hint_y:None
            height:dp(20)

    """
)


class LenderWalletScreen(Screen):
    def __init__(self, loan_amount_text=None, **kwargs):
        super().__init__(**kwargs)
        self.type = None
        self.loan_amount = loan_amount_text
        print(self.loan_amount)  # Print the loan amount received during initialization
        data = app_tables.fin_wallet.search()
        email = self.email()
        w_email = []
        w_id = []
        w_amount = []
        for i in data:
            w_email.append(i['user_email'])
            w_id.append(i['wallet_id'])
            w_amount.append(i['wallet_amount'])

        index = 0
        if email in w_email:
            index = w_email.index(email)
            self.ids.total_amount.text = str(round(w_amount[index], 2))
        else:
            print("no email found")

        if loan_amount_text is not None and w_amount[index] >= loan_amount_text:
            button = MDRoundFlatButton(
                text="       Loan Disbursement       ",
                height="40dp",
                theme_text_color='Custom',
                text_color=(1, 1, 1, 1),
                font_name="Roboto-Bold",
                pos_hint={'center_x': 0.5},
                md_bg_color=(0.043, 0.145, 0.278, 1)
            )
            button.bind(on_release=self.disbrsed_loan)
            self.ids.box.add_widget(button)
        elif loan_amount_text != None and w_amount[index] < loan_amount_text:
            print("Amount Not Sufficient")

    def on_amount_touch_down(self):
        self.ids.enter_amount.input_type = 'number'
    def view_transaction_history(self):
        sm = self.manager
        # Create a new instance of the LenderWalletScreen
        wallet_screen = TransactionLH(name='TransactionLH')
        # Add the LenderWalletScreen to the existing ScreenManager
        sm.add_widget(wallet_screen)
        # Switch to the LenderWalletScreen
        sm.current = 'TransactionLH'

    def disbrsed_loan(self, instance):
        print("amount paid")
        view_loan_text = anvil.server.call("view_loan_text")
        if view_loan_text == "view_loan_text":
            self.manager.get_screen('ViewUnderScreenLR').paynow()
        else:
            self.manager.get_screen('ViewLoansProfileScreenLR').paynow()

    def highlight_button(self, button_type):
        if button_type == 'deposit':
            self.ids.deposit_button_grid.md_bg_color = 0, 0, 0, 1
            self.ids.withdraw_button_grid.md_bg_color = 1, 1, 1, 1
            self.ids.deposit_button_grid.text_color = 1, 1, 1, 1
            self.ids.withdraw_button_grid.text_color = 0, 0, 0, 1
            self.type = 'deposit'
        elif button_type == 'withdraw':
            self.ids.deposit_button_grid.md_bg_color = 1, 1, 1, 1
            self.ids.withdraw_button_grid.md_bg_color = 0, 0, 0, 1
            self.ids.withdraw_button_grid.text_color = 1, 1, 1, 1
            self.ids.deposit_button_grid.text_color = 0, 0, 0, 1
            self.type = 'withdraw'

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
        self.manager.current = 'LenderDashboard'

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

    def open_dashboard_screen(self, dialog):
        dialog.dismiss()
        self.manager.current = 'LenderWalletScreen'

    def submit(self):
        enter_amount = self.ids.enter_amount.text
        if self.type == None:
            self.show_validation_error3('Please Select Transaction Type')
        elif self.ids.enter_amount.text == '' and not self.ids.enter_amount.text.isdigit():
            self.show_validation_error3('Enter Valid Amount')
        elif self.type == 'deposit':
            data = app_tables.fin_wallet.search()
            transaction = app_tables.fin_wallet_transactions.search()
            email = self.email()
            w_email = []
            w_id = []
            w_amount = []
            w_customer_id = []
            for i in data:
                w_email.append(i['user_email'])
                w_id.append(i['wallet_id'])
                w_amount.append(i['wallet_amount'])
                w_customer_id.append(i['customer_id'])

            t_id = []
            for i in transaction:
                t_id.append(i['transaction_id'])

            if len(t_id) >= 1:
                transaction_id = 'TA' + str(int(t_id[-1][2:]) + 1).zfill(4)
            else:
                transaction_id = 'TA0001'

            transaction_date_time = datetime.today()
            if email in w_email:
                index = w_email.index(email)
                data[index]['wallet_amount'] = int(enter_amount) + w_amount[index]
                self.show_validation_error(f'Amount {enter_amount} Deposited Successfully')
                self.ids.enter_amount.text = ''
                app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                           customer_id=w_customer_id[index], user_email=email,
                                                           transaction_type=self.type, amount=int(enter_amount),
                                                           status='success', wallet_id=w_id[index],
                                                           transaction_time_stamp=transaction_date_time)
            else:
                print("no email found")
            self.refresh()

        elif self.type == 'withdraw':
            data = app_tables.fin_wallet.search()
            transaction = app_tables.fin_wallet_transactions.search()
            email = self.email()
            w_email = []
            w_id = []
            w_amount = []
            w_customer_id = []
            for i in data:
                w_email.append(i['user_email'])
                w_id.append(i['wallet_id'])
                w_amount.append(i['wallet_amount'])
                w_customer_id.append(i['customer_id'])

            t_id = []
            for i in transaction:
                t_id.append(i['transaction_id'])

            if len(t_id) >= 1:
                transaction_id = 'TA' + str(int(t_id[-1][2:]) + 1).zfill(4)
            else:
                transaction_id = 'TA0001'

            transaction_date_time = datetime.today()

            if email in w_email:
                index = w_email.index(email)
                if w_amount[index] >= int(self.ids.enter_amount.text):
                    data[index]['wallet_amount'] = w_amount[index] - int(self.ids.enter_amount.text)
                    self.show_validation_error(
                        f'Amount {self.ids.enter_amount.text} Withdraw Successfully')
                    self.ids.enter_amount.text = ''
                    app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                               customer_id=w_customer_id[index], user_email=email,
                                                               transaction_type=self.type, amount=int(enter_amount),
                                                               status='success', wallet_id=w_id[index],
                                                               transaction_time_stamp=transaction_date_time)
                else:
                    self.show_validation_error2(
                        f'Insufficient Amount {self.ids.enter_amount.text} Please Deposit Required Money')
                    app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                               customer_id=w_customer_id[index], user_email=email,
                                                               transaction_type=self.type, amount=int(enter_amount),
                                                               status='fail', wallet_id=w_id[index],
                                                               transaction_time_stamp=transaction_date_time)
                    self.ids.enter_amount.text = ''
            else:
                print("no email found")
        self.refresh()

    def refresh(self):
        self.ids.box1.clear_widgets()
        current_loan_amount = anvil.server.call('loan_amount_text')
        self.__init__(loan_amount_text=current_loan_amount)

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Transaction Success",
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

    def show_validation_error2(self, error_message):
        dialog = MDDialog(
            title="Transaction Failure",
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

    def show_validation_error3(self, error_message):
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
    def email(self):
        return anvil.server.call('another_method')


class MyScreenManager(ScreenManager):
    pass
