import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Calculadora de Notas"),
    html.Div("Esta aplicacion es para calcular la nota que debo sacar en la ultima evaluación"),
    html.Form(id='form1',children=[
        dcc.Input(id='porcentaje1', type='number', min=0, max=100, placeholder="Porcentaje nota 1"),
        dcc.Input(id='nota1', type='number', min=0, max=5, placeholder="nota 1")
        ]),
    html.Form(id='form2',children=[
        dcc.Input(id='porcentaje2', type='number', min=0, max=100, placeholder="Porcentaje nota 2"),
        dcc.Input(id='nota2', type='number', min=0, max=5, placeholder="nota 2")
        ]),
    html.Form(id='form3',children=[
        dcc.Input(id='porcentaje3', type='number', min=0, max=100, placeholder="Porcentaje nota 3"),
        dcc.Input(id='nota3', type='number', min=0, max=5, placeholder="nota 3")
        ]),
    html.Div("La nota que debes sacar para ganar la materia en 3 es: "),
    html.Div(id='notadesalida',children="")
])

@app.callback(Output('notadesalida','children'),Input('porcentaje1','value'),Input('porcentaje2','value'),Input('porcentaje3','value'),Input('nota1','value'),Input('nota2','value'),Input('nota3','value'))
def calculadora(p1,p2,p3,n1,n2,n3):
    notafinal = (3 - ((float(p1)/100)*n1 + (float(p2)/100)*n2 + (float(p3)/100)*n3))/(1-((float(p1)/100)+(float(p2)/100)+(float(p3)/100)))
    return notafinal

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=80)
