import os
from data import login as Login

try:os.mkdir("CP")
except:pass
try:os.mkdir("OK")
except:pass
Login.login()
