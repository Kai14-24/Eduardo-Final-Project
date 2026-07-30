import csv
import os
import traceback
from typing import Dict, Tuple, Any
from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi


class breedLogic(QMainWindow):
    """Controller class managing user interactions, data validation,external CSV data loading, and weight calculations for the Dog Health GUI application"""
    def __init__(self) -> None:
        """Initializes the main window, loads the Qt Designer interface file, loads external breed data"""
        super().__init__()
        current_dir: str = os.path.dirname(os.path.abspath(__file__)) # Load UI file dynamically from the current script directory
        ui_path: str = os.path.join(current_dir, "guifinal1.ui")
        loadUi(ui_path, self)
        self.__breed_data: Dict[str, Dict[str, Any]] = {}  # Private data encapsulation for breed information
        csv_path: str = os.path.join(current_dir, "breed.csv") # External File I/O: Load breed reference metrics from CSV
        self.__load_breed_data(csv_path)
        self.clear_outputs()
        self.pushButton.clicked.connect(self.search_dog_info)  # Connect button click event to event handler

    def __load_breed_data(self, file_path: str) -> None:
        """Reads dog breed specifications from an external CSV data file"""
        if not os.path.exists(file_path):
            return
        try:
            with open(file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    breed_name: str = row["breed"].strip()
                    self.__breed_data[breed_name] = {
                        "weight_range": (float(row["min_weight"]), float(row["max_weight"])),
                        "lifespan": row["lifespan"].strip(),
                        "info": row["info"].strip()
                    }
        except Exception as e:
            print(f"Error loading CSV file: {e}")

    def clear_outputs(self) -> None:
        """Clears all text fields and resets warning labels to their hidden state"""
        self.text_lifespan.clear()
        self.text_status_weight.clear()
        self.text_goinover.clear()
        self.text_goinunder.clear()
        self.textBrowser.clear()
        self.label_resulr_overweight.hide()  # Reset warning labels visually using exact UI widget identifiers
        self.label_result_underweight.hide()

    def calculate_weight_difference(self, current_weight: float, min_weight: float, max_weight: float) -> Tuple[
        str, float, str]:
        """
        Calculates whether a dog's weight deviates from standard breed ranges and determines the difference
        :return: A tuple containing (status_message, deviation_amount, condition_category)
        """
        if current_weight > max_weight:
            over_amount: float = current_weight - max_weight
            return "Your dog is overweight", over_amount, "over"
        elif current_weight < min_weight:
            under_amount: float = min_weight - current_weight
            return "Your dog is under the weight", under_amount, "under"
        else:
            return "Your dog is at a normal weight", 0.0, "normal"

    def search_dog_info(self) -> None:
        """Handles user input from the UI, performs input validation, evaluates weight logic,and renders calculated outputs to the GUI display widgets"""
        try:
            self.clear_outputs()
            selected_breed: str = self.combo_bread.currentText().strip() #Retrieve and validate selected breed
            if selected_breed not in self.__breed_data:
                self.textBrowser.setText("Please select a valid dog breed.")
                return
            raw_weight: str = self.text_weight.toPlainText().strip() #Extract and validate keyboard input for weight
            try:
                current_weight: float = float(raw_weight)
                if current_weight <= 0:
                    raise ValueError("Weight must be greater than zero.")
            except ValueError:
                self.textBrowser.setText("Error: Enter a valid positive number for weight.")
                return
            data: Dict[str, Any] = self.__breed_data[selected_breed] #Retrieve reference data for selected breed
            min_w, max_w = data["weight_range"]
            self.text_lifespan.setText(str(data["lifespan"]))  #Display breed metrics
            self.textBrowser.setText(str(data["info"]))
            status_msg, diff_amount, condition = self.calculate_weight_difference(current_weight, min_w, max_w) #Perform mathematical weight status calculation
            self.text_status_weight.setText(str(status_msg))
            if condition == "under": #Dynamically update UI text fields and warning notifications
                self.text_goinunder.setText(f"{diff_amount:.2f} kg") 
                self.label_result_underweight.show()
            elif condition == "over":
                self.text_goinover.setText(f"{diff_amount:.2f} kg")
                self.label_resulr_overweight.show()

        except Exception as e:
            print("Runtime execution error:", e)
            traceback.print_exc()
            self.textBrowser.setText(f"An unexpected error occurred: {str(e)}")
