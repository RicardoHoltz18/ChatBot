from twilio.rest import Client 
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from datetime import datetime, timedelta

#Configurações do Twilio
account_sid = 'ACb175e6e4316a33429fd56ba297912d73'
auth_token = '72d7d2beaeb9897f1fcf93e4ec5da3bd'
client = Client(account_sid, auth_token)

app = Flask (__name__)
#data e horas 
data_horas_disponiveis = [
    datetime(2024,3, 9, 9, 30 ),
    datetime(2024,3, 9, 10, 0 ),
    datetime(2024,3, 9, 10, 30 ),
    datetime(2024,3, 9, 11, 0 ),
    datetime(2024,3, 9, 11, 30 ),
    datetime(2024,3, 9, 12, 0 ),
    datetime(2024,3, 9, 12, 30 ),
    datetime(2024,3, 9, 13, 0 )
]
@app.route('/webhook', methods= ['GET','POST'])
def webhook () : 
    incoming_message = request.values.get( 'Body','' )
    response = process_message(incoming_message)
    twiml = MessagingResponse()
    twiml.message(response)
    return str (twiml)

def process_message(message):
    return 'Oi, tudo bem? \n Estes são as horas disponíveis para consulta: ' + ObterDatasHorasDisponiveis()

def ObterDatasHorasDisponiveis ():
    return '\n'.join([dh.strftime('%d-%m-%Y - %H:%M') for dh in data_horas_disponiveis])
if __name__ == '__main__':
    app.run(debug=True)
    



