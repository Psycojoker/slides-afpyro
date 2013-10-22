a = "hello"

b = "world"

class Pouet():
    def hello_world(self, c, d):
        from ipdb import set_trace; set_trace()
        print c, d

Pouet().hello_world(a, b)
