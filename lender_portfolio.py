from anvil import Label
from anvil.tables import app_tables
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.base import runTouchApp
from kivy.properties import ListProperty, NumericProperty, ColorProperty
from kivy.clock import Clock
from kivy.utils import get_color_from_hex

import numpy as np
from math import sin, cos
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.utils import platform
from kivy.clock import mainthread
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle
import matplotlib.pyplot as plt
from kivy.core.image import Image as CoreImage
import matplotlib.pyplot as plt
import io
from kivy.factory import Factory
from kivy.properties import ListProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget

from datetime import datetime

borrower_portfolio = '''
<WindowManager>:
    Lend_Portfolio:
    LenViewPortfolio:

<Lend_Portfolio>:

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

<LenViewPortfolio>:

    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Portfolio"
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
                MDBoxLayout:
                    orientation: "vertical"
                    size_hint_x: None
                    spacing:dp(5)
                    size_hint_y: None
                    height: dp(660)
                    width:dp(800)
                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                    MDLabel:
                        text: "Ascend Score Summary" 
                        size_hint_y:None
                        font_style: "H6"
                        bold: True
                        height:dp(30)
                        font_size: dp(22)
                        halign: "center" 
                    Gauge:
                        id: gauge

                        size_hint: None, None
                        size: dp(200), dp(200)
                        fill_fraction: 0.4  # Default value
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: dp(15)
                        padding: dp(1)
                        size_hint: None, None
                        height:dp(-120)
                        width:dp(200)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                    MDLabel:
                        id:ascend_percentage
                        text: " "
                        size_hint_y:None
                        bold: True
                        height:dp(0)
                        font_size: dp(25)
                        halign: "center"


                    MDLabel:
                        id:status
                        text: "fwrfwf" 
                        size_hint_y:None
                        height:dp(43)
                        bold: True
                        font_size: dp(20)
                        halign: "center" 
                    MDBoxLayout:
                        orientation: "horizontal"
                        spacing: dp(1)
                        padding: dp(1)
                        size_hint: None, None
                        height:dp(20)
                        width:dp(200)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                        MDLabel:
                            text: "0" 
                            size_hint_y:None
                            height:dp(-10)

                            font_size: dp(22)
                            halign: "center"
                        MDLabel:

                            text: "100" 
                            size_hint_y:None
                            height:dp(-10)
                            font_size: dp(22)
                            halign: "center" 
                    MDBoxLayout:
                        orientation: "horizontal"
                        spacing: dp(1)
                        padding: dp(1)
                        size_hint: None, None
                        height:dp(80)
                        width:dp(400)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        MDLabel:
                            text: "Borrower Financial Overview" 
                            size_hint_y:None
                            font_style: "H6"
                            bold: True
                            spacing:dp(20)
                            padding:dp(20)
                            height:dp(40)
                            font_size: dp(22)
                            halign: "center"  
                    PieChartWidget:
                        id: chart_widget
                        size_hint: None, None
                        size: dp(400), dp(400)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}





<Gauge>:
    on_size: self.recalculate_lines()
    on_pos: self.recalculate_lines()
    on_fill_fraction: self.recalculate_lines()
    canvas:
        Color:
            rgba: 0.7, 0.7, 0.7, 1
        Line:
            points: self.line_points
            width: self.height * 0.03
        Color:
            rgba: self.color
        Line:
            points: self.filled_in_points
            width: self.height * 0.03


'''
Builder.load_string(borrower_portfolio)
date = datetime.today()
print(date)


class Gauge(Widget):
    line_points = ListProperty([])
    filled_in_points = ListProperty([])
    fill_fraction = NumericProperty(0.4)
    color = ColorProperty([1, 1, 1, 1])

    def __init__(self, **kwargs):
        super(Gauge, self).__init__(**kwargs)
        self.bind(fill_fraction=self.update_color)
        Clock.schedule_once(self.recalculate_lines, 0)

    def recalculate_lines(self, *args):
        centre_x, centre_y = self.center
        radius = self.height * 0.4
        start_angle = np.radians(220)
        end_angle = np.radians(-40)
        angles = np.linspace(start_angle, end_angle, 1000)

        line_points = []
        for angle in angles:
            line_points.append((cos(angle) * radius, sin(angle) * radius))

        self.line_points = [(x + centre_x, y + centre_y) for x, y in line_points]
        self.filled_in_points = self.line_points[:int(self.fill_fraction * len(self.line_points))]

    def update_color(self, *args):
        score = self.fill_fraction * 100
        if score > 65:
            self.color = [0, 1, 0, 1]  # Green
        elif 50 < score <= 65:
            self.color = [1, 0.5, 0, 1]  # Orange
        elif 25 < score <= 50:
            self.color = [1, 0.5, 0, 1]  # Orange
        else:
            self.color = [1, 0, 0, 1]  # Red


