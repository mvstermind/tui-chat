class TextOverlap(Exception):
    """Exception raised when text overlaps other text"""

    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.error_code = error_code
        self.message = message

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


class OutOfBounds(Exception):
    """Exception raised when text will be  out of bounds of terminal screen"""

    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.error_code = error_code
        self.message = message

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"
