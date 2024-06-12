package com.example.deliveryapp;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.web.bind.annotation.*;

@RestController
public class DeliveryController {

    @Autowired
    private StringRedisTemplate redisTemplate;

    @PostMapping("/updateStatus")
    public String updateStatus(@RequestBody DeliveryRequest request) {
        String orderId = request.getOrderId();
        String status = request.getStatus();
        redisTemplate.opsForValue().set(orderId + "_status", status);
        return "Status updated to " + status;
    }

    @GetMapping("/getStatus/{orderId}")
    public String getStatus(@PathVariable String orderId) {
        return redisTemplate.opsForValue().get(orderId + "_status");
    }
}
