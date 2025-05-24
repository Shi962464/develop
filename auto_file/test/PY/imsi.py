import os
import time
from fromemail import Email
Email()
while 1:
    time.sleep(10)
    a = os.popen("cat /tmp/scripts.log |grep 'Get IMSI' ").read()
    with open('/tmp/imsi',mode='w+',encoding='UTF-8')as file:
        file.write(a)

    # a = os.popen("cat /tmp/scripts.log |grep 'Get IMSI' ").read()
    # os.system("echo '%s' > /tmp/imsi" % a)