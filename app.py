import math
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get form data
            a = int(request.form['a'])
            b = int(request.form['b'])
            c = int(request.form['c'])

            # Call the equation solver function
            result = equeationSolver(a, b, c)

            # Render the results in a template
            return render_template('result.html', result=result)
        except ValueError:
            # Handle invalid input (e.g., non-numeric values)
            return render_template('index.html', error="Please enter valid numbers for a, b, and c.")
    else:
        return render_template('index.html')

def equeationSolver(a, b, c):
    """Solves the quadratic equation ax^2 + bx + c = 0 and returns the roots."""
    dis = (b**2) - 4 * a * c
    if dis == 0:
        root1 = root2 = (-b / (2 * a))
        return f'Root 1: {root1}\nRoot 2: {root2}'
    elif dis > 0:
        root1 = (-b + math.sqrt(dis)) / (2 * a)
        root2 = (-b - math.sqrt(dis)) / (2 * a)
        return f'Root 1: {root1}\nRoot 2: {root2}'
    else:
        realPart = (-b / (2 * a))
        imPart = (math.sqrt(-dis) / (2 * a))
        return f'Root 1: {realPart} + {imPart}i\nRoot 2: {realPart} - {imPart}i'

if __name__ == '__main__':
    app.run(debug=True)
