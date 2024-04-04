import matplotlib.pyplot as plt

def main():
    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,2]
    plt.plot(x_coords , y_coords, marker ='o')

    plt.title('Sales by year')

    plt.xlabel('Year')
    plt.ylabel('Sales')

    plt.xticks([5,15,25,35,45],
               ['2019','2020','2021','2022','2023'])
    plt.yticks([0,100,200,300,400,500],
               ['$0m','$1m','$2m','$3m','$4m','$5m'])
 

    # Displaying the plot
    plt.show() 
main()