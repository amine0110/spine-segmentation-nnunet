import os
from glob import glob
import shutil

if __name__=="__main__":

    dataset_id = "300"
    rename_trainset = True
    rename_testset  = True
    STRUCTURE = "SPINE"

    path_to_data = "/workspace/datasets/spine_segmentation_nnunet/split"
    path_to_train_image = glob(os.path.join(path_to_data, "train/images/*.nii.gz"))
    path_to_train_labels = glob(os.path.join(path_to_data, "train/labels/*.nii.gz"))
    path_to_test_image  = glob(os.path.join(path_to_data, "valid/images/*.nii.gz"))
    path_to_test_labels  = glob(os.path.join(path_to_data, "valid/labels/*.nii.gz"))


    output_path  = f"/workspace/datasets/nnunet_data/nnUNet_raw/Dataset300_{STRUCTURE}"
    path_to_nnunet_imagesTr = os.path.join(output_path, "imagesTr")
    path_to_nnunet_labelsTr = os.path.join(output_path, "labelsTr")
    path_to_nnunet_imagesTs = os.path.join(output_path, "imagesTs")

    os.makedirs(path_to_nnunet_imagesTr, exist_ok=True)
    os.makedirs(path_to_nnunet_imagesTs, exist_ok=True)
    os.makedirs(path_to_nnunet_labelsTr, exist_ok=True)

    if rename_trainset:

        for i, (vol, seg) in enumerate(zip(path_to_train_image, path_to_train_labels)):

            # Rename the training segmentations
            print(f"Segmentation file: {seg}")
            new_seg_filename = f"{STRUCTURE}_{str(i).zfill(3)}.nii.gz"
            new_seg_filepath = os.path.join(path_to_nnunet_labelsTr, new_seg_filename) 
            print(f"new segmenation file: {new_seg_filepath}")

            shutil.copy(seg, new_seg_filepath)

            # Rename the training volumes
            print(f"Volume file: {vol}")
            new_volume_filename = f"{STRUCTURE}_{str(i).zfill(3)}_0000.nii.gz"
            new_volume_filepath = os.path.join(path_to_nnunet_imagesTr, new_volume_filename)
            print(f"new volume file: {new_volume_filepath}") 

            shutil.copy(vol, new_volume_filepath)

                    
    if rename_testset:     

        for i, (vol, seg) in enumerate(zip(path_to_test_image, path_to_test_labels)):

            # Rename the testing volumes
            print(f"Volume file: {vol}")
            new_volume_filename = f"{STRUCTURE}_{str(i).zfill(3)}_0000.nii.gz"
            new_volume_filepath = os.path.join(path_to_nnunet_imagesTs, new_volume_filename)
            print(f"new volume file: {new_volume_filepath}") 

            shutil.copy(vol, new_volume_filepath)

            # Rename the testing segmentations
            print(f"segmentation file: {seg}")
            new_seg_filename = f"{STRUCTURE}_{str(i).zfill(3)}.nii.gz"
            new_seg_filepath = os.path.join(path_to_nnunet_imagesTs, new_seg_filename)
            print(f"new segmentation file: {new_seg_filepath}") 

            shutil.copy(seg, new_seg_filepath)