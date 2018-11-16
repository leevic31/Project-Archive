import pandas as pd
import query
import matplotlib.pyplot as plt
import database
import numpy as np


def pie_chart_one_field(title, query, number):
    """Generate a pie chart to display proportion of data in a specific field

    Arguments:
        title {String} -- the graphic title, can be None
        query {Dataframe} -- the query result
        number {int} -- the top N number of data to be displayed

    Returns:
        [plot] -- the generated plot
    """

    try:
        # if the title is none, assign title to the graph by its field name
        if title == None:
            title = query.columns.values[0]
        # generate new dataframe to store proportion of each data in the field
        summary = query.apply(pd.value_counts)
        # get the sum of other proportion that is not in top N number
        other_total = np.sum(summary.iloc[number:].values)
        # create series and assign index 'Others' to be displayed in chart
        df = pd.Series(data=[other_total], index=['Others'])
        # obtain the top N number of data
        data = summary.head(number)
        # concat the top N number of data and 'Others'
        data = pd.concat([data[title], df])
        # generate pie chart
        graph = data.plot.pie(subplots=True, legend=False,
                              autopct='%.2f', title=title)
        plt.ylabel('')
        return plt
    except:
        # return None if error
        return False


if __name__ == "__main__":
    connection = database.get_db_connection()
    results = query.manual_sql_query(
        connection, "select Language from countrylanguage group by CountryCode")
    if pie_chart_one_field(None, results, 5) != False:
        pie_chart_one_field(None, results, 5).show()
