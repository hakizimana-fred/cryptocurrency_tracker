from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/track-coin/', methods=['GET'])
def trackCoin():
    coin = request.args.get('coin')
    response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={coin}&tsyms=USD,EUR')
    return jsonify(response.json()) 

@app.route('/track/top-coins/', methods=['GET'])
def trackTopCoins():
    f = open('coins.txt', 'r')
    coins = f.readlines()
    cryptos = []

    for i, coin in enumerate(coins):
        response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={coin.rstrip()}&tsyms=USD,EUR')
        cryptos.append({"symbol": coin, "value": response.json()})
    return jsonify(cryptos)
    


if __name__ == '__main__':
    app.run()
