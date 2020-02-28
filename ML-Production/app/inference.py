from commons import get_model, get_tensor
import numpy as np
from torchvision.utils import make_grid
from dataloaders.utils import  *

def get_mask(image_bytes):
    tensor_in = get_tensor(image_bytes)
    model = get_model()
    model.eval()

    with torch.no_grad():
        output = model(tensor_in)

    grid_image = make_grid(decode_seg_map_sequence(torch.max(output[:3], 1)[1].detach().cpu().numpy()), 
    3, normalize=False, range=(0, 255))
    return grid_image