Get Image information for the memory dump.

`./vol.py -f Roasty.raw imageinfo`

Get console outputs.

`./vol.py -f Roasty.raw --profile Win7SP1x86_23418 consoles`

In the consoles output we can see the executable was Rubeus and there is a kerberoast attack occuring. You can also pull the pid of the powershell process.
