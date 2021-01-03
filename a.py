import pandas as pd
import altair as alt
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/HP AY/Desktop/Studies/chromedriver')

source_covid = pd.read_csv("us-covid-info-by-state.csv", index_col=0)
source_states = pd.read_csv("us-states-info.csv")
source_dates = pd.read_csv("us-covid-dates.csv")

print(source_covid)

for date_id in range(1, 344):

    cd = "0" * (3 - len(str(date_id))) + str(date_id)

    source = pd.merge(source_covid[(source_covid.date_id == date_id) & (source_covid.deaths_total != 0)],
                      source_states, left_on="state_id", right_on="id")

    bars = alt.Chart(source).mark_bar(height=15).encode(
        x=alt.X('deaths_total:Q', axis=alt.Axis(labels=False), scale=alt.Scale(domain=(0, 37200))),
        y=alt.Y('name:N', sort='-x'),
        color=alt.value("#137751")
    )

    text = bars.mark_text(
        align='left',
        baseline='middle',
        dx=3  # Nudges text to right so it doesn't appear on top of the bar
    ).encode(
        text='deaths_total:Q'
    )

    rule = alt.Chart(source).mark_rule(color="red").encode(
        x='mean(deaths_total):Q'
    )

    (bars + text).properties(
        width=800
    ).configure_axis(
        grid=False,
        tickColor=None,
        title=None,
        domain=False
    ).configure_view(
        stroke=None
    ).save("test/dt_" + cd + ".svg", method='selenium', webdriver=driver)

