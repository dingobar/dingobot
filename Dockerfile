FROM python:3.8 as builder

# Install poetry
ENV PATH="/root/.local/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python -

# Copy the files into the container
COPY . .

# Install and build binary
RUN poetry install && poetry build

FROM python:3.8-slim

# Copy binary from build container
ENV WHEEL_FILENAME=dingobot-0.1.0-py3-none-any.whl
COPY --from=builder dist/${WHEEL_FILENAME} ./${WHEEL_FILENAME}

RUN pip install ./${WHEEL_FILENAME}