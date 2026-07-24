packet_sizes = [1000, 2000, 4000, 5000]
labels = ["No", "No", "Attack", "Attack"]

splits = [1500, 3000, 4500]


def gini(labels):
    total = len(labels)

    if total == 0:
        return 0

    attack_count = 0
    no_count = 0

    for label in labels:
        if label == "Attack":
            attack_count += 1
        else:
            no_count += 1

    attack_probability = attack_count / total
    no_probability = no_count / total

    return 1 - (attack_probability**2 + no_probability**2)


def weighted_gini(left_gini, right_gini, left_size, right_size):
    total = left_size + right_size

    return ((left_size / total) * left_gini) + \
           ((right_size / total) * right_gini)


best_split = None
best_gini = float("inf")

for split in splits:

    left_labels = []
    right_labels = []

    for i in range(len(packet_sizes)):

        if packet_sizes[i] <= split:
            left_labels.append(labels[i])
        else:
            right_labels.append(labels[i])

    left_g = gini(left_labels)
    right_g = gini(right_labels)

    weighted = weighted_gini(
        left_g,
        right_g,
        len(left_labels),
        len(right_labels)
    )

    print(f"Split: {split}")
    print("Left:", left_labels)
    print("Right:", right_labels)
    print("Weighted Gini:", weighted)
    print()

    if weighted < best_gini:
        best_gini = weighted
        best_split = split

print("Best Split =", best_split)
print("Best Gini =", best_gini)