from django import forms

FIRST_VARIABLE_CHOICES = (
	('LAUNCH_ANGLE', 'LAUNCH_ANGLE'),
	('EXIT_SPEED', 'EXIT_SPEED'),
	('EXIT_DIRECTION', 'EXIT_DIRECTION'),
	('HIT_DISTANCE', 'HIT_DISTANCE'),
	('HANG_TIME', 'HANG_TIME'),
	('HIT_SPIN_RATE', 'HIT_SPIN_RATE'),
	('PLAY_OUTCOME', 'PLAY_OUTCOME'),
)
SECOND_VARIABLE_CHOICES = (
	('PLAY_OUTCOME', 'PLAY_OUTCOME'),
	('LAUNCH_ANGLE', 'LAUNCH_ANGLE'),
	('EXIT_SPEED', 'EXIT_SPEED'),
	('EXIT_DIRECTION', 'EXIT_DIRECTION'),
	('HIT_DISTANCE', 'HIT_DISTANCE'),
	('HANG_TIME', 'HANG_TIME'),
	('HIT_SPIN_RATE', 'HIT_SPIN_RATE'),
	('NONE', 'NONE')
)

GRAPH_TYPE = (
	('Bar Chart', 'Bar Chart'),
	('Scatter Plot', 'Scatter Plot'),
	('Histogram', 'Histogram'),
)
class SimulationForm(forms.Form):
	variable1 = forms.ChoiceField(choices=FIRST_VARIABLE_CHOICES)
	variable2 = forms.ChoiceField(choices=SECOND_VARIABLE_CHOICES)
	graph = forms.ChoiceField(choices=GRAPH_TYPE)