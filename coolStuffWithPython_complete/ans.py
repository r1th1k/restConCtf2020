#!/usr/bin/env python3

import base64

message = ''.join([ chr(int(n)-1) for n in base64.b64decode("ODMgNzAgODQgODUgNjggODAgNzkgMTI0IDExNyAxMTggMTE1IDExNyAxMDkgMTAyIDk2IDEwNiAxMTYgOTYgMTAwIDExMiAxMTIgMTA5IDEyNiA=".encode("ascii")).decode("ascii").split(" ")[:-1]])

print(message)