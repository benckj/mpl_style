import os
import matplotlib    

style_name = 'uzh.mplstyle'
with open(style_name, 'r') as file:
    data = file.read().rstrip()

dirname = os.path.abspath(os.path.join(matplotlib.get_configdir(), 'stylelib'))

if not os.path.isdir(dirname): 
    os.makedirs(dirname)

open(os.path.join(dirname, style_name),'w').write(data)
