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

ideal_temperature = control.Consequent(np.arange(0, 41, 1), 'Temperatura ideal')
ideal_temperature['maxima'] = fuzzy.trapmf(ideal_temperature.universe, [0, 0, 10, 19])
ideal_temperature['frio'] = fuzzy.trimf(ideal_temperature.universe, [17, 19, 21])
ideal_temperature['meio frio'] = fuzzy.trimf(ideal_temperature.universe, [19, 21, 23.5])
ideal_temperature['confortavel'] = fuzzy.trimf(ideal_temperature.universe, [21, 24, 26])
ideal_temperature['meio quente'] = fuzzy.trimf(ideal_temperature.universe, [24, 26, 28])
ideal_temperature['desligado'] = fuzzy.trapmf(ideal_temperature.universe, [26, 33, 40, 40])

rule1 = control.Rule(heat_index['frio'] & internal_temperature['frio'], ideal_temperature['desligado'])
rule2 = control.Rule(heat_index['frio'] & internal_temperature['meio frio'], ideal_temperature['desligado'])
rule3 = control.Rule(heat_index['frio'] & internal_temperature['confortavel'], ideal_temperature['desligado'])
rule4 = control.Rule(heat_index['frio'] & internal_temperature['meio quente'], ideal_temperature['desligado'])
rule5 = control.Rule(heat_index['frio'] & internal_temperature['quente'], ideal_temperature['meio quente'])
rule6 = control.Rule(heat_index['confortavel'] & internal_temperature['frio'], ideal_temperature['desligado'])
rule7 = control.Rule(heat_index['confortavel'] & internal_temperature['meio frio'], ideal_temperature['desligado'])
rule8 = control.Rule(heat_index['confortavel'] & internal_temperature['confortavel'], ideal_temperature['desligado'])
rule9 = control.Rule(heat_index['confortavel'] & internal_temperature['meio quente'], ideal_temperature['desligado'])
rule10 = control.Rule(heat_index['confortavel'] & internal_temperature['quente'], ideal_temperature['meio frio'])
rule11 = control.Rule(heat_index['desconfortavel'] & internal_temperature['frio'], ideal_temperature['meio frio'])
rule12 = control.Rule(heat_index['desconfortavel'] & internal_temperature['meio frio'], ideal_temperature['meio frio'])
rule13 = control.Rule(heat_index['desconfortavel'] & internal_temperature['confortavel'], ideal_temperature['meio frio'])
rule14 = control.Rule(heat_index['desconfortavel'] & internal_temperature['meio quente'], ideal_temperature['frio'])
rule15 = control.Rule(heat_index['desconfortavel'] & internal_temperature['quente'], ideal_temperature['frio'])
rule16 = control.Rule(heat_index['quente'] & internal_temperature['frio'], ideal_temperature['frio'])
rule17 = control.Rule(heat_index['quente'] & internal_temperature['meio frio'], ideal_temperature['frio'])
rule18 = control.Rule(heat_index['quente'] & internal_temperature['confortavel'], ideal_temperature['meio frio'])
rule19 = control.Rule(heat_index['quente'] & internal_temperature['meio quente'], ideal_temperature['maxima'])
rule20 = control.Rule(heat_index['quente'] & internal_temperature['quente'], ideal_temperature['maxima'])
rule21 = control.Rule(heat_index['super quente'] & internal_temperature['frio'], ideal_temperature['frio'])
rule22 = control.Rule(heat_index['super quente'] & internal_temperature['meio frio'], ideal_temperature['frio'])
rul223 = control.Rule(heat_index['super quente'] & internal_temperature['confortavel'], ideal_temperature['frio'])
rule24 = control.Rule(heat_index['super quente'] & internal_temperature['meio quente'], ideal_temperature['maxima'])
rule25 = control.Rule(heat_index['super quente'] & internal_temperature['quente'], ideal_temperature['maxima'])
rule26 = control.Rule(heat_index['risco a saude'] & internal_temperature['frio'], ideal_temperature['frio'])
rule27 = control.Rule(heat_index['risco a saude'] & internal_temperature['meio frio'], ideal_temperature['maxima'])
rule28 = control.Rule(heat_index['risco a saude'] & internal_temperature['confortavel'], ideal_temperature['maxima'])
rule29 = control.Rule(heat_index['risco a saude'] & internal_temperature['meio quente'], ideal_temperature['maxima'])
rule30 = control.Rule(heat_index['risco a saude'] & internal_temperature['quente'], ideal_temperature['maxima'])

air_control = control.ControlSystem([
    rule1,
    rule2,
    rule3,
    rule4,
    rule5,
    rule6,
    rule7,
    rule8,
    rule9,
    rule10,
    rule11,
    rule12,
    rule13,
    rule14,
    rule15,
    rule16,
    rule17,
    rule18,
    rule19,
    rule20,
    rule21,
    rule22,
    rul223,
    rule24,
    rule25,
    rule26,
    rule27,
    rule28,
    rule29,
    rule30
])

simulator = control.ControlSystemSimulation(air_control)

simulator.input['Temperatura interna'] = 23
simulator.input['IC'] = 32

simulator.compute()

print(simulator.output['Temperatura ideal'])

heat_index.view(sim=simulator)
internal_temperature.view(sim=simulator)
ideal_temperature.view(sim=simulator)

plt.show()
