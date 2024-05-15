from utils import MultiClassNiftiMerger, MetadataCopier

def merge_nifties():
    volume_dir = 'datasets/volumes'
    class_dirs = ['datasets/vertebrae_C11225/segmentations', 
                'datasets/vertebrae_C21225/segmentations',
                'datasets/vertebrae_C31225/segmentations',
                'datasets/vertebrae_C41225/segmentations',
                'datasets/vertebrae_C51225/segmentations',
                'datasets/vertebrae_C61225/segmentations',
                'datasets/vertebrae_C71225/segmentations',
                'datasets/vertebrae_T11225/segmentations',
                'datasets/vertebrae_T21225/segmentations',
                'datasets/vertebrae_T31225/segmentations',
                'datasets/vertebrae_T41225/segmentations',
                'datasets/vertebrae_T51225/segmentations',
                'datasets/vertebrae_T61225/segmentations',
                'datasets/vertebrae_T71225/segmentations',
                'datasets/vertebrae_T81225/segmentations',
                'datasets/vertebrae_T91225/segmentations',
                'datasets/vertebrae_T101225/segmentations',
                'datasets/vertebrae_T111225/segmentations',
                'datasets/vertebrae_T121225/segmentations',
                'datasets/vertebrae_L11225/segmentations',
                'datasets/vertebrae_L21225/segmentations',
                'datasets/vertebrae_L31225/segmentations',
                'datasets/vertebrae_L41225/segmentations',
                'datasets/vertebrae_L51225/segmentations',
                'datasets/vertebrae_S11225/segmentations']

    output_dir = 'datasets/corrected'
    MultiClassNiftiMerger.process_directories(volume_dir, class_dirs, output_dir, move_volumes=True)

def correct_metadata():
    copier = MetadataCopier('datasets/corrected/volumes', 'datasets/corrected/segmentations', 'datasets/spine_segmentation_nnunet_v2/volumes', 'datasets/spine_segmentation_nnunet_v2/segmentations')
    copier.load_and_copy_metadata()


if __name__ == '__main__':
    correct_metadata()