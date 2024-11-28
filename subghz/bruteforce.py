with open("brute_force_codes.sub", "w") as file:
    file.write("Filetype: Flipper SubGhz Key File\nVersion: 1\nFrequency: 433920000\nPreset: FuriHalSubGhzPresetOok650Async\nProtocol: RAW\n")
    for code in range(0x00000, 0xFFFFF):  # Generate codes from 0x00000 to 0xFFFFF
        file.write("RAW_Data: " + " ".join(f"{bit}" for bit in format(code, "020b")) + "\n")
print("Brute force file generated!")

# Python script to generate Sub-GHz brute force codes
