from glob import glob
from os import path

import numpy as np
import pandas as pd
import tifffile
import seaborn as sns
import matplotlib.pyplot as plt

files = glob('/nfs/turbo/umms-jzsexton/VirtualStaining/data_merged/predictions/tifs/*.tif')
for f in files:
    basename = path.basename(f)
    img = tifffile.imread(f)
    mean = np.mean(img, axis=(1,2))
    df = pd.DataFrame(data={"z-stack": list(range(1, 82)), "average intensity value": mean}) 
    line_plot = sns.lineplot(data=df, x="z-stack", y="average intensity value")
    fig = line_plot.get_figure()
    fig.savefig("/nfs/turbo/umms-jzsexton/VirtualStaining/data_merged/predictions/tifs/plots/" + basename + ".jpg")
    plt.clf()

