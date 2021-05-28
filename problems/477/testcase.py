from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[4, 14, 2], Output=6))
        self.testcases.append(case(Input=[4, 14, 4], Output=4))

    def get_testcases(self):
        return self.testcases
