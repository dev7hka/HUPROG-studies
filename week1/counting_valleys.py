def countingValleys(steps, path):
    """
    :param steps: integer, number of steps
    :param path: list[int], steps
    :return: integer, number of valleys
    """
    altitude = 0      # +1 for "U", -1 for "D"
    count_valley = 0
    for step in path:
        if step == "D":
            altitude-=1
        else:
            altitude+=1
        if altitude == 0 and step == "U":
            count_valley+=1
    return count_valley