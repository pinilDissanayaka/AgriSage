import math
import random

class OTP(object):
    def generateOTP(self) :
 
        digits = "0123456789"
        self.OTP = ""
 
        for i in range(5) :
            self.OTP += digits[math.floor(random.random() * 10)]
 
        return self.OTP
    
    def checkOTP(self, otp:int):
        if otp==self.OTP:
            return True
        else:
            return False
        
    
    