# PECCU

- PECCU is the dataset we try to run fnet upon

## Set up on Great Lakes

### Installation

``` shell
module load python3.7-anaconda/2020.02
# recommended way (use the environment.yml I export from the conda environment)
# Note that there are two different conda environments due to some compatibility issue of underlying image-processing-related libraries (versions of tifffile required are different)

# 
conda env create -f environment.yml
conda env create -f environment_preprocess.yml

# alternative way (might not work, but it's an illustration of the steps I used earlier to create conda environment from nowhere)
conda create -n MPstain
conda activate MPstain
conda install pytorch==1.6.0 torchvision=0.7.0 cudatoolkit=10.2 -c pytorch
conda install urllib3
conda install quilt3
conda uninstall botocore
conda install botocore
pip install pytorch_toolbelt

# make sure an environment setting of MKL correctly setup
export MKL_SERVICE_FORCE_INTEL=1

```

