DECLARE
v_message SYS.AQ$_JMS_TEXT_MESSAGE;
  v_enqueue_options DBMS_AQ.ENQUEUE_OPTIONS_T;
  v_message_properties DBMS_AQ.MESSAGE_PROPERTIES_T;
  v_message_handle RAW(16);
BEGIN
FOR i IN 1..100000 LOOP
    v_message := SYS.AQ$_JMS_TEXT_MESSAGE('Order details for order ' || i);
    DBMS_AQ.ENQUEUE(
      queue_name          => 'user_queue',
      enqueue_options     => v_enqueue_options,
      message_properties  => v_message_properties,
      payload             => v_message,
      msgid               => v_message_handle
    );
END LOOP;
COMMIT;
END;
/
EXIT;