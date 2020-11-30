from glob import glob

with open('./image_list_train.csv', 'w') as f:
    f.write('path_signal,path_target\n')
    for well_id in range(1, 24): 
        f.write(glob('/nfs/turbo/umms-jzsexton/VirtualStaining/data_merged/PECCU_A{:02d}_T0001F001L01A0*C01.tif'.format(well_id))[0])
        f.write(',')
        f.write(glob('/nfs/turbo/umms-jzsexton/VirtualStaining/data_merged/PECCU_A{:02d}_T0001F001L01A0*C06.tif'.format(well_id))[0])
        f.write('\n')

with open('./image_list_test.csv', 'w') as f:
    f.write('path_signal,path_target\n')
    for well_id in range(1, 24): 
        f.write(glob('/nfs/turbo/umms-jzsexton/VirtualStaining/data_merged/PECCU_B{:02d}_T0001F001L01A0*C01.tif'.format(well_id))[0])
        f.write(',')
        f.write(glob('/nfs/turbo/umms-jzsexton/VirtualStaining/data_merged/PECCU_B{:02d}_T0001F001L01A0*C06.tif'.format(well_id))[0])
        f.write('\n')

