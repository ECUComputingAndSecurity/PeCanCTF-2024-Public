```
# Recognise the directory "Windows.old" is a backup of the "Windows" directory
unzip upgrade.zip

# Install pypykatz (https://github.com/skelsec/pypykatz)
pip3 install pypykatz

# Extract SAM Secrets with SAM and SYSTEM registry hives
pypykatz registry Windows.old/System32/config/SYSTEM --sam Windows.old/System32/config/SAM

# Crack the User Accounts NTLM Hash
echo -ne "217e50203a5aba59cefa863c724bf61b" > hash.txt
hashcat -m 1000 hash.txt /usr/share/wordlists/rockyou.txt

# Flag
pecan{P@ssw0rd!}
```
