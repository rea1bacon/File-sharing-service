# Simple File sharing tool

## Sharing client usage

(You will need to use python3 for linux)

```bash
main.py --send -f file/path
```

Optionnal flags :
- pwd : set a password

## Receiving client usage

(You will need to use python3 for linux)

```bash
main.py --recv -adr remote_host_address -port remote_host_port
```
Optionnal flags :
- o : output the file in a different firectory or different name
