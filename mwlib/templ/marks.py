
class mark(str):
    def __new__(klass, msg):
        r=str.__new__(klass)
        r.msg = msg
        return r
    
    def __repr__(self):
        return '<%s %r>' % (self.__class__.__name__, self.msg,)

class mark_start(mark): pass
class mark_end(mark): pass
class mark_maybe_newline(mark): pass

maybe_newline = mark_maybe_newline('maybe_newline')
dummy_mark = mark('dummy')

class _eqmark(str):
    def __eq__(self, other):
        return self is other

eqmark = _eqmark("=")
