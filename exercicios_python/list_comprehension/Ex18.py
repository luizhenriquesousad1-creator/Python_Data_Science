# Ex 18

produtos = [{"nome": "teclado", "preço": 100}, {"nome": "mouse","preço": 50}, {"nome": "monitor","preço": 900}]

print([produto["preço"] for produto in produtos if produto["preço"] > 100])