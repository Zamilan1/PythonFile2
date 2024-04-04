import matplotlib.pyplot as plt

def main():
    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,1]

    plt.plot(x_coords,y_coords)

    plt.title('Simple Data')

    plt.xlabel('This is x axis')
    plt.xlabel('This is y axis')

    plt.xlim(xmin=-1, xmax=10)
    plt.ylim(ymin=-1, ymax=6)

    plt.grid(True)

    plt.show()
main()