# DoS'ed out

---

The core challenge is to find out what happened to the attacked server by reading the output of a provided packet capture.
The participant is tasked with determining what the suspected IP address is, where that address originated from and how many packets they sent with a SYN flag only.

I have used Kali to generate some DoS traffic to the Server which was really just another Virtual Machine in that contained environment. The biggest hint is in the second part of the file name which is "Synflood".

Determining the IP address that the attack is coming from should be rather straight forward, the start of the DoS attack is quite easy to pick up that something suspicious is going on. The second part of the flag is slightly trickier to find but a simple question to Google, which will help you find the way to capture the packets quite quickly.

Determining the IP address' originating country you use Google to help you find an IP geolocation tool and paste the address you have found to give you the originating country of that address.

Wireshark filter to find the number of packets: `tcp.flags.syn==1 && tcp.flags.ack==0 && ip.addr==90.4.7.157`
