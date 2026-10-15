import secrets
import string
import subprocess
import sys

BACKGROUND = "\033[48;5;53m\033[97m"
RESET = "\033[0m" + BACKGROUND
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"

types = {
    "1": ["Нижний регистр", string.ascii_lowercase, True],
    "2": ["Верхний регистр", string.ascii_uppercase, True],
    "3": ["Цифры", string.digits, True],
    "4": ["Спецсимволы", "!@#$%^&*()-_=+?", True],
}
length = 16
password = ""


def make_password():
    groups = [t[1] for t in types.values() if t[2]]
    alphabet = "".join(groups)
    while True:
        result = "".join(secrets.choice(alphabet) for _ in range(length))
        if all(any(c in result for c in g) for g in groups):
            return result


def crack_time():
    alphabet_size = sum(len(t[1]) for t in types.values() if t[2])
    seconds = alphabet_size ** length // 2 // 10_000_000_000
    result = ""
    for name, size in [("лет", 31536000), ("дн.", 86400), ("ч.", 3600), ("мин.", 60), ("сек.", 1)]:
        count, seconds = divmod(seconds, size)
        if count:
            result += f"{count} {name} "
    return result or "меньше секунды"


def copy_to_clipboard(text):
    if sys.platform == "darwin":
        command = ["pbcopy"]
    elif sys.platform.startswith("win"):
        command = ["clip"]
    else:
        command = ["xclip", "-selection", "clipboard"]
    try:
        subprocess.run(command, input=text.encode(), check=True)
        return True
    except (OSError, subprocess.CalledProcessError):
        return False


def show_screen():
    print(BACKGROUND + "\033[2J\033[H", end="")
    print(f"{CYAN}=== ГЕНЕРАТОР ПАРОЛЕЙ ==={RESET}\n")
    for key, (name, _, enabled) in types.items():
        status = f"{GREEN}ВКЛ{RESET}" if enabled else f"{RED}ВЫКЛ{RESET}"
        print(f"{YELLOW}{key}{RESET}. {name}: {status}")
    print(f"{YELLOW}5{RESET}. Длина пароля: {length}")
    print(f"{YELLOW}g{RESET}. Сгенерировать")
    print(f"{YELLOW}c{RESET}. Скопировать пароль")
    print(f"{YELLOW}q{RESET}. Выход\n")
    if password:
        print(f"Пароль: {GREEN}{password}{RESET}")
        print(f"Время взлома: {crack_time()}\n")


message = ""
while True:
    show_screen()
    if message:
        print(message + "\n")
    choice = input("> ").strip().lower()
    message = ""

    if choice in types:
        types[choice][2] = not types[choice][2]
        password = ""
    elif choice == "5":
        value = input("Новая длина (4-128): ")
        if value.isdigit() and 4 <= int(value) <= 128:
            length = int(value)
            password = ""
        else:
            message = f"{RED}Нужно число от 4 до 128{RESET}"
    elif choice == "g":
        if any(t[2] for t in types.values()):
            password = make_password()
        else:
            message = f"{RED}Включите хотя бы один тип символов{RESET}"
    elif choice == "c":
        if not password:
            message = f"{YELLOW}Сначала сгенерируйте пароль (g){RESET}"
        elif copy_to_clipboard(password):
            message = f"{GREEN}Пароль скопирован{RESET}"
        else:
            message = f"{RED}Не удалось скопировать (на Linux нужен xclip){RESET}"
    elif choice == "q":
        break

print("\033[0m\033[2J\033[H", end="")