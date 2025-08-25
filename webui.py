from flask import Flask, request
from difflib import SequenceMatcher
from ollama_model import *
from lang import *

user = configparser.ConfigParser()
user.read('user.ini')

app = Flask(__name__)

check = 0

def password_recovery_func(username, password, threshold=0.7):
    user_password = user[username]["password"]
    ratio = SequenceMatcher(None, user_password, password).ratio()
    if ratio >= threshold:
        password = user[username]["password"]
        return f"{your_password}: {password}"
    else:
        return f"{password_recovery_failed}"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        lang = request.form['lang']
        set_lang(lang)
    else:
        lang = "Language"
    global check
    check = 0
    return f"""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <title>{app_title}</title>
    <h1 class="ms-2">{app_title}</h1>
    <form action="/" method="post">
    <select class="form-select form-select-sm position-absolute end-0 me-2" onchange="this.form.submit()" name="lang" style="top: 7px; width: 15%;">
    <option value="" disabled selected hidden>{lang}</option>
    <option value="TR">TR</option>
    <option value="EN">EN</option>
    </select>
    </form>
    <form action="/login" method="post">
    <input class="form-control form-control-sm w-75 ms-2" type="text" name="username" placeholder="{user_name_input}"/> <br>
    <input class="form-control form-control-sm w-75 ms-2" type="password" name="password" placeholder="{password_input}"/> <br>
    <input class="btn btn-primary ms-2" type="submit" value="{login_var}"/>
    </form>
    <a class="btn btn-primary ms-2" href="/user">{new_user_register}</a>
    """

@app.route('/login', methods=['POST'])
def login():
    global check
    username = request.form['username']
    password = request.form['password']

    if username in user and user[username]["password"] == password:
        check = 1
        return f"""
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <title>{login_successfully}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <h1 class="ms-2">{login_successfully}</h1> <p class="ms-2">{welcome}, {username}</p>
        <a class="btn btn-primary ms-2" href="/app">{go_to_app}</a>
        """
    else:
        username = request.form['username']
        return f"""
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <title>{login_failed}</title>
        <h1 class="ms-2">{login_failed}</h1> <p class="ms-2">{login_failed_description}</p>
        <form action="/passrecovery" method="post">
        <input type="hidden" name="username" value="{username}"/>
        <a class="btn btn-primary ms-2" href="/user">{user_register}</a><a class="btn btn-primary ms-2" href="/">{try_again}</a>
        <br>
        <input class="btn btn-primary ms-2 mt-2" type="submit" value="{password_forget}"/>
        </form>
        """

@app.route('/passrecovery', methods=['GET', 'POST'])
def pass_recovery():
    if request.method == 'POST':
        username = request.form['username']
        return f"""
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <title>{password_recovery}</title>
        <h1 class="ms-2">{password_recovery}</h1>
        <p class="ms-2">{username} {password_recovery_}</p>
        <form action="/recovery" method="post">
        <input type="hidden" name="username" value="{username}"/>
        <input class="form-control form-control-sm w-75 ms-2" type="password" name="password" placeholder="{password_recovery_input} {username} {pass_rec_}"/> <br>
        <input class="btn btn-primary ms-2" type="submit" value="{password_recovery_submit}"/>
        </form>
        """
@app.route('/recovery', methods=['GET', 'POST'])
def recovery():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f"""
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <title>{password_recovery_report}</title>
        <h1 class="ms-2">{password_recovery_report}</h1>
        <p class="ms-2">{password_recovery_func(username, password)}</p>
        <a class="btn btn-primary ms-2" href="/">{try_again}</a>
        """

@app.route('/user')
def user_form():
    if request.method == 'POST':
        username = request.form['username']

        if username in user:
            return f"""
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
            <title>{user_register_failed}</title>
            <h1>{user_register_failed}</h1>
            <a href="/user">{try_again}</a>
            """

    return f"""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <title>{new_user_register}</title>
    <h1 class="ms-2">{new_user_register}</h1>
    <form action="/adduser" method="post">
    <input class="form-control form-control-sm w-75 ms-2" type="text" name="username" placeholder="{user_name_input}"/> <br>
    <input class="form-control form-control-sm w-75 ms-2" type="password" name="password" placeholder="{password_input}"/> <br>
    <input class="btn btn-primary ms-2" type="submit" value="{register}"/>
    </form>
    """

@app.route('/adduser', methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    ip_address = request.remote_addr
    if user.has_section(f"{username}"):
        return f"""
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <h1 class="ms-2">{user_register_failed_title}</h1> <p class="ms-2">{user_register_failed}</p>
            <a class="btn btn-primary ms-2" href="/user">{try_again}</a>
        """
    for section in user.sections():
        if user[section]["ip_address"] == ip_address:
            return f"""
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
            <title>{user_register_failed_title}</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <h1 class="ms-2">{user_register_failed_title}</h1> <p class="ms-2">{user_register_ip}</p>
            <a class="btn btn-primary ms-2" href="/user">{try_again}</a>
            """
    else:
        if password == "":
            return f"""
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
            <title>{user_register_failed_title}</title>
            <h1 class="ms-2">{user_register_failed_title}</h1> <p class="ms-2">{user_register_failed_description}</p>
            <a class="btn btn-primary ms-2" href="/user">{try_again}</a>
            """
    user_ip = request.remote_addr
    user.add_section(f"{username}")
    user.set(f"{username}", "password", f"{password}")
    user.set(f"{username}", "ip_address", f"{user_ip}")
    with open("user.ini", "w") as configfile:
        user.write(configfile)
        return f"""
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <title>{user_register_successfully}</title>
        <h1 class="ms-2">{user_register_successfully}</h1> <p class="ms-2">{user_register_successfully_description}</p>
        <a class="btn btn-primary ms-2" href="/">{login_var}</a>
        """

@app.route('/app', methods=['GET', 'POST'])
def app_page():
    if check == 1:
        return f"""
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <title>{ollama_web_ui_title}</title>
        <h1 class="ms-2">{ollama_web_ui_title}</h1>
        <form action="/chat" method="post">
        <input class="form-control form-control-sm w-75 ms-2" type="text" name="model" placeholder="{user_model}"/>
        <input class="form-control form-control-sm w-75 ms-2 mt-2" type="text" name="msg" placeholder="{model_question}"/> <br>
        <input class="btn btn-primary ms-2" type="submit" value="{model_submit}"/>
        </form>
        <a class="btn btn-primary ms-2" href="/">{exit}</a>
        """
    else:
        return f"""
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <title>{app_requirements}</title>
        <h1 class="ms-2">{app_requirements}</h1>
        <p class="ms-2">{app_requirements_description}</p>
        <a  class="btn btn-primary ms-2" href="/">{login_var}</a>
        """
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == "POST":
        model = request.form["model"]
        msg = request.form["msg"]
        user_response = f"{user_}: {msg}"
        model_response = load_model(model, msg)
        return f"""
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <title>{model}</title>
            <p class="alert alert-primary w-75 ms-2 mt-2">{user_response}</p>
            <p class="alert alert-success w-75 ms-2">{model}: {model_response}</p>
            <form action="/chat" method="post">
                <input type="hidden" name="model" value="{model}"/>
                <input class="form-control form-control-sm w-75 ms-2" type="text" name="msg" placeholder="{model_question}"/>
                <input class="btn btn-primary ms-2 mt-2" type="submit" value="{model_submit}"/>
            </form>
            <a  class="btn btn-primary ms-2" href="/">{exit}</a>
            """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)