import numpy as np
import skfuzzy as fuzzy
import matplotlib.pyplot as plt

from skfuzzy import control
from meteocalc import heat_index as calc_heat_index, Temp

heat_index = control.Antecedent(np.arange(0, 71, 1), 'Heat index')
heat_index['Cold'] = fuzzy.trapmf(heat_index.universe, [0, 0, 10, 21])
heat_index['Comfortable'] = fuzzy.trimf(heat_index.universe, [10, 21, 32])
heat_index['Uncomfortable'] = fuzzy.trimf(heat_index.universe, [22, 31, 40])
heat_index['Hot'] = fuzzy.trimf(heat_index.universe, [34, 41, 48])
heat_index['Very hot'] = fuzzy.trimf(heat_index.universe, [43, 50, 58])
heat_index['Health risk'] = fuzzy.trapmf(heat_index.universe, [50, 61, 70, 70])

internal_temperature = control.Antecedent(np.arange(0, 41, 1), 'Internal temperature')
internal_temperature['Cold'] = fuzzy.trapmf(internal_temperature.universe, [0, 0, 10, 20])
internal_temperature['Kinda cold'] = fuzzy.trimf(internal_temperature.universe, [15, 20, 25])
internal_temperature['Comfortable'] = fuzzy.trimf(internal_temperature.universe, [20, 25, 30])
internal_temperature['Kinda hot'] = fuzzy.trimf(internal_temperature.universe, [25, 30, 35])
internal_temperature['Hot'] = fuzzy.trapmf(internal_temperature.universe, [30, 35, 40, 40])

ideal_temperature = control.Consequent(np.arange(0, 41, 1), 'Ideal temperature')
ideal_temperature['Max'] = fuzzy.trapmf(ideal_temperature.universe, [0, 0, 10, 19])
ideal_temperature['Cold'] = fuzzy.trimf(ideal_temperature.universe, [17, 19, 21])
ideal_temperature['Kinda cold'] = fuzzy.trimf(ideal_temperature.universe, [19, 21, 23.5])
ideal_temperature['Comfortable'] = fuzzy.trimf(ideal_temperature.universe, [21, 24, 26])
ideal_temperature['Kinda hot'] = fuzzy.trimf(ideal_temperature.universe, [24, 26, 28])
ideal_temperature['Off'] = fuzzy.trapmf(ideal_temperature.universe, [26, 33, 40, 40])

rule1 = control.Rule(heat_index['Cold'] & internal_temperature['Cold'], ideal_temperature['Off'])
rule2 = control.Rule(heat_index['Cold'] & internal_temperature['Kinda cold'], ideal_temperature['Off'])
rule3 = control.Rule(heat_index['Cold'] & internal_temperature['Comfortable'], ideal_temperature['Off'])
rule4 = control.Rule(heat_index['Cold'] & internal_temperature['Kinda hot'], ideal_temperature['Off'])
rule5 = control.Rule(heat_index['Cold'] & internal_temperature['Hot'], ideal_temperature['Kinda hot'])
rule6 = control.Rule(heat_index['Comfortable'] & internal_temperature['Cold'], ideal_temperature['Off'])
rule7 = control.Rule(heat_index['Comfortable'] & internal_temperature['Kinda cold'], ideal_temperature['Off'])
rule8 = control.Rule(heat_index['Comfortable'] & internal_temperature['Comfortable'], ideal_temperature['Off'])
rule9 = control.Rule(heat_index['Comfortable'] & internal_temperature['Kinda hot'], ideal_temperature['Off'])
rule10 = control.Rule(heat_index['Comfortable'] & internal_temperature['Hot'], ideal_temperature['Kinda cold'])
rule11 = control.Rule(heat_index['Uncomfortable'] & internal_temperature['Cold'], ideal_temperature['Kinda cold'])
rule12 = control.Rule(heat_index['Uncomfortable'] & internal_temperature['Kinda cold'], ideal_temperature['Kinda cold'])
rule13 = control.Rule(heat_index['Uncomfortable'] & internal_temperature['Comfortable'], ideal_temperature['Kinda cold'])
rule14 = control.Rule(heat_index['Uncomfortable'] & internal_temperature['Kinda hot'], ideal_temperature['Cold'])
rule15 = control.Rule(heat_index['Uncomfortable'] & internal_temperature['Hot'], ideal_temperature['Cold'])
rule16 = control.Rule(heat_index['Hot'] & internal_temperature['Cold'], ideal_temperature['Cold'])
rule17 = control.Rule(heat_index['Hot'] & internal_temperature['Kinda cold'], ideal_temperature['Cold'])
rule18 = control.Rule(heat_index['Hot'] & internal_temperature['Comfortable'], ideal_temperature['Kinda cold'])
rule19 = control.Rule(heat_index['Hot'] & internal_temperature['Kinda hot'], ideal_temperature['Max'])
rule20 = control.Rule(heat_index['Hot'] & internal_temperature['Hot'], ideal_temperature['Max'])
rule21 = control.Rule(heat_index['Very hot'] & internal_temperature['Cold'], ideal_temperature['Cold'])
rule22 = control.Rule(heat_index['Very hot'] & internal_temperature['Kinda cold'], ideal_temperature['Cold'])
rul223 = control.Rule(heat_index['Very hot'] & internal_temperature['Comfortable'], ideal_temperature['Cold'])
rule24 = control.Rule(heat_index['Very hot'] & internal_temperature['Kinda hot'], ideal_temperature['Max'])
rule25 = control.Rule(heat_index['Very hot'] & internal_temperature['Hot'], ideal_temperature['Max'])
rule26 = control.Rule(heat_index['Health risk'] & internal_temperature['Cold'], ideal_temperature['Cold'])
rule27 = control.Rule(heat_index['Health risk'] & internal_temperature['Kinda cold'], ideal_temperature['Max'])
rule28 = control.Rule(heat_index['Health risk'] & internal_temperature['Comfortable'], ideal_temperature['Max'])
rule29 = control.Rule(heat_index['Health risk'] & internal_temperature['Kinda hot'], ideal_temperature['Max'])
rule30 = control.Rule(heat_index['Health risk'] & internal_temperature['Hot'], ideal_temperature['Max'])

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

simulator.input['Internal temperature'] = 23

temperature = float(input("Enter the temperature: "))
humidity = float(input("Enter the humidity: "))

simulator.input['Heat index'] = calc_heat_index(temperature=Temp(temperature, 'c'), humidity=humidity).c

simulator.compute()

print("The ideal temperature is " + str(simulator.output['Ideal temperature']))

heat_index.view(sim=simulator)
internal_temperature.view(sim=simulator)
ideal_temperature.view(sim=simulator)

plt.show()
