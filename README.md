# nodelist-to-json

- This has only been tested on FSXNET nodelist with Python 3.
- I only need certain data in the JSON, so many of the unessisary node flags are omitted.
- No Zone or Region handing, assume fsxNet's Zone & Region 21.
- HOSTS, PVT, DOWN nodes are skipped -- just includes nodes that can be accessed via Telnet.
