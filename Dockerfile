FROM nginx:alpine


ADD ./hr_django /root/hr_django
ADD ./hr_django/nginx.conf /etc/nginx/conf.d/default.conf
WORKDIR "/root/hr_django"

RUN apk add --no-cache build-base
RUN apk add --no-cache python3 ; ln -sf python3 /usr/bin/python
RUN apk add --no-cache py3-pip
RUN apk add --no-cache python3-dev
RUN pip install -r requirements.txt
RUN apk add --no-cache go
RUN go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
RUN go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
RUN mv /root/go/bin/subfinder /usr/bin/subfinder
RUN mv /root/go/bin/nuclei /usr/bin/nuclei
RUN rm -rf /etc/nginx/conf.d/default.conf
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic

CMD python -m celery  -A hr worker -l info
CMD gunicorn hr.wsgi