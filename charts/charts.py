import matplotlib.pyplot as plt

def generate_piechart():
    labels=['A', 'B', 'C']
    values = [200,34,120]

    fig, ax = plt.subplots() #Definimos figura y coordenadas
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()


