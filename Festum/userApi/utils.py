import math
import uuid
import random
from django.core.cache import cache



# @@@ refer code generator
def generate_ref_code():
    code = str(uuid.uuid4().hex[0:8]).replace("-", "")
    return code


# @@@@ OTP Generator
def generateOTP() :
        
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP


# Ticket number
def TicketNum():
    num = str(uuid.uuid4().hex[0:11]).replace("-", "")
    return num


    
  