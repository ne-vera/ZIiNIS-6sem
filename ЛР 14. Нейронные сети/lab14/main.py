from tpm import TPM
import numpy as np
import time
import matplotlib.pyplot as plt

def random_vector():
    return np.random.randint(-l, l + 1, [k, n])

def sync_score(m1, m2):
    return 1.0 - np.average(1.0 * np.abs(m1.W - m2.W)/(2 * l - 1))

# Parameters
k = 4
n = 7
l = 4
update_rule = 'anti_hebbian'

steps = []
times = []
updates = []
updates_sum = 0
updates_avg_vector = []
iterations = 500
for i in range(1, iterations + 1):
    machine_1 = TPM(k, n, l)
    machine_2 = TPM(k, n, l)

    sync = False
    updates_counter = 0
    start_time = time.time()
    sync_history = []

    while(not sync):
        X = random_vector()

        tau_1 = machine_1(X)
        tau_2 = machine_2(X)

        machine_1.update(tau_2, update_rule)
        machine_2.update(tau_1, update_rule)
        updates_counter += 1

        score = 100 * sync_score(machine_1, machine_2)
        sync_history.append(score)

        if score == 100:
            sync = True

    end_time = time.time()
    time_taken = end_time - start_time

    steps.append(i)
    times.append(time_taken)
    updates.append(updates_counter)
    updates_sum += updates_counter
    updates_avg_vector.append(updates_sum / i)


print(f'Average updates number: {updates_avg_vector[iterations - 1]}')
print(f'Average synchronization time: {sum(times) / iterations}')
plt.plot(steps, updates_avg_vector)
plt.show()
