def calc_location(n):
    guess = 1
    while guess**2 < n:
        guess += 2
    print(n,'is on level',guess)
    if n > guess**2 - guess:
        # bottom side - how far away from the center?
        move = abs(n-(guess**2-guess//2))
    elif n > guess**2 - 2*guess + 1:
        # left side
        move = abs(n-(guess**2-guess+1-guess//2))
    elif n > guess**2 - 3*guess + 2:
        # top side
        move = abs(n-(guess**2-2*guess+2-guess//2))
    else:
        # right side
        move = abs(n-(guess**2-3*guess+3-guess//2))
    return move + guess//2

print('part 1:',calc_location(289326))
    
