def start_The_Simulation(answer):
    answer = raw_input('Would you like to start the simulation? y or n')
    if answer == 'y':
        return 'true'
    if answer == 'n':
        return 'false'


answer = ''
answer = start_The_Simulation(answer)
print answer

if answer == 'true':
    pass