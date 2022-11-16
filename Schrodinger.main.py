"""
main-script to open functions and create the wanted output
"""
import argparse
import os.path
import schrodinger_interpolator as pol
import schrodinger_solver as sol


_DESCRIPTION = """
Script to solve the 1D Schrodinger Equation
"""
def Command():
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    msg = "Directory (default: .)"
    parser.add_argument('-d', '--directory', default='.',metavar='DIR', 
                    help=msg)
    args=parser.parse_args()
    print("Directory: '{}".format(args.directory))

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
        print(f"Directory: {path} does not exist".format(path))
        print("The programm will be run in the current directory")
    except NotADirectoryError:
        print(f"{path} is not a directory".format(path))
        print("The programm will be run in the current directory")
    except PermissionError:
        print(f"You do not have permissions to change to {path}".format(path))
        print("The programm will be run in the current directory")
    else:
        print('Seomething didnt work out')
    # e.g. C:\Users\Bob\Desktop
    # or /home/Bob/Desktop
else:
    print('You haven not enter y or n, we stay in current directory')

pol.schrodinger_interpol("Case2/")
sol.schrodinger_solver("Case2/")

