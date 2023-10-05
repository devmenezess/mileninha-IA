from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QMovie
from rich import print
from PyQt5 import QtWidgets

import sys
# import datetime
import psutil
# import time
# import os
import speech_recognition as sr
# import threading

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)
        self.resize(100, 410)

        self.background_label = QtWidgets.QLabel(self)
        movie = QtGui.QMovie("img/LCPT.gif")
        movie.setScaledSize(QtCore.QSize(500, 380))  # Define o tamanho como 100x400
        self.background_label.setMovie(movie)
        movie.start()

        # Centraliza a imagem dentro da QLabel
        self.background_label.setAlignment(QtCore.Qt.AlignCenter)

        # Arredonda as bordas da janela
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        layout.addWidget(self.background_label)
        self.voice_label = QtWidgets.QLabel(self)
        self.voice_label.setText("Fala: ")
        self.voice_label.setWordWrap(True)
        layout.addWidget(self.voice_label)

        self.label_sara = QLabel(self)
        self.label_sara.setText("Mileninha")
        self.label_sara.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sara.move(10, 10)
        self.label_sara.setStyleSheet(
            'QLabel {font:bold;font-size:40px;color:#ffffff}')
        self.label_sara.resize(520, 355)

        self.label_sara = QLabel(self)
        self.label_sara.setText("❤")
        self.label_sara.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sara.move(172, 160)
        self.label_sara.setStyleSheet(
            'QLabel {font:arial;font-size:20px;color:#1E90FF}')
        self.label_sara.resize(230, 30)

        # Initialize the speech recognition engine
        self.recognizer = sr.Recognizer()

        # Start a thread to continuously listen to the microphone
        self.listen_thread = ListenThread(
            self.recognizer, self.update_voice_label)
        self.listen_thread.start()

    def MostrarHorras(self):
        hora_atual = QTime.currentTime()
        label_time = hora_atual.toString('hh:mm:ss')
        self.label_horas.setText(label_time)

    def update_voice_label(self, recognized_text):
        # Update the voice label with recognized speech
        self.voice_label.setText(f"Fala: {recognized_text}")

class ListenThread(QThread):
    def __init__(self, recognizer, callback):
        super().__init__()
        self.recognizer = recognizer
        self.callback = callback

    def run(self):
        while True:
            try:
                with sr.Microphone() as source:
                    audio = self.recognizer.listen(source)
                recognized_text = self.recognizer.recognize_google(
                    audio, language='pt-BR')
                print('Fala: %s' % recognized_text)
                self.callback(recognized_text)
            except Exception as e:
                self.callback("")


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


