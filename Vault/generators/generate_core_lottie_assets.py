#!/usr/bin/env python3
"""
Core Lottie Vector Assets Generator
Generates clean, production-ready Lottie JSON animations directly into the vault.
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOTTIE_DIR = os.path.join(BASE_DIR, "lottie_assets")
os.makedirs(LOTTIE_DIR, exist_ok=True)


def make_radar_lottie():
    # Rotating radar sweep in Bodymovin JSON format
    d = {
        "v": "5.7.4", "fr": 60, "ip": 0, "op": 120, "w": 300, "h": 300, "nm": "HUD Radar Sweep",
        "ddd": 0, "assets": [],
        "layers": [
            {
                "ddd": 0, "ind": 1, "ty": 4, "nm": "Sweep Arm", "sr": 1, "ks": {
                    "o": {"a": 0, "k": 100},
                    "r": {"a": 1, "k": [{"t": 0, "s": [0]}, {"t": 120, "s": [360]}]},
                    "p": {"a": 0, "k": [150, 150, 0]},
                    "a": {"a": 0, "k": [0, 0, 0]},
                    "s": {"a": 0, "k": [100, 100, 100]}
                },
                "shapes": [
                    {
                        "ty": "gr", "it": [
                            {"ty": "sh", "ks": {"a": 0, "k": {"c": False, "v": [[0, 0], [120, 0]], "i": [[0, 0], [0, 0]], "o": [[0, 0], [0, 0]]}}},
                            {"ty": "st", "c": {"a": 0, "k": [0, 1, 0.61, 1]}, "o": {"a": 0, "k": 100}, "w": {"a": 0, "k": 3}},
                            {"ty": "tr", "p": {"a": 0, "k": [0, 0]}, "a": {"a": 0, "k": [0, 0]}, "s": {"a": 0, "k": [100, 100]}, "r": {"a": 0, "k": 0}, "o": {"a": 0, "k": 100}}
                        ]
                    }
                ]
            },
            {
                "ddd": 0, "ind": 2, "ty": 4, "nm": "Outer Ring", "sr": 1, "ks": {
                    "o": {"a": 0, "k": 80}, "r": {"a": 0, "k": 0}, "p": {"a": 0, "k": [150, 150, 0]}, "a": {"a": 0, "k": [0, 0, 0]}, "s": {"a": 0, "k": [100, 100, 100]}
                },
                "shapes": [
                    {
                        "ty": "gr", "it": [
                            {"ty": "el", "s": {"a": 0, "k": [240, 240]}, "p": {"a": 0, "k": [0, 0]}},
                            {"ty": "st", "c": {"a": 0, "k": [0, 0.8, 1, 1]}, "o": {"a": 0, "k": 90}, "w": {"a": 0, "k": 2}},
                            {"ty": "tr", "p": {"a": 0, "k": [0, 0]}, "a": {"a": 0, "k": [0, 0]}, "s": {"a": 0, "k": [100, 100]}, "r": {"a": 0, "k": 0}, "o": {"a": 0, "k": 100}}
                        ]
                    },
                    {
                        "ty": "gr", "it": [
                            {"ty": "el", "s": {"a": 0, "k": [140, 140]}, "p": {"a": 0, "k": [0, 0]}},
                            {"ty": "st", "c": {"a": 0, "k": [0, 0.5, 0.7, 1]}, "o": {"a": 0, "k": 50}, "w": {"a": 0, "k": 1}},
                            {"ty": "tr", "p": {"a": 0, "k": [0, 0]}, "a": {"a": 0, "k": [0, 0]}, "s": {"a": 0, "k": [100, 100]}, "r": {"a": 0, "k": 0}, "o": {"a": 0, "k": 100}}
                        ]
                    }
                ]
            }
        ]
    }
    path = os.path.join(LOTTIE_DIR, "hud_radar_vector.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f)
    print(f"Generated Lottie Asset: {path}")

def make_target_reticle_lottie():
    # Pulsing target lock reticle
    d = {
        "v": "5.7.4", "fr": 60, "ip": 0, "op": 90, "w": 200, "h": 200, "nm": "Target Lock Reticle",
        "ddd": 0, "assets": [],
        "layers": [
            {
                "ddd": 0, "ind": 1, "ty": 4, "nm": "Rotating Ring", "sr": 1, "ks": {
                    "o": {"a": 0, "k": 100},
                    "r": {"a": 1, "k": [{"t": 0, "s": [0]}, {"t": 90, "s": [180]}]},
                    "p": {"a": 0, "k": [100, 100, 0]}, "a": {"a": 0, "k": [0, 0, 0]},
                    "s": {"a": 1, "k": [{"t": 0, "s": [100, 100]}, {"t": 45, "s": [108, 108]}, {"t": 90, "s": [100, 100]}]}
                },
                "shapes": [
                    {
                        "ty": "gr", "it": [
                            {"ty": "el", "s": {"a": 0, "k": [130, 130]}, "p": {"a": 0, "k": [0, 0]}},
                            {"ty": "st", "c": {"a": 0, "k": [0, 0.96, 1, 1]}, "o": {"a": 0, "k": 100}, "w": {"a": 0, "k": 2}, "d": [{"n": "d", "v": {"a": 0, "k": 12}}, {"n": "g", "v": {"a": 0, "k": 12}}]},
                            {"ty": "tr", "p": {"a": 0, "k": [0, 0]}, "a": {"a": 0, "k": [0, 0]}, "s": {"a": 0, "k": [100, 100]}, "r": {"a": 0, "k": 0}, "o": {"a": 0, "k": 100}}
                        ]
                    }
                ]
            }
        ]
    }
    path = os.path.join(LOTTIE_DIR, "target_lock_vector.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f)
    print(f"Generated Lottie Asset: {path}")

if __name__ == "__main__":
    make_radar_lottie()
    make_target_reticle_lottie()
