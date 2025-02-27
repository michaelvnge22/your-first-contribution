def modality(sequence):
    maxe = 0
    for element in sequence:
        if sequence.count(element) > maxe:
            maxe = element

    return maxe