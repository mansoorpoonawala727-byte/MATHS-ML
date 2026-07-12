import numpy as np

packet_sizes = np.array([200, 1500, 300, 1200, 400, 1100, 250, 1400, 350, 1000])
print("MEAN:",np.mean(packet_sizes))
print("variance:",np.var(packet_sizes))
print("Standard Deviation:",np.std(packet_sizes))
print("MINIMUM:",np.min(packet_sizes))
print("MAXIMUM:",np.max(packet_sizes))
normal = np.array([400, 420, 380, 410, 390, 405, 415, 395])
suspicious = np.array([200, 1500, 210, 1480, 190, 1450, 220, 1490])
print("variance(normal):",np.var(normal))
print("Standard Deviation(normal):",np.std(normal))
print("variance(sus):",np.var(suspicious))
print("Standard Deviation(sus):",np.std(suspicious))
def is_suspicious(packet_sizes):
    if np.std(packet_sizes)>300:
        return True
    else:
        return False
print(is_suspicious(normal))
print(is_suspicious(suspicious))    