import string
from random import *


Max_String_Value = 5
Cal_Int_Times = 5
Min_char = 10
Max_char = 20
all_char = string.ascii_letters
all_char_with_num = string.ascii_letters + string.digits


# result = randomVar(1)
# print(result[1])
def randomVar (initType):
    varName = "".join(choice(all_char) for i in range(randint(Min_char, Max_char)))
    if(initType == 0):
        # int
        code = "NSInteger " + varName + " = " + str(randint(0, 30000)) + ";\n"
    else:
        # string
        strValue = "".join(choice(all_char_with_num) for x in range(randint(Min_char, 50)))
        code = "NSString *" + varName + " = @\"" + strValue + "\";\n"
    return (varName, code)


# print(randomComment())
def randomComment (lineCount):
    comment = "/**\n"
    for i in range(0, lineCount):
        new = ''.join(choice(all_char_with_num) for i in range(50, 200))
        comment = comment + new + '\n'
    comment = comment + "*/\n"
    return comment


def gen_code_chunk():
    chunk = ""
    # comment
    chunk = chunk + randomComment(randint(3, 10))
    # string
    for i in range(0, Max_String_Value):
        chunk = chunk + randomVar(2)[1]
    # int
    int_val_names = []
    for i in range(0, 3):
        new_name, new_val = randomVar(0)
        int_val_names.append(new_name)
        chunk = chunk + new_val
    # int cal
    func_list = ['+', '-', '*', '/']
    for i in range(0, 5):
        chunk = chunk + int_val_names[randint(0, 2)] + ' = ' + int_val_names[randint(0, 2)] + ' ' + func_list[randint(0, 3)] + ' ' + int_val_names[randint(0, 2)] + ';\n'
    # comment
    chunk = chunk + randomComment(randint(3, 10))
    return chunk


def tweek_file(path):
    indexList = []
    with open(path, mode='r+', encoding='utf-8') as file:
        file_str_list = file.readlines()
        print(file_str_list)
        for index, line in enumerate(file_str_list):
            if 'return' in line and '//' not in line:
                indexList.append(index)
        indexList.reverse()
        for index in indexList:
            file_str_list.insert(index, gen_code_chunk())
        file.seek(0)
        file.writelines(file_str_list)
