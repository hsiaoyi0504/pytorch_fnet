from glob import glob
import numpy as np
import pandas as pd
import tifffile
from matplotlib import pyplot as plt

# for channel 1
print('Processing channel 1 ...')
for well_alphabet in ['A', 'B']:
    for well_id in range(1, 24): 
        files = sorted(glob('/nfs/turbo/umms-jzsexton/VirtualStaining/BRO0117014VirtStain-20X_20201111_163715/PECCU/PECCU_{}{:02d}_T0001F001L01A0*Z*C01.tif'.format(well_alphabet, well_id)))
        new_file_name = files[0].split('/')[-1].split('Z01')[0] + 'C01.tif'
        with tifffile.TiffWriter('/nfs/turbo/umms-jzsexton/VirtualStaining/data_merged/' + new_file_name) as tif:
            for fname in files:
                img = tifffile.imread(fname)
                tif.write(img, metadata=None, photometric='minisblack')
                del img

print('Processing channel 2 ...')
for well_alphabat in ['A', 'B']:
    for well_id in range(1, 24):
        files = sorted(glob('/nfs/turbo/umms-jzsexton/VirtualStaining/BRO0117014VirtStain-20X_20201111_163715/PECCU/PECCU_{}{:02d}_T0001F001L01A0*Z*C02.tif'.format(well_alphabet, well_id)))
        new_file_name = files[0].split('/')[-1].split('Z01')[0] + 'C02.tif'
        with tifffile.TiffWriter('/nfs/turbo/umms-jzsexton/VirtualStaining/data_merged/' + new_file_name) as tif:
            for fname in files:
                img = tifffile.imread(fname)
                tif.write(img, metadata=None, photometric='minisblack')
                del img

print('Processing channel 3 ...')
for well_alphabat in ['A', 'B']:
    for well_id in range(1, 24):
        files = sorted(glob('/nfs/turbo/umms-jzsexton/VirtualStaining/BRO0117014VirtStain-20X_20201111_163715/PECCU/PECCU_{}{:02d}_T0001F001L01A0*Z*C03.tif'.format(well_alphabet, well_id)))
        new_file_name = files[0].split('/')[-1].split('Z01')[0] + 'C03.tif'
        with tifffile.TiffWriter('/nfs/turbo/umms-jzsexton/VirtualStaining/data_merged/' + new_file_name) as tif:
            for fname in files:
                img = tifffile.imread(fname)
                tif.write(img, metadata=None, photometric='minisblack')
                del img

print('Processing channel 4 ...')
for well_alphabat in ['A', 'B']:
    for well_id in range(1, 24):
        files = sorted(glob('/nfs/turbo/umms-jzsexton/VirtualStaining/BRO0117014VirtStain-20X_20201111_163715/PECCU/PECCU_{}{:02d}_T0001F001L01A0*Z*C04.tif'.format(well_alphabet, well_id)))
        new_file_name = files[0].split('/')[-1].split('Z01')[0] + 'C04.tif'
        with tifffile.TiffWriter('/nfs/turbo/umms-jzsexton/VirtualStaining/data_merged/' + new_file_name) as tif:
            for fname in files:
                img = tifffile.imread(fname)
                tif.write(img, metadata=None, photometric='minisblack')
                del img

print('Processing channel 5 ...')
for well_alphabat in ['A', 'B']:
    for well_id in range(1, 24):
        files = sorted(glob('/nfs/turbo/umms-jzsexton/VirtualStaining/BRO0117014VirtStain-20X_20201111_163715/PECCU/PECCU_{}{:02d}_T0001F001L01A0*Z*C05.tif'.format(well_alphabet, well_id)))
        new_file_name = files[0].split('/')[-1].split('Z01')[0] + 'C05.tif'
        with tifffile.TiffWriter('/nfs/turbo/umms-jzsexton/VirtualStaining/data_merged/' + new_file_name) as tif:
            for fname in files:
                img = tifffile.imread(fname)
                tif.write(img, metadata=None, photometric='minisblack')
                del img

# for channel 6
print('Processing channel 6 (bright field) ...')
for well_alphabet in ['A', 'B']:
    for well_id in range(1, 24):
        files = sorted(glob('/nfs/turbo/umms-jzsexton/VirtualStaining/BRO0117014VirtStain-20X_20201111_163715/PECCU/PECCU_{}{:02d}_T0001F001L01A0*Z*C06.tif'.format(well_alphabet, well_id)))
        new_file_name = files[0].split('/')[-1].split('Z01')[0] + 'C06.tif'
        with tifffile.TiffWriter('/nfs/turbo/umms-jzsexton/VirtualStaining/data_merged/' + new_file_name) as tif:
            for fname in files:
                img = tifffile.imread(fname)
                tif.write(img, metadata=None, photometric='minisblack')
                del img

# img3 = tifffile.imread('./temp.tif')
# print(img3.shape)

# image_sequence = tifffile.TiffSequence('/nfs/turbo/umms-jzsexton/VirtualStaining/BRO0117014VirtStain-20X_20201111_163715/PECCU/PECCU_A23_T0001F001L01A03Z*C01.tif', pattern='axes')
# print(image_sequence.axes)
# print(image_sequence.shape)
# print(image_sequence.asarray().shape)

