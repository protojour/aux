from aux.logging import LogController
from aux.internals.configuration import config
from datetime import datetime

logcontroller = LogController(config)

logcontroller.summary['started'] = datetime.now()

logcontroller.summary['logfolder'] = "fakdir/dir/dir"

logcontroller.summary['testsubject'] = "machine13"

logcontroller.summary['test'] = "atestname"

logcontroller.summary['tester'] = "mr.imatester"

logcontroller.summary['externalref'] = "our_test_test"

logcontroller.summary['success'] = True

logcontroller.summary['ended'] = datetime.now()


# POST /api/test/result HTTP/1.1
# Host: 192.168.0.135:8080
# Cache-Control: no-cache
# Content-Length: 200
# Authorization: Basic dGVzdGVyOnRlc3Rlcg==
# User-Agent: Aux/0.1 (X11;Ubuntu;Linux x86_64;rv:24.0)

# {"started": "2014-12-12 15:01:00.030206",
#  "ended": "2014-12-12 15:01:00.030236",
#  "testsubject": "machine21",
#  "test": "testname",
#  "tester": "auxscript",
#  "success": false,
#  "logfolder": "fakdir/dir/dir"}


# POST /api/test/result HTTP/1.1
# Host: 192.168.0.135:8080
# Connection: keep-alive
# Content-Length: 237
# User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36
# Cache-Control: no-cache
# Origin: chrome-extension://fdmmgilgnpjigdojojpjoooidkmcomcm
# Authorization: Basic dGVzdGVyOnRlc3Rlcg==
# Content-Type: text/plain;charset=UTF-8
# Accept: */*
# Accept-Encoding: gzip,deflate
# Accept-Language: en-US,en;q=0.8,nb;q=0.6
# Cookie: remember_token=540dca214af87e1bb6cfd637|9a3b22c600ef35cce6ec9e919b1ca79e762299b9; session=.eJytjl1rgzAYhf9KeK9llOhuhN4M2-IgcR1pJRml2DRTY6IliXS0-N_XfcHY9a4O5-J5zrnC_tVUvlEe0pcroPAVB0jhUG4vEi97sZ7PYYrgyajKK2SGGrU9CgOqpFTeo9C0Hp2qWt3Bbor-wbGLbqec8g2kwY3q1tojpN_GYrXsOKtnQj8YmnUXykwrbJ4ItkiK8tEQXZ8p28TU5p-LcnRO9WF_coNWMvxWUbbGRJP7IpMzXvKE4k3M8VYX2dFy_Ww_8NEr94c5ixVtiF78MG_c5phj0VFNYpimdzrybJs.B2yE2Q.uBjfG0JVO5ijDbrpk62Z2h8X470
# 
# {"started": "2014-11-08 18:36:51.639000",
# "ended": "2014-11-08 18:40:00.639000",
# "testsubject": "a computer",
# "test": "shimmering test",
# "tester": "mr testman",
# "externalref": "a test",
# "success": false,
# "logfolder": "somewhere/on/disk"}


