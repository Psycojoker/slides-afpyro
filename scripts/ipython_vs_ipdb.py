for i in range(3):
    from IPython import embed; embed()
    print i

for i in range(3):
    from ipdb import set_trace; set_trace()
    print i
