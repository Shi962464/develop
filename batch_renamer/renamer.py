# -*- coding: utf-8 -*-
import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='log.txt')


def batch_renamer(folder_path, prefix='Txt'):
    """
    :param folder_path: 文件夹路径
    :param prefix: 更改后的文件名称开头
    :return:
    """
    count = 1
    # 文件夹计数
    for filename in os.listdir(folder_path):
        # 遍历文件夹中的文件
        full_path = os.path.join(folder_path, filename)
        # 将遍历的文件拼接成完成路径
        if os.path.isfile(full_path) and filename.lower().endswith('.txt'):
            # 判断这个路径是否是普通路径并且判断这个文件夹下的文件后缀是否是.txt
            new_name = f'{prefix}_{count:03}.txt'
            # 新的文件名是Txt_加上三位数，不够的0补全，从count的初始值开始
            new_path = os.path.join(folder_path, new_name)
            # 拼接改名之后的新路径
            os.rename(full_path, new_path)
            # 重命名文件，将初始文件名改为新的文件名
            aa = full_path[-11:-8]
            bb = new_path[-3:]
            logging.info(f'Renamed {aa} to {bb}')
            count += 1
            # 遍历完一个，计数加一


batch_renamer(
    r'C:\Users\Administrator\Desktop\Python资料及其他\Python_Study\StudyPython\Pyton之自动化脚本炼金术\batch_renamer\test\Txt_001.txt')


