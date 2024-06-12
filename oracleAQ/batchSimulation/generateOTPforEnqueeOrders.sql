DECLARE
CURSOR order_cursor IS SELECT order_id FROM order_table WHERE status = 'PENDING';
v_otp VARCHAR2(10);
BEGIN
FOR order_rec IN order_cursor LOOP
    v_otp := DBMS_RANDOM.VALUE(1000, 9999);
UPDATE order_table SET otp = v_otp WHERE order_id = order_rec.order_id;
END LOOP;
COMMIT;
END;
/
EXIT;