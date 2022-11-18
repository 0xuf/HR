FROM golang

RUN go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
RUN go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
RUN mv $GOPATH/bin/subfinder /usr/bin/subfinder
RUN mv $GOPATH/bin/nuclei /usr/bin/nuclei


FROM python:3.10

ADD ./hr_django /root/hr_django
ADD nginx/default.conf /etc/nginx/conf.d/default.conf
WORKDIR "/root/hr_django"

RUN pip install -r requirements.txt
RUN apt update -y
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic

CMD ["/bin/bash", "/root/hr_django/run.sh"]