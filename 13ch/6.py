class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"
    
    def public_method(self):
        print("OK")

    def _unsafe_method(self):
        pass

public = PublicPrivateExample()
#public.public_method()

public._unsafe_method()
