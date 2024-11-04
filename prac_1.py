from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute,IBMQ 
from qiskit.tools.monitor import job_monitor 
IBMQ.enable_account('ENTER API TOKEN HERE') 
provider = IBMQ.get_provider(hub='ibm-q') 
q = QuantumRegister(16,'q') 
c = ClassicalRegister(16,'c') 
circuit = QuantumCircuit(q,c) 
circuit.h(q) # Applies hadamard gate to all qubits 
circuit.measure(q,c) # Measures all qubits  
backend = provider.get_backend('ibmq_qasm_simulator') 
job = execute(circuit, backend, shots=1) 
print('Executing Job...\n')                  
job_monitor(job) 
counts = job.result().get_counts() 
print('RESULT: ',counts,'\n') 
print('Press any key to close')