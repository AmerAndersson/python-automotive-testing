

# Automotive testing 

Automotive testing in Python can cover a wide range of activities,
including unit testing, integration testing, and system testing for software components in vehicles. 

For example of how we might approach unit testing for a hypothetical automotive component using the unittest module in Python.

- Test the functionality of the Engine class:
- Test the functionality of the Employee class:
- Test the functionality of the Math class:


`pip install -r requirements.txt`


- python -m unittest -v tests/test_module.py
  
test_add_two_number (tests.test_module.TestModule.test_add_two_number) ... ok
test_divide_two_number (tests.test_module.TestModule.test_divide_two_number) ... ok
test_multiply_two_number (tests.test_module.TestModule.test_multiply_two_number) ... ok
test_subtract_two_number (tests.test_module.TestModule.test_subtract_two_number) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK


- python -m unittest -v tests/test_engine.py
  
test_start_with_enough_fuel (tests.test_engine.TestEngine.test_start_with_enough_fuel)
Tests if the engine starts when there is enough fuel ... ok
test_start_with_low_fuel (tests.test_engine.TestEngine.test_start_with_low_fuel)
Tests if the engine doesn't start when the fuel level is too low ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
  

- python -m unittest -v tests/test_employee.py

setupClass
test_apply_raise (tests.test_employee.TestEmployee.test_apply_raise) ... setUp
test_apply_raise
tearDown

ok
test_email (tests.test_employee.TestEmployee.test_email) ... setUp
test_email
tearDown

ok
test_fullname (tests.test_employee.TestEmployee.test_fullname) ... setUp
test_fullname
tearDown

ok
test_monthly_schedule (tests.test_employee.TestEmployee.test_monthly_schedule) ... setUp
tearDown

ok
teardownClass

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK

