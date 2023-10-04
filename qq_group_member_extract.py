"""
@FILE_NAME : 群成员提取
-*- coding : utf-8 -*-
@Author : Zhaokugua
@Time : 2022/12/11 10:11
"""
import re
import json


def read_file(file_name):
    with open(file_name, 'r', encoding='utf8') as f:
        return f.readlines()


def find_name_qq(each_row):
    result = re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (.*)?[(<](.*?)[)>]", each_row)
    if result:
        print(result)
        return result[0]
    else:
        return None


if __name__ == '__main__':
    filename = input('请把聊天记录文件重命名为“聊天记录.txt”并放在和程序同路径或者直接拖到这里然后敲回车：')
    if not filename:
        filename = '聊天记录.txt'

    lines = read_file(filename)
    result_dict = {}
    for each_line in lines:
        result_temp = find_name_qq(each_line)
        if result_temp:
            value, key = result_temp
            if not result_dict.get(key):
                result_dict[key] = [value]
            else:
                if value not in result_dict[key]:
                    result_dict[key].append(value)

    with open(f'{filename}__result.json', 'w+', encoding='utf8') as f:
        json.dump(result_dict, f, ensure_ascii=False, indent=2)
