import pandas as pd
import query
import matplotlib.pyplot as plt
import database


def pie_chart(title, query, number):
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
            title = query.columns.values
        # generate new dataframe to store proportion of each data in the field
        data = query.apply(pd.value_counts).head(number)
        # generate pie chart
        graph = data.plot.pie(subplots=True, legend=False,
                              autopct='%.2f', title=title)
        plt.ylabel('')
        return plt
    except:
        return None


if __name__ == "__main__":
    connection = database.get_db_connection()
    results = query.manual_sql_query(
        connection, "select Language from countrylanguage")
    pie_chart(None, results, 7)
