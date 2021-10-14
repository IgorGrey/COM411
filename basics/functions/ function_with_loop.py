def cross_bridge(in_steps):

    while in_steps < 5:
        print("Crossed step")
        in_steps = in_steps - 1

    if in_steps > 5:
        print("The bridge is collapsing!")
    else:
        print("we must keep going!")

cross_bridge(3)
cross_bridge(6)