import sys
from PyQt6.QtWidgets import QApplication
from models.breed_model import BreedRepository
from controllers.main_controller import MainController


def main() -> None:
    """Application entry point."""
    app = QApplication(sys.argv)

    try:
        # Load dataset repository
        repository = BreedRepository("data/breeds.csv")

        # Initialize and display the main controller window
        window = MainController(repository)
        window.show()

        sys.exit(app.exec())
    except Exception as e:
        print(f"Critical error starting application: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()