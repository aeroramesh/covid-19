from PyQt5.QtWidgets import *
from graphics_scene import QDMGraphicsScene


class prop_wnd(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # Create Graphic scene

        self.grScene = QDMGraphicsScene()

        self.view = QGraphicsView(self)
        self.view.setScene(self.grScene)
        # self.layout =

        self.layout.addWidget(self.view)




