import numpy as np
from tslearn.metrics import dtw, dtw_path

def calc_euclidean(actual, predic):
    return np.sqrt(np.sum((actual - predic) ** 2))

def calc_mape(actual, predic):
    return np.mean(np.abs((actual - predic) / actual))

def calc_correlation(actual, predic):
    a_diff = actual - np.mean(actual)
    p_diff = predic - np.mean(predic)
    numerator = np.sum(a_diff * p_diff)
    denominator = np.sqrt(np.sum(a_diff**2)) * np.sqrt(np.sum(p_diff**2))
    return numerator / denominator

def calc_dtw(actual, predic):
    return dtw(actual, predic)

def calculate_similarity(df, target_col):

    col_list = df.columns
    target_y = df[target_col]

    euclidean = []
    mape = []
    pcorr = []
    dtw = []

    for col in col_list:

        candidate_y = df[col]
        euclidean.append(calc_euclidean(target_y, candidate_y))
        mape.append(calc_mape(target_y, candidate_y))
        pcorr.append(calc_correlation(target_y, candidate_y))
        dtw.append(calc_dtw(target_y, candidate_y))

    results = pd.DataFrame(
        list(zip(col, euclidean, mape, pcorr, dtw)),
        columns=["col", "euclidean", "mape", "pcorr", "dtw"],
    )

    return results