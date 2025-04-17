# Use the official Golang image as the base image
FROM golang:1.22-alpine AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy the Go mod and sum files to download dependencies
COPY go.mod go.sum ./
RUN go mod download

# Copy the rest of the application files
COPY . .

# Build the Go application
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o recommend-service .

# Use a minimal base image to run the application
FROM alpine:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the built Go binary from the builder image
COPY --from=builder /app/recommend-service .

# Expose the port the service will run on
EXPOSE 8081

# Set the entrypoint to run the Go service
ENTRYPOINT ["/app/recommend-service"]

