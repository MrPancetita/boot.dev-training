# https://www.boot.dev/lessons/baf149d0-5884-46d0-adbc-156aea3fc415

def check_mount_rental(time_used, time_purchased):
    if time_used >= time_purchased:
        return "overtime charged"
    return "no charges yet"