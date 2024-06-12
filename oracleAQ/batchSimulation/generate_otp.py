# python generate_otp.py
import redis
import random

r = redis.Redis(host='localhost', port=6379, db=0)

for i in range(100000):
    order_id = f"{i+1}"
    otp = random.randint(1000, 9999)
    r.set(order_id, otp)
    print(f"Generated OTP {otp} for order {order_id}")
