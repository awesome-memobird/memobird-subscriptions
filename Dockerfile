FROM python:3-alpine

# download temprun
ENV TEMPRUN_VER=0.2-alpha
ENV TEMPRUN_URL=https://github.com/tevino/temprun/releases/download/${TEMPRUN_VER}/temprun.v${TEMPRUN_VER}.lnx.tar.gz
RUN wget -O- ${TEMPRUN_URL} | tar -xv -C /bin/

# add tzdata
RUN apk add --no-cache tzdata

# install memobird package
ADD . /memobird
RUN pip install /memobird

# time to run on weekdays and weekends
ENV WEEK_HOUR=9
ENV WEEKEND_HOUR=10

ENV TZ='Asia/Shanghai'

ENV AK="YOUR_ACCESS_TOKEN"
ENV DEVICE_ID="YOUR_DEVICE_ID"

ENV CAIYUN_TOKEN="YOUR_CAIYUN_API_TOKEN"
ENV CAIYUN_LOCATION="YOUR_LOCATION"


# entrypoint
ENTRYPOINT [ "/bin/temprun.lnx", "-src", "/memobird/crontab", "-dst", "/etc/crontabs/root", "/bin/sh", "-c" ]
CMD [ "date; crond -f -l 0" ]