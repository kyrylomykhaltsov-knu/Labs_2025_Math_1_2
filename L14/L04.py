# У папці з програмою міститься перелік текстових файлів. Реалізуйте
# програму, що:
# • виводить на екран вміст заданого файлу; 63
# • коректно опрацьовує ситуацію, у випадку якщо заданий файл не
# існує за вказаним розташуванням або не доступний для читання
# та виводить на екран відповідне повідомлення.

def readFile(fileName):
    try:
        with open(fileName, encoding="utf-8") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError as  fnf_err:
        print(f"Файл {fnf_err.filename} не знайдено")

readFile("input04.txt")