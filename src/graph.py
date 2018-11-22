import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import database


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


def pie_chart_two_field(title, query):
    """Generate a pie chart to display percentage of data in a specific field

    Arguments:
        title {String} -- the graphic title
        query {Dataframe} -- the query result (independent variable as first,
        dependent variable as second in query)

    Returns:
        [plot] -- the generated plot
    """

    try:
        # generate pie chart
        query = query.set_index(query.columns.values[0])
        graph = query.plot.pie(subplots=True, legend=False,
                               autopct='%.2f', title=title)
        plt.ylabel("")
        return plt
    except:
        # return None if error
        return None


def line_chart(title, query):
    """Generate a pie chart to display percentage of data in a specific field

    Arguments:
        title {String} -- the graphic title, can be None
        query {Dataframe} -- the query result (independent variable as first,
        dependent variable as second in query)

    Returns:
        [plot] -- the generated plot
    """

    try:
        # if the title is none, assign title to the graph by its field name
        if title == None:
            title = query.columns.values[0]
        # generate pie chart
        query = query.set_index(query.columns.values[0])
        graph = query.plot.line(title=title)
        graph.locator_params(integer=True)
        return plt
    except:
        # return None if error
        return None


if __name__ == "__main__":
    result = database.manual_sql_query(
        "Select Continent, count(*) from Country group by Continent")
    pie_chart_two_field(None, result).show()
    result2 = database.manual_sql_query(
        "select continent from country")
    pie_chart_one_field(None, result2, 10).show()
