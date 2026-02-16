import os
import string


def get_drives():
    drives = []
    for letter in string.ascii_uppercase:
        drive = f"{letter}:\\"
        if os.path.exists(drive):
            drives.append(drive)
    return drives


def list_directory_contents(path):
    try:
        print(f"\nДиск {path}")
        items = os.listdir(path)

        if not items:
            print("  [Пусто]")
            return

        for index, item in enumerate(items, 1):
            full_path = os.path.join(path, item)
            item_type = "папка" if os.path.isdir(full_path) else "файл"
            print(f"{index} {item_type}: {item}")
            

        file_func(path, items)
        
    except PermissionError:
        print("Ошибка: Нет доступа к этому диску (требуются права администратора).")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def main():
    drives = get_drives()

    if not drives:
        print("Диски не найдены.")
        return

    print("Выберите диск:")
    for i, drive in enumerate(drives, 1):
        print(f"{i} {drive}")

    try:
        choice = int(input("Вариант: "))
        if 1 <= choice <= len(drives):
            selected_drive = drives[choice - 1]
            list_directory_contents(selected_drive)
        else:
            print("Неверный номер варианта.")
    except ValueError:
        print("Пожалуйста, введите число.")


def file_func(path, items):
    choice = int(input("Выберите номер папки для входа: "))
    
    selected_item = items[choice - 1]
    selected_path = os.path.join(path, selected_item)
    
    if os.path.isdir(selected_path):
        new_items = os.listdir(selected_path)
        list_directory_contents(selected_path)
        file_func(selected_path, new_items)
    else:
        print(f"Ошибка: '{selected_item}' является файлом, а не папкой")
        list_directory_contents(selected_path)
        file_func(path, items)


main()
