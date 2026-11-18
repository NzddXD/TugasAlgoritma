class Output:
    def __init__(self, passedText = None):
        self.passedText = passedText or 'Text'

    COLORS = {
        'ERR': '\033[91m',
        'INFO': '\033[94m',
        'WARN': '\033[93m',
        'RESET': '\033[0m'
    }
    
    # Methods
    def info(self, text = None):
        msg = text or self.passedText
        print(f'\n{self.COLORS['INFO']}[I]: {msg} {self.COLORS['RESET']}')

    def warn(self, text = None):
        msg = text or self.passedText
        print(f'\n{self.COLORS['WARN']}[W]: {msg} {self.COLORS['RESET']}')

    def err(self, text = None):
        msg = text or self.passedText
        print(f'\n{self.COLORS['ERR']}[E]: {msg} {self.COLORS['RESET']}')