# AAAS — Autonomous Authenticity Assurance System

import torch
from torchvision import transforms, models
from PIL import Image

model = models.convnext_tiny(weights=models.ConvNeXt_Tiny_Weights.DEFAULT)
model.eval()

def analyze_image(img_path):
    img = Image.open(img_path).convert("RGB")
    t = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor()
    ])
    x = t(img).unsqueeze(0)

    with torch.no_grad():
        out = model(x)

    probs = torch.softmax(out,1)[0]
    confidence = probs.max().item()
    anomaly = round(1 - confidence, 4)
    return anomaly
