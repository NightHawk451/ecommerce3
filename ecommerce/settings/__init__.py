#comment out the ones you don't want to use
#when working in local, put local out of try block
from .base import *

#

from .production import *

#from .local_micah import *

#from .local import *

# try:
# 	from .local import *
# except:
# 	pass

try:
	from .local_micah import *
except:
	pass