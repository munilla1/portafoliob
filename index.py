from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/curriculumb')
def curriculumb():
    return render_template('curriculumb.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == "__main__":
    
    app.run(debug=True,
            port=8080)