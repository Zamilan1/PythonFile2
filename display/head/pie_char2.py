import matplotlib.pyplot as plt

def main():
    sales = [100,200,300,400]

    slices_labels = ['1st Qtr','2nd Qtrd','3rd Qtr','4th Qtrd']

    plt.pie(sales , labels=slices_labels)

    plt.title('sales by Quarter')
    plt.show()
main()