from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QGridLayout,
                             QLineEdit, QPushButton)
import sys
import datetime
class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        # Create widget
        name_label = QLabel("Name: ")
        self.name_line_edit = QLineEdit()
        date_label = QLabel("Date of Birth MM/DD/YYYY")
        self.date_of_birth = QLineEdit()

        # Create button
        calculate_button = QPushButton("Calculate age")
        calculate_button.clicked.connect(self.calculate_age)

        self.output_label = QLabel("")


        # Add widgets to grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_label, 1, 0)
        grid.addWidget(self.date_of_birth, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.datetime.now().year
        date_of_birth = self.date_of_birth.text()
        year_of_bitrh = datetime.datetime.strptime(date_of_birth, "%m/%d/%Y").date().year
        age = current_year - year_of_bitrh
        print(age)
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old.")

app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())