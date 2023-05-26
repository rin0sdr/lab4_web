from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html', 'r') as file:
        return file.read()

# Відповідь на запит GET /script.js
@app.route('/script.js')
def script():
    with open('script.js', 'r') as file:
        return file.read()



# Обробка запиту GET /api
@app.route('/api', methods=['GET'])
def api():
    # Отримання параметрів запиту
    expression = request.args.get('expression')
    # Виконання обробки
    url = 'https://newton.vercel.app/api/v2/derive/' + expression
    response = requests.get(url)
    data = response.json()
    result = data['result']
    return result

if __name__ == '__main__':
    import sys

    # Перевірка аргументів командного рядка для задання порту
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080

    # Запуск сервера на вказаному порті
    app.run(port=port)
