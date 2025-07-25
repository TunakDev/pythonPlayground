import matplotlib.pyplot as plt

from js import document
from pyodide.ffi import create_proxy
from pyscript import display


def Setup_Button_Listeners():
    btnList = document.querySelectorAll(".button")
    for i in range(len(btnList)):
        e = document.getElementById(btnList[i].id)
        btn_event = create_proxy(Process_Button)
        e.addEventListener("click", btn_event)


async def Process_Button(event):
    if document.getElementById("evtMsg").innerHTML == '100':  # button plot_it
        fig = await plot_it()
        # pyscript.write('lineplot', fig)
        display(fig, target="lineplot")


async def plot_it(*args, **kwargs):
    fig, ax = plt.subplots()
    year_1 = [2016, 2017, 2018, 2019, 2020, 2021]
    population_1 = [42, 43, 45, 47, 48, 50]
    year_2 = [2016, 2017, 2018, 2019, 2020, 2021]
    population_2 = [43, 43, 44, 44, 45, 45]
    plt.plot(year_1, population_1, marker='o', linestyle='--', color='g', label='Country 1')
    plt.plot(year_2, population_2, marker='d', linestyle='-', color='r', label='Country 2')
    plt.xlabel('Year')
    plt.ylabel('Population (M)')
    plt.title('Year vs Population')
    plt.legend(loc='lower right')
    fig
    return fig


Setup_Button_Listeners()