import re
import sys
import fileinput

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    dic = {}
    with fileinput.input(files=input_file) as f:
        for line in f:
            sentence = re.split('-| |\n', line)
            for word in sentence:
                if word in dic:
                    dic[word]=dic[word]+1
                else:
                    dic[word]=1
        for key, value in sorted(dic.items(), key=lambda x:(x[1],x[0])):
            print(key, value)
