# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QDoubleSpinBox,
    QFrame,
    QLabel,
    QMainWindow,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QSpinBox,
    QStatusBar,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 644)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(70, 320, 49, 16))
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(130, 310, 531, 101))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(280, 450, 171, 61))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(120, 30, 501, 16))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(180, 60, 361, 41))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(True)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(180, 250, 411, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(460, 280, 241, 20))
        self.generando_label = QLabel(self.centralwidget)
        self.generando_label.setObjectName("generando_label")
        self.generando_label.setGeometry(QRect(140, 420, 511, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QRect(10, 560, 741, 16))
        font2 = QFont()
        font2.setPointSize(7)
        self.label_6.setFont(font2)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(10, 590, 771, 16))
        self.label_7.setFont(font2)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.label_8.setGeometry(QRect(50, 140, 161, 16))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.label_9.setGeometry(QRect(50, 120, 161, 16))
        self.cfg_doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.cfg_doubleSpinBox.setObjectName("cfg_doubleSpinBox")
        self.cfg_doubleSpinBox.setGeometry(QRect(240, 140, 88, 24))
        self.cfg_doubleSpinBox.setValue(7.000000000000000)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.label_10.setGeometry(QRect(50, 180, 161, 16))
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.label_11.setGeometry(QRect(50, 200, 171, 16))
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setGeometry(QRect(240, 200, 88, 24))
        self.spinBox.setValue(50)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.label_12.setGeometry(QRect(390, 150, 71, 16))
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.label_13.setGeometry(QRect(420, 170, 49, 16))
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.label_14.setGeometry(QRect(420, 190, 49, 16))
        self.height_spinBox_2 = QSpinBox(self.centralwidget)
        self.height_spinBox_2.setObjectName("height_spinBox_2")
        self.height_spinBox_2.setGeometry(QRect(480, 160, 88, 24))
        self.height_spinBox_2.setMaximum(5100)
        self.height_spinBox_2.setValue(512)
        self.width_spinBox_3 = QSpinBox(self.centralwidget)
        self.width_spinBox_3.setObjectName("width_spinBox_3")
        self.width_spinBox_3.setGeometry(QRect(480, 190, 88, 24))
        self.width_spinBox_3.setMaximum(5100)
        self.width_spinBox_3.setValue(512)
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.label_15.setGeometry(QRect(380, 130, 281, 16))
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.label_16.setGeometry(QRect(580, 170, 49, 16))
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.label_17.setGeometry(QRect(580, 190, 49, 16))
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.label_18.setGeometry(QRect(520, 430, 71, 16))
        self.device_label = QLabel(self.centralwidget)
        self.device_label.setObjectName("device_label")
        self.device_label.setGeometry(QRect(600, 430, 121, 16))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(50, 240, 671, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName("line_2")
        self.line_2.setGeometry(QRect(50, 100, 671, 16))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName("line_3")
        self.line_3.setGeometry(QRect(50, 530, 671, 16))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "Petici\u00f3n:", None)
        )
        self.plainTextEdit.setPlainText(
            QCoreApplication.translate(
                "MainWindow",
                "professional photo, photo of autumn landscape, dramatic lighting, gloomy, cloudy weather",
                None,
            )
        )
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", "GENERAR", None)
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow", "GENERACION DE IMAGENES CON EL MODELO PREENTRENADO", None
            )
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "MainWindow", "realisticVisionV60B1_v51HyperVAE", None
            )
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                "[SUJETO], [DESCRIPCI\u00d3N], [ESTILO], [CALIDAD], [ILUMINACI\u00d3N], [FONDOS]",
                None,
            )
        )
        self.label_5.setText(
            QCoreApplication.translate(
                "MainWindow",
                "(Ingl\u00e9s, no est\u00e1 bien entrenado para Espa\u00f1ol)",
                None,
            )
        )
        self.generando_label.setText(
            QCoreApplication.translate("MainWindow", "-", None)
        )
        self.label_6.setText(
            QCoreApplication.translate(
                "MainWindow", "Este modelo fue desarrollado por Stability AI. ", None
            )
        )
        self.label_7.setText(
            QCoreApplication.translate(
                "MainWindow",
                "[realisticVisionV60B1_v51HyperVAE] est\u00e1 disponible en [https://civitai.com/models/4201/realistic-vision-v60-b1] bajo la Open RAIL++-M License.",
                None,
            )
        )
        self.label_8.setText(
            QCoreApplication.translate(
                "MainWindow", "(CFG SCALE ) Guidance_scale:", None
            )
        )
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", "Recomendado: 3.5 - 7", None)
        )
        self.label_10.setText(
            QCoreApplication.translate("MainWindow", "Recomendado: 50", None)
        )
        self.label_11.setText(
            QCoreApplication.translate(
                "MainWindow", "N\u00famero de pasos de inferencia: ", None
            )
        )
        self.label_12.setText(
            QCoreApplication.translate("MainWindow", "Resoluci\u00f3n:", None)
        )
        self.label_13.setText(QCoreApplication.translate("MainWindow", "Alto:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", "Ancho:", None))
        self.label_15.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Recomendado:  [512x512] (m\u00e1s grande =  m\u00e1s lento)",
                None,
            )
        )
        self.label_16.setText(QCoreApplication.translate("MainWindow", "Height", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", "Width", None))
        self.label_18.setText(
            QCoreApplication.translate("MainWindow", "Cargado en: ", None)
        )
        self.device_label.setText(QCoreApplication.translate("MainWindow", "-", None))

    # retranslateUi
