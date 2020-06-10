FROM python:3.7.7-alpine

ENV ECS_MESSAGE "初回実行"

COPY test.py .

CMD ["sh", "-c", "python3 ./test.py $ECS_MESSAGE"]