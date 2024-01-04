from abc import ABC, abstractmethod


class InputOutput(ABC):
    def __init__(self, text: str) -> None:
        self.__text = text

    def __str__(self) -> str:
        return str(self.__text)

    @abstractmethod
    def input(self, text: str):
        pass

    @abstractmethod
    def output(self, text: str):
        pass


class Console(InputOutput):
    @classmethod
    def input(self, text: str):
        user_input = input(text)
        return user_input

    @classmethod
    def output(self, text):
        text = str(text)
        print(text)
