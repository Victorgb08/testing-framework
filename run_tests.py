# Este script foi implementado como parte da Questão 7: Executando Todos os Testes
# Ele utiliza TestLoader, TestSuite e TestRunner para executar todas as classes de teste.

from test_loader import TestLoader
from test_runner import TestRunner
from test_case_test import TestCaseTest
from test_suite_test import TestSuiteTest
from test_loader_test import TestLoaderTest
from test_suite import TestSuite

# Inicializando o TestLoader e TestRunner
loader = TestLoader()
runner = TestRunner()

# Criando suítes de testes para cada classe de teste
test_case_suite = loader.make_suite(TestCaseTest)
test_suite_suite = loader.make_suite(TestSuiteTest)
test_loader_suite = loader.make_suite(TestLoaderTest)

# Adicionando todas as suítes em uma suíte principal
suite = TestSuite()
suite.add_test(test_case_suite)
suite.add_test(test_suite_suite)
suite.add_test(test_loader_suite)

# Executando todos os testes
runner.run(suite)