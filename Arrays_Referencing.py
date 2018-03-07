import copy

counters = [0] * 8
print(counters)
c = counters
counters[1] = 1
print(counters)
print(c)
backup = list(counters)
counters[2] = 1
print(backup)
print(counters)
ones = [1] * 8 + ['asd']
xx = copy.deepcopy(counters)
counters.extend(ones)
print(counters)
