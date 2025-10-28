from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
('Weather', 'Humidity'),
('Weather', 'PlayTennis'),
('Humidity', 'PlayTennis')
])

cpd_weather = TabularCPD(variable='Weather', variable_card=2,
values=[[0.6], [0.4]],
state_names={'Weather': ['Sunny', 'Rainy']})
cpd_humidity = TabularCPD(variable='Humidity', variable_card=2,
values=[[0.3, 0.8],
[0.7, 0.2]],
evidence=['Weather'],
evidence_card=[2],
state_names={'Humidity': ['High', 'Normal'],
'Weather': ['Sunny', 'Rainy']})

cpd_play = TabularCPD(variable='PlayTennis', variable_card=2,
values=[[0.4, 0.9, 0.1, 0.5], # Yes
[0.6, 0.1, 0.9, 0.5]], # No
evidence=['Weather', 'Humidity'],
evidence_card=[2, 2],
state_names={'PlayTennis': ['Yes', 'No'],
'Weather': ['Sunny', 'Rainy'],
'Humidity': ['High', 'Normal']})

model.add_cpds(cpd_weather, cpd_humidity, cpd_play)
assert model.check_model(), "Model is incorrect!"

infer = VariableElimination(model)
query_result = infer.query(variables=['PlayTennis'], evidence={'Weather': 'Sunny'})

print(query_result)
