ARG image_go
ARG image_alpine
FROM ${image_go} AS builder

WORKDIR /app
COPY PtN .
RUN go build -o program main.go

FROM ${image_alpine}
RUN apk --no-cache add ca-certificates bash
WORKDIR /root/
COPY --from=builder /app/program .
EXPOSE 8080
ENTRYPOINT ["./program"]
