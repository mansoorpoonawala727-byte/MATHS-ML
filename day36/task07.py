packet_sizes = [1500, 1800, 5200,5200, 9000, 9500]
labels = ["No", "No", "Attack","Attack", "Attack", "Attack"]
new_packet = 5000
closest_distance=float('inf')
closest_index=-1
second_distance=float('inf')
second_index=-1
third_distance=float('inf')
third_index=-1

if len(packet_sizes)!=len(labels):
    print("invalid data")
else:
    for i in range(len(packet_sizes)):
        distance=abs(new_packet-packet_sizes[i])
        print("Distance to",packet_sizes[i],"=",abs(distance))
        if distance < closest_distance:
            third_distance=second_distance
            third_index=second_index
            second_distance=closest_distance
            second_index=closest_index
            closest_distance=distance
            closest_index=i
        elif distance < second_distance:
             third_distance=second_distance
             third_index=second_index
             second_distance=distance
             second_index=i
        elif distance < third_distance:
            third_distance=distance
            third_index=i     
    print(closest_distance)
    print(second_distance)
    print(third_distance)
    nearest_labels = [labels[closest_index], labels[second_index], labels[third_index]]
    attack_count = nearest_labels.count("Attack")
    no_count = nearest_labels.count("No")
    if attack_count > no_count:
        prediction = "Attack"
    else:
        prediction = "No"

    print(f"The prediction for the new packet is: {prediction}") 
