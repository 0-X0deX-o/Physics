light_speed_mps = 299_792_458

def light_speed_ns_per_foot_from_mps(speed):
    speed *= 100
    speed /= 2.54
    speed /= 12
    speed /= 1e+9
    return 1/speed


# 100 cm in m 
# 2.54 cm in in
# 12 in foot

ns = light_speed_ns_per_foot_from_mps(light_speed_mps)
print(ns)