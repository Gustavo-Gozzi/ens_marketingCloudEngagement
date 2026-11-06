from src.Application.Service.whatsapp_ens_service import WhatsAppENSService
from flask import request, jsonify, make_response

class WhatsAppENSController:
    @staticmethod
    def parseJson():
        data = request.get_json()
        response = WhatsAppENSService.parseJson(data)

        return make_response(jsonify(response))

    @staticmethod
    def get(token, challenge):
        return WhatsAppENSService.get(token, challenge)