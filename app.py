from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form5', methods=['GET', 'POST'])
def form5():
    if request.method == 'POST':
        qiziqishlar = request.form.getlist('qiziqish')
        return f"<h2>Sizning qiziqishlaringiz:</h2><p>{qiziqishlar}</p><br><a href='/'>Orqaga</a>"
    return render_template('form5.html')

if __name__ == '__main__':
    app.run(debug=True)
