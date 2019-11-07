#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# Loading your IBM Q account(s)
provider = IBMQ.load_account()


# In[2]:


from qiskit import QuantumProgram# Create a QuantumProgram object instance.
qp = QuantumProgram()# Create a Quantum Register called "qr" with 2 qubits.
qr = qp.create_quantum_register('qr',2)# Create a Classical Register called "cr" with 2 bits.
cr = qp.create_classical_register('cr',2)# Create a Quantum Circuit called "qc" involving qr and cr.
qc = qp.create_circuit('HelloWorldCircuit', [qr],[cr])


# In[3]:


from IPython.display import IFrame
IFrame(src="http://www.youtube.com/embed/RrUTwq5jKM4", width=1920/2, height=1080/2)


# In[4]:


from qiskit import *


# In[5]:


qr = QuantumRegister(2)
cr = ClassicalRegister(2)


# In[6]:


circuit = QuantumCircuit(qr, cr)


# In[7]:


circuit = QuantumCircuit(2,2)


# In[8]:


circuit.draw()


# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')
circuit.draw(output='mpl')


# In[10]:


# the quantum circuit has two qubits. they are indexed as qubits 0 and 1
circuit.h(0)
circuit.cx(0,1) # order is control, target
circuit.measure([0,1], [0,1]) # qubits [0,1] are measured and results are stored in classical bits [0,1] in order
circuit.draw(output='mpl')


# In[ ]:





# In[11]:


simulator = Aer.get_backend('qasm_simulator')


# In[12]:


result = execute(circuit, backend=simulator).result()


# In[13]:


from qiskit.visualization import plot_histogram


# In[14]:


plot_histogram(result.get_counts(circuit))


# In[15]:


IBMQ.load_account()
provider = IBMQ.get_provider(hub = 'ibm-q')


# In[16]:


qcomp = provider.get_backend('ibmq_16_melbourne')


# In[17]:


num_qubits = 2

from qiskit.providers.ibmq import least_busy
possible_devices = provider.backends(filters=lambda x: 
                                     x.configuration().n_qubits >= num_qubits
                                       and 
                                     x.configuration().simulator == False)
qcomp = least_busy(possible_devices)
print(qcomp)


# In[18]:


import qiskit.tools.jupyter
get_ipython().run_line_magic('qiskit_job_watcher', '')


# In[19]:


job = execute(circuit, backend=qcomp)


# In[ ]:


from qiskit.tools.monitor import job_monitor
job_monitor(job)


# In[ ]:




