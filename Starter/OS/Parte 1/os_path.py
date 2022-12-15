import os
os.getcwd()

os.path.join(os.getcwd(), 'pasta')
os.getcwd() + "/pasta"

os.path.basename(os.getcwd())
os.getcwd()
os.getcwd().split("/")[-1]

os.path.split(os.getcwd())
os.path.split(os.getcwd())[1]
os.path.split(os.getcwd())[0]
os.path.dirname(os.getcwd())

curr_dir = os.getcwd()
lt = os.path.getmtime(curr_dir)#data em segundos

from datetime import datetime
datetime.utcfromtimestamp(lt)