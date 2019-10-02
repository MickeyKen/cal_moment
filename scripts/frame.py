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

class Test(QDialog):
    def __init__(self,parent=None):
        # GUI。
        super(Test, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # p = self.palette()
        # p.setColor(self.backgroundRole(), Qt.lightGray)
        # self.setPalette(p)
        self.init_draw()


    def init_draw(self):
        qimg = QImage(self.ui.show_img, self.ui.show_img.shape[1], self.ui.show_img.shape[0], QImage.Format_RGB888)
        self.ui.imageLabel.setPixmap(QPixmap.fromImage(qimg))




if __name__ == '__main__':
    # rospy.init_node('turtlesim_talker')
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
