def mysum(*args):
    if not args:
        return 0
    result = args[0]
    for i in args[1:]:
        result += i
    return result