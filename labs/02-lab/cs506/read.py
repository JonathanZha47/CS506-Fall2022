from ast import Num
import csv

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    f = open(csv_file_path,"r")
    csvreader = csv.reader(f)
    matrix = []
    for row in csvreader:
            matrix.append(row)
    return matrix


        
    
print(read_csv("/Users/jonathanzha/Desktop/cs506/CS506-Fall2022/labs/02-lab/tests/test_files/dataset_1.csv"))