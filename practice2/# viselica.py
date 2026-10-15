import random
from getpass import getpass

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

ALPHABET = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
MAX_MISTAKES = 6

WORDS = {
    "Животные": ["крокодил", "жираф", "пингвин", "медведь", "верблюд", "кенгуру", "носорог", "попугай"],
    "Профессии": ["программист", "врач", "учитель", "пожарный", "художник", "архитектор", "повар", "пилот"],
    "Предметы": ["телефон", "холодильник", "компьютер", "чемодан", "зеркало", "будильник", "рюкзак", "лампа"],
    "Природа": ["водопад", "пустыня", "вулкан", "радуга", "океан", "тайга", "ураган", "ледник"],
}

GALLOWS = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]


def show_screen(word, category, guessed, mistakes, message):
    print("\033c", end="")
    print(f"{CYAN}=== ВИСЕЛИЦА ==={RESET}\n")
    print(f"Тема: {YELLOW}{category}{RESET}")
    print(RED + GALLOWS[len(mistakes)] + RESET)
    masked = " ".join(letter if letter in guessed else "_" for letter in word)
    print(f"\nСлово: {GREEN}{masked}{RESET}")
    print(f"Ошибки ({len(mistakes)}/{MAX_MISTAKES}): {RED}{' '.join(mistakes)}{RESET}")
    if message:
        print(f"\n{message}")


def random_word():
    category = random.choice(list(WORDS))
    return random.choice(WORDS[category]), category


def custom_word():
    print("\033c", end="")
    print(f"{CYAN}=== СВОЁ СЛОВО ==={RESET}\n")
    print("Загадайте слово для другого игрока (ввод будет скрыт).\n")
    while True:
        word = getpass("Слово: ").strip().lower().replace("ё", "е")
        if len(word) >= 2 and all(letter in ALPHABET for letter in word):
            break
        print(f"{RED}Нужно слово из русских букв, минимум 2 буквы{RESET}")
    category = input("Категория (Enter - пропустить): ").strip()
    return word, category or "Своё слово"


def choose_mode():
    print("\033c", end="")
    print(f"{CYAN}=== ВИСЕЛИЦА ==={RESET}\n")
    print(f"{YELLOW}1{RESET}. Случайное слово")
    print(f"{YELLOW}2{RESET}. Своё слово и категория (игра для двоих)\n")
    while True:
        choice = input("Выберите режим: ").strip()
        if choice == "1":
            return random_word()
        if choice == "2":
            return custom_word()


def play(word, category):
    guessed = set()
    mistakes = []
    message = ""

    while True:
        show_screen(word, category, guessed, mistakes, message)
        message = ""

        if all(letter in guessed for letter in word):
            print(f"\n{GREEN}Победа! Вы угадали слово: {word.upper()}{RESET}")
            return
        if len(mistakes) >= MAX_MISTAKES:
            print(f"\n{RED}Вы проиграли. Было загадано: {word.upper()}{RESET}")
            return

        guess = input("\nВведите букву: ").strip().lower().replace("ё", "е")

        if len(guess) != 1 or guess not in ALPHABET:
            message = f"{YELLOW}Введите одну русскую букву{RESET}"
        elif guess in guessed or guess in mistakes:
            message = f"{YELLOW}Буква «{guess}» уже была{RESET}"
        elif guess in word:
            guessed.add(guess)
            message = f"{GREEN}Есть такая буква!{RESET}"
        else:
            mistakes.append(guess)
            message = f"{RED}Нет такой буквы{RESET}"


while True:
    word, category = choose_mode()
    play(word, category)
    again = input("\nСыграть ещё раз? (д/н): ").strip().lower()
    if again not in ("д", "да", "y"):
        print("До встречи!")
        break