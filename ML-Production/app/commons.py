import io
import torch
from PIL import Image
from torchvision import transforms
from modeling.deeplab import *

def get_model():
    model = DeepLab(num_classes=21, backbone='resnet', output_stride=16, sync_bn=False, freeze_bn=False)
    ckpt = torch.load('deeplab-resnet.pth.tar', map_location='cpu')
    model.load_state_dict(ckpt['state_dict'])
    return model

def get_tensor(image_bytes):    
    composed_transforms = transforms.Compose([transforms.ToTensor(), transforms.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))])
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    return composed_transforms(image).unsqueeze(0)