import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import query
import database
import textwrap


def pie_chart(title, query):
    """Generate pie chart to display percentage of data

    Arguments:
        title {String} -- the plot title
        query {Dataframe} -- the query result (independent variable as first,
        dependent variable as second field in query)

    Returns:
        [plot] -- the generated plot
    """

    # wrap the tile to display in appropriate length
    title = textwrap.fill(title)
    # set the first column as index
    query = query.set_index(query.columns.values[0])
    # generate pie chart, display legend, correct the percentage to 2 d.p.
    graph = query.plot.pie(subplots=True, legend=False,
                           autopct='%.2f', title=title)
    # removed the y-axis label
    plt.ylabel("")
    # return the graph
    return plt


def line_chart(title, query):
    """Generate line chart to display changes over time

    Arguments:
        title {String} -- the plot title
        query {Dataframe} -- the query result (independent variable as first,
        dependent variable as second field in query)

    Returns:
        [plot] -- the generated plot
    """

    # wrap the tile to display in appropriate length
    title = textwrap.fill(title)
    # set the first column as index
    query = query.set_index(query.columns.values[0])
    # plot and assign title to the graph
    graph = query.plot.line(title=title)
    # only allow integer in the graph
    graph.locator_params(integer=True)
    # return the graph
    return plt


def bar_chart(title, query):
    """
    Generate a bar chart that displays changes over time

    Arguments:
        title {String} -- the plot title
        query {Dataframe} -- the query result (independent variable is the
        first field in query, dependent variable is second field in query)

    Return:
        [plot] -- the generated plot
    """
    # wrap the tile to display in appropriate length
    title = textwrap.fill(title)
    # set the first column as index
    query = query.set_index(query.columns.values[0])
    # plot and assign title to the graph
    graph = query.plot.bar(title=title, rot=0)
    # return the graph
    return plt
