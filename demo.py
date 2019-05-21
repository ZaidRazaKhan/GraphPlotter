import plotly
import plotly.plotly as py
import plotly.graph_objs as go


plotly.tools.set_credentials_file(username='zaidRaza', api_key='uADqV4uvTk7KJxzXWusP')


trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = [trace0, trace1]

out ='<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>' + plotly.offline.plot(data, include_plotlyjs=False, output_type='div')
print(out)
# print(plotly.offline.plot(data, include_plotlyjs=False, output_type='div'))

