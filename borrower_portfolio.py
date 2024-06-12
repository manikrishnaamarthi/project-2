from anvil import Label
from anvil.tables import app_tables
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.progressbar import MDProgressBar

from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import *
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.utils import platform
from kivy.clock import mainthread
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle
import matplotlib.pyplot as plt
from kivy.graphics import Color, Rectangle, Line
from kivy.core.text import Label as CoreLabel
import numpy as np
from matplot_figure import MatplotFigure
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.progressbar import MDProgressBar
from datetime import datetime

borrower_portfolio = '''
<WindowManager>:
    LenderDetails:
    ViewPortfolio:

<LenderDetails>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Lender Details"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'left'
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:
            MDList:
                id: container

<ViewPortfolio>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Lender Portfolio"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            title_align: 'left'
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding:dp(10)
                spacing:dp(25)
                size_hint_y: None
                height: self.minimum_height
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(20)

                    BoxLayout:
                        id: box1
                        orientation: 'vertical'
                        size_hint_y: None
                        height: dp(800)
                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1
                            Line:
                                width: 0.25
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                        MDBoxLayout:
                            orientation: "vertical"
                            pos_hint: {"top": 1}

                            spacing: dp(5)
                            padding:dp(10)
                            size_hint_y: None
                            height: dp(100)
                            spacing:
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1
                                Line:
                                    width: 0.1
                                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                            text_size: self.width - dp(20), None

                            Image:
                                id: selected_image1
                                source: 'background.jpg'
                                halign: 'center'
                                valign: 'middle'
                                size_hint_x: None
                                allow_stretch: True
                                keep_ratio: True
                                width: dp(20)
                                spacing: dp(30)
                                padding: dp(30)
                                height:dp(20)
                                theme_text_color: 'Custom'
                                text_color: 0.043, 0.145, 0.278, 1
                                size: dp(60), dp(20)
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                                canvas.before:
                                    Color:
                                        rgba: 1, 1, 1, 1

                                canvas:
                                    StencilPush
                                    Ellipse:
                                        size: self.width + 15, self.height + 8
                                        pos: self.x -5, self.y -5
                                    StencilUse
                                    RoundedRectangle:
                                        texture: self.texture
                                        size: self.width + 25, self.height + 15
                                        pos: self.x -5, self.y -5

                                    StencilUnUse
                                    StencilPop

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Full Name" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: full_name      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"                    
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Mobile Number" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: mobile_number      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Date of Birth" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: date_of_birth      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Gender" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: gender      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Marital Status" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: marital_status      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Type of Address" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: type_of_address      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Qualification" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: qualification      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Profession" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: profession      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Annual Salary" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: annual_salary      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"  

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Membership Type" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: membership      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"         
                                color: (0, 0, 0, 1)
                                font_size: dp(19)
                                bold: True

                    # Heading for Chart
                    MDLabel:
                        text: "Financial Status Overview"
                        size_hint_y: None
                        height: dp(60)  # Increased height to add space
                        bold: True
                        font_style: "H6"
                        halign: "center"
                        valign: "middle"
                        padding_y: dp(10)



                    AnchorLayout:
                        size_hint_y: None
                        height: dp(380)  # Decreased height to reduce space
                        padding: dp(10)
                        anchor_x: 'center'
                        anchor_y: 'center'
                        BoxLayout:
                            id: chart_container
                            orientation: "horizontal"
                            padding: dp(10)
                            spacing: dp(40)

                    BoxLayout:
                        orientation: 'horizontal'
                        spacing: dp(20)  # Spacing between the two columns
                        size_hint_y: None
                        height: dp(40)
                        padding: dp(10)

                        # Column 1: Investment
                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(5)  # Space between the widget and label
                            size_hint_y: None
                            height: dp(40)
                            Widget:
                                size_hint_x: None
                                width: dp(13)
                                size_hint_y: None
                                height: dp(13)
                                canvas:
                                    Color:
                                        rgba: 0, 1, 0, 1  # Green color
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                            MDLabel:
                                text: "Investment"
                                halign: 'left'
                                valign: 'middle'
                                size_hint_y: None
                                height: dp(13)

                        # Column 2: Returns
                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(5)  # Space between the widget and label
                            size_hint_y: None
                            height: dp(40)
                            Widget:
                                size_hint_x: None
                                width: dp(13)
                                size_hint_y: None
                                height: dp(13)
                                canvas:
                                    Color:
                                        rgba: 1, 0, 0, 1  # Red color
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                            MDLabel:
                                text: "Returns"
                                halign: 'left'
                                valign: 'middle'
                                size_hint_y: None
                                height: dp(13)

'''
Builder.load_string(borrower_portfolio)
date = datetime.today()
print(date)


