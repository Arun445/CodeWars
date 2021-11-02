def bouncing_ball(h, bounce, window):
    if h < 0:
        return -1
    if bounce >= 1 or bounce <= 0:
        return -1
    if window >= h:
        return -1
    times = 1
    h *= bounce
    while window < h:
        times += 2
        h *= bounce

    return times
