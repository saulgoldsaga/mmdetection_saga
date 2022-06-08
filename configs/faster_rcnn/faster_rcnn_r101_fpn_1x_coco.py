_base_ = ['./faster_rcnn_r50_fpn_1x_coco.py','../_base_/datasets/666.py']
model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                      checkpoint='torchvision://resnet101')))
