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
CMD ["socat", "-dd", "TCP4-LISTEN:1357,fork,reuseaddr", "EXEC:/home/ctf/vuln,pty,echo=0,raw,iexten=0"]
EXPOSE 1357/tcp
