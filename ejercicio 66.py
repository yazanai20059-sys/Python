def count_matching_indices(values):
    count = 0
    for i, v in enumerate(values):
        if i == v:
            count += 1
    return count


valors = [0, 2, 3, 3, 4]
resultat = count_matching_indices(valors)
print(f'El nombre d\'elements on l\'índex coincideix amb el valor és: {resultat}')