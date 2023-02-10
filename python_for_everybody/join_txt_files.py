import json

from config import basedir

cases = basedir.joinpath('..', 'static', 'input_cases.txt')
expected = basedir.joinpath('..', 'static', 'expected_cases.txt')
final = basedir.joinpath('..', 'static', 'test_cases.json')

try:
    lcases = list()
    lexpected = list()

    with open(cases.absolute()) as cases, open(expected.absolute()) as expected:
        lcases = [c.strip() for c in cases]
        lexpected = [e.strip() for e in expected]

    ljson = list()
    for i in range(0, len(lcases)):
        ljson.append({'test_input': lcases[i], 'expected': lexpected[i]})

    with open(final.absolute(), 'w') as final:
        json.dump(ljson, final)
except IOError as e:
    print('Operation failed: %s' % e.strerror)
