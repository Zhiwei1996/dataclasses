PYTHON37_SRC = ../python/cpython

sdist:
	python3 setup.py sdist

wheel:
	python3 setup.py bdist_wheel

tests:
	PYTHONPATH=. python3 test/test_dataclasses.py

diff:
	@echo "Here's the diff that's needed to go from the 3.7 version to 3.6, and"
	@echo "from using Python's \"-m test\" to using \"PYTHONPATH=. python3.6 test/test_dataclasses.py\"."
	@echo ""
	-diff -u $(PYTHON37_SRC)/Lib/dataclasses.py .
	-diff -u $(PYTHON37_SRC)/Lib/test/test_dataclasses.py test
	-diff -u $(PYTHON37_SRC)/Lib/test/dataclass_module_1.py test
	-diff -u $(PYTHON37_SRC)/Lib/test/dataclass_module_1_str.py test
	-diff -u $(PYTHON37_SRC)/Lib/test/dataclass_module_2.py test
	-diff -u $(PYTHON37_SRC)/Lib/test/dataclass_module_2_str.py test