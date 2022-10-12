"""
main-script to open functions and create the wanted output
"""
import os.path
import plotter as pt
import interinterpolator as pol
import solver as sol

print(os.getcwd())

answer = input("Is the file in the current path [y/n]?")

if answer == "y":
    print('cwd:      ', os.getcwd())

elif answer =='n':
    path = input("Enter a file path:" )
    try:
        os.chdir(path)
        print(path)
    except FileNotFoundError:
        print("Directory: {0} does not exist".format(path))
    except NotADirectoryError:
        print("{0} is not a directory".format(path))
    except PermissionError:
        print("You do not have permissions to change to {0}".format(path))
    else:
        print('Seomething didnt work out')
    # e.g. C:\Users\Bob\Desktop
    # or /home/Bob/Desktop
else:
    print('You have to enter y or n')

pt.interpol()
sol.schroedinger_solver()
pol.visualizer()