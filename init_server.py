from flask import Flask, request

app = Flask(__name__)

@app.route('/main')
def main():
    print(f"Utilize a URL como base http://127.0.0.1:8085/main?nota1=6&nota2=7 para enviar os parametros de nota1 e nota2 para saber se a média dessas 2 notas o possibilita passar de ano.")

    nota1 = request.args.get('nota1')
    nota2 = request.args.get('nota2')
    
    if nota1 and nota2:
        nota1 = float(nota1)
        nota2 = float(nota2)

        media = (nota1 + nota2) / 2

        resultado_final = 'aaaaaaaaaaaaaaaaaaaaaaaaaa'

        if media >= 7.0:
            resultado_final = f'Parabéns! Você foi aprovado com média {media}.'
        elif media >=5.0:
            res = 7 - media
            resultado_final = f'Putz. Você foi reprovado com média {media}, mas como falta essa quatidade, {res}, para a média. Você pode pedir recuperação para passar.'
        else:
            resultado_final = f'Desculpa. Você foi reprovado com média {media}. Meus pêsames'
            
        return resultado_final
    print(resultado_final)
    
if __name__ == '__main__':
    app.run(port=8085, host='0.0.0.0', debug=True, threaded=True)