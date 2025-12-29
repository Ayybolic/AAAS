# AAAS — Autonomous Authenticity Assurance System

from detectors.image_detector import analyze_image
from provenance.ledger import verify
from agents.reasoning_agent import decide
from datetime import datetime

def analyze(img_path):
    score = analyze_image(img_path)
    verified = verify(img_path)
    verdict = decide(score, verified)

    with open("logs/evidence.log","a") as f:
        f.write(f"{datetime.now()} | {img_path} | {verdict} | {score}\n")

    return {
        "risk_score": score,
        "verified": verified,
        "verdict": verdict
    }
