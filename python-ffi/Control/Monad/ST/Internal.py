def map_(f):
    return lambda a: lambda: f(a())


def pure_(a):
    return lambda: a


def bind_(a):
    return lambda f: lambda: f(a())()


def run(f):
    return f()


def while_(f):
    def ap_a(a):
        def ap():
            while f():
                a()
            return ()

        return ap

    return ap_a


globals()["while"] = while_


def for_(lo):
    def ap_hi(hi):
        def ap_f(f):
            def ap():
                for i in range(lo, hi):
                    f(i)()

            return ap

        return ap_f

    return ap_hi


globals()["for"] = for_


def foreach(as_):
    def ap_f(f):
        def ap():
            for a in as_:
                f(a)()

        return ap

    return ap_f


def new(val):
    return lambda: {"value": val}


def read(ref):
    return lambda: ref["value"]


def modify_(f):
    def ap_ref(ref):
        def ap():
            t = f(ref["value"])
            ref["value"] = t["state"]
            return t["value"]

        return ap

    return ap_ref


globals()["modify'"] = modify_


def write(a):
    def ap_ref(ref):
        def ap():
            ref["value"] = a
            return

        return ap

    return ap_ref

