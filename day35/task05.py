import numpy as np
def anomaly(packet):
    mean=np.mean(packet)
    std=np.std(packet)
    print("MEAN:",mean)
    print("STANDARD DEVIATION:",std)
    if std == 0:
        print("All packets are identical. No anomalies detected.")
    else:    
        for i in range(len(packet)):
            print("PACKET ",i+1," = ",packet[i])
            z_score=(packet[i]-mean)/std
            print(f"Z-score = {z_score:.2f}")
            if abs(z_score)>3:
                print("⚠️ Anomaly detected at packet ",i+1)
            else:
                print("✅ Normal packet")    
    
   
pack1= np.array([
1498,1499,1500,1501,1497,
1500,1502,1499,1501,1498,
1500,1501,1499,1502,1498,
1500,1499,1501,1500,12000
])
anomaly(pack1)
       