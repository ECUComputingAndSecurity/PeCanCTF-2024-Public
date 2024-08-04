Get Image information for the memory dump.

`./vol.py -f Roasty.raw imageinfo`

Get console outputs.

`./vol.py -f Roasty.raw --profile Win7SP1x86_23418 consoles`

Get Network information.

`./vol.py -f Roasty.raw --profile Win7SP1x86_23418 netscan`
We are able to compile the flag by getting the domain controller IP by finding connections over port 88 which is known for Kerberos.
