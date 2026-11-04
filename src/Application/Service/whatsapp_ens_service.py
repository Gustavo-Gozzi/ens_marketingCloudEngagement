#from src.Domain.whatsapp_ens import WhatsAppENS


class WhatsAppENSService:
    @staticmethod
    def parseJson(lista):
        try:
            if lista[0][""]["senderType"] == "WhatsApp":
                json = lista[0]

                messageId = json["messageId"]
                channelId = json["channelId"]
                mobileNumber = json["mobileNumber"]
                contactId = json["contactId"]
                messageBody = json["messageBody"]["text"]["body"]

                return {
                    "messageId": json["messageId"],
                    "channelId": json["channelId"],
                    "mobileNumber": json["mobileNumber"],
                    "contactId": json["contactId"],
                    "messageBody": json["messageBody"]["text"]["body"]
                }
        except:
            print("Caiu no Except: ", lista)
            return lista



        
        
