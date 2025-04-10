import qiskit
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer.noise import NoiseModel

n_qubits = 5
circ = QuantumCircuit(n_qubits)

circ.h(0)
for qubit in range(n_qubits - 1):
    circ.cx(qubit, qubit + 1)
circ.measure_all()
print(circ)