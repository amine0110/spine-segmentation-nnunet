![header](https://capsule-render.vercel.app/api?type=venom&height=300&color=gradient&text=Spine%20Segmentation)


[![Static Badge](https://img.shields.io/badge/PYCAD-Blog-%23ffc800?logoColor=ffc800&link=https%3A%2F%2Fpycad.co%2F)](https://pycad.co/) [![Static Badge](https://img.shields.io/badge/PYCAD-YouTube-%23e80202?logoColor=ffc800&link=https%3A%2F%2Fgithub.com%2Famine0110%2Fpycad%2Ftree%2Fmain%2Fdocs)](https://www.youtube.com/channel/UCdYyILlPlehK4fKS5DiuMXQ) [![Static Badge](https://img.shields.io/badge/PYCAD-Portfolio-%23eb5d10?logoColor=ffc800&link=https%3A%2F%2Fgithub.com%2Famine0110%2Fpycad%2Ftree%2Fmain%2Fdocs)](https://pycad.co/portfolio/)

*Welcome to the spine segmentation with nnUNet course 👊*

This course consists of training a machine learning model for spine segmentation (multiclass). The model that will be used is a UNet, but not just a normal UNet, we will use the framework nnUNet to train the model as it is a state of the art model for medical image segmentation.

![demo](/images/demo.gif)

The model has been built on `1089 CT scans` taken from the TotalSegmentator dataset. The dataset used ofor the course is hosted in Kaggle and can be accessed [here](https://www.kaggle.com/datasets/pycadmk/spine-segmentation-from-ct-scans).

## Materials
This repository is hosting some materials that helps you prepare your dataset, train the model and even some demos of how you can use or deploy your model with different technologies such as QT, Streamlit or Trame.
- Prepare your dataset with the different modules available in [dataset.py](/utils/dataset.py) file.
- Life time access to the dataset in [Kaggle](https://www.kaggle.com/datasets/pycadmk/spine-segmentation-from-ct-scans).
- The [model](https://www.dropbox.com/scl/fi/9nv9zsr07avkl78edwlwl/sample_outputs.zip?rlkey=xr4f1jyv2gxq5j903phnoebdz&st=l9t2e3ld&dl=0) trained during the course.
- Sample [STLs](/demos/assets/stls/) for 3D visualization.
- Multiple [demos](/demos/) where you can deploy your model after training.

In the figure below you can see the training graph:

<img src="/images/progress.png" alt="progress" width="600">

And in the table below you can find some useful information:

| N. train data | N. valid data | N. eval data | N. epochs | Train dice | Valid dice | Eval dice | Model ckpt | Valid samples |
| ------------- | ------------- | ------------ | ----------| ---------- | ---------- | --------- | --- | --- |
| 608           | 152           | 217          | 250       | 91.44%     | 88%        | 85%       | [ckpts](https://www.dropbox.com/scl/fi/yj981c7chepg6fqwceg04/configs.zip?rlkey=uwvytlgztowj4p6m3qflcgy76&st=gwfe8oxc&dl=0) | [samples](https://www.dropbox.com/scl/fi/9nv9zsr07avkl78edwlwl/sample_outputs.zip?rlkey=xr4f1jyv2gxq5j903phnoebdz&st=l9t2e3ld&dl=0) |


To get an idea about the whole process steps, you can check [this guidelines doc](guidelines.md).
 ---
## Our Medical Imaging Resources
- [Free medical imaging ebook.](https://pycad.co/medical-imaging-ebook/)
- [Weekly medical imaging newsletter.](https://pycad.co/join-us/)
- [> 50 medical imaging blog posts.](https://pycad.co/blog/)
- [30:30 medical imaging notebooks.](https://pycad.co/30-30-medical-imaging-notebooks/)