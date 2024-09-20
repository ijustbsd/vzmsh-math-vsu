FROM alpine

COPY exec.sh /exec.sh

RUN \
    chmod +x /exec.sh && \
    apk add --update --no-cache python3 curl cmd:pip3 && \
    pip3 install --break-system-packages --upgrade pip && \
    pip3 install --break-system-packages pelican markdown tzdata && \
    rm -rf /var/cache/apk/*

CMD ["/exec.sh"]
