import random
from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

def bb84_round(register_size=5):
    """Runs one round of BB84 on a register of given size."""
    qc = QuantumCircuit(register_size, register_size)
    
    # Alice's bits and bases
    alice_bits = [random.randint(0, 1) for _ in range(register_size)]
    alice_bases = [random.choice(['Z', 'X']) for _ in range(register_size)]
    
    for i in range(register_size):
        if alice_bits[i] == 1:
            qc.x(i)
        if alice_bases[i] == 'X':
            qc.h(i)
    qc.barrier()
    
    # Eve intercept-resend (optional — can remove if simulating without attack)
    eve_bases = [random.choice(['Z', 'X']) for _ in range(register_size)]
    for i in range(register_size):
        if eve_bases[i] == 'X':
            qc.h(i)
    qc.barrier()
    
    # Bob's basis choices and measurement
    bob_bases = [random.choice(['Z', 'X']) for _ in range(register_size)]
    for i in range(register_size):
        if bob_bases[i] == 'X':
            qc.h(i)
    qc.barrier()
    
    qc.measure(range(register_size), range(register_size))

    backend = AerSimulator()
    pm = generate_preset_pass_manager(backend=backend, optimization_level=2)
    isa_circuit = pm.run(qc)
    job = backend.run(isa_circuit)
    result = job.result()
    counts = result.get_counts()
    measured_bits = list(counts.keys())[0]
    
    return alice_bits, alice_bases, bob_bases, measured_bits


def generate_bb84_key(target_length=40, register_size=5):
    """Generates a secure BB84 key of desired length."""
    sifted_key = []
    while len(sifted_key) < target_length:
        alice_bits, alice_bases, bob_bases, measured_bits = bb84_round(register_size)
        for i in range(register_size):
            if alice_bases[i] == bob_bases[i]:
                sifted_key.append(int(measured_bits[-i-1]))  # reverse index
    
    return sifted_key[:target_length]