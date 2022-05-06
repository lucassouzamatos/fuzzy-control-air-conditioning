import numpy as np
import skfuzzy as fuzzy

from skfuzzy import control
import matplotlib.pyplot as plt

heat_index = control.Antecedent(np.arange(0, 71, 1), 'IC')
heat_index['frio'] = fuzzy.trapmf(heat_index.universe, [0, 0, 10, 21])
heat_index['confortavel'] = fuzzy.trimf(heat_index.universe, [10, 21, 32])
heat_index['desconfortavel'] = fuzzy.trimf(heat_index.universe, [22, 31, 40])
heat_index['quente'] = fuzzy.trimf(heat_index.universe, [34, 41, 48])
heat_index['super quente'] = fuzzy.trimf(heat_index.universe, [43, 50, 58])
heat_index['risco a saude'] = fuzzy.trapmf(heat_index.universe, [50, 61, 70, 70])

internal_temperature = control.Antecedent(np.arange(0, 41, 1), 'Temperatura interna')
internal_temperature['frio'] = fuzzy.trapmf(internal_temperature.universe, [0, 0, 10, 20])
internal_temperature['meio frio'] = fuzzy.trimf(internal_temperature.universe, [15, 20, 25])
internal_temperature['confortavel'] = fuzzy.trimf(internal_temperature.universe, [20, 25, 30])
internal_temperature['meio quente'] = fuzzy.trimf(internal_temperature.universe, [25, 30, 35])
internal_temperature['quente'] = fuzzy.trapmf(internal_temperature.universe, [30, 35, 40, 40])

ideal_temperature = control.Antecedent(np.arange(0, 41, 1), 'Temperatura ideal')
ideal_temperature['maxima'] = fuzzy.trapmf(ideal_temperature.universe, [0, 0, 10, 19])
ideal_temperature['frio'] = fuzzy.trimf(ideal_temperature.universe, [17, 19, 21])
ideal_temperature['meio frio'] = fuzzy.trimf(ideal_temperature.universe, [19, 21, 23.5])
ideal_temperature['confortavel'] = fuzzy.trimf(ideal_temperature.universe, [21, 24, 26])
ideal_temperature['meio quente'] = fuzzy.trimf(ideal_temperature.universe, [24, 26, 28])
ideal_temperature['desligado'] = fuzzy.trapmf(ideal_temperature.universe, [26, 33, 40, 40])

plt.show()
