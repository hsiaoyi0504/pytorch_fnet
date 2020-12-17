import os
import argparse

###################################################
# Assume the user already ran download_and_train.py
###################################################

parser = argparse.ArgumentParser()

parser.add_argument("--gpu_id", default=0, type=int, help="GPU to use.")

args = parser.parse_args()

# Normally this would be run via command-line but this Fnet call will be updated as a python API becomes available
gpu_id = args.gpu_id

image_save_dir = "{}/images/".format(os.getcwd())
model_save_dir = "{}/model/".format(os.getcwd())

data_save_path_test = "{}/image_list_test.csv".format(os.getcwd())
path_save_dir = "{}/predictions/".format(os.getcwd())

command_str = (
    "python ../fnet/cli/predict.py "
    "--path_model_dir {} "
    "--dataset fnet.data.MultiChTiffDataset "
    '--dataset_kwargs \'{{"path_csv": "{}"}}\' '
    "--path_save_dir {} "
    "--gpu_ids {}".format(model_save_dir, data_save_path_test, path_save_dir, gpu_id)
)

print(command_str)
os.system(command_str)