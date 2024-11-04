from qiskit import QuantumRegister, ClassicalRegister 
from qiskit import QuantumCircuit, execute,IBMQ 
# from qiskit.tools.monitor import job_monitor 
from qiskit.circuit.library import QFT 
import numpy as np 
pi = np.pi 
# IBMQ.enable_account('8b23d3de61e4e60d2ec298e0ff7e2a8ac73d007cca4b87c0fba0a6179649e483
#  89a49bff72a94d9ec7519c2a088bcc5c86037bdba853fe31a894035d70419a74') 
provider = IBMQ.get_provider(hub='ibm-q') 
backend = provider.get_backend('ibmq_qasm_simulator') 
q = QuantumRegister(5,'q') 
c = ClassicalRegister(5,'c') 
circuit = QuantumCircuit(q,c) 
circuit.x(q[4]) 
circuit.x(q[2]) 
circuit.x(q[0]) 
circuit &= QFT(num_qubits=5, approximation_degree=0, do_swaps=True, inverse=False, 
insert_barriers=False, name='qft') 
circuit.measure(q,c) 
circuit.draw(output='mpl', filename='qft1.png') 
print(circuit) 
job = execute(circuit, backend, shots=1000) 
# job_monitor(job) 
counts = job.result().get_counts() 
print("\n QFT Output") 
print("-------------") 
print(counts) 
input() 
q = QuantumRegister(5,'q') 
c = ClassicalRegister(5,'c') 
circuit = QuantumCircuit(q,c) 
circuit.x(q[4]) 
circuit.x(q[2]) 
circuit.x(q[0]) 
circuit &= QFT(num_qubits=5, approximation_degree=0, do_swaps=True, inverse=False, 
insert_barriers=True, name='qft') 
circuit &= QFT(num_qubits=5, approximation_degree=0, do_swaps=True, inverse=True, 
insert_barriers=True, name='qft') 
circuit.measure(q,c) 
circuit.draw(output='mpl',filename='qft2.png') 
print(circuit) 
job = execute(circuit, backend, shots=1000) 
job_monitor(job) 
counts = job.result().get_counts() 
print("\n QFT with inverse QFT Output") 
print("------------------------------") 
print(counts) 