from test_case_test import TestCaseTest
from test_suite_test import TestSuiteTest
from test_result import TestResult
from test_suite import TestSuite

result = TestResult()
suite = TestSuite()

# Adicionando testes de TestCaseTest
suite.add_test(TestCaseTest('test_result_success_run'))
suite.add_test(TestCaseTest('test_result_failure_run'))
suite.add_test(TestCaseTest('test_result_error_run'))
suite.add_test(TestCaseTest('test_result_multiple_run'))
suite.add_test(TestCaseTest('test_was_set_up'))
suite.add_test(TestCaseTest('test_was_run'))
suite.add_test(TestCaseTest('test_was_tear_down'))
suite.add_test(TestCaseTest('test_template_method'))

# Adicionando testes de TestSuiteTest
suite.add_test(TestSuiteTest('test_suite_size'))
suite.add_test(TestSuiteTest('test_suite_success_run'))
suite.add_test(TestSuiteTest('test_suite_multiple_run'))

# Executando a suíte de testes
suite.run(result)
print(result.summary())