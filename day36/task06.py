packet_sizes = [1500, 1800, 5200, 9000, 9500]
labels = ["No", "No", "Attack", "Attack", "Attack"]
new_packet = 5000
closest_distance=float('inf')
closest_index=0

if len(packet_sizes)!=len(labels):
    print("invalid data")
else:
    for i in range(len(packet_sizes)):
        distance=abs(new_packet-packet_sizes[i])
        print("Distance to",packet_sizes[i],"=",abs(distance))
        if closest_distance >distance:
            closest_distance=distance
            closest_index=i      
    print("The prediction for new packet is",labels[closest_index])  
