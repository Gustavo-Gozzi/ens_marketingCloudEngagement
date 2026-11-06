from src.Application.Controller.whatsapp_ens_controller import WhatsAppENSController
from flask import Flask, request

def register_routes(app):

    @app.route('/ens', methods=["POST"])
    def wpp_ens():
        return WhatsAppENSController.parseJson()


    @app.route('/ens', methods=["GET"])
    def get_ens():
        token = request.args.get("hub.verify_token", default="")
        challenge = request.args.get("hub.challenge", default="")

        return WhatsAppENSController.get(token, challenge)