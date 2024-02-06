import matplotlib.pyplot as plt

def myplot(plot):
    def wrapper(*args, **kwargs):
        plt.rc('font', size=10) #controls default text size
        plt.rc('axes', titlesize=12) #fontsize of the title
        plt.rc('axes', labelsize=10) #fontsize of the x and y labels
        plt.rc('xtick', labelsize=10) #fontsize of the x tick labels
        plt.rc('ytick', labelsize=10) #fontsize of the y tick labels
        plt.rc('legend', fontsize=8) #fontsize of the legend
        output=plot(*args, **kwargs)
        return output
    return wrapper

x = [3, 4, 6, 7, 8]
y = [12, 14, 15, 19, 24]

#create a scatter plot with customized font sizes
@myplot
def plot(x, y):
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.scatter(x, y, label="dots")
    ax.set_title('title')
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    ax.legend()
    return fig

fig = plot(x, y)
fig.savefig("es2.pdf")
plt.show()
