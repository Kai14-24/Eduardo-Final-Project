import csv
from typing import List
from PyQt6.QtWidgets import QMainWindow
from gui_final import Ui_MainWindow

class BreedClass:

    def __init__(self, breed: str, min_weight: float, max_weight: float, lifespan: int, information: str) -> None:
        self.__breed: str = breed
        self.__minWeight: float = min_weight
        self.__maxWeight: float = max_weight
        self.__lifespan: int = lifespan
        self.__information: str = information


class Logic(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setupUI(self)
        self.breeds_list = []
        

