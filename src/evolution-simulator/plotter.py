from matplotlib import pyplot as plt


def lineplot(
    x, y, label_x=None, label_y=None, title=None, legend_line=None, legend=False
):
    plt.plot(x, y, label=legend_line)

    plt.title(title)
    plt.xlabel(label_x)
    plt.ylabel(label_y)

    plt.legend() if legend else None

    plt.show()