class WindowManager(ScreenManager):
    pass


class LenderDetails(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.populate_lender_list()

    def populate_lender_list(self):
        data = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()

        lender_details = {}

        for loan in data:
            if loan['loan_updated_status'] in ['disbursed', 'foreclosure', 'extension']:
                lender_id = loan['lender_customer_id']
                if lender_id not in lender_details:
                    lender_details[lender_id] = {
                        'full_name': loan['lender_full_name'],
                        'mobile_number': '',
                        'product_name': loan['product_name']
                    }

        for prof in profile:
            if prof['customer_id'] in lender_details:
                lender_details[prof['customer_id']]['mobile_number'] = prof['mobile']

        for lender_id, details in lender_details.items():
            item = ThreeLineAvatarIconListItem(
                IconLeftWidget(icon="account"),
                text=f"Lender Name: {details['full_name']}",
                secondary_text=f"Lender Mobile Number: {details['mobile_number']}",
                tertiary_text=f"Product Name: {details['product_name']}",
                text_color=(0, 0, 0, 1),
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0, 0, 0, 1),
                tertiary_theme_text_color='Custom'
            )
            item.bind(on_release=lambda instance, lender_id=lender_id: self.icon_button_clicked(instance, lender_id))
            self.ids.container.add_widget(item)

    def icon_button_clicked(self, instance, lender_id):
        sm = self.manager
        approved = ViewPortfolio(name='ViewPortfolio')
        sm.add_widget(approved)
        sm.current = 'ViewPortfolio'
        self.manager.get_screen('ViewPortfolio').initialize_with_value(lender_id)

    def go_back(self):
        self.manager.current = 'DashboardScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def refresh(self):
        self.ids.container.clear_widgets()
        self.__init__()


class HorizontalLinesAndBarsWidget(Widget):
    def __init__(self, investment_percentage, return_percentage, investment_amount, return_amount, bar_width=dp(50),
                 bar_spacing=dp(10), **kwargs):
        super().__init__(**kwargs)
        self.investment_percentage = investment_percentage
        self.return_percentage = return_percentage
        self.investment_amount = investment_amount
        self.return_amount = return_amount
        self.bar_width = bar_width
        self.bar_spacing = bar_spacing
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.clear()
        step = 20  # Draw lines every 20%
        margin = dp(10)
        bar_total_width = self.bar_width * 2 + self.bar_spacing  # Total width for two bars and spacing
        bar_start_x = self.center_x - bar_total_width / 2
        with self.canvas:
            Color(0.8, 0.8, 0.8, 1)  # Cement color for lines
            for i in range(0, 101, step):
                line_y = self.y + (i / 100) * self.height
                Line(points=[self.x, line_y, self.right, line_y], width=1)

                # Label for percentage
                line_percentage_text = f"{i}%"
                line_label = CoreLabel(text=line_percentage_text, font_size=dp(12),
                                       color=(0, 0, 0, 1))  # Black color for text
                line_label.refresh()
                line_text_width, line_text_height = line_label.texture.size
                line_text_x = self.x - line_text_width - dp(5)  # Position to the left of the widget
                line_text_y = line_y - line_text_height / 2
                Rectangle(texture=line_label.texture, pos=(line_text_x, line_text_y), size=line_label.texture.size)

            # Draw investment bar
            investment_bar_height = self.height * self.investment_percentage / 100
            Color(0, 1, 0, 1)  # Green color for investment bar
            Rectangle(pos=(bar_start_x, self.y), size=(self.bar_width, investment_bar_height))

            # Draw return bar
            return_bar_height = self.height * self.return_percentage / 100
            Color(1, 0, 0, 1)  # Red color for return bar
            Rectangle(pos=(bar_start_x + self.bar_width + self.bar_spacing, self.y),
                      size=(self.bar_width, return_bar_height))

            # Label for investment amount
            investment_amount_text = f"₹{self.investment_amount}"  # Add label prefix
            investment_label = CoreLabel(text=investment_amount_text, font_size=dp(12),
                                         color=(0, 0, 0, 1))  # Black color for text
            investment_label.refresh()
            investment_text_width, investment_text_height = investment_label.texture.size
            investment_text_x = bar_start_x + (self.bar_width - investment_text_width) / 2
            investment_text_y = self.y + investment_bar_height + dp(5)
            Rectangle(texture=investment_label.texture, pos=(investment_text_x, investment_text_y),
                      size=investment_label.texture.size)

            # Label for return amount
            return_amount_text = f"₹{self.return_amount}"  # Add label prefix
            return_label = CoreLabel(text=return_amount_text, font_size=dp(12),
                                     color=(0, 0, 0, 1))  # Black color for text
            return_label.refresh()
            return_text_width, return_text_height = return_label.texture.size
            return_text_x = bar_start_x + self.bar_width + self.bar_spacing + (self.bar_width - return_text_width) / 2
            return_text_y = self.y + return_bar_height + dp(5)
            Rectangle(texture=return_label.texture, pos=(return_text_x, return_text_y), size=return_label.texture.size)


class ViewPortfolio(Screen):
    def go_back(self):
        self.manager.current = 'LenderDetails'

    def initialize_with_value(self, lender_id):
        profile = app_tables.fin_user_profile.get(customer_id=lender_id)

        if profile:
            self.ids.full_name.text = f"{profile['full_name']}"
            self.ids.mobile_number.text = f"{profile['mobile']}"
            self.ids.date_of_birth.text = f"{profile['date_of_birth']}"
            self.ids.gender.text = f"{profile['gender']}"
            self.ids.marital_status.text = f"{profile['marital_status']}"
            self.ids.type_of_address.text = f"{profile['present_address']}"
            self.ids.qualification.text = f"{profile['qualification']}"
            self.ids.profession.text = f"{profile['profession']}"
            self.ids.annual_salary.text = f"{profile['annual_salary']}"

            lender_data = app_tables.fin_lender.get(customer_id=lender_id)
            if lender_data:
                membership = lender_data['membership']
                membership_color = {
                    'silver': (255 / 255, 255 / 255, 0 / 255, 1),   # Yellow
                    'gold': (255 / 255, 165 / 255, 0 / 255, 1),     # Orange
                    'platinum': (0 / 255, 128 / 255, 0 / 255, 1)    # Green
                }.get(membership.lower(), (0, 0, 0, 1))  # Default to black if no match

                self.ids.membership.text = membership.capitalize()
                self.ids.membership.theme_text_color = 'Custom'
                self.ids.membership.text_color = membership_color

                all_lenders = app_tables.fin_lender.search()
                if all_lenders:
                    max_commitments = max(lender['lender_total_commitments'] for lender in all_lenders)

                    total_commitments = lender_data['lender_total_commitments']
                    return_on_investment = lender_data['return_on_investment']

                    if max_commitments > 0:
                        investment_percentage = (total_commitments / max_commitments) * 100
                    else:
                        investment_percentage = 0

                    if total_commitments > 0:
                        return_percentage = (return_on_investment / total_commitments) * 100
                    else:
                        return_percentage = 0

                    investment_amount = lender_data['lender_total_commitments']  # Assuming this is the column name
                    return_amount = lender_data['return_on_investment']  # Assuming this is the column name

                    chart_widget = HorizontalLinesAndBarsWidget(investment_percentage, return_percentage,
                                                                investment_amount, return_amount,
                                                                bar_width=dp(90), bar_spacing=dp(20))

                    self.ids.chart_container.clear_widgets()
                    self.ids.chart_container.add_widget(chart_widget)