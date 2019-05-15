Atlanta Batted Ball Data Analysis

A simple web app that uses given excel sheet to visualize the relationship between two chosen variables.

Uses pandas for excel analysis
Utilizes Matplotlib, pylab, numpy for data visualization

Libraries implemented can be found in requirements.txt

First enter the directory downloaded using cd bravesWeb

Then install using "pip install -r requirements.txt" in terminal

None of these graphs and visualizations were hardcoded, the data analysis is done all in backend in the /batData/analyze/analyzelib python file.

Currently the combinations that should be used include the following:

For Bar Graphs: Variable1= PLAY_OUTCOME, Variable2= Any of the others

For Histograms: Variable1= Any, Variable2= Histogram does not consider variable2

For Line Graph: Variable1= Any, Variable2 = Any

Front end is done in all html,CSS, and Django-python implementation

Once pip install is complete, please type "python manage.py runserver" in terminal

If this causes an error involving some libraries "not being installed", try:
"pip3 install -r requirements.txt" in the terminal

If needed, static files can be located in bravesWeb/static/graphs/plot.png

Documentation for analyzelib.py can be found in the file!