__author__ = 'gabriel'

import util
import time
import os

while True:
    if util.has_internet_connection():
        os.system("./wireless_up")
    else:
        time.sleep(3)
