# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'force_moment.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
import numpy as np
import cv2

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 500)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(340, 440, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.dial = QtWidgets.QDial(Dialog)
        self.dial.setGeometry(QtCore.QRect(340, 350, 111, 131))
        self.dial.setObjectName("dial")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 370, 160, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSlider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.verticalSlider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout.addWidget(self.verticalSlider)

        self.imageLabel = QtWidgets.QLabel(Dialog)
        self.imageLabel.move(20,20)
        self.imageLabel.setMouseTracking(True)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(445, 450, 50, 25))
        self.label.setObjectName("label")

        self.show_img = np.zeros((300,660,3), dtype=np.uint8)
        self.show_img.fill(255)
        cv2.circle(self.show_img, (self.show_img.shape[1]/2, self.show_img.shape[0]/2), 7, (0, 0, 0), thickness=-1)
        cv2.circle(self.show_img, (self.show_img.shape[1]/2, self.show_img.shape[0]/2), 10, (0, 0, 0), thickness=2)
        qimg = QImage(self.show_img, self.show_img.shape[1], self.show_img.shape[0], QImage.Format_RGB888)
        # self.uic.imageLabel.setWindowOpacity(0.8)
        self.imageLabel.setPixmap(QPixmap.fromImage(qimg))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
