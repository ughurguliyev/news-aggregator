FROM redis:4.0.11

ENV REDIS_PASSWORD 1qvSgjrAIRAHqD2ZqdV1Ojzxw

CMD ["sh", "-c", "exec redis-server --requirepass \"$REDIS_PASSWORD\""]