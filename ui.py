import os
import tkinter
from pynput.mouse import Button, Controller


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

        self.mouse_x: int
        self.mouse_y: int

    def get_mouse_position(self) -> tuple[int, int]:
        mouse = Controller()
        self.mouse_x = round(mouse.position[0])
        self.mouse_y = round(mouse.position[1])
        return self.mouse_x, self.mouse_y


def main():
    display = Display()
    while True:
        try:
            print(display.get_mouse_position())
        except KeyboardInterrupt:
            print("done")


if __name__ == "__main__":
    main()