# -*- coding: utf-8 -*-
import os
import logging

logging.basicConfig(filename='../log_searcher/log2.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
def find_keyword(path, key):
    """
    :param path: 需要识别的路径
    :param key: 关键字
    :return:
    """
    for name in os.listdir(path):
        # 遍历文件夹中的文件
        if name.endswith('.txt') or name.endswith('.log'):
            # 判断文件的后缀是否是 txt 或者 log 结尾
            new_name = os.path.join(path, name)
            # 将文件拼接成完整路径
            with open(new_name, 'r', encoding='utf-8') as file:
                # 对遍历的文件执行read操作
                for line_number, mess in enumerate(file, start=1):
                    # enumerate 为每一行增加行号，从1开始,并返回 行号和对应的数据
                    if key in mess:
                        # 判断key是否在数据中
                        print(f'找到 {key} 在 {name} 中的 {line_number}行')
                        print(mess)
                        logging.info(f'{key} to {name} in {line_number} line')
                    else:
                        print('未找到')
find_keyword(
    r'C:\Users\Administrator\Desktop\Python资料及其他\Python_Study\StudyPython\Pyton之自动化脚本炼金术\batch_renamer\test',
    'INFO')
