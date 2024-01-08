#!/usr/bin/env python3


# Complete the following to implement the described hamming distance function.
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def hamming_dist(signal_1, signal_2):
    def get_data(signal):
        return signal["data"] if type(signal) == dict else signal
    signal_1 = get_data(signal_1)
    signal_2 = get_data(signal_2)
    if len(signal_1) != len(signal_2):
        return "Empty signal on at least one of the sensors"
    res = []
    for sig1, sig2 in zip(signal_1, signal_2):
        if len(sig1) != len(sig2):
            return "Sensor defect detected"
        hamm_dist = 0
        for bit1, bit2 in zip(sig1, sig2):
            if bit1 != bit2:
                hamm_dist += 1
        if hamm_dist > 0:
            res.append((sig1, sig2, hamm_dist))
    return res


# The following lines print your function's output for an exemplary input to the console.
# Note that this does not include any of the mentioned edge cases for defective sensors or signals of different lenghts.
# Try to write your own tests for this.

signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
signal_sensor_2 = ("00101110", "11001001", "11110011", "01111011", "11001101", "00011011")
print(hamming_dist(signal_sensor_1, signal_sensor_2))

signal_sensor_1 = { "times": [0, 2, 5], "data": ["0010", "1101", "1100"] }

signal_sensor_2 =("0010", "1111", "0000")
print(hamming_dist(signal_sensor_1, signal_sensor_2))

#[
#    ("1101","1111", 1),
#    ("1100", "0000", 2)
#]
