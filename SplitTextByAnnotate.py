#!/usr/bin/python3

# 将一个文本文件按照 # 注释分割为多个文件，文件名就是#注释内容
# Usage：python3 SplitTextByAnnotate.py input.txt 
import sys

input_file = open(sys.argv[1]).readlines()
line_num = len(input_file)
L = 0
while L < line_num:
    if len(input_file[L].strip().split()) > 0:

        first_word = input_file[L].strip().split()[0]
        splited_file_name = ''
        if first_word == '#':

            for word in input_file[L].strip().split()[1:]:
                word = word.replace('/', '_')
                splited_file_name += word
            splited_file = open(splited_file_name,'w')
        else:
            splited_file.write(input_file[L])
        L += 1
    else:
        L +=1
