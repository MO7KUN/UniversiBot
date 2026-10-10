FROM rasa/rasa:3.6.20-full
WORKDIR /app
COPY --chown=1001:0 config.yml domain.yml credentials.yml endpoints.yml /app/
COPY --chown=1001:0 data /app/data
COPY --chown=1001:0 tests/test_stories.yml tests/nlu.yml /app/tests/
USER 1001

