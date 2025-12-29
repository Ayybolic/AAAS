# AAAS — Autonomous Authenticity Assurance System

def decide(score, verified):
    if verified:
        return "AUTHENTIC"
    if score > 0.7:
        return "DEEPFAKE"
    if score > 0.3:
        return "HIGH_RISK"
    return "CLEAN"
