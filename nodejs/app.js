const express = require('express');
const bodyParser = require('body-parser');
const redis = require('redis');
const client = redis.createClient();

const app = express();
app.use(bodyParser.json());

app.post('/placeOrder', (req, res) => {
    const orderDetails = req.body;
    client.rpush('user_queue', JSON.stringify(orderDetails));
    res.send('Order placed');
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
