## 1、自动整理文件类型(auto_file)

```python
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
    organize_folder(test_path)
```

### 1.1 os 模块

```python
os.path.exists(path)			# 判断这个文件是否存在

os.makedirs(path)				# 递归创建文件夹，创建 a/b/c，即使 a 和 b 都不存在，也会一并创建

os.lijstdir(path)				# 列出目录下的所有文件和文件夹名，不递归

os.path.join(path1,path2,...) 	# 拼接成完整路径
full_path = os.path.join(folder_path, filename)

os.path.isfile(path)			# 判断某个路径是否是普通路径
if os.path.isfile("a.txt"):		# 返回True或者False
    
os.path.splitext(filiname)  	# 将文件名拆分成 文件名+后缀名
_,ext=os.path.shlitext(filename)# 两个变量分别存储文件名和后缀名，_表示不需要的变量
```

### 1.2 shutil 模块

```Python
shutil.copy(src,dst)			# 复制文件到，目标路径，不保留元数据（修改时间等）
shutil.copy('a.txt', 'backup/a.txt') # 如果backup是文件夹，则复制；如文件已存在，则覆盖

shutil.copy2(src,dst)			# 同上，保留元数据

shutil.copyfile(src,dst)		# 只复制内容 src和dst都必须是文件路径
shutil.copyfile('a.txt', 'b.txt')

shutil.move(src,dst)			# 移动文件或目录，目标可以重命名
shutil.move('a.txt', 'dir/a.txt')

shutil.rmtree(path)				# 递归删除整个文件夹和所有子内容  等同于rm -rf
shutil.rmtree('old_backup')
```

### 1.3 logging 模块

#### 1.3.1 显示级别

日志按级别可分为：**debug**、**info**、**warning**、**error**、**critical**

|   级别   |                         可见范围                          |
| :------: | :-------------------------------------------------------: |
|  debug   | **debug**、**info**、**warning**、**error**、**critical** |
|   info   |      **info**、**warning**、**error**、**critical**       |
| warning  |           **warning**、**error**、**critical**            |
|  error   |                  **error**、**critical**                  |
| critical |                       **critical**                        |

其中debug级别最高，可以查看所有信息

info除了debug看不了其他都可以

warning除了debug、info看不了其他也可以看

error只能看error和critical

critical只能看自身

#### 1.3.2 使用方法

```python
import logging

logging.basicConfig(
    filename='log.txt'
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s'
)
logging.info("这是一条调试日志")
```

##### 1.3.2.1 其中 **basicConfig**中的可选参数包括：

|    参数名    |  类型   |                             说明                             |
| :----------: | :-----: | :----------------------------------------------------------: |
| **filename** |   str   |     设置日志输出到的文件名（如果不写，默认输出到控制台）     |
|   filemode   |   str   |           写入模式，默认是'a'追加，可设置为'w'覆盖           |
|  **level**   | int/str |  设置日志级别，例如logging.DEBUG，表示输出级别及以上的日志   |
|  **format**  |   str   | 日志输出格式（包括时间、级别、文件名、行号、正文、记录器名称、产生日志函数名、模块名、线程名、进程ID名等） |
|   datefmt    |   str   |              设置时间格式（%Y-%m-%d %H:%M:%S）               |
|    style     |   str   |              格式化风格，默认是%，可改为{、$等               |
|   hanglres   |  list   |                 自定义一个或多个**Handler**                  |
|   encoding   |   str   |                         设置文件编码                         |
|    stream    | IO对象  |     设置输出目标（如 sys.stdout），用于替代**filename**      |

```Python

logging.basicConfig(
    level=logging.DEBUG,  # 设置日志级别为 DEBUG
    filename="mylog.txt",  # 设置日志文件名
    filemode="w",  # 以覆盖方式写入
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",  # 日志格式
    datefmt="%Y-%m-%d %H:%M:%S",  # 时间格式
    style="%",  # 使用 % 风格
    encoding="utf-8",  # 日志文件使用 UTF-8 编码
    errors="ignore",  # 忽略编码错误
    stream=sys.stdout,  # 同时输出到标准输出（注意：与 filename 互斥时用 handlers）
    handlers=None,  # 不使用额外的 handler，或手动指定多个 handler
    force=True,  # 强制重新配置（覆盖之前的设置）
    validate=True  # 校验参数合法性
)
```

##### 1.3.2.2 format参数

| 占位符        | 含义                       |
| ------------- | -------------------------- |
| %(asctime)s   | 当前时间                   |
| %(levelname)s | 日志级别名称               |
| %(message)s   | 日志消息内容               |
| %(filename)s  | 文件名                     |
| %(lineno)d    | 所在行号                   |
| %(funcName)s  | 函数名                     |
| %(name)s      | logger名称（默认为“root”） |

```Python
logging.basicConfig(level='log.txt',
                    format='%(asctime)s - %(levelnme)s - %(message)s - %(filename)s:%(lineno)d'
                   )
```

#### 1.3.3 其他使用方法(输出到文件及控制台)

##### 1.3.3.1 输出到文件 logging.FileHandler()

##### 1.3.3.2 输出到控制台 logging.StreamHandler()

```python 
import logging		# 导入模块
logger = logging.getLogger('my_log')		# 创建logger 里面带参数就相当于指定format里的%(name)s为my_log,不带参数就默认为 root
logger.setLevel(logging.DEBUG)				# 设置这个logger的日志总开关级别为DEBUG

ch = logging.StreamHandler()				# 创建一个Handler，将日志输出到控制台
ch.setLevel(logging.DEBUG)					# 设置级别为DEBUG
ch.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))		# 设置日志的输出格式

fh = logging.FileHandler(filename= 'log.txt',encoding='utf-8')			# 创建爱你另一个Handler，将信息保存到文件中，所有需要配置文件路径及编码方式
fh.setLevel(logging.INFO)												# 设置级别为INFO
fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))			# 设置日志的输出格式

logger.addHandler(ch)						# 将两个Handler添加到logger中
logger.addHandler(fh)

logger.debug('这是debug级别的调试信息')			# 这个会输出到控制台，但不会输出到文件中
logger.info('这是info级别的调试信息')			# 这个会输出到控制台和文件
```

## 2、自动化批量重命名工具（batch_renamer）

```python 
# -*- coding: utf-8 -*-
import os
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
            count += 1
            # 遍历完一个，计数加一
batch_renamer(
    r'C:\Users\Administrator\Desktop\Python资料及其他\Python_Study\StudyPython\Pyton之自动化脚本炼金术\batch_renamer\test')
```

### 2.1 自动识别文件中的关键字

```python

```





































