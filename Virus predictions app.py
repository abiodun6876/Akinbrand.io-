import numpy as np

import matplotlib.pyplot as plt

def virus_spread_model(population, beta, gamma, T):

    # Initialize the number of infected and recovered individuals

    infected = [1]

    recovered = [0]

    susceptible = [population - 1]

    

    # Model the spread of the virus over time

    for t in range(1, T):

        new_infections = beta * susceptible[t-1] * infected[t-1] / population

        new_recoveries = gamma * infected[t-1]

        

        infected.append(infected[t-1] + new_infections - new_recoveries)

        recovered.append(recovered[t-1] + new_recoveries)

        susceptible.append(population - infected[t] - recovered[t])

    

    # Plot the results

    plt.plot(infected, label='Infected')

    plt.plot(recovered, label='Recovered')

    plt.plot(susceptible, label='Susceptible')

    plt.legend()

    plt.xlabel('Time (days)')

    plt.ylabel('Population')

    plt.show()

# Example usage: model the spread of a virus in a population of 100,000 people

virus_spread_model(100000, 0.2, 0.1, 100)

