__author__ = 'gabriel'

import obd
import sys

reload(sys)
sys.setdefaultencoding('Cp1252')
obd.debug.console = True

con = obd.OBD()