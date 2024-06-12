from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle
import matplotlib.pyplot as plt
import numpy as np

class MatplotFigure(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fig, self.ax = plt.subplots()
        self.texture = None

    def draw_chart(self, data):
        self.ax.clear()
        labels = list(data.keys())
        values = list(data.values())

        bar_width = 0.35
        index = np.arange(len(labels))

        bars1 = self.ax.bar(index, [v['investment'] for v in values], bar_width, label='Investment')
        bars2 = self.ax.bar(index + bar_width, [v['my_returns'] for v in values], bar_width, label='My Returns')

        self.ax.set_xlabel('Loans')
        self.ax.set_ylabel('Amount')
        self.ax.set_title('Investment vs My Returns')
        self.ax.set_xticks(index + bar_width / 2)
        self.ax.set_xticklabels(labels)
        self.ax.legend()

        self.fig.canvas.draw()
        self.update_graph()

    def update_graph(self):
        print("Updating graph")
        texture = Texture.create(size=(self.fig.canvas.get_width_height()), colorfmt='rgb')
        texture.blit_buffer(self.fig.canvas.tostring_rgb(), colorfmt='rgb', bufferfmt='ubyte')
        self.texture = texture

        with self.canvas:
            self.canvas.clear()
            Rectangle(texture=self.texture, pos=self.pos, size=self.size)

    def on_size(self, *args):
        if self.texture:
            self.update_graph()
