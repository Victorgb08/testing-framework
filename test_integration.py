from test_case import TestCase
from test_result import TestResult

class MyTest(TestCase):

    def set_up(self):
        print('set_up')

    def tear_down(self):
        print('tear_down')

    def test_success(self):
        print('test_success')

    def test_failure(self):
        assert False

    def test_error(self):
        raise Exception("Error occurred")

# Executando os testes
result = TestResult()

test = MyTest('test_success')
test.run(result)

test = MyTest('test_failure')
test.run(result)

test = MyTest('test_error')
test.run(result)

print(result.summary())