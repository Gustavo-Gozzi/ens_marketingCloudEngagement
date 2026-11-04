from src.Application.Controller.whatsapp_ens_controller import WhatsAppENSController


def register_routes(app):

    @app.route('/ens', methods=["POST"])
    def wpp_ens():
        return WhatsAppENSController.parseJson()