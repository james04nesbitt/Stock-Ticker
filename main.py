from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys
import stocks






class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Ticker")
        self.setStyleSheet('background-color:gray')
        self.setFixedHeight(600)
        self.setFixedWidth(600)

        layout = QVBoxLayout()
        self.setLayout(layout)

        title = QLabel("STOCK WATCHLIST")
        subtitle = QLabel("Enter the ticker of the stock you want to look up")
        title.setStyleSheet('font-size:16px;')
        self.stock_price = QLabel(" ")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stock_price.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet('font-size:30px; color:purple')
        self.stock_price.setStyleSheet('font-size: 20px; color: purple')

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.stock_price)

        self.input = QLineEdit(self)
        self.input.setFixedWidth(75)
        self.input.setStyleSheet('background-color:white; color:purple')
        layout.addWidget(self.input, alignment=Qt.AlignmentFlag.AlignCenter)

        btn = QPushButton("Get Text")
        btn.clicked.connect(self.get)
        layout.addWidget(btn)

    def get(self):
        text = self.input.text()
        price = stocks.get_price(text)
        self.stock_price.setText(price)


app = QApplication([])

window = Window()

window.show()

sys.exit(app.exec())
