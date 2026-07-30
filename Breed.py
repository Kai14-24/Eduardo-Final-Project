import traceback
from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi


class Logic(QMainWindow):
    def __init__(self) -> None:
        """Inicializa la ventana principal y conecta las señales con los slots."""
        super().__init__()

        # Carga el archivo de interfaz creado en Qt Designer (.ui)
        loadUi("guifinal1.ui", self)

        # Diccionario con información técnica de cada raza:
        # 'weight_range': (peso_min_kg, peso_max_kg)
        # 'lifespan': 'años'
        # 'info': 'descripción breve'
        self.breed_data = {
            "Labrador Retriever": {
                "weight_range": (25.0, 36.0),
                "lifespan": "10-12 yrs",
                "info": "Active, outgoing, and friendly companion."
            },
            "Bulldog": {
                "weight_range": (18.0, 25.0),
                "lifespan": "8-10 yrs",
                "info": "Docile, willful, and friendly breed."
            },
            "German Shepherd": {
                "weight_range": (22.0, 40.0),
                "lifespan": "7-10 yrs",
                "info": "Smart, confident, and highly capable working dog."
            },
            "Chihuahua": {
                "weight_range": (1.5, 5.0),
                "lifespan": "12-20 yrs",
                "info": "Graceful, alert, and swift small dog."
            },
            "Poodle": {
                "weight_range": (20.0, 32.0),
                "lifespan": "10-18 yrs",
                "info": "Very intelligent, proud, and active dog."
            },
            "Saint Berbard": {  # Mantiene la ortografía del archivo UI
                "weight_range": (54.0, 82.0),
                "lifespan": "8-10 yrs",
                "info": "Playful, charming, and giant working breed."
            },
            "Pomeranian": {
                "weight_range": (1.4, 3.2),
                "lifespan": "12-16 yrs",
                "info": "Compact, curious, and lively toy dog."
            }
        }

        # Estado inicial del UI
        self.clear_outputs()

        # Conexión de evento al presionar el botón "Search"
        self.pushButton.clicked.connect(self.search_dog_info)

    def clear_outputs(self) -> None:
        """Limpia los campos de texto y oculta las alertas visuales al inicio o ante errores."""
        self.text_lifespan.clear()
        self.text_status_weight.clear()
        self.text_goinover.clear()
        self.text_goinunder.clear()
        self.textBrowser.clear()

        # Oculta las etiquetas de advertencia por defecto
        self.label_resulr_overweight.hide()
        self.label_result_underweight.hide()

    def calculate_weight_difference(self, current_weight: float, min_weight: float, max_weight: float):
        """Calcula si el perro está sobre o bajo peso y por cuánto."""
        if current_weight > max_weight:
            return "Your dog is overweight", current_weight - max_weight, "over"
        elif current_weight < min_weight:
            return "Your dog is under the weight", min_weight - current_weight, "under"
        else:
            return "Your dog is at a normal weight", 0.0, "normal"

    def search_dog_info(self) -> None:
        """Procesa la entrada del usuario, valida los datos y calcula el estado del peso."""
        try:
            self.clear_outputs()

            # 1. Obtener la raza seleccionada (limpiando espacios extra)
            selected_breed = self.combo_bread.currentText().strip()

            if selected_breed not in self.breed_data:
                self.textBrowser.setText("Please select a valid dog breed.")
                return

            # 2. Obtener y validar el peso ingresado
            raw_weight = self.text_weight.toPlainText().strip()

            try:
                current_weight = float(raw_weight)
                if current_weight <= 0:
                    raise ValueError("Weight must be greater than zero.")
            except ValueError:
                self.textBrowser.setText("Error: Enter a valid positive number for weight.")
                return

            # 3. Recuperar datos de la raza seleccionada
            data = self.breed_data[selected_breed]
            min_w, max_w = data["weight_range"]

            # 4. Desplegar información básica
            self.text_lifespan.setText(data["lifespan"])
            self.textBrowser.setText(data["info"])

            status_msg, diff_amount, codition = self.calculate_weight_difference(current_weight, min_w, max_w)
            self.text_status_weight.setText(status_msg)

            # 5. Evaluar la condición física del perro
            if codition == "under":
                self.text_goinunder.setText(f"{diff_amount:.2f} kg")
                self.label_result_underweight.show()
            elif codition == "over":
                self.text_goinover.setText(f"{diff_amount:.2f} kg")
                self.label_resulr_overweight.show()
        except Exception as e:
            print("Error: during the search", e)
            traceback.print_exc()
            self.textBrowser.setText(f"An unexpected error occurred: {str(e)}")
