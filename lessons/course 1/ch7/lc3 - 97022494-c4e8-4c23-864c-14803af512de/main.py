# https://www.boot.dev/lessons/97022494-c4e8-4c23-864c-14803af512de

def has_enough_energy(energy_available, distance_one_way, meters_per_energy):
    energy_needed = distance_one_way / meters_per_energy * 2
    return energy_available >= energy_needed
