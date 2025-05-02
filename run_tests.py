from test_loader import TestLoader
from test_runner import TestRunner
from test_case_test import TestCaseTest
from test_suite_test import TestSuiteTest
from test_loader_test import TestLoaderTest
from test_suite import TestSuite  # Importando TestSuite

loader = TestLoader()
runner = TestRunner()

# Criando suítes de testes
test_case_suite = loader.make_suite(TestCaseTest)
test_suite_suite = loader.make_suite(TestSuiteTest)
test_loader_suite = loader.make_suite(TestLoaderTest)

# Adicionando todas as suítes em uma suíte principal
suite = TestSuite()
suite.add_test(test_case_suite)
suite.add_test(test_suite_suite)
suite.add_test(test_loader_suite)

# Executando os testes
runner.run(suite)