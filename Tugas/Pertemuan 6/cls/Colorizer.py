class Colorizer:
    def __init__(self, color, textContent = None):
        self.color = color
        self.textContent = textContent or ''

    COLORS = {
        'RED': '\033[91m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'BLUE': '\033[94m',
        'MAGENTA': '\033[95m',
        'CYAN': '\033[96m',
        'RESET': '\033[0m'
    }

    # Colorize the text
    def colorize(self, color = None, text = None):
        chosenColor = (color or self.color).upper()
        msg = text if text is not None else self.textContent

        color_code = self.COLORS.get(chosenColor, self.COLORS['RESET'])
        return f'{color_code}{msg}{self.COLORS['RESET']}'

       