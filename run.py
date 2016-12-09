import os

input_arr = ["sample_input.txt", "a1.txt", "a2.txt", "a3.txt", "a4.txt"]
output_arr = ["sample_output.txt", "a1_a.txt", "a2_a.txt", "a3_a.txt", "a4_a.txt"]

for i in range(len(input_arr)):
    cmd = "python3 count_words.py "+input_arr[i]+" "+ str(i)+"_output.txt"
    os.system(cmd)
    cmd = "python judge.py "+output_arr[i]+" "+ str(i)+"_output.txt"
    os.system(cmd)
