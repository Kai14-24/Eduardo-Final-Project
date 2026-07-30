import csv
from typing import List
from PyQt6.QtWidgets import QMainWindow
from gui_final import Ui_MainWindow

class BreedClass:
    """Here is the class to store the breed of dog in a simple way."""
    def __init__(self, breed_name: str, min_weight: float, max_weight: float, lifespan: int, information: str) -> None:
        self.breed_name: str = breed_name
        self.min_weight: float = min_weight
        self.max_weight: float = max_weight
        self.lifespan: int = lifespan
        self.information: str = information


class BreedLogic(QMainWindow, Ui_MainWindow):
    """Here we have the interface for the main window"""
    def __init__(self) -> None:
        super().__init__()
        self.setupUI(self)
        self.breeds_list = []   #here we set a list
        self.load_data()        #here we have the value to upload the data from the csv file
        self.populate_combo_box() #here the value for populating the combo box
        self.label_result_overweight.setText("")
        self.label_result_underweight.setText("")
        self.pushButton.clicked.connect(self.calculate_status) #here we have the botttom to to give the result and does the math

    def load_data(self) -> None:
        """Here is ere the data from the csv is extracter and the row breed is save in the list"""
        try:
            with open("breed.csv", mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader: #here we creat valuse from the row in the csv 
                    breed = BreedClass(
                        breed_name=row["Breed"],
                        min_weight=float(row["MinWeight"]),
                        max_weight=float(row["MaxWeight"]),
                        lifespan=int(row["Lifespan"]),
                        information=row["information"]
                    )
                        
                    self.breeds_list.append(breed)
        except FileNotFoundError:
            self.textBrowser.setText("Error: 'breed.csv' file not found.")
        except Exception as e:
            self.textBrowser.setText(f"Error: loading CSV file: {e}")

    def populate_combo_box(self) -> None:
        """Here is were the population of the combo box is set fro the breeds"""
        self.combo_bread.clear()
        self.combo_bread.addItem("Select")
        for breed in self.breeds_list:
            self.combo_bread.addItem(breed.breed_name)

    def calculate_status(self) -> None:
        """here is where the calculation of the weight status is done and the result is displayed in the interface"""
        self.clear_results()
        selected_breed_name = self.combo_bread.currentText()
        weight_input = self.text_weight.toPlainText().strip() if hasattr(self.text_weight, 'toPlainText') else self.text_weight.text().strip()
        if selected_breed_name == "Select" or self.combo_bread.currentIndex() == 0: #here from line 60 to 65 we have the error handling for the user input in the interface
            self.textBrowser.setText("Error: Please select a dog breed.")
            return
        if weight_input == "":
            self.textBrowser.setText("Error: Please enter the weight of your dog.")
            return
        # here we have the grab the actual weight and check if it is a valid number and greater than zero
        try:
            actual_weight = float(weight_input)
            if actual_weight <= 0:
                self.textBrowser.setText("Error: Weight must be greater than zero.")
                return
        except ValueError:
            self.textBrowser.setText("Error: Please enter a valid number for weight (e.g., 24.5).")
            return

        # here we have the selection of the breed from the list
        selected_breed = None
        for breed in self.breeds_list:
            if breed.breed_name == selected_breed_name:
                selected_breed = breed
                break

        # here we have the results of the calculation depeding if the calculation is goign over or under the weight of the breed
        if selected_breed:
            self.text_lifespan.setText(f"{selected_breed.lifespan} years")
            self.textBrowser.setText(selected_breed.information)
            if actual_weight < selected_breed.min_weight: #cheking if goin under
                diff = round(selected_breed.min_weight - actual_weight, 2)
                self.text_status_weight.setText("Underweight")
                self.text_goinover.setText("0 kg")
                self.text_goinunder.setText(f"{diff} kg")
                self.label_result_underweight.setText("Your dog is underweight, please visit a vet.")
            elif actual_weight > selected_breed.max_weight: #checking if goin over
                diff = round(actual_weight - selected_breed.max_weight, 2)
                self.text_status_weight.setText("Overweight")
                self.text_goinover.setText(f"{diff} kg")
                self.text_goinunder.setText("0 kg")
                self.label_result_overweight.setText("Your dog is overweight, please visit a vet.")
            else:
                self.text_status_weight.setText("Ideal Weight")
                self.text_goinover.setText("0 kg")
                self.text_goinunder.setText("0 kg")

    def clear_results(self) -> None:
        """Here we claen the results from the previous calculation to avoid confusion for the user"""
        self.text_lifespan.clear()
        self.text_status_weight.clear()
        self.text_goinover.clear()
        self.text_goinunder.clear()
        self.textBrowser.clear()
        self.label_result_overweight.setText("")
        self.label_result_underweight.setText("")
