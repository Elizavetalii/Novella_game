# ANSI escape-последовательности для цветов и стилей
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
STRIKETHROUGH = "\033[9m"

# Цвета текста
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Цвета фона
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

# Примеры использования
print(f"{CYAN}Этот текст красного цвета{RESET}")
print(f"{GREEN}{BOLD}Этот текст зеленого цвета и полужирный{RESET}")
print(f"{BLUE}{ITALIC}Этот текст синего цвета и курсив{RESET}")
print(f"{BG_YELLOW}{BLACK}Этот текст с желтым фоном и черным текстом{RESET}")
def type(text: str, name: str = None) -> None:
    for letter in text:
        if kbhit():
            key = getch()
            
            if key == b'\r':
                command("cls")
                print(text)
            
            break

        print(letter, end="", flush=True)
        sleep(0.025)