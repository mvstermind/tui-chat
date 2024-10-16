import enum
import os
import tkinter
from pynput.mouse import Button, Controller
import errors


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
        self.data_stored: dict[str, tuple[int, int]] = {}

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

    def text_on_screen(self, text: str, x_cords: int, y_cords: int) -> None:
        if x_cords + len(text) > self.TERMINAL_COLUMNS:
            raise errors.OutOfBounds(
                f"Text {text} will be out of bounds for x: {x_cords}", 3
            )
        if y_cords > self.TERMINAL_ROWS:
            raise errors.OutOfBounds(
                f"Text {text} will be out of bounds for y: {y_cords}", 4
            )

        if len(self.data_stored) != 0:
            for key, value in enumerate(self.data_stored):
                if y_cords == value[0] and x_cords == value[1]:
                    raise errors.TextOverlap(f'Text "{text}" overlaps {key}', 2)

        self.data_stored[text] = (x_cords, y_cords)
        names = []
        for names in sorted(self.data_stored.keys()):
            


def main():
    display = Display()
    display.text_on_screen(text="first", x_cords=1, y_cords=10)
    display.text_on_screen(text="third", x_cords=4, y_cords=13)
    display.text_on_screen(text="second", x_cords=2, y_cords=12)


if __name__ == "__main__":
    main()
