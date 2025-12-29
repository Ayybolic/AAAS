# AAAS — Autonomous Authenticity Assurance System

import imagehash, hashlib
from PIL import Image

ledger = {}

def register(img):
    h = imagehash.phash(Image.open(img))
    ledger[str(h)] = hashlib.sha256(open(img,'rb').read()).hexdigest()

def verify(img):
    h = imagehash.phash(Image.open(img))
    return str(h) in ledger
