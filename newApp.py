from flask import Flask
from flask import render_template
import plotly as py
import plotly.graph_objs as go
app = Flask(__name__, static_url_path='')
import numpy as np
import pandas as pd

# plotly.tools.set_credentials_file(username='zaidRaza', api_key='uADqV4uvTk7KJxzXWusP')
ImportedJs = '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>'

# trace0 = go.Scatter(
#     x=[1, 2, 3, 4],
#     y=[10, 15, 13, 17]
# )
# trace1 = go.Scatter(
#     x=[1, 2, 3, 4],
#     y=[16, 5, 11, 9]
# )
# data = [trace0, trace1]

# out = plotly.offline.plot(data, include_plotlyjs=False, output_type='div')
# out ='<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>' + plotly.offline.plot(data, include_plotlyjs=False, output_type='div')
# print(plotly.offline.plot(data, include_plotlyjs=False, output_type='div'))
# help(plotly.offline.plot)
# print(out)



@app.route('/')
def root():
    return render_template('demo_html.html')


@app.route('/get_graph')
def index():
    trace0 = go.Scatter(
    	x=[1, 2, 3, 4],
    	y=[10, 15, 13, 17]
    	)
    trace1=go.Scatter(
    	x=[1, 2, 3, 4], 
    	y=[16, 5, 11, 9]
    	)# data = [ trace0, trace1 ]
    data=[trace0, trace1]
    out ='<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>' + py.offline.plot(data, include_plotlyjs=False, output_type='div')
    return out


@app.route('/get_scattered_graph')
def get_scattered_graph():
	N = 1000
	random_x = np.random.randn(N)
	random_y = np.random.randn(N)
	trace = go.Scatter(x = random_x, y = random_y, mode = 'markers')
	data = [trace]
	ImportedJs = '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>'
	out = ImportedJs+py.offline.plot(data, include_plotlyjs=False, output_type='div')
	return out


@app.route('/get_pie_chart')
def get_pie_chart():
	labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
	values = [4500,2500,1053,500]
	trace = go.Pie(labels=labels, values=values)
	data = [trace]
	ImportedJs = '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>'
	out = ImportedJs+py.offline.plot(data, include_plotlyjs=False, output_type='div')
	return out


@app.route('/get_histogram')
def get_histogram():
	data = [go.Bar(x=['giraffes', 'orangutans', 'monkeys'], y=[20, 14, 23])]
	ImportedJs = '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>'
	out = ImportedJs+py.offline.plot(data, include_plotlyjs=False, output_type='div')
	return out


@app.route('/get_table')
def get_table():
    trace = go.Table(
    header=dict(values=['A Scores', 'B Scores']),
    cells=dict(values=[[100, 90, 80, 90],
                       [95, 85, 75, 95]]))
    data = [trace] 
    out = ImportedJs+py.offline.plot(data, include_plotlyjs='False', output_type='div')
    return out


if __name__ == '__main__':
    app.run(debug=True)
