import os
import os.path as path

MENU = """1. Просмотр каталога 
2. На уровень вверх 
3. На уровень вниз 
4. Количество файлов и каталогов
5. Размер каталога 
6. Поиск файла 
7. Выход из программы """


def error():
    print("Ошибка при вводе команды.")


def show_catalog():
    for filename in sorted(os.listdir()):
        print(filename, end="")
        if path.isdir(filename):
            print("/", end="")
            print()


def move_up():
    os.chdir(path.split(os.getcwd())[0])


def move_down(d):
    os.chdir(path.join(os.getcwd(), d))


def _count_files(d):
    count = 0
    for filename in os.listdir(d):
        filepath = os.path.join(d, filename)
        if path.isdir(filepath):
            count += _count_files(filepath)
            count += 1
        else:
            count += 1
    return count


def count_files(d):
    print("Количество файлов и подкаталогов в `{}`:\n{}".format(d,_count_files(d)))


def _count_bytes(d):
    size = 0
    for filename in os.listdir(d):
        filepath = os.path.join(d, filename)
        if path.isdir(filepath):
            size += _count_bytes(filepath)
            size += path.getsize(filepath)
        else:
            size += path.getsize(filepath)
    return size


def count_bytes(d):
    print("Размер файлов внутри в `{}`\n{} байт".format(d,_count_bytes(d)))


def _find_files(target, d):
    count = 0
    for filename in os.listdir(d):
            filepath = os.path.join(d, filename)
    if path.isdir(filepath):
        if target in filepath:
            print(filepath)
            count += 1
            count += _find_files(target, filepath)
    else:
        if target in filepath:
            print(filepath)
            count += 1
    return count


def find_files(target, d):
    count = _find_files(target, d)
    if 0 == count:
        print("Ничего не найдено :(")
    else:
        print("Найдено {} файлов".format(count))


def prg_exit():
    print("Выход")

commands = {-1:error, 1:show_catalog,2:move_up,3:move_down,4: count_files,5: count_bytes,6: find_files,7: prg_exit}
QUIT = 7


def accept_command():
    try:
        command, *args = input("> ").split()
        command = int(command)
        if command not in commands:
            return -1, tuple()
        else:
            return command, args
    except ValueError:
        return -1, tuple()

def run_command(command, args):
    commands[command](*args)


def main():
    while True:
        print(os.getcwd())
        print(MENU)
        err = None
        command, args = accept_command()
        try:
            run_command(command, args)
        except TypeError as a:
            err = a
            print("Неправильное количество аргументов:")
        except Exception as a:
            err = a
            print("Ошибка при исполнении подпрограммы:")
        finally:
            if err:
                print(" {}".format(err))
        if QUIT == command:
            print("Работа программы завершена.")
            break
main()
