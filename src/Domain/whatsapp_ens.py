class WhatsAppENS:
    def __init__(self, messageId, channelId, mobilenumber, contactid, messageBody):
        self.messageId = messageId
        self.channelId = channelId
        self.mobilenumber = mobilenumber
        self.contactid = contactid
        self.messageBody = messageBody

    
    def to_dict(self):
        return {
            "messageId": self.messageId
            "channelId": self.channelId
            "mobilenumber": self.mobilenumber
            "contactid": self.contactid
            "messageBody": self.messageBody
        }