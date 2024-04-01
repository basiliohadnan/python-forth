import time, importlib
# from memory_profiler import profile

# Import the function to be tested
# from forth import evaluate

# @profile
def test_performance(solution):
    # Start the timer
    start_time = time.time()
    
    # Define your test data
    input_data = [
    '1 2 3 4 5',
    '-1 -2 -3 -4 -5',
    '1 2 +',
    '3 4 -',
    '2 4 *',
    '12 3 /',
    '8 3 /',
    '1 dup',
    '1 2 dup',
    '1 drop',
    '1 2 drop',
    '1 2 swap',
    '1 2 3 swap',
    '1 2 over',
    '1 2 3 over',
    ': dup-twice dup dup ;',
    '1 dup-twice',
    ': countup 1 2 3 ;',
    'countup',
    ': foo dup ;',
    ': foo dup dup ;',
     '1 foo',
    ': swap dup ; ',
    '1 swap',
    ': + * ; ',
    '3 4 +',
    ': foo 5 ; ',
    ': bar foo ; ',
    ': foo 6 ; ',
    'bar foo',
    ': foo 10 ; ',
    ': foo foo 1 + ; ',
    'foo',
    '1 DUP Dup dup',
    '1 2 3 4 DROP Drop drop',
    '1 2 SWAP 3 Swap 4 swap',
    '1 2 OVER Over over',
    ': foo dup ; ',
    '1 FOO Foo foo',
    ': SWAP DUP Dup dup ; ',
    '1 swap'
    ]
    
    # Execute the function with the test data
    result = solution.evaluate(input_data)
    
    # End the timer
    end_time = time.time()
    
    # Calculate execution time
    execution_time = end_time - start_time
    
    # Print the result and execution time
    print(f"Performance testing for script: {solution.__name__}")
    print("Execution Time:", execution_time, "seconds")

# Run the test
script_files = ['solution_a.py', 'solution_b.py', 'forth.py']

for script_file in script_files:
    # Import the performance test module dynamically
    performance_test_module = importlib.import_module('performance_test')
    
    # Load the script file dynamically
    solution = importlib.import_module(script_file[:-3])  # Remove '.py' extension
    
    # Call the performance test function with the loaded script module
    performance_test_module.test_performance(solution)
