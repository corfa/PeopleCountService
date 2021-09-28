
FROM python:latest
EXPOSE 8000

RUN git clone https://github.com/corfa/FixPeopleCountService.git
RUN pip install --no-cache-dir -r /PeopleCountService/requirements.txt
RUN python /PeopleCountService/main.py

