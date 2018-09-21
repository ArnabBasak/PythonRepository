import  pyping
r = pyping.ping('google.com')
if r.ret_code == 0:
    print("not reachable")
else:
    print("hello")