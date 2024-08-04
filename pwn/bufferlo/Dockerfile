# If you like, you can work on this locally by running something like:
# docker build -t buffalo .
# docker run -d -p 1358:1358 --name buffalo buffalo
#
# Then, you can just 'nc localhost 1358' to mess around with it on your own computer!

FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends socat=1.7.4.4-2 && \
    rm -rf /var/lib/apt/lists/*

COPY vuln flag.txt /home/ctf/
RUN chmod +x /home/ctf/vuln && \
    chmod +r /home/ctf/flag.txt && \
    useradd -ms /bin/bash ctf && \
    chown -R root:root /home/ctf

USER ctf
WORKDIR /home/ctf

# Run the challenge using socat
EXPOSE 1358/tcp
CMD ["socat", "-dd", "TCP4-LISTEN:1358,fork,reuseaddr", "EXEC:/home/ctf/vuln,pty,echo=0,raw,iexten=0"]
