#from src.Domain.whatsapp_ens import WhatsAppENS
from flask import Flask, make_response

class WhatsAppENSService:
    @staticmethod
    def parseJson(lista):
        try:
            if lista[0]["senderType"] == "WhatsApp":
                json = lista[0]

                messageId = json["messageId"]
                channelId = json["channelId"]
                mobileNumber = json["mobileNumber"]
                contactId = json["contactId"]
                messageBody = json["messageBody"]["text"]["body"]

                resposta = {
                    "messageId": json["messageId"],
                    "channelId": json["channelId"],
                    "mobileNumber": json["mobileNumber"],
                    "contactId": json["contactId"],
                    "messageBody": json["messageBody"]["text"]["body"]
                }
                print(resposta)
                return resposta
        except:
            print("Caiu no Except: ", lista)
            return lista


    @staticmethod
    def get(token, challenge):
        response = make_response(challenge, 200) 
        response.mimetype = "text/plain" 
        return response
        
        
