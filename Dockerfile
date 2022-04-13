FROM python
RUN pip install pipenv
WORKDIR /app
COPY /Pipfile .
COPY . .
EXPOSE 8000
RUN pipenv install --system --deploy
CMD["uvicorn","app.main:app","--host=0.0.0.0","--reload"]