from statistics import stdev, mean
from scipy.stats import skew, kurtosis, entropy


# Cálculo vetores de características
def extract_values(values, is_dictionary=True):
    if is_dictionary:
        return {
            'averate': calc_average(values),
            'standard_deviation': calc_standard_deviation(values),
            'skew': calc_skew(values),
            'kurtosis': calc_kurtosis(values),
            'entropy': calc_entropy(values)
        }
    else:
        return [calc_average(values),
                calc_standard_deviation(values),
                calc_skew(values),
                calc_kurtosis(values),
                calc_entropy(values)
                ]


# Cálculo da média
def calc_average(values):
    return mean(values)


# Cálculo do desvio padrão
def calc_standard_deviation(values):
    return stdev(values)


# Cálculo do grau de assimetria
def calc_skew(values):
    return skew(values)


# Cálculo da curtose
def calc_kurtosis(values):
    return kurtosis(values)


# Cálculo da entropia
def calc_entropy(values):
    return entropy(values)
