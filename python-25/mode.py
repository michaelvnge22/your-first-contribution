def modality(sequence):
    maxes = 0
    for element in sequence:
        if sequence.count(element) > maxes:
            maxes = element

    return maxes