import random 
from django.core.cache import cache




def send_otp_to_mobile(mobile , user_obj):
    if cache.get(mobile):
        return False , cache.ttl(mobile)
    try:
        otp_to_sent = random.randint(1000 , 9999)
        cache.set(mobile,otp_to_sent , timeout=60)
        user_obj.otp = otp_to_sent
        user_obj.save()
        return True , 0
    except Exception as e:
        print(e)