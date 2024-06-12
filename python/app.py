from flask import Flask, request
import random
import redis

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/generateOtp', methods=['POST'])
def generate_otp():
    order_id = request.json['order_id']
    otp = random.randint(1000, 9999)
    r.set(order_id, otp)
    return {'otp': otp}

@app.route('/validateOtp', methods=['POST'])
def validate_otp():
    order_id = request.json['order_id']
    input_otp = request.json['otp']
    stored_otp = r.get(order_id)
    if stored_otp == input_otp:
        r.set(f'{order_id}_status', 'DELIVERED')
        return {'status': 'DELIVERED'}
    else:
        r.set(f'{order_id}_status', 'FAILED')
        return {'status': 'FAILED'}

if __name__ == '__main__':
    app.run(port=5000)
