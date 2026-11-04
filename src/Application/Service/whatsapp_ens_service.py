#from src.Domain.whatsapp_ens import WhatsAppENS


class WhatsAppENSService:
    @staticmethod
    def parseJson(lista):
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
        
