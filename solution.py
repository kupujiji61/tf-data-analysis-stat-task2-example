import pandas as pd
import numpy as np

import scipy.stats


chat_id = 778100570 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    return np.sqrt((len(x) - 1) * np.std(x)**2 / scipy.stats.chi2.ppf(p + alpha / 2, df=(len(x) - 1))) * 26, \
           np.sqrt((len(x) - 1) * np.std(x)**2 / scipy.stats.chi2.ppf((1 - p) / 2, df=(len(x) - 1))) * 26
