FROM python:3-slim-bookworm

RUN apt-get update && \
    apt-get install -y --no-install-recommends socat=1.7.4.4-2 && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir pycryptodome==3.20.0

COPY chall.py flag.txt /home/ctf/
RUN useradd -ms /bin/bash ctf && \
    chown -R root:root /home/ctf

USER ctf
WORKDIR /home/ctf

# Run the challenge using socat
EXPOSE 1360
CMD ["socat", "-dd", "TCP4-LISTEN:1360,fork,reuseaddr", "EXEC:\"python3 chall.py\",pty,echo=0,raw,iexten=0"]