class WindowManager(ScreenManager):
    pass


class Lend_Portfolio(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.populate_lender_list()

    def populate_lender_list(self):
        data = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()

        borrower_details = {}

        for loan in data:
            if loan['loan_updated_status'] in ['disbursed', 'foreclosure', 'extension']:
                borrower_id = loan['borrower_customer_id']
                if borrower_id not in borrower_details:
                    borrower_details[borrower_id] = {
                        'full_name': loan['borrower_full_name'],
                        'mobile_number': '',
                        'product_name': loan['product_name']
                    }

        for prof in profile:
            if prof['customer_id'] in borrower_details:
                borrower_details[prof['customer_id']]['mobile_number'] = prof['mobile']

        for borrower_id, details in borrower_details.items():
            item = ThreeLineAvatarIconListItem(
                IconLeftWidget(icon="account"),
                text=f"Borrower Name: {details['full_name']}",
                secondary_text=f"Borrower Mobile Number: {details['mobile_number']}",
                tertiary_text=f"Product Name: {details['product_name']}",
                text_color=(0, 0, 0, 1),
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0, 0, 0, 1),
                tertiary_theme_text_color='Custom'
            )
            item.bind(
                on_release=lambda instance, borrower_id=borrower_id: self.icon_button_clicked(instance, borrower_id))
            self.ids.container.add_widget(item)

    def icon_button_clicked(self, instance, borrower_id):
        sm = self.manager
        approved = LenViewPortfolio(name='LenViewPortfolio')
        sm.add_widget(approved)
        sm.current = 'LenViewPortfolio'
        self.manager.get_screen('LenViewPortfolio').initialize_with_value(borrower_id)

    def go_back(self):
        self.manager.current = 'LenderDashboard'

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


class PieChartWidget(MDBoxLayout):
    def __init__(self, **kwargs):
        super(PieChartWidget, self).__init__(**kwargs)
        self.chart_image = Image(allow_stretch=True, size_hint=(5.5, 1))
        self.add_widget(self.chart_image)
        self.plot_pie_chart()

    def plot_pie_chart(self):
        Marks = [67, 88, 63, 77, 20]
        Subject = ['Available Balance', 'No of loans closed', 'No of loans open', 'Total loan amount taken',
                   'My Commitments']
        plt.axis("equal")
        plt.pie(Marks, labels=Subject, explode=[0, 0, 0, 0, 0.2], autopct="%1.2f%%")

        # Convert matplotlib plot to texture
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        im = CoreImage(buf, ext='png').texture
        plt.close()

        # Display the plot
        self.chart_image.texture = im


class LenViewPortfolio(Screen):
    def go_back(self):
        self.manager.current = 'Lend_Portfolio'

    def initialize_with_value(self, borrower_id):
        profile = app_tables.fin_user_profile.get(customer_id=borrower_id)

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
            # Update the gauge widget color based on ascend_value
            ascend_value = profile['ascend_value']
            self.ids.ascend_percentage.text = f"{profile['ascend_value']}%"
            gauge_widget = self.ids.gauge
            gauge_widget.fill_fraction = ascend_value / 100  # Assuming ascend_value is a percentage

            if ascend_value > 65:
                self.ids.status.text = "Very Good"
                self.ids.status.color = get_color_from_hex('#00FF00')  # Green
            elif 50 < ascend_value <= 65:
                self.ids.status.text = "Good"
                self.ids.status.color = get_color_from_hex('#FFFF00')  # Orange
            elif 25 < ascend_value <= 50:
                self.ids.status.text = "Average"
                self.ids.status.color = get_color_from_hex('#FFA500')  # Orange
            else:
                self.ids.status.text = "Bad"
                self.ids.status.color = get_color_from_hex('#FF0000')  # Red