#  #! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from frame_gui import Ui_Dialog
# import rospy
# from geometry_msgs.msg import Twist
# import rospkg
from subprocess import *
# import rosnode
import math
import numpy as np
import cv2

class Test(QDialog):
    def __init__(self,parent=None):
        # GUI。
        super(Test, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # p = self.palette()
        # p.setColor(self.backgroundRole(), Qt.lightGray)
        # self.setPalette(p)
        self.ui.dial.setMinimum(0)
        self.ui.dial.setMaximum(360)
        self.ui.dial.setValue(180)
        self.ui.dial.valueChanged.connect(self.sliderMoved)
        self.init_draw()
        self.img_draw(180)


    def init_draw(self):
        qimg = QImage(self.ui.show_img, self.ui.show_img.shape[1], self.ui.show_img.shape[0], QImage.Format_RGB888)
        self.ui.imageLabel.setPixmap(QPixmap.fromImage(qimg))

    def sliderMoved(self):
    	value = self.ui.dial.value() - 180
        self.ui.label.setText(str(value))
        self.img_draw(value)

    def img_draw(self, angle):
        L_p = [-330,0]
        R_p = [330,0]
        x, y = self.cal_rot(L_p, R_p, angle)
        img = np.copy(self.ui.show_img)
        cv2.line(img, (x[0][0], y[0][0]), (x[1][0], y[1][0]), (255, 0, 0), thickness=1, lineType=cv2.LINE_8)
        qimg = QImage(img, self.ui.show_img.shape[1], self.ui.show_img.shape[0], QImage.Format_RGB888)
        # self.uic.imageLabel.setWindowOpacity(0.8)
        self.ui.imageLabel.setPixmap(QPixmap.fromImage(qimg))

    def cal_rot(self, left, right, ang):
        x = [[0],[0]]
        y = [[0],[0]]
        center = [[self.ui.show_img.shape[1]/2],[20 + self.ui.show_img.shape[0]/2 - 20]]
        # center = [[0],[0]]
        x[0][0] = int(left[0] * math.cos(math.radians(ang)) - left[1] * math.sin(math.radians(ang)))
        y[0][0] = int(left[0] * math.sin(math.radians(ang)) + left[1] * math.cos(math.radians(ang)))
        x[1][0] = int(right[0] * math.cos(math.radians(ang)) - right[1] * math.sin(math.radians(ang)))
        y[1][0] = int(right[0] * math.sin(math.radians(ang)) + right[1] * math.cos(math.radians(ang)))
        x[0][0] += center[0][0]
        y[0][0] += center[1][0]
        x[1][0] += center[0][0]
        y[1][0] += center[1][0]
        return x, y

if __name__ == '__main__':
    # rospy.init_node('turtlesim_talker')
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
