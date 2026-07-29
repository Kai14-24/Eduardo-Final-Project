import csv
from typing import List
from PyQt6.QtWidgets import QMainWindow
from gui_final import Ui_MainWindow

class BreedClass:
    """here is to clase the breed of dog in simple way"""
    def __init__(self, breed_name: str, min_weight: float, max_weight: float, lifespan: int, information: str) -> None:
        self.__breed: str = breed_name
        self.__minWeight: float = min_weight
        self.__maxWeight: float = max_weight
        self.__lifespan: int = lifespan
        self.__information: str = information


class BreedLogic(QMainWindow, Ui_MainWindow):
    """Here we have the interface for the main window"""
    def __init__(self) -> None:
        super().__init__()
        self.setupUI(self)
        self.breeds_list = []   #here we set a list
        self.load_data()        #here in the the next 2 line we have the population of the combo box and also to load the data from the csv
        self.populate_combo_box()
        self.label_resulr_overweight("")
        self.label_result_underweight("")
        self.pushButton.clicked.connect(self.calculate_status) #here we have the botttom to to give the result

    def load_data(self) -> None:
        try:
            with open("breed.csv", mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    breed = Breed(
                        breed_name=row["Breed"]
                        min_weigth=float(row["MinWeight"])
                        max_weight=float(row["MaxWeight"])
                        lifespan=int(row["Lifespan"])
                        information=row["information"]
                    )
                    self.breeds_list.append(breed)
        except FileNotFoundError:
            self.testBrowser.setText("Error: 'breed.csv' file not found.")
        except Exception as e:
            self.textBrowser,setText("Error: loading CSV file: {e}")

    def populate_combo_box(self) -> None:
        self.combo_bread.clear()
        self.combo_bread.addItem("Select")
        for breed in self.breeds_list:
            self.combo_bread.addItem(breed.breed_name)

    def calculate_status(self) -> None:
        self.clear_result()
        selected_breed_name = self.combo_bread.currentText()
        weight_input = self.text_weight.toPlainText().strip() if hasattr(self.text_weight, 'toPlainText') else self.text_weight.text().strip()
        if selected_breed_name == "Select" or self.combo_bread.currentIndex() == 0:
            self.textBrowser.setText("Error: Please select a dog breed.")
            return
        if weight_input == "":
            self.textBrowser.setText("Error: Please enter the weight of your dog.")
            return

        try:
            actual_weight = float(weight_input)
            if actual_weight <= 0:
                self.textBrowser.setText("Error: Weight must be greater than zero.")
                return
        except ValueError:
            self.textBrowser.setText("Error: Please enter a valid number for weight (e.g., 24.5).")
            return

        selected_breed = None
        for breed in self.breeds_list:
            if breed.name == selected_breed_name:
                selected_breed = breed
                break

        if selected_breed:
            self.text_lifespan.setText(f"{selected_breed.lifespan} years")
            self.textBrowser.setText(selected_breed.information)
            if actual_weight < selected_breed.min_weight:
                diff = round(selected_breed.min_weight - actual_weight, 2)
                self.text_status_weight.setText("Underweight")
                self.text_goinover.setText("0 kg")
                self.text_goinunder.setText(f"{diff} kg")
                self.label_result_underweight.setText("Your dog is underweight, please visit a vet.")
            elif actual_weight > selected_breed.max_weight:
                diff = round(actual_weight - selected_breed.max_weight, 2)
                self.text_status_weight.setText("Overweight")
                self.text_goinover.setText(f"{diff} kg")
                self.text_goinunder.setText("0 kg")
                self.label_resulr_overweight.setText("Your dog is overweight, please visit a vet.")
            else:
                self.text_status_weight.setText("Ideal Weight")
                self.text_goinover.setText("0 kg")
                self.text_goinunder.setText("0 kg")

    def clear_results(self) -> None:
        """Limpia los campos de salida en la interfaz."""
        self.text_lifespan.clear()
        self.text_status_weight.clear()
        self.text_goinover.clear()
        self.text_goinunder.clear()
        self.textBrowser.clear()
        self.label_resulr_overweight.setText("")
        self.label_result_underweight.setText("")
