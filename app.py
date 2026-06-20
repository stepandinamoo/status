from flask import Flask, render_template_string, request

app = Flask(__name__)

current_status = "off"

last_command = ""

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Статус сервера</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
            background: #f0f0f0;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            width: 400px;
            margin: 0 auto;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            font-size: 24px;
            margin-bottom: 20px;
        }
        .status {
            font-size: 24px;
            font-weight: bold;
            padding: 12px;
            margin: 15px 0;
            border-radius: 8px;
        }
        .on {
            background: #4CAF50;
            color: white;
        }
        .off {
            background: #f44336;
            color: white;
        }
        .button {
            display: inline-block;
            padding: 8px 16px;
            margin: 5px;
            font-size: 16px;
            cursor: pointer;
            text-decoration: none;
            color: white;
            border-radius: 5px;
            border: none;
        }
        .btn-on {
            background: #4CAF50;
        }
        .btn-off {
            background: #f44336;
        }
        .btn-command {
            background: #2196F3;
        }
        .btn-command:hover {
            background: #0b7dda;
        }
        .info {
            margin-top: 20px;
            padding: 10px;
            background: #e0e0e0;
            border-radius: 5px;
            font-family: monospace;
            font-size: 12px;
        }
        .message {
            margin-top: 15px;
            padding: 10px;
            background: #d4edda;
            color: #155724;
            border-radius: 5px;
            font-size: 14px;
            font-weight: bold;
        }
        code {
            font-size: 11px;
        }
        .commands-section {
            margin-top: 20px;
            padding-top: 15px;
            border-top: 1px solid #ddd;
        }
        h3 {
            font-size: 18px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Статус</h1>

        <div class="status {% if status == 'on' %}on{% else %}off{% endif %}">
            {% if status == 'on' %}
                 ON
            {% else %}
                 OFF
            {% endif %}
        </div>

        <div>
            <a href="/?status=on" class="button btn-on">Включить</a>
            <a href="/?status=off" class="button btn-off">Выключить</a>
        </div>

        <div class="commands-section">
            <h3>Команды</h3>
            <div>
                <a href="/?command=1" class="button btn-command">Команда 1</a>
                <a href="/?command=2" class="button btn-command">Команда 2</a>
                <a href="/?command=3" class="button btn-command">Команда 3</a>
            </div>
        </div>

        {% if message %}
        <div class="message">
            {{ message }}
        </div>
        {% endif %}

        <div class="info">
            <strong>URL команды:</strong><br>
            <code>/?status=on</code> - Включить<br>
            <code>/?status=off</code> - Выключить<br>
            <code>/?command=1</code> - Команда 1<br>
            <code>/?command=2</code> - Команда 2<br>
            <code>/?command=3</code> - Команда 3
        </div>
    </div>
</body>
</html>
'''


@app.route('/')
def index():
    global current_status, last_command

    status_param = request.args.get('status')
    command_param = request.args.get('command')

    message = None

    if status_param == 'on':
        current_status = 'on'
        print(f"Статус изменен на: ON")
    elif status_param == 'off':
        current_status = 'off'
        print(f"Статус изменен на: OFF")
    if command_param == '1':
        message = "Операция выполнена! (Команда 1)"
        print(f"Выполнена команда 1")
    elif command_param == '2':
        message = "Операция выполнена! (Команда 2)"
        print(f"Выполнена команда 2")
    elif command_param == '3':
        message = "Операция выполнена! (Команда 3)"
        print(f"Выполнена команда 3")

    return render_template_string(HTML_TEMPLATE, status=current_status, message=message)


if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("Сервер запущен на порту 80!")
    print("Откройте: http://localhost:80")
    print("\nДоступные команды:")
    print("   ?status=on   - Включить")
    print("   ?status=off  - Выключить")
    print("   ?command=1   - Команда 1")
    print("   ?command=2   - Команда 2")
    print("   ?command=3   - Команда 3")
    print("=" * 50 + "\n")

    app.run(debug=True, host='0.0.0.0', port=80)