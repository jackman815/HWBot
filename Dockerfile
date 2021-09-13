FROM python:slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update
RUN apt-get install -y unzip curl wget libxss1 libappindicator1 libindicator7
RUN apt-get install -y fonts-liberation libasound2 libatk-bridge2.0-0 libdrm2 libgbm1 libgtk-3-0 libnspr4 libnss3 libxkbcommon0 libxshmfence1 xdg-utils
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb && apt install -f
COPY . .
RUN wget https://chromedriver.storage.googleapis.com/$(curl https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip

ENV DOCKER 1
ENV USERID ""
ENV moodle_host ""
ENV moodle_username ""
ENV moodle_password ""
ENV chrome_driver "./chromedriver"
ENV Discord_APIKEY ""

CMD [ "python", "./main.py" ]