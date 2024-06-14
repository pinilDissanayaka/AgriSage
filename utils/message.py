import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")

class Message(object):
    def __init__(self) -> None:
        self.servicePlanId = os.getenv('SMS_SERVICE_PLAN_ID')
        self.apiToken = os.getenv('SMS_API')
        self.sinchNumber = os.getenv('SMS_SINCH_NUMBER')
        self.toNumber = None
        self.url = "https://us.sms.api.sinch.com/xms/v1/" + self.servicePlanId + "/batches"
        
    
    def sendSms(self, otp:int, toNumber:int):
        payload = {
            "from": self.sinchNumber,
            "to": [
                toNumber
            ],
            "body": f"Your verification code for completing your profile setup is: {otp}."
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.apiToken
        }
        
        response = requests.post(self.url, json=payload, headers=headers)
