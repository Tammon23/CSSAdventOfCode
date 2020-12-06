from datetime import date
import webbrowser
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

            # opening the problem in the default browser
            question_webpage = "https://adventofcode.com/2020/day/" + str(day)
            webbrowser.open(question_webpage, new=1)
            webbrowser.open(question_webpage + "/input", new=2)

        except FileExistsError:
            print("Folder for day", day, "already exists")
