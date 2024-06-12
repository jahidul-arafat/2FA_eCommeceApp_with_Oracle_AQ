# python enqueue_orders.py
import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

for i in range(100000):
    order_details = {
        "orderId": f"{i+1}",
        "username": f"user{i+1}",
        "deliveryLocation": f"location{i+1}",
        "status": "PENDING"
    }
    r.rpush('user_queue', json.dumps(order_details))
