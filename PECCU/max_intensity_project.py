from glob import glob
from os import path

import numpy as np
import tifffile


files = glob('/nfs/turbo/umms-jzsexton/VirtualStaining/data_merged/predictions/tifs/*.tif')
for f in files:
    basename = path.basename(f)
    img = tifffile.imread(f)
    project_img = np.max(img, axis=0)
    tifffile.imwrite('/nfs/turbo/umms-jzsexton/VirtualStaining/data_merged/predictions/tifs/projections/' + basename, project_img, metadata=None)


# example_tiff_path = '/nfs/turbo/umms-jzsexton/VirtualStaining/data_merged/PECCU_A01_T0001F001L01A03C01.tif'
# img = tifffile.imread(example_tiff_path)
# print(img.shape)
# print(img.dtype)

# project_img = np.max(img, axis=0)
# print(project_img.shape)
# print(img.dtype)
# tifffile.imwrite('/nfs/turbo/umms-jzsexton/VirtualStaining/data_merged/PECCU_A01_T0001F001L01A03C01_proj.tif', project_img, metadata=None)

