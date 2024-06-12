FROM openjdk:11
VOLUME /tmp
ADD target/delivery-app-1.0-SNAPSHOT.jar delivery-app.jar
ENTRYPOINT ["java","-jar","/delivery-app.jar"]
