# Springboard

## pytorch-deeplab-xception

| Backbone  | train/eval os  |mIoU in val |Pretrained Model|
| :-------- | :------------: |:---------: |:--------------:|
| ResNet    | 16/16          | 58.3%      | to be updated  |

### Introduction
This is a PyTorch(0.4.1) implementation of [DeepLab-V3-Plus](https://arxiv.org/pdf/1802.02611). It
can use Modified Aligned Xception and ResNet as backbone. Currently, I am transferring Jupyter Notebook to python modules.

![Results](doc/results.png)

The predictions will be saved as `.png` images using the default palette in the passed fodler name, if not, `outputs\` is used.
21 classes are used in this model out of total classes in COCO dataset.

![Colour_Scheme](doc/colour_scheme.png)