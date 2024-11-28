start_frequency = 300000000  #start frequency
end_frequency = 900000000    #end frequency
step = 100000                #step size

with open("frequency_scan.sub", "w") as file:
    file.write("Filetype: Flipper SubGhz Key File\nVersion: 1\n")
    current_frequency = start_frequency
    while current_frequency <= end_frequency:
        file.write(f"Frequency: {current_frequency}\nRAW_Data: 10101010\n")
        current_frequency += step
print("Frequency hopping file generated!")
