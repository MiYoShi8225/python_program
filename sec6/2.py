class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        #clientが使っていい場所
        pass #pass文は文が必須な構文で何もしない場合につかう

    def _unsafe_method(self):
        #clientは使ってはいけない(原則)
        pass


