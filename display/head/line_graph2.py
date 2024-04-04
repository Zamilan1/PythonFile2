import matplotlib.pyplot as plt

def main():
    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,2]
    plt.plot(x_coords,y_coords) # plot the points on a line graph

    plt.title('Simple data')
    plt.xlabel('This is the x Axis')
    plt.ylabel('This is the Y axis')
    
    plt.grid(True)

    plt.show()
main()