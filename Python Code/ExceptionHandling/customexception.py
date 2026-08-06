class Temp(Exception):
    pass

try:
    res = 10 / 0
except:
    raise Temp("Denominoter must be > 0")