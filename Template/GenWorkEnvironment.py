from datetime import date
import shutil
import os

if __name__ == "__main__":
    today = date.today()
    day = today.day

    if today.month != 12:
        print("It's not december anymore what you even doing")

    else:
        folder_name = "../Day " + str(day)
        try:
            os.mkdir(folder_name)
            shutil.copyfile("BaseFile.py", folder_name + "/Dec" + str(day) + "_P1.py")
            shutil.copyfile("BaseFile.py", folder_name + "/Dec" + str(day) + "_P2.py")
            with open(folder_name + "/input.txt", "w"):
                pass

        except FileExistsError:
            print("Folder for day", day, "already exists")
