from functools import wraps

def extract_first_arg(arg):
    if not isinstance(arg, str):
        return None
    if not (arg.startswith('@') or arg.startswith('$')):
        return None

    sink, source = [], []
    for a in arg.split('$'):
        if a.startswith('@'):
            sink.append(a[1:].strip())
        elif a == '':
            continue
        else:
            source.append(a.strip())
    return source, sink


def decorator(fn):
    @wraps(fn)
    def wrapper(self, *args, **kw):

        datasrc, datasink = [], []
        newargs = []

        try:
            datasrc, datasink = extract_first_arg(args[0])
        except TypeError as e:
            newargs = [ args[0] ]
        except IndexError:
            pass

        for i, arg in enumerate(args[1:]):
            newargs.append(arg)
        newargs = [self.data[src] for src in datasrc ] + newargs

        if len(datasink) > 1:
            pass # warning
        else:
            output = fn(self, *newargs, **kw)
            try:
                self.data[datasink[0]] = output
            except IndexError:
                return output 

    return wrapper


class MetaDecorator(type):
    def __new__(cls, name, bases, local):
        local['data'] = {}
        local['images'] = {}
        for key, value in local.items():
            if key.startswith("__"): continue
            if not hasattr(value, "__call__"): continue
            local[key] = decorator(value)
        return type.__new__(cls, name, bases, local)


class DataPipe(object):
    __metaclass__ = MetaDecorator


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# test
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class TestDataPipe(DataPipe):
    def get2(self):
        return 2
    def mulitply(self, data, factor):
        return data*factor

def test_decorator():
    p = TestDataPipe()
    p.get2('@test')
    assert p.data['test'] == 2

    p.mulitply('@multiple $test', 5)
    assert p.data['multiple'] == 10

    assert p.get2() == 2
