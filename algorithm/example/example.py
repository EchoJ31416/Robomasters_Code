import os
import sys
sys.path.append("../auto_grader/")
from auto_grader import auto_grader
ag = auto_grader()
# 读入图片
print(ag.link(0, 0, 0, 0))
os.system('pause')
