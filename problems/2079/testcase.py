from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 2, 3, 3], 5], Output=14))
		self.testcases.append(case(Input=[[1, 1, 1, 4, 2, 3], 4], Output=30))
		self.testcases.append(case(Input=[[7, 7, 7, 7, 7, 7, 7], 8], Output=49))

	def get_testcases(self):
		return self.testcases
