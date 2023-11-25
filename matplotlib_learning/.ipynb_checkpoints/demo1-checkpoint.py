# import matplotlib
# print(matplotlib.__version__)

# import os
# current_path = os.getcwd()
# print(f"当前工作目录：{current_path}")

import sys
print(sys.executable)

import torch
print(torch.__version__)
print(torch.version.cuda)
print(torch.cuda.is_available())