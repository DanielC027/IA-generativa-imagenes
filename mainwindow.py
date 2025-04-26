from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Slot
from mainwindow_ui import Ui_MainWindow
import threading
import random
import os

from generative_ai import ImageGenerationThread


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.promptList = [
            "professional photo, photo of autumn landscape, dramatic lighting, gloomy, cloudy weather",
            "Modern tropical house exterior, luxurious entrance with wide marble steps, stone and wood facade, large glass doors opening to a lush interior, tropical plants, warm ambient lighting, high-resolution, ultra-realistic render, architectural visualization, photorealistic, golden hour lighting.",
            "unreal engine 5 render, jungle, river, flowers, extremely detailed, colorful",
            "UHD, 8K, ultra detailed, a cinematic photograph of hyperrealistic art (Photorealistic:1.2), alaska paradise",
        ]
        i = random.randint(0, 3)
        prompt_show = self.promptList[i]
        self.ui.plainTextEdit.setPlainText("")
        self.ui.plainTextEdit.setPlainText(prompt_show)

        self.ui.pushButton.clicked.connect(self.generateImage)

    @Slot()
    def generateImage(self):
        try:
            prompt = self.ui.plainTextEdit.toPlainText()
            print(prompt)
            cfg = self.ui.cfg_doubleSpinBox.value()
            steps = self.ui.spinBox.value()
            height = self.ui.height_spinBox_2.value()
            width = self.ui.width_spinBox_3.value()

            if prompt == "" or cfg == 0 or steps == 0 or height == 0 or width == 0:
                message = "Peticion vacia o incorrecta!"
                alerta = QMessageBox()
                alerta.setWindowTitle("Alerta")
                alerta.setText(message)
                alerta.setIcon(QMessageBox.Warning)
                alerta.setStandardButtons(QMessageBox.Ok)
                alerta.exec()

            else:
                self.createImage(prompt, cfg, steps, height, width)

        except Exception as e:
            print(e)

    def createImage(self, prompt, cfg, steps, height, width):
        # Ruta del modelo (asegúrate de que es la correcta)
        model_path = "./realisticVisionV60B1_v51HyperVAE.safetensors"
        # Crear el hilo para la generación de imágenes
        self.thread = ImageGenerationThread(
            model_path, prompt, cfg, steps, height, width
        )

        # Conectar señales del hilo a métodos
        self.thread.device_used.connect(self.on_device_used)
        self.thread.image_generated.connect(self.on_image_generated)
        self.thread.error_occurred.connect(self.on_error)

        # Iniciar el hilo
        self.thread.start()

        # Cambiar el texto mientras se genera la imagen
        self.ui.generando_label.setText(
            "Generando...(esto puede tardar algunos minutos)"
        )

    def on_device_used(self, device):
        self.ui.device_label.setText(device)

    def on_image_generated(self, path):
        message = "Generación exitosa!! "
        self.ui.generando_label.setText(message)
        alerta = QMessageBox()
        alerta.setWindowTitle("Alerta")
        alerta.setText(message + path)
        alerta.setIcon(QMessageBox.Warning)
        alerta.setStandardButtons(QMessageBox.Ok)
        alerta.exec()

    def on_error(self, message):
        print(message)
        self.ui.generando_label.setText(message)
        alerta = QMessageBox()
        alerta.setWindowTitle("Error")
        alerta.setText(message)
        alerta.setIcon(QMessageBox.Critical)
        alerta.setStandardButtons(QMessageBox.Ok)
        alerta.exec()
