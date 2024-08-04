Get Image information for the memory dump.

`./vol.py -f Roasty.raw imageinfo`

Get console outputs.

`./vol.py -f Roasty.raw --profile Win7SP1x86_23418 consoles`

In the consoles output we can find all the kerberos hashes for the SPNS under all the accounts. Of which contains the Administrator and Backup account hashes.

Save the hashes to a file and crack the hashes with hashcat.

```
$krb5tgs$23$*Administrator$PECAN.LOCAL$kafka/FINWWEBS1000000*$<snip>
$krb5tgs$23$*backup$PECAN.LOCAL$HTTP/backups.kerberos.pecan.local*$<snip>
```

`sudo hashcat -m 13100 hashes.kerb /usr/share/wordlists/rockyou.txt --force`
