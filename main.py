from flask import Flask, render_template, request, redirect, url_for, session, make_response

app = Flask(__name__)


app.secret_key = 'f3c26108e4e0747b5bada82bc68cf60c8ff47ab27974fca8693ccd00043a4f68'

@app.route('/')
def index():
    if 'login' in session:
        return f'Привет, {session["login"]}'
    else:
        return redirect(url_for('submit'))



@app.get('/submit/')
def submit_get():
    context = {
        'login': 'Авторизация'
    }
    return render_template('form.html', **context)


@app.post('/submit/')
def submit_post():
    session['login'] = request.form.get('login')
    session['email'] = request.form.get('email')
    return redirect(url_for('success'))


@app.route('/success/', methods=['GET', 'POST'])
def success():
    if 'login' in session:
        context = {
            'login': session['login'],
            'email': session['email'],
            'title': 'Добро пожаловать'
        }
        if request.method == 'POST':
            session.pop('login', None)
            session.pop('email', None)
            return redirect(url_for('submit_get'))
        return render_template('success.html', **context)
    else:
        return redirect(url_for('login'))


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

