import anvil.server
from anvil.tables import app_tables
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.lang import Builder
from kivy.core.window import Window
import sqlite3
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.uix.widget import Widget
from kivymd.uix.button import MDRaisedButton, MDFillRoundFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.list import *
from kivy.animation import Animation
from kivymd.uix.label import MDLabel
from kivymd.uix.list import IconLeftWidget, IconRightWidget, ImageLeftWidget
from lender_view_loans_request import view_loan_request, ViewLoansProfileScreenLR, ViewLoansProfileScreenRL

view_loans = '''
<WindowManager>
    # ViewLoansScreen:
    ALlLoansScreen:
    OpenViewLoanScreen:
    ViewLoansProfileScreens:
    ViewLoansProfileScreens2:
    ViewRejectedLoansScreen:
    ViewUnderProcessLoansScreen:
    ViewClosedLoansScreen:
# <ViewLoansScreen>
#     MDTopAppBar:
#         title: "View Loans"
#         elevation: 3
#         left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
#         pos_hint: {'top': 1}
#         md_bg_color: 0.043, 0.145, 0.278, 1
# 
#     MDGridLayout:
#         cols: 2
#         spacing: dp(15)
#         size_hint_y: None
#         pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#         height: self.minimum_height
#         width: self.minimum_width
#         size_hint_x: None
# 
#         MDFlatButton:
#             size_hint: None, None
# 
#             pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#             md_bg_color: 0.043, 0.145, 0.278, 1
# 
#             size_hint_y: None
#             height: dp(60)
#             size_hint_x: None
#             width: dp(110)
#             on_release: root.go_to_open_loans()
#             BoxLayout:
#                 orientation: 'horizontal'
#                 spacing:dp(10)
#                 MDLabel:
#                     text: "Open Loans"
#                     font_size:dp(14)
#                     bold:True
#                     theme_text_color: 'Custom'
#                     halign: "center"
#                     text_color:1,1,1,1
#                     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
# 
#         MDFlatButton:
#             size_hint: None, None
# 
#             pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#             md_bg_color: 0.043, 0.145, 0.278, 1 
#             on_release: root.go_to_under_process_loans()
#             size_hint_y: None
#             height: dp(60)
#             size_hint_x: None
#             width: dp(110)
# 
#             BoxLayout:
#                 orientation: 'horizontal'
#                 spacing:dp(10)
#                 MDLabel:
#                     text: "UnderProcess Loans"
#                     font_size:dp(14)
#                     bold:True
#                     theme_text_color: 'Custom'
#                     halign: "center"
#                     text_color:1,1,1,1
#                     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
# 
#         MDFlatButton:
#             size_hint: None, None
# 
#             pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#             md_bg_color: 0.043, 0.145, 0.278, 1
#             on_release: root.go_to_rejected_loans()
#             size_hint_y: None
#             height: dp(60)
#             size_hint_x: None
#             width: dp(110)
# 
#             BoxLayout:
#                 orientation: 'horizontal'
#                 spacing:dp(10)
#                 MDLabel:
#                     text: "Rejected Loans"
#                     font_size:dp(14)
#                     bold:True
#                     theme_text_color: 'Custom'
#                     halign: "center"
#                     text_color:1,1,1,1
#                     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
# 
#         MDFlatButton:
#             size_hint: None, None
# 
#             pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#             md_bg_color: 0.043, 0.145, 0.278, 1 
#             on_release: root.go_to_closed_loans()
#             size_hint_y: None
#             height: dp(60)
#             size_hint_x: None
#             width: dp(110)
#             BoxLayout:
#                 orientation: 'horizontal'
#                 spacing:dp(10)
#                 MDLabel:
#                     text: "Closed Loans"
#                     font_size:dp(14)
#                     bold:True
#                     theme_text_color: 'Custom'
#                     halign: "center"
#                     text_color:1,1,1,1
#                     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
# 
# 
#         MDFlatButton:
#             size_hint: None, None
#             md_bg_color: 0.043, 0.145, 0.278, 1 
# 
#             size_hint_y: None
#             height: dp(60)
#             size_hint_x: None
#             width: dp(110)
#             on_release: root.all_loanscreen()
#             BoxLayout:
#                 orientation: 'horizontal'
#                 spacing:dp(10)
#                 MDLabel:
#                     text: "All Loans"
#                     font_size:dp(14)
#                     bold:True
#                     theme_text_color: 'Custom'
#                     halign: "center"
#                     text_color:1,1,1,1
<OpenViewLoanScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Open Loans"
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
                elevation: 3
                size_hint_y: None
                height: self.minimum_height



<ALlLoansScreen> 
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
                id: container2
                orientation: 'vertical'
                padding: dp(40)
                spacing: dp(10)
                elevation: 3
                size_hint_y: None
                height: self.minimum_height


<ViewRejectedLoansScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Rejected Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDBoxLayout:
            padding:30
            orientation: 'vertical'
            md_bg_color: 0.5,0.5,0.5,1
            MDScrollView:
                MDList:
                    id: container1
                    padding:150
                    size_hint_y: None

<ViewClosedLoansScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Closed Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container6

<ViewLoansProfileScreens>
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
            padding: dp(20)
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
            MDLabel:
                text: ''
                halign: 'left'
                size_hint_y: None
                height: dp(5)
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

<ViewLoansProfileScreens2>
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
            padding: dp(20)
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
                    text: '     Amount:'
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

            MDGridLayout:
                cols: 3

                MDLabel:
                    text: '     Total'
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
        MDLabel:
            text: ''
            halign: 'left'
            size_hint_y: None
            height: dp(25)
    '''

