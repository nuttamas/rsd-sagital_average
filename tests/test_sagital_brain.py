import numpy as np
from pathlib import Path
from .sagital_brain import run_averages

Test_Directory = Path(__file__).parent  # Tell the program where the test directory is

def test_average():
    # Creates input file
    data_input = np.zeros((20, 20))
    data_input[-1, :] = 1

    # The expeted result is all zeros, except the last one, it should be 1
    expected = np.zeros(20)
    expected[-1] = 1

    np.savetxt(Test_Directory/"brain_sample.csv", data_input, fmt='%d', delimiter=',')

    # run python program
    run_averages(file_input=Test_Directory/ "brain_sample.csv", file_output=Test_Directory/ "brain_average.csv")

    # Check result
    result = np.loadtxt(Test_Directory/"brain_average.csv",  delimiter=',')
    np.testing.assert_array_equal(result, expected)