import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import database
import textwrap


def pie_chart_one_field(title, query, number):
    """Generate a pie chart to display percentage of data in a specific field

    Arguments:
        title {String} -- the graphic title
        query {Dataframe} -- the query result [ONE COLUMN ONLY]
        number {int} -- the top N number of data to be displayed

    Returns:
        [plot] -- the generated plot
    """

    try:
        # generate new dataframe to store proportion of each data in the field
        summary = query.apply(pd.value_counts)
        # check whether 'other' field is necessary
        if summary.size > number:
            # obtain the top N number of data
            data = summary.head(number)
            # get the sum of other proportion that is not in top N number
            other_total = np.sum(summary.iloc[number:].values)
            # create series and assign index 'Others' to be displayed in chart
            df = pd.Series(data=[other_total], index=['Others'])
            # concat the top N number of data and 'Others'
            data = pd.concat([data[title], df])
        else:
            data = summary
        # generate pie chart
        graph = data.plot.pie(subplots=True, legend=False,
                              autopct='%.2f', title=title)
        plt.ylabel('')
        return plt
    except:
        # return None if error
        return None


def pie_chart(title, query):
    """Generate pie chart to display percentage of data

    Arguments:
        title {String} -- the plot title
        query {Dataframe} -- the query result (independent variable as first,
        dependent variable as second field in query)

    Returns:
        [plot] -- the generated plot
    """

    try:
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
    except:
        # return None if error
        return None


def line_chart(title, query):
    """Generate line chart to display changes over time

    Arguments:
        title {String} -- the plot title
        query {Dataframe} -- the query result (independent variable as first,
        dependent variable as second field in query)

    Returns:
        [plot] -- the generated plot
    """

    try:
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
    except:
        # return None if error
        return None


if __name__ == "__main__":
    result = database.manual_sql_query(
        "Select case when Month(date) between 1 and 2 then '20-24' when Month(date) between 3 and 4 then '25-29' else 'other' end as `age group`, count(*) as Count from test group by `age group` order by `age group`")
    pie_chart("percentage of the people that are being referred to employment services in different age groups", result).show()
    result2 = database.manual_sql_query(
        "select continent from country")
