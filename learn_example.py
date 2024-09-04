from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QGridLayout,
                             QLineEdit, QPushButton, QComboBox)
import sys
import datetime
class DistanceCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Distance Calculator")
        grid = QGridLayout()

        # Create widget
        distance_label = QLabel("Distance:")
        self.distance_edit = QLineEdit()
        Time_label = QLabel("Time(hours)")
        self.time_edit = QLineEdit()

        # Create Option box
        self.options = QComboBox()
        self.options.addItems(["Kilometers", "Miles"])

        # Create button
        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_distance)

        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_edit, 0, 1)

        # Options (0, 2)
        grid.addWidget(self.options, 0, 2)

        grid.addWidget(Time_label, 1, 0)
        grid.addWidget(self.time_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_distance(self):
        selected_option = self.options.currentText()
        uni = selected_option.lower()
        if selected_option == "Kilometers":
            self.avg_speed = int(self.distance_edit.displayText()) / int(self.time_edit.displayText())
        elif selected_option == "Miles":
            self.avg_speed = int(self.distance_edit.displayText()) / int(self.time_edit.displayText())


        self.output_label.setText(f"Average speed is {self.avg_speed} {uni}")

app = QApplication(sys.argv)
distance_calculator = DistanceCalculator()
distance_calculator.show()
sys.exit(app.exec())