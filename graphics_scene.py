from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class QDMGraphicsScene(QGraphicsScene):
    def __init__(self,parent=None):

        super().__init__(parent)
        self.grScene = grScene

        self.initUI()

        self.setScene(self.grScene)

        self.mode = MODE_NOOP
        self.editingFlag = False
        self.rubberBandDraggingRectangle = False

        self.zoomInFactor = 1.25
        self.zoomClamp = True
        self.zoom = 10
        self.zoomStep = 1
        self.zoomRange = [0, 10]

        # cutline
        self.cutline = QDMCutLine()
        self.grScene.addItem(self.cutline)

        # listeners
        self._drag_enter_listeners = []
        self._drop_listeners = []

