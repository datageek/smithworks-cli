FROM python:3.8

WORKDIR /opt/smithworks-cli

# install poetry to container
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH /root/.poetry/bin:$PATH

# build project env
COPY ./pyproject.toml /opt/smithworks-cli/pyproject.toml
RUN poetry install