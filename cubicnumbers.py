import matplotlib.pyplot as plt

""" Simple function to plot the first five,
and the first 5 thousand cubic numbers"""

cubes = []
n =int(input("enter either 6 or 50001 "))
        
def thecubes():
    for numbers in range(n):
        cubic = numbers**3
        (cubes.append(cubic))
        break
    plt.plot(cubes)
    plt.show()
    

thecubes()
           

    
