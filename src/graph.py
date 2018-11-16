import pandas as pd
import query
import matplotlib.pyplot as plt
import database


def pie_chart(title, query, number):
    if title == None:
        title = query.columns.values
    data = query.apply(pd.value_counts).head(number)
    graph = data.plot.pie(subplots=True, legend=False,
                          autopct='%.2f', title=title)
    plt.ylabel('')
    return plt


if __name__ == "__main__":
    connection = database.get_db_connection()
    results = query.manual_sql_query(
        connection, "select Continent from country")
    pie_chart(None, results, 7).show()
