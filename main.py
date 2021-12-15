""" This is the main.py for csv read """
import time
from pathlib import Path
import pandas as pd
from calc.calculations.add import Addition
from calc.calculations.subtract import Subtraction
from calc.calculations.multiply import Multiplication
from calc.calculations.divide import Division


add= pd.read_csv("tests/data/add.csv")
sub = pd.read_csv("tests/data/subtract.csv")
div = pd.read_csv("tests/data/divide.csv")
mul = pd.read_csv("tests/data/multiply.csv")
try:
    res_dir = Path("Log_Files/")
    res_dir.mkdir(parents=True, exist_ok=True)

    output_dir = Path("Done_Folder/")
    output_dir.mkdir(parents=True, exist_ok=True)

except FileNotFoundError:
    print("Directories Already Present")

files_names= ["add.csv", "subtract.csv","multiply.csv","divide.csv"]
files= [add,sub,mul,div]
op=[Addition,Subtraction,Multiplication,Division]

for i in range(len(files_names)): # pylint: disable= consider-using-enumerate
    name = files_names[i]
    print(name + " Process Running")
    t = time.time()
    file1 = open("Log_Files/Log.txt", "a",encoding="utf-8") # pylint: disable= consider-using-with
    file1.write("\nUNIX_time_stamp "+str(t)+ "\t File_name: "+ name + "\n")
    file1.write("Record_No" + "\t" +"Value_1" + "\t" + "Value_2" + "\t"
                + "Operation" + "\t" + "Result" + "\n")
    if i==3:
        file2 = open("Log_Files/EXC_Log.txt", "a", encoding="utf-8")  # pylint: disable= consider-using-with
        file2.write("\nUNIX_time_stamp " + str(t) + "\t File_name: " + name + "\n")
        file2.write("Record_No" + "\t" + "Value_1" + "\t" + "Value_2"
                    + "\t" + "Operation" + "\t" + "Result" + "\n")
    for j in range(len(files[i])): # pylint: disable= consider-using-enumerate

        nums= (files[i]['value_1'][j],files[i]['value_2'][j])

        if i == 3:

            try:
                division = Division(nums)
                result = division.get_result()
                file1.write(str(j) + "\t" + str(nums[0]) + "\t" + str(nums[1])
                            + "\t" + (files_names[i][:-4]) + "\t" + str(result) + "\n")
                files[i].to_csv("Done_Folder/" + files_names[i])

            except ZeroDivisionError:
                file2.write(str(j) + "\t" + str(nums[0]) + "\t" + str(nums[1])
                            + "\t" + (files_names[i][:-4]) + "\t" + "ZeroDivisionError" + "\n")
            continue

        cal = op[i](nums)
        res= cal.get_result()

        file1.write(str(j)+ "\t"+str(nums[0])+"\t"+str(nums[1])
                    +"\t"+(files_names[i][:-4])+"\t"+ str(res)+"\n")
        files[i].to_csv("Done_Folder/"+files_names[i])
    file1.close()
