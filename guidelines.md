# Steps & Guidelines

1. Create the folders to store the datasets:
```
mkdir /workspace/datasets
mkdir /workspace/datasets/nnunet_data
mkdir /workspace/datasets/nnunet_data/nnUNet_raw
mkdir /workspace/datasets/nnunet_data/nnUNet_preprocessed
mkdir /workspace/datasets/nnunet_data/nnUNet_results
mkdir /workspace/datasets/nnunet_data/nnUNet_predictions
```

2. Download the dataset from Dropbox:
```
wget https://www.dropbox.com/scl/fi/q85nv6tx5rrr1d70pw5mh/spine_segmentation_nnunet_v2.zip?rlkey=vsthm34gdlx6ebpbwa9wd2jvv&st=y6rx7454
```

Rename the downloaded file to: `spine_segmentation_nnunet_v2.zip`

3. Unzip the downloaded file from Dropbox:

```
# optional only if you are using vast.ai server
sudo apt-get update
sudo apt-get install unzip
```

```
unzip spine_segmentation_nnunet_v2.zip
```

4. Export the paths to the environment variable:

***For linux***
```
export nnUNet_raw="/workspace/datasets/nnunet_data/nnUNet_raw"
export nnUNet_preprocessed="/workspace/datasets/nnunet_data/nnUNet_preprocessed"
export nnUNet_results="/workspace/datasets/nnunet_data/nnUNet_results"
```

***For windows***
```
set nnUNet_raw=/workspace/datasets/nnunet_data/nnUNet_raw
set nnUNet_preprocessed=/workspace/datasets/nnunet_data/nnUNet_preprocessed
set nnUNet_results=/workspace/datasets/nnunet_data/nnUNet_results
```

5. Install the requirements:
```
pip install nibabel==5.2.1
pip install SimpleITK==2.3.1
pip install numpy==1.26.4
```
```
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
```

6. Install nnUNet
more info can be found [here](https://github.com/amine0110/nnUNet/blob/master/documentation/installation_instructions.md).
```
git clone https://github.com/amine0110/nnUNet.git
cd nnUNet
pip install -e .
```

```
pip install --upgrade git+https://github.com/FabianIsensee/hiddenlayer.git
```

7. Split the dataset to train/valid/test:
```python
from utils import DataSplitter

img = '/workspace/datasets/spine_segmentation_nnunet/volumes'
msk = '/workspace/datasets/spine_segmentation_nnunet/segmentations'
output = '/workspace/datasets/spine_segmentation_nnunet/split'

splitter = DataSplitter(img, msk, output, 0.7, 0.2, 0.1, delete_input=True)
splitter.run()
```

8. Rename the dataset to matc nnUNet expectations:
```python
from utils import DataRenamer
input_nifti = '/workspace/datasets/spine_segmentation_nnunet/split'

nnunet_data = '/workspace/datasets/nnunet_data/nnUNet_raw'

renamer = DataRenamer(input_nifti, nnunet_data, 100, 'SPINE')
renamer.run()
```

9. Create the dataset.json file:
```json
{   
    "channel_names": {
        "0": "CT" 
    }, 
    "labels": {
        "background": 0,
        "vertebrae_C1": 1,
        "vertebrae_C2": 2,
        "vertebrae_C3": 3,
        "vertebrae_C4": 4,
        "vertebrae_C5": 5,
        "vertebrae_C6": 6,
        "vertebrae_C7": 7,
        "vertebrae_T1": 8,
        "vertebrae_T2": 9,
        "vertebrae_T3": 10,
        "vertebrae_T4": 11,
        "vertebrae_T5": 12,
        "vertebrae_T6": 13,
        "vertebrae_T7": 14,
        "vertebrae_T8": 15,
        "vertebrae_T9": 16,
        "vertebrae_T10": 17,
        "vertebrae_T11": 18,
        "vertebrae_T12": 19,
        "vertebrae_L1": 20,
        "vertebrae_L2": 21,
        "vertebrae_L3": 22,
        "vertebrae_L4": 23,
        "vertebrae_L5": 24,
        "vertebrae_S1": 25
    }, 
    "numTraining": 762, 
    "file_ending": ".nii.gz",
    "overwrite_image_reader_writer": "SimpleITKIO"
}
```

10. Run the preprocessing algorithm from nnUNet:
```
nnUNetv2_plan_and_preprocess -d 100 -c 3d_fullres --verify_dataset_integrity -np 1
```

11. Run the training algorithm from nnUNet:
```
nnUNetv2_train 100 3d_fullres 0 -tr nnUNetTrainer_250epochs
```

12. Run the prediction algorithm from nnUNet:
```
nnUNetv2_predict -i /workspace/datasets/nnunet_data/nnUNet_raw/Dataset100_SPINE/imagesTs -o /workspace/datasets/nnunet_data/nnUNet_predictions/ -d 100 -c 3d_fullres -tr nnUNetTrainer_250epochs -f all
```

13. Run the evaluation algorithm from nnUNet:
```
nnUNetv2_evaluate_folder /workspace/datasets/nnunet_data/nnUNet_raw/Dataset100_SPINE/labelsTs/ /workspace/datasets/nnunet_data/nnUNet_predictions/ -djfile /workspace/datasets/nnunet_data/nnUNet_raw/Dataset100_SPINE/dataset.json -pfile /workspace/datasets/nnunet_data/nnUNet_results/Dataset100_SPINE/nnUNetTrainer_250epochs__nnUNetPlans__3d_fullres/plans.json
```