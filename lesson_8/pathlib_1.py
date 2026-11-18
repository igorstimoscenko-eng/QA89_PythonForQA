from pathlib import Path
import os

data_folder = Path("test_data")
file_path = data_folder/"user.csv"
print(file_path)

print(file_path.exists())

screenshot_folder = Path("screenshots")
screenshot_folder.mkdir(exist_ok=True)
reportsFolders = Path("reports/2027")
reportsFolders.mkdir(parents=True, exist_ok=True)

base_dir = Path(__file__).resolve().parent
folder = base_dir / "reports"

folder = base_dir / "reports"
folder = Path("../lesson_9")


def create_reports_folder():
    reports_dir = Path("reports_1")
    reports_dir.mkdir(exist_ok=True)
    result_file = reports_dir / "result.txt"
    with open(result_file,"w",encoding="utf-8") as file:
        file.write("Homework completed successfully!")





current_pzthon_location = os.path.dirname(__file__)
print(current_pzthon_location)

current_pzthon_location_short = os.getcwd()
print(current_pzthon_location_short)

print("************ example 5 (resolve parent directory) ************")
base_dir = Path(".").resolve().parent              # получает абсолютный путь к текущей папке и переходит на один уровень выше
folders = base_dir / "reports"                     # формирует путь к папке reports внутри родительской директории
print(folders)                                     # выводит полный путь к папке reports
print()

print("************ example 6 (create folder one level above) ************")
folder = Path("../lesson_9")                        # создаёт путь к папке lesson9 на один уровень выше текущей
folder.mkdir(exist_ok=True)                        # создаёт папку, если её ещё нет
print()

print("************ example 7 (current directory) ************")
current_dir = Path(".").resolve()                  # получает абсолютный путь к текущей директории
print(current_dir)                                # выводит текущую директорию
print()


# screenshot_folder = Path("screenshots")
#
# screenshot_folder.mkdir(exist_ok=True)
#
# reportsFolders = Path("reports/2027")
#
# reportsFolders.mkdir(parents=True, exist_ok=True)
#
# base_dir = Path(__file__).resolve().parent
#
# folder = base_dir / "reports"
#
# folder = Path("../lesson9")
#
# folder.mkdir(exist_ok=True)
#
# def create_reports_folder(): new*
#
# reports_dir = Path("reports_1")
#
# reports_dir.mkdir(exist_ok=True)
#
# result_file = reports_dir / "result.txt"
#
# with open(result_file, "w", encoding="utf-8") as
#
# self, s: str, /
#
# file.write("Homework completed successfully!")