from abc import abstractmethod
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


class Day01Solver(Solver):
    elf_calories: list[int]

    def initialize(self, file_path: str):
        self.elf_calories = self.__load_data_structures(file_path)

    def __load_data_structures(self, file_path: str) -> list[int]:
        input = load_text_file(file_path)
        elf_calories = input.split("\n\n")
        elf_calorie_sum = [
            sum([int(calorie) for calorie in elf.strip().split("\n")])
            for elf in elf_calories
        ]
        return elf_calorie_sum

    @abstractmethod
    def solve(self) -> int:
        ...
