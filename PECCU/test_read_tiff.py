import numpy as np
import pandas as pd
import tifffile
from matplotlib import pyplot as plt

example_tiff_path = '/home/yihsiao/pytorch_fnet/examples//fovs/6677e50c_3500001004_100X_20170623_5-Scene-1-P24-E06.ome.tiff'
img = tifffile.imread(example_tiff_path)
print(img.shape)
print(img.dtype)

PECCU_tiff_path = '/nfs/turbo/umms-jzsexton/VirtualStaining/BRO0117014VirtStain-20X_20201111_163715/PECCU/PECCU_A01_T0001F001L01A01Z01C02.tif'
img2 = tifffile.imread(PECCU_tiff_path) 
print(img2.shape)
print(img2.dtype)

