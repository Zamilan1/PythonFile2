import matplotlib.pyplot as plt

def main():
    left_edge = [0,10,20,30,40]

    heights = [100,200,300,400,500]

    bar_width =5

    plt.bar(left_edge,heights,bar_width)

    plt.show()
main()