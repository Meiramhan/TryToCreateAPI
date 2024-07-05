from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api()

getSettings = {
                "wid": "11001234567@c.us",
                "countryInstance": "",
                "typeAccount": "",
                "webhookUrl": "https://mysite.com/webhook/green-api/",
                "webhookUrlToken": "",
                "delaySendMessagesMilliseconds": 5000,
                "markIncomingMessagesReaded": "no",
                "markIncomingMessagesReadedOnReply": "no",
                "sharedSession": "no",
                "outgoingWebhook": "yes",
                "outgoingMessageWebhook": "yes",
                "outgoingAPIMessageWebhook": "yes",
                "incomingWebhook": "yes",
                "deviceWebhook": "no",
                "statusInstanceWebhook": "no",
                "stateWebhook": "no",
                "enableMessagesHistory": "no",
                "keepOnlineStatus": "no",
                "pollMessageWebhook": "no",
                "incomingBlockWebhook": "yes",
                "incomingCallWebhook": "yes"
        }

getStateInstance = {
    "stateInstance": "authorized"
}



sendMessage = {
"chatId": "@c.us"
}





class GetSettings(Resource):
    def getSettings(self):
        return getSettings

class GetStateInstance(Resource):
    def getStateInstance(self):
        return getStateInstance


class SendMessage(Resource):
    def sendMessage(self):
        return sendMessage


class SendFileByUrl(Resource):
    def sendFileByUrl(self):
        return sendMessage



api.add_resource(GetSettings, "/7103.api.greenapi.com/waInstance7103954757/getSettings/3eb176d047084b1999b22dbe791210b579e115ef6ab24a648d")
api.add_resource(GetStateInstance, "/7103.api.greenapi.com/waInstance7103954757/getStateInstance/3eb176d047084b1999b22dbe791210b579e115ef6ab24a648d")
api.add_resource(SendMessage, "/7103.api.greenapi.com/waInstance7103954757/sendMessage/3eb176d047084b1999b22dbe791210b579e115ef6ab24a648d")
api.add_resource(SendFileByUrl, "/7103.api.greenapi.com/waInstance7103954757/sendFileByUrl/3eb176d047084b1999b22dbe791210b579e115ef6ab24a648d")
api.init_app(app)



if __name__ == "__main__":
    app.run(debug=True, port=7103, host="localhost")