FROM alpine

COPY exec.sh /exec.sh

RUN \
    chmod +x /exec.sh && \
    apk add --update --no-cache python3 wget cmd:pip3 && \
    pip3 install --upgrade pip && \
    pip3 install pelican markdown && \
    rm -rf /var/cache/apk/*

CMD ["/exec.sh"]
