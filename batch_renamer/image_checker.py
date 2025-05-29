# -*- coding: utf-8 -*-
import os
import logging
from PIL import Image

logging.basicConfig(filename='image.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_size = []
def image_checker(path):
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    # 添加可以识别的后缀
    for filename in os.listdir(path):
        # 遍历文件夹，不包含子文件夹
        if filename.endswith(image_extensions):
            # 判断文件后缀
            file_path = os.path.join(path, filename)
            # 完整路径
            with Image.open(file_path) as image:
                # 用pillow打开图片
                width, height = image.size
                # 获取文件的尺寸
                file = file_path[-11:]
                file_size.append((file, width, height))
                logging.info(f' - {file} has {width} p x {height} p')

    total = len(file_size)
    if total > 0:
        logging.info(f'   总图片数：{total}')
        sorted_images = sorted(file_size, key=lambda x: x[1] * x[2])
        # sorted将file_size中下标1和2相乘的值以降序排列
        small = sorted_images[0]
        # 为分辨率最小
        large = sorted_images[-1]
        # 分辨率最大
        logging.info(f'最小尺寸图片：{small[0]}，尺寸：{small[1]}x{small[2]}')
        logging.info(f'最大尺寸图片：{large[0]}，尺寸：{large[1]}x{large[2]}')
    else:
        print('总数为0，不进行排序')
image_checker(r'C:\Users\Administrator\Desktop\Python资料及其他\Python_Study\StudyPython\Pyton之自动化脚本炼金术\image')