Builder.load_string(view_loans)
conn = sqlite3.connect('fin_user_profile.db')
cursor = conn.cursor()


class ALlLoansScreen(Screen):
    def __init__(self, loan_id=None, instance=None, **kwargs):
        super().__init__(**kwargs)
        data = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        product_name = []
        interest_rate = []
        loan_amount = []

        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])
            product_name.append(i['product_name'])
            interest_rate.append(i['interest_rate'])
            loan_amount.append(i['loan_amount'])

        profile_customer_id = []
        profile_mobile_number = []
        ascend_value = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            ascend_value.append(i['ascend_value'])

        c = -1
        index_list = []
        for i in range(s):
            c += 1
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
            card = MDCard(
                orientation='vertical',
                size_hint=(None, None),
                size=("280dp", "180dp"),
                padding="8dp",
                spacing="5dp",
                elevation=3
            )
            horizontal_layout = BoxLayout(orientation='horizontal')
            image = Image(
                source='img.png',  # Update with the actual path to the image
                size_hint_x=None,
                height="60dp",
                width="70dp"
            )
            horizontal_layout.add_widget(image)

            horizontal_layout.add_widget(Widget(size_hint_x=None, width='10dp'))
            text_layout = BoxLayout(orientation='vertical')
            text_layout.add_widget(MDLabel(
                text=f"[b]{borrower_name[i]}[/b],  [b]{profile_mobile_number[number]}[/b]",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Loan Amount:[/b] {loan_amount[i]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Ascend Score:[/b] {ascend_value[number]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))

            text_layout.add_widget(MDLabel(
                text=f"[b]Interest Rate:[/b] {interest_rate[i]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            horizontal_layout.add_widget(text_layout)
            card.add_widget(horizontal_layout)

            card.add_widget(Widget(size_hint_y=None, height='10dp'))
            button_layout = BoxLayout(
                size_hint_y=None,
                height="40dp",
                padding="10dp",
                spacing="20dp"
            )
            status_color = (0.545, 0.765, 0.290, 1)  # default color
            if loan_status[i] in ["under process", "Under Process", "UnderProcess"]:
                status_color = (253 / 255, 218 / 255, 13 / 255, 1)  # yellow
            elif loan_status[i] in ["Disbursed Loan", "disbursed loan", "disbursed", "Disbursed", "Disbursed loan",
                                    "disbursed Loan", "DisbursedLoan", "disbursedloan", "Disbursedloan",
                                    "disbursedLoan"]:
                status_color = (255 / 255, 88 / 255, 93 / 255, 1)  # pink
            elif loan_status[i] in ["closed", "Closed", "Closed loan", "closed Loan", "Closed Loan", "closed loan",
                                    "Closedloan", "closedLoan", "ClosedLoan", "closedloan"]:
                status_color = (0 / 255, 100 / 255, 0 / 255, 1)  # bottle-green
            elif loan_status[i] in ["extension", "Extension", "Extension Loan", "Extension loan", "extension loan",
                                    "extension Loan", "ExtensionLoan", "Extensionloan", "extensionloan",
                                    "extensionLoan"]:
                status_color = (255 / 255, 165 / 255, 0 / 255, 1)  # orange
            elif loan_status[i] in ["foreclosure", "Foreclosure", "Foreclosure Loan", "Foreclosure loan",
                                    "forclosure loan", "forclosure Loan", "ForeclosureLoan", "Foreclosureloan",
                                    "forclosureloan", "forclosureLoan"]:
                status_color = (0.424, 0.663, 0.859, 1.0)  # sky blue
            elif loan_status[i] in ["accepted", "Accepted", "Accepted loan", "Accepted Loan", "accepted loan",
                                    "accepted Loan", "Acceptedloan", "AcceptedLoan", "acceptedloan", "acceptedLoan"]:
                status_color = (0 / 255, 128 / 255, 0 / 255, 1)  # light green
            elif loan_status[i] in ["rejected", "Rejected", "rejected loan", "Rejected loan", "rejected Loan",
                                    "Rejected Loan", "rejectedloan", "Rejectedloan", "rejectedLoan", "RejectedLoan"]:
                status_color = (210 / 255, 4 / 255, 45 / 255, 1)  # cherry
            elif loan_status[i] in ["approved", "Approved", "approved loan", "Approved Loan", "approved Loan",
                                    "Approved loan", "approvedloan", "ApprovedLoan", "approvedLoan", "Approvedloan"]:
                status_color = (0 / 255, 128 / 255, 0 / 255, 1)  # light green
            elif loan_status[i] in ["decline", "declined", "Declined", "Decline"]:
                status_color = (210 / 255, 4 / 255, 45 / 255, 1)  # cherry

            status_text = {
                "under process": "Under Process",
                "disbursed loan": "Disburse Loan",
                "closed loan": "  Closed Loan  ",
                "extension": " Extension Loan ",
                "foreclosure": "   Foreclosure   ",
                "accepted": "Accepted Loan",
                "rejected": "Rejected Loan",
                "approved": "Approved Loan",
                "decline": "Declined Loan"
            }
            button1 = MDFillRoundFlatButton(
                text=status_text.get(loan_status[i], loan_status[i]),
                size_hint=(None, None),
                height="40dp",
                width="250dp",
                pos_hint={"center_x": 0},
                md_bg_color=status_color,
                # on_release=lambda x, i=i: self.close_loan(i)
            )
            button2 = MDFillRoundFlatButton(
                text="View Details",
                size_hint=(None, None),
                height="40dp",
                width="250dp",
                pos_hint={"center_x": 1},
                md_bg_color=(0.043, 0.145, 0.278, 1),
                on_release=lambda x, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id)
            )

            button_layout.add_widget(button1)
            button_layout.add_widget(button2)
            card.add_widget(button_layout)

            # card.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
            self.ids.container2.add_widget(card)

    def icon_button_clicked(self, instance, loan_id):
        data = app_tables.fin_loan_details.search()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = ViewLoansProfileScreens2(name='ViewLoansProfileScreens2')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ViewLoansProfileScreens2'
        self.manager.get_screen('ViewLoansProfileScreens2').initialize_with_value(loan_id, data)

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
        self.ids.container2.clear_widgets()
        self.__init__()


class ViewLoansScreen(Screen):

    def all_loanscreen(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

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
        Clock.schedule_once(lambda dt: self.performance_all_loanscreen(modal_view), 2)

    def performance_all_loanscreen(self, modal_view):
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = ALlLoansScreen(name='ALlLoansScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'ALlLoansScreen'


#     def go_to_open_loans(self):
#         modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])
#
#         # Create MDLabel with white text color, increased font size, and bold text
#         loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
#                                 theme_text_color="Custom", text_color=[1, 1, 1, 1],
#                                 font_size="50sp", bold=True)
#
#         # Set initial y-position off-screen
#         loading_label.y = -loading_label.height
#
#         modal_view.add_widget(loading_label)
#         modal_view.open()
#
#         # Perform the animation
#         self.animate_loading_text(loading_label, modal_view.height)
#
#         # Perform the actual action (e.g., fetching loan requests)
#         # You can replace the sleep with your actual logic
#         Clock.schedule_once(lambda dt: self.performance_go_to_open_loans(modal_view), 2)
#
#     def performance_go_to_open_loans(self, modal_view):
#         # self.manager.current = 'ViewProfileScreen'
#         modal_view.dismiss()
#         sm = self.manager
#
#         # Create a new instance of the LoginScreen
#         open = OpenViewLoanScreen(name='OpenViewLoanScreen')
#
#         # Add the LoginScreen to the existing ScreenManager
#         sm.add_widget(open)
#
#         # Switch to the LoginScreen
#         sm.current = 'OpenViewLoanScreen'
#
#     def go_to_rejected_loans(self):
#         modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])
#
#         # Create MDLabel with white text color, increased font size, and bold text
#         loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
#                                 theme_text_color="Custom", text_color=[1, 1, 1, 1],
#                                 font_size="50sp", bold=True)
#
#         # Set initial y-position off-screen
#         loading_label.y = -loading_label.height
#
#         modal_view.add_widget(loading_label)
#         modal_view.open()
#
#         # Perform the animation
#         self.animate_loading_text(loading_label, modal_view.height)
#
#         # Perform the actual action (e.g., fetching loan requests)
#         # You can replace the sleep with your actual logic
#         Clock.schedule_once(lambda dt: self.performance_go_to_rejected_loans(modal_view), 2)
#
#     def performance_go_to_rejected_loans(self, modal_view):
#         # self.manager.current = 'ViewProfileScreen'
#         modal_view.dismiss()
#         sm = self.manager
#
#         # Create a new instance of the LoginScreen
#         rejected = ViewRejectedLoansScreen(name='ViewRejectedLoansScreen')
#
#         # Add the LoginScreen to the existing ScreenManager
#         sm.add_widget(rejected)
#
#         # Switch to the LoginScreen
#         sm.current = 'ViewRejectedLoansScreen'
#
#     def go_to_under_process_loans(self):
#         modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])
#
#         # Create MDLabel with white text color, increased font size, and bold text
#         loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
#                                 theme_text_color="Custom", text_color=[1, 1, 1, 1],
#                                 font_size="50sp", bold=True)
#
#         # Set initial y-position off-screen
#         loading_label.y = -loading_label.height
#
#         modal_view.add_widget(loading_label)
#         modal_view.open()
#
#         # Perform the animation
#         self.animate_loading_text(loading_label, modal_view.height)
#
#         # Perform the actual action (e.g., fetching loan requests)
#         # You can replace the sleep with your actual logic
#         Clock.schedule_once(lambda dt: self.performance_go_to_under_process_loans(modal_view), 2)
#
#     def performance_go_to_under_process_loans(self, modal_view):
#         # self.manager.current = 'ViewProfileScreen'
#         modal_view.dismiss()
#         from lender_underprocess import ViewUnderProcess
#         sm = self.manager
#
#         # Create a new instance of the LoginScreen
#         under_process = ViewUnderProcess(name='ViewUnderProcess')
#
#         # Add the LoginScreen to the existing ScreenManager
#         sm.add_widget(under_process)
#
#         # Switch to the LoginScreen
#         sm.current = 'ViewUnderProcess'
#
#     def go_to_closed_loans(self):
#         modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])
#
#         # Create MDLabel with white text color, increased font size, and bold text
#         loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
#                                 theme_text_color="Custom", text_color=[1, 1, 1, 1],
#                                 font_size="50sp", bold=True)
#
#         # Set initial y-position off-screen
#         loading_label.y = -loading_label.height
#
#         modal_view.add_widget(loading_label)
#         modal_view.open()
#
#         # Perform the animation
#         self.animate_loading_text(loading_label, modal_view.height)
#
#         # Perform the actual action (e.g., fetching loan requests)
#         # You can replace the sleep with your actual logic
#         Clock.schedule_once(lambda dt: self.performance_go_to_closed_loans(modal_view), 2)
#
#     def performance_go_to_closed_loans(self, modal_view):
#         # self.manager.current = 'ViewProfileScreen'
#         modal_view.dismiss()
#         sm = self.manager
#
#         # Create a new instance of the LoginScreen
#         closed = ViewClosedLoansScreen(name='ViewClosedLoansScreen')
#
#         # Add the LoginScreen to the existing ScreenManager
#         sm.add_widget(closed)
#
#         # Switch to the LoginScreen
#         sm.current = 'ViewClosedLoansScreen'
#
#
# class OpenViewLoanScreen(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         data = app_tables.fin_loan_details.search()
#         profile = app_tables.fin_user_profile.search()
#         customer_id = []
#         loan_id = []
#         borrower_name = []
#         loan_status = []
#         product_name = []
#         s = 0
#         for i in data:
#             s += 1
#             customer_id.append(i['borrower_customer_id'])
#             loan_id.append(i['loan_id'])
#             borrower_name.append(i['borrower_full_name'])
#             loan_status.append(i['loan_updated_status'])
#             product_name.append(i['product_name'])
#
#         profile_customer_id = []
#         profile_mobile_number = []
#         for i in profile:
#             profile_customer_id.append(i['customer_id'])
#             profile_mobile_number.append(i['mobile'])
#         c = -1
#         index_list = []
#         for i in range(s):
#             c += 1
#             if loan_status[c] == 'disbursed':
#                 index_list.append(c)
#
#         b = 1
#         k = -1
#         for i in reversed(index_list):
#             b += 1
#             k += 1
#             if customer_id[i] in profile_customer_id:
#                 number = profile_customer_id.index(customer_id[i])
#             else:
#                 number = 0
#             item = ThreeLineAvatarIconListItem(
#
#                 IconLeftWidget(
#                     icon="card-account-details-outline"
#                 ),
#                 text=f"Borrower Name : {borrower_name[i]}",
#                 secondary_text=f"Borrower Mobile Number : {profile_mobile_number[number]}",
#                 tertiary_text=f"Product Name : {product_name[i]}",
#                 text_color=(0, 0, 0, 1),  # Black color
#                 theme_text_color='Custom',
#                 secondary_text_color=(0, 0, 0, 1),
#                 secondary_theme_text_color='Custom',
#                 tertiary_text_color=(0, 0, 0, 1),
#                 tertiary_theme_text_color='Custom'
#             )
#             item.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
#             self.ids.container1.add_widget(item)
#
#     def icon_button_clicked(self, instance, loan_id):
#         # Handle the on_release event here
#
#         data = app_tables.fin_loan_details.search()
#         sm = self.manager
#
#         # Create a new instance of the LoginScreen
#         profile = ViewLoansProfileScreens(name='ViewLoansProfileScreens')
#
#         # Add the LoginScreen to the existing ScreenManager
#         sm.add_widget(profile)
#
#         # Switch to the LoginScreen
#         sm.current = 'ViewLoansProfileScreens'
#         self.manager.get_screen('ViewLoansProfileScreens').initialize_with_value(loan_id, data)
#
#     def on_pre_enter(self):
#         # Bind the back button event to the on_back_button method
#         Window.bind(on_keyboard=self.on_back_button)
#
#     def on_pre_leave(self):
#         # Unbind the back button event when leaving the screen
#         Window.unbind(on_keyboard=self.on_back_button)
#
#     def on_back_button(self, instance, key, scancode, codepoint, modifier):
#         # Handle the back button event
#         if key == 27:  # 27 is the keycode for the hardware back button on Android
#             self.go_back()
#             return True  # Consume the event, preventing further handling
#         return False  # Continue handling the event
#
#     def go_back(self):
#         # Navigate to the previous screen with a slide transition
#         self.manager.transition = SlideTransition(direction='right')
#         sm = self.manager
#         profile = ViewLoansScreen(name='ViewLoansScreen')
#
#         # Add the LoginScreen to the existing ScreenManager
#         sm.add_widget(profile)
#
#         # Switch to the LoginScreen
#         sm.current = 'ViewLoansScreen'
#
#     def refresh(self):
#         self.ids.container1.clear_widgets()
#         self.__init__()


class ViewLoansProfileScreens(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_back_button_press(self):
        if self.ids.status.text == 'disbursed':
            self.manager.current = 'OpenViewLoanScreen'
        elif self.ids.status.text == 'rejected':
            self.manager.current = 'ViewRejectedLoansScreen'
        elif self.ids.status.text == 'under process':
            self.manager.current = 'ViewUnderProcessLoansScreen'
        elif self.ids.status.text == 'closed':
            self.manager.current = 'ViewClosedLoansScreen'

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
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        if self.ids.status.text == 'disbursed':
            self.manager.current = 'OpenViewLoanScreen'
        elif self.ids.status.text == 'rejected':
            self.manager.current = 'ViewRejectedLoansScreen'
        elif self.ids.status.text == 'under process':
            self.manager.current = 'ViewUnderProcessLoansScreen'
        elif self.ids.status.text == 'closed':
            self.manager.current = 'ViewClosedLoansScreen'


class ViewLoansProfileScreens2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_back_button_press(self):
        self.manager.current = 'ALlLoansScreen'

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
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')

        self.manager.current = 'ALlLoansScreen'


# class ViewRejectedLoansScreen(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         data = app_tables.fin_loan_details.search()
#         profile = app_tables.fin_user_profile.search()
#         customer_id = []
#         loan_id = []
#         borrower_name = []
#         loan_status = []
#         product_name = []
#         s = 0
#         for i in data:
#             s += 1
#             customer_id.append(i['borrower_customer_id'])
#             loan_id.append(i['loan_id'])
#             borrower_name.append(i['borrower_full_name'])
#             loan_status.append(i['loan_updated_status'])
#             product_name.append(i['product_name'])
#
#         profile_customer_id = []
#         profile_mobile_number = []
#         for i in profile:
#             profile_customer_id.append(i['customer_id'])
#             profile_mobile_number.append(i['mobile'])
#         c = -1
#         index_list = []
#         for i in range(s):
#             c += 1
#             if loan_status[c] == 'rejected':
#                 index_list.append(c)
#
#         b = 1
#         k = -1
#         for i in reversed(index_list):
#             b += 1
#             k += 1
#             if customer_id[i] in profile_customer_id:
#                 number = profile_customer_id.index(customer_id[i])
#             else:
#                 number = 0
#             item = ThreeLineAvatarIconListItem(
#
#                 IconLeftWidget(
#                     icon="card-account-details-outline"
#                 ),
#                 text=f"Borrower Name : {borrower_name[i]}",
#                 secondary_text=f"Borrower Mobile Number : {profile_mobile_number[number]}",
#                 tertiary_text=f"Product Name : {product_name[i]}",
#                 text_color=(0, 0, 0, 1),  # Black color
#                 theme_text_color='Custom',
#                 secondary_text_color=(0, 0, 0, 1),
#                 secondary_theme_text_color='Custom',
#                 tertiary_text_color=(0, 0, 0, 1),
#                 tertiary_theme_text_color='Custom'
#             )
#             item.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
#             self.ids.container4.add_widget(item)
#
#     def icon_button_clicked(self, instance, loan_id):
#         # Handle the on_release event here
#         data = app_tables.fin_loan_details.search()
#         sm = self.manager
#
#         # Create a new instance of the LoginScreen
#         profile = ViewLoansProfileScreens(name='ViewLoansProfileScreens')
#
#         # Add the LoginScreen to the existing ScreenManager
#         sm.add_widget(profile)
#
#         # Switch to the LoginScreen
#         sm.current = 'ViewLoansProfileScreens'
#         self.manager.get_screen('ViewLoansProfileScreens').initialize_with_value(loan_id, data)
#
#     def on_pre_enter(self):
#         # Bind the back button event to the on_back_button method
#         Window.bind(on_keyboard=self.on_back_button)
#
#     def on_pre_leave(self):
#         # Unbind the back button event when leaving the screen
#         Window.unbind(on_keyboard=self.on_back_button)
#
#     def on_back_button(self, instance, key, scancode, codepoint, modifier):
#         # Handle the back button event
#         if key == 27:  # 27 is the keycode for the hardware back button on Android
#             self.go_back()
#             return True  # Consume the event, preventing further handling
#         return False  # Continue handling the event
#
#     def go_back(self):
#         # Navigate to the previous screen with a slide transition
#         self.manager.transition = SlideTransition(direction='right')
#         self.manager.current = 'ViewLoansScreen'
#
#     def refresh(self):
#         self.ids.container4.clear_widgets()
#         self.__init__()
#
#
# class ViewClosedLoansScreen(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         data = app_tables.fin_loan_details.search()
#         profile = app_tables.fin_user_profile.search()
#         customer_id = []
#         loan_id = []
#         borrower_name = []
#         loan_status = []
#         product_name = []
#         s = 0
#         for i in data:
#             s += 1
#             customer_id.append(i['borrower_customer_id'])
#             loan_id.append(i['loan_id'])
#             borrower_name.append(i['borrower_full_name'])
#             loan_status.append(i['loan_updated_status'])
#             product_name.append(i['product_name'])
#
#         profile_customer_id = []
#         profile_mobile_number = []
#         for i in profile:
#             profile_customer_id.append(i['customer_id'])
#             profile_mobile_number.append(i['mobile'])
#         c = -1
#         index_list = []
#         for i in range(s):
#             c += 1
#             if loan_status[c] == 'closed':
#                 index_list.append(c)
#
#         b = 1
#         k = -1
#         for i in reversed(index_list):
#             b += 1
#             k += 1
#             if customer_id[i] in profile_customer_id:
#                 number = profile_customer_id.index(customer_id[i])
#             else:
#                 number = 0
#             item = ThreeLineAvatarIconListItem(
#
#                 IconLeftWidget(
#                     icon="card-account-details-outline"
#                 ),
#                 text=f"Borrower Name : {borrower_name[i]}",
#                 secondary_text=f"Borrower Mobile Number : {profile_mobile_number[number]}",
#                 tertiary_text=f"Product Name : {product_name[i]}",
#                 text_color=(0, 0, 0, 1),  # Black color
#                 theme_text_color='Custom',
#                 secondary_text_color=(0, 0, 0, 1),
#                 secondary_theme_text_color='Custom',
#                 tertiary_text_color=(0, 0, 0, 1),
#                 tertiary_theme_text_color='Custom'
#             )
#             item.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
#             self.ids.container6.add_widget(item)
#
#     def icon_button_clicked(self, instance, loan_id):
#         # Handle the on_release event here
#         data = app_tables.fin_loan_details.search()
#         sm = self.manager
#
#         # Create a new instance of the LoginScreen
#         profile = ViewLoansProfileScreens(name='ViewLoansProfileScreens')
#
#         # Add the LoginScreen to the existing ScreenManager
#         sm.add_widget(profile)
#
#         # Switch to the LoginScreen
#         sm.current = 'ViewLoansProfileScreens'
#         self.manager.get_screen('ViewLoansProfileScreens').initialize_with_value(loan_id, data)
#
#     def on_pre_enter(self):
#         # Bind the back button event to the on_back_button method
#         Window.bind(on_keyboard=self.on_back_button)
#
#     def on_pre_leave(self):
#         # Unbind the back button event when leaving the screen
#         Window.unbind(on_keyboard=self.on_back_button)
#
#     def on_back_button(self, instance, key, scancode, codepoint, modifier):
#         # Handle the back button event
#         if key == 27:  # 27 is the keycode for the hardware back button on Android
#             self.go_back()
#             return True  # Consume the event, preventing further handling
#         return False  # Continue handling the event
#
#     def go_back(self):
#         # Navigate to the previous screen with a slide transition
#         self.manager.transition = SlideTransition(direction='right')
#         self.manager.current = 'ViewLoansScreen'
#
#     def refresh(self):
#         self.ids.container6.clear_widgets()
#         self.__init__()
class MyScreenManager(ScreenManager):
    pass
