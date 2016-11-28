import dask.array as da
from dask.diagnostics import Profiler

a = da.random.random(size=(10000, 1000), chunks=(1000, 1000))
q, r = da.linalg.qr(a)
a2 = q.dot(r)

with Profiler() as prof:
    out = a2.compute()
    import code
    code.interact(local=locals())
    prof.visualize()
