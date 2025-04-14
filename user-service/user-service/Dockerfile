FROM openjdk:17-jdk-slim
WORKDIR /app
#Copy maven build jar file
COPY /target/user-service-1.0-SNAPSHOT.jar app.jar
#Expose the app
EXPOSE 8080
#Run jar file
ENTRYPOINT ["java", "-jar", "app.jar"]
