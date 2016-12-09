import re
import sys
import string
import fileinput

def process(word):
    word = word.lower()
    return word

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    dic = {}
    with fileinput.input(files=input_file) as f:
        for line in f:
            # to eliminate the symbol at the end of sentence
            line = line[0:-2]
            # eliminate dash
            sentence = re.split('-| |\n', line)
            for word in sentence:
                # transfer to lowercase and eliminate symbols
                word = process(word)
                if bool(re.search(r'\d', word)):
                    # remove number
                    continue
                elif word == '':
                    # remove empty string
                    continue
                elif word in dic:
                    dic[word]=dic[word]+1
                else:
                    dic[word]=1
        for key, value in sorted(dic.items(), key=lambda x:(x[1],x[0]), reverse=True):
            print(key, value)


