"""
main-script to open functions and create the wanted output
"""
import os
import plotter as pt
import interinterpolator as pol
import solver as sol

answer = input("Is the file in the current path [y/n]?")

if answer != "n":
    print('getcwd:      ', os.getcwd())

else:
    file_path = input('Enter a file path: ')

    # e.g. C:\Users\Bob\Desktop\example.txt
    # or /home/Bob/Desktop/example.txt
    print(file_path)

    if os.path.exists(file_path):
        print('The file exists')

        with open(file_path, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()

            print(lines)
    else:
        print('The specified file does NOT exist')

pt.interpol()
sol.schroedinger_solver()
pol.visualizer()