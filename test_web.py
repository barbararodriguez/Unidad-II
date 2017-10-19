from potential_energy import potential
from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def home() -> '302':
    return redirect('/entry')


@app.route('/entry')
def go_entry() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to the form')


@app.route('/calculate', methods=['POST'])
def calculate() -> 'html':
    G = float(request.form['G'])
    M = float(request.form['M'])
    m = float(request.form['m'])
    r = float(request.form['r'])

    result = potential(G, M, m, r)
    title = "Gravitational Potential Energy"
    return render_template('result.html', the_G=G, the_M=M, the_m=m, the_r=r, the_result=result, the_title=title)


app.run(debug=True)
