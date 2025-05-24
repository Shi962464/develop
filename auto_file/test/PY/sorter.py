# -*- coding: utf-8 -*-
import os
# 执行复制、移动、删除文件等操作
import shutil
# 日志记录
import logging

logging.basicConfig(filename='log.txt',  # 日志文件为log.txt
                    level=logging.INFO,  # 日志级别为 info
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 格式为时间、级别、信息


def create_folder_if_not_exists(path):
    """
    判断文件夹是否存在，不存在就自动创建它
    :param path: 文件夹
    :return:
    """
    if not os.path.exists(path):
        os.makedirs(path)


def get_extension_folder(ext):
    """
    输入后缀名，判断子文件夹名
    :param ext: 后缀
    :return: 大写的后缀名
    """
    return ext[1:].upper() if ext else "not_extension"


def organize_folder(folder_path):
    for filename in os.listdir(folder_path):  # 遍历文件夹中的所有文件名
        full_path = os.path.join(folder_path, filename)  # 得到完整路径
        print(full_path)
        if os.path.isfile(full_path):  # 只处理文件，不处理子目录
            _, ext = os.path.splitext(filename)  # 拆分扩展名（如 .txt）
            folder_name = get_extension_folder(ext)  # 转换为目标子文件夹名
            dest_folder = os.path.join(folder_path, folder_name)  # 拼接出目标子文件夹路径

            create_folder_if_not_exists(dest_folder)  # 如有必要，创建子文件夹
            new_path = os.path.join(dest_folder, filename)  # 移动后的目标路径

            logging.info(f'Moving {filename} → {folder_name}')  # 记录日志
            shutil.move(full_path, new_path)  # 执行文件移动


if __name__ == '__main__':
    test_path = os.path.abspath("test")
    print(test_path)
    organize_folder(test_path)
