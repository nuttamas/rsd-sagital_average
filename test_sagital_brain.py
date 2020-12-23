import numpy as np
import subprocess

# Make new output file
data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_sample.csv", data_input, fmt="%d", delimiter=",")

# Run sagital brain file to generate output
subprocess.run(
    ["python", "sagital_brain.py"], check=True
)  # Add 'check' to be abe to run a file and see the result

# Load output
loaded = np.loadtxt("brain_average.csv", delimiter=",")

# Expected output
expected = np.array(
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1.0,
    ]
)

# Check the values are identical
np.testing.assert_array_equal(loaded, expected)
