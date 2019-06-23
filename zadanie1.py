def father_twice_old(father_age, son_age):
    if -(father_age - 2 * son_age) < 0:
        return f'Było to {abs(-(father_age - 2 * son_age))} lat temu'
    else:
        return f'Będzie to za {-(father_age - 2 * son_age)} lat'

