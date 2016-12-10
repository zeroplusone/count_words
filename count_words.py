import re
import sys
import fileinput

abbr = ["dr", "st", "no", "tennis.com"]
symbols = [",", ".", "?", "!", ":", ";","\"",
           "(", ")", "[", "]", "$", "[", "]", "{", "}"]


def process(word):
    word = word.lower()
    is_abbr = False
    for s in symbols:
        if word[-1] == s or word[0] == s:
            for a in abbr:
                if word[0:-1] == a:
                    is_abbr = True
                    break
            if not is_abbr:
                for c in word:
                    if c in symbols:
                        word = word.replace(c,"")
    return word

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    dic = {}
    # with fileinput.input(files=input_file) as f:
    with open(input_file, 'r') as f:
        for line in f:
            # eliminate dash
            sentence = re.split('-| |\n', line)
            for word in sentence:     
                if bool(re.search(r'\d', word)):
                    # remove number
                    continue
                elif word == '':
                    # remove empty string
                    continue
                # transfer to lowercase and eliminate symbols
                word = process(word)
                if word in dic:
                    dic[word] = dic[word] + 1
                else:
                    dic[word] = 1
    f.close()
    # sort the dic (sort secondary key first, then sort primary key)
    ans = sorted(dic.items(), key=lambda x: x[0], reverse=False)
    ans = sorted(ans, key=lambda x: x[1], reverse=True)
    with open(output_file, 'w') as f:
        for key, value in ans:
            f.write(key + " " + str(value) + "\n")
    f.close()
