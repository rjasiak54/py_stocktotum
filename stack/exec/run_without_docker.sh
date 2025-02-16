#!/usr/bin/env sh
set -a
. ./stack/env-sandbox/.env
export CNT_PORT_HTTP=$HOST_PORT_HTTP
set +a

python3 -m py_stocktotum.server.start