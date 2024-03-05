temperature = -1
is_sun_shining = True

if temperature > 0 and is_sun_shining:
    print("Idziemy na spacer.")
else:
    print("Zostajemy w domu.")

print("-" * 20)

if not (temperature < 0 or not is_sun_shining):
    print("Idziemy na spacer")
else:
    print("Zostajemy w domu.")