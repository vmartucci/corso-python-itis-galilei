import re


def tokenize_regex(stringa):
    x = re.findall("[0-9]+|[+\-*=/()]+", example)
    print(x)

def tokenize(stringa):
    token_num = ['0','1','2','3','4','5','6','7','8','9']
    token_op = ['+','-','*','=','/','(',')']
    list_out = []

    len_string = len(stringa)-1
    for i in range(0,len_string):
        s = stringa[i]

        if s in token_op:
            list_out.append(s)
        elif s in token_num :
            while i < len_string and stringa[i + 1] in token_num :
                s = s+stringa[i + 1]
                i = i+1
            list_out.append(s)

    print(list_out)


if __name__ == "__main__":
    example = "(4+3)=70"
    tokenize(example)
    tokenize_regex(example)
