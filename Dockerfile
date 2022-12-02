FROM python:3.8

# set environment 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
#set directory
WORKDIR /cinematica
#set requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . /cinematica
RUN python manage.py makemigrations
RUN python manage.py migrate
EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]