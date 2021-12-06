import os

import numpy as np
import pandas as pd

def load_data(folder_path: str):
    files = os.listdir(folder_path)
    candidates = []
    for channel in files:
        with open(os.path.join(folder_path, channel), mode='r', encoding='utf-8') as f:
            _candidates = [c.strip() for c in f.readlines()]
            candidates += _candidates
    return candidates

def random_draw(candidates, num, seed=8848):
    """
    removed
    """
    np.random.seed(seed)
    return np.random.choice(candidates, size=num, replace=False)

def generate_seed():
    pass

