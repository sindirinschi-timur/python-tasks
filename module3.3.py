gender = input ("Enter your biological gender (male/female): ")
hemoglobin = input ("Enter your hemoglobin value (g/l): ")

if str(gender) == "female" and 117 < int(hemoglobin) < 155:
    print("Hemoglobin level is normal.")
elif str(gender) == "female" and int(hemoglobin) <= 117:
    print("Hemoglobin level is low.")
elif str(gender) == "female" and int(hemoglobin) >= 155:
    print("Hemoglobin level is high.")
elif str(gender) == "male" and 134 < int(hemoglobin) < 167:
    print("Hemoglobin level is normal.")
elif str(gender) == "male" and int(hemoglobin) <= 134:
    print("Hemoglobin level is low.")
elif str(gender) == "male" and int(hemoglobin) >= 167:
    print("Hemoglobin level is high.")
else:
    print("Invalid gender or hemoglobin value.")