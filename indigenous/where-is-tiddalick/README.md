1. OSINT search for Tiddalick’s location to reveal password = `Wollombi`
  - Reverse image search with Google Lens (Exact Matches) to find the source of the image: <https://historyofaboriginalsydney.edu.au/north-west/location/wollombi-place-where-waters-meet>
2. `steghide extract -sf Where_Is_Tiddalick.JPG`, password = `Wollombi`
  - This extracts the metadata into `flag.txt`, which contains `pecan{VGhlX3dvcmRfV29sbG9tYmlfbWVhbnNfUGxhY2VfV2hlcmVfV2F0ZXJzX01lZXQ=}` (and a hint)
3. Decrypt the contents of the `{}`s with base64 and compose the final flag.
