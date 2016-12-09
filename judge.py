import sys
if __name__ == "__main__":
    filename1=sys.argv[1]
    filename2=sys.argv[2]
    file1 = open(filename1)
    output1 = file1.read()
    file2 = open(filename2)
    output2 = file2.read()
    if output1==output2:
        print ("PASS")
    else:
        print ("FAIL")
