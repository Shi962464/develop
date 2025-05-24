from datetime import *
def main():
    log_name = input('请输入log标题：')
    if log_name.upper() == 'Q':
        print('error')
    name = input('请输入日志内容:')

    tiems = datetime.now().strftime('%Y-%m-%d--%H-%M-%S')
    file = '{}-{}.txt'.format(log_name, tiems)
    with open(file, mode='a', encoding='utf-8') as file_name:
        file_name.write(name)
        # file_name.flush()
if __name__ == '__main__':
    main()