import os
import tkinter
from pynput.mouse import Button, Controller


class TextOverlap(Exception):
    """Exception raised when text overlaps other text"""
    def __init__(self, message: str, error_code:int):
        super().__init__(message)
        self.error_code = error_code
        self.message = message
    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})" 

class Display:
    def __init__(self) -> None:
        self.root = tkinter.Tk()
        tsize: os.terminal_size = os.get_terminal_size()
        self.TERMINAL_COLUMNS: int = tsize[0]
        self.TERMINAL_ROWS: int = tsize[1]

        self.SCREEN_WIDTH: int = self.root.winfo_screenwidth()
        self.SCREEN_HEIGHT: int = self.root.winfo_screenheight()

        self.TERMINAL_CELL_WIDTH: int = int(self.SCREEN_WIDTH / self.TERMINAL_COLUMNS)
        self.TERMINAL_CELL_HEIGHT: int = int(self.SCREEN_HEIGHT / self.TERMINAL_ROWS)

        self.mouse_cords = self.get_mouse_position()
        self.mouse_x: int = self.__get_mouse_x()
        self.mouse_y: int = self.__get_mouse_y()

        # this contains text that is displayed and x, y cords
        self.data_stored: dict{str: tuple(int,int)} 

    def __get_mouse_x(self) -> int:
        mouse = Controller()
        return round(mouse.position[0])

    def __get_mouse_y(self) -> int:
        mouse = Controller()
        return round(mouse.position[1])

    def get_mouse_position(self) -> tuple[int, int]:
        return self.__get_mouse_x(), self.__get_mouse_y()

    def clear_screen(self) -> None:
        print("\033[2J\033[H")


    def text_on_screen(self,text:str, x:int, y:int)-> None:

        for data in self.data_stored.values():
            if y == data[0] and x == data[1]:
                raise TextOverlap(f"Text \"{text}\" overlaps {self.data_stored[data]}", 2)


def main():
    display = Display()
    display.clear_screen()
    # while True:
    #     try:
    #         print(display.get_mouse_position())
    #     except KeyboardInterrupt:
    #         print("done")


if __name__ == "__main__":
    main()
