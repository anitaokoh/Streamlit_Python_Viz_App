import streamlit as st
import pandas as pd
import plotly as py
import numpy as np
import plotly.graph_objs as go
from PIL import Image
from plotly.subplots import make_subplots

# Data Source
gap_index = pd.read_csv('data/gender_gap_2010_2020_complete.csv')
new_df = gap_index[['2010', '2011', '2012', '2013',
       '2014', '2015', '2016', '2017', '2018', '2019']]

code_1 = """
           fig = make_subplots(rows=1, cols=2, specs=[[{"type": "Box", "colspan": 1}, {"type": "Scatter", "colspan": 1}]],
                  subplot_titles=('The distribution of the gender gap index overtime', "The Average Gender gap index trend"), shared_yaxes=True)
           fig.add_box(y = new_df['2010'], name = '2010', row=1, col=1)
           fig.add_box(y = new_df['2011'], name = '2011', row=1, col=1)
           fig.add_box(y = new_df['2012'], name = '2012', row=1, col=1)
           fig.add_box(y = new_df['2013'], name = '2013', row=1, col=1)
           fig.add_box(y = new_df['2014'], name = '2014', row=1, col=1)
           fig.add_box(y = new_df['2015'], name = '2015', row=1, col=1)
           fig.add_box(y = new_df['2016'], name = '2016', row=1, col=1)
           fig.add_box(y = new_df['2017'], name = '2017', row=1, col=1)
           fig.add_box(y = new_df['2018'], name = '2018', row=1, col=1)
           fig.add_box(y = new_df['2019'], name = '2019', row=1, col=1)
           fig.add_scatter(x = new_df.mean(axis = 0).index, y = new_df.mean(axis = 0).round(2).values, mode = 'lines', row=1, col=2)
           fig.update_layout(template="plotly_dark",title_text=" Global Gender Gap Progress in the last Decade")
           """

code_2 = """
            gap_index['text'] = gap_index['Country'] + '<br>' + \
                                gap_index['2010'].astype(str)
            gap_index['texts']= gap_index['Country'] + '<br>' + \
                                gap_index['2019'].astype(str)

            fig = make_subplots(rows=2, cols=1,specs=[[{"type": "Choropleth", "rowspan": 1}], [{"type": "Choropleth", "rowspan": 1}]],vertical_spacing = 0.05,subplot_titles=("2019", "2010"), )

            fig.add_choropleth(
                                locations=gap_index['Country'], # Spatial coordinates
                                z = gap_index['2019'], # Data to be color-coded
                                locationmode='country names', # set of locations match entries in `locations`

                                hoverinfo = 'text',
                                text=gap_index['texts'], # hover text
                                coloraxis = "coloraxis",
                                reversescale=True,
                                marker_line_color='white', # line markers between states
                                 row=1, col=1,
                                )
            fig.add_choropleth(
                                locations=gap_index['Country'], # Spatial coordinates
                                z = gap_index['2010'], # Data to be color-coded
                                locationmode='country names',# set of locations match entries in `locations`
                                hoverinfo = 'text',
                                text=gap_index['text'], # hover text
                                marker_line_color='white',
                                coloraxis = "coloraxis",
                                reversescale=True, # line markers between states
                               row=2, col=1
                              )
            fig.update_layout(coloraxis = {'colorscale':'viridis', 'reversescale': True},

                                title_text = 'World Gender Gap Index by Countries - Now and 2010',
                                geo = dict(
                                    scope='world',
                                    projection=go.layout.geo.Projection(type = 'equirectangular'),
                                    showlakes=True,
                                    showframe=False,
                                    showcoastlines=False,# lakes
                                    lakecolor='rgb(255, 255, 255)', ),
                                geo2 = dict(
                                    scope='world',
                                    projection=go.layout.geo.Projection(type = 'equirectangular'),
                                    showlakes=False,
                                    showframe=False,
                                    showcoastlines=False,# lakes
                                    lakecolor='rgb(255, 255, 255)',),
                                width=900,height=900,autosize=False,
                                margin=go.layout.Margin(
                                                        l=10,
                                                        r=10,
                                                        b=20,
                                                        t=100,
                                                        pad=0
                                                        )
                               )
"""

def load_page():
    sidebar_info()
    body()


def sidebar_info():
    st.sidebar.subheader('Gender Gap Index')
    st.sidebar.markdown("""
                   This visualization is made on the WEF
                   recent report on Glabal Gender Gap
                   index.

                   **Years considered**: 2010 - 2019

                   **Library Used**: Plotly
                   """)

def viz1():
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "Box", "colspan": 1}, {"type": "Scatter", "colspan": 1}]],
                    subplot_titles=('The distribution of the gender gap index overtime', "The Average Gender gap index trend"),
                    shared_yaxes=True)

    fig.add_box(y = new_df['2010'], name = '2010', row=1, col=1)
    fig.add_box(y = new_df['2011'], name = '2011', row=1, col=1)
    fig.add_box(y = new_df['2012'], name = '2012', row=1, col=1)
    fig.add_box(y = new_df['2013'], name = '2013', row=1, col=1)
    fig.add_box(y = new_df['2014'], name = '2014', row=1, col=1)
    fig.add_box(y = new_df['2015'], name = '2015', row=1, col=1)
    fig.add_box(y = new_df['2016'], name = '2016', row=1, col=1)
    fig.add_box(y = new_df['2017'], name = '2017', row=1, col=1)
    fig.add_box(y = new_df['2018'], name = '2018', row=1, col=1)
    fig.add_box(y = new_df['2019'], name = '2019', row=1, col=1)

    fig.add_scatter(x = new_df.mean(axis = 0).index, y = new_df.mean(axis = 0).round(2).values, mode = 'lines', row=1, col=2)
    fig.update_layout(template="plotly_dark", width=900,
    height=500,title_text=" Global Gender Gap Progress in the last Decade")

    return fig

def viz2():
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "Box", "colspan": 1}, {"type": "Scatter", "colspan": 1}]],
                    subplot_titles=('The distribution of the gender gap index overtime', "The Average Gender gap index trend"),
                    )

    fig.add_box(y = new_df['2010'], name = '2010', row=1, col=1)
    fig.add_box(y = new_df['2011'], name = '2011', row=1, col=1)
    fig.add_box(y = new_df['2012'], name = '2012', row=1, col=1)
    fig.add_box(y = new_df['2013'], name = '2013', row=1, col=1)
    fig.add_box(y = new_df['2014'], name = '2014', row=1, col=1)
    fig.add_box(y = new_df['2015'], name = '2015', row=1, col=1)
    fig.add_box(y = new_df['2016'], name = '2016', row=1, col=1)
    fig.add_box(y = new_df['2017'], name = '2017', row=1, col=1)
    fig.add_box(y = new_df['2018'], name = '2018', row=1, col=1)
    fig.add_box(y = new_df['2019'], name = '2019', row=1, col=1)

    fig.add_scatter(x = new_df.mean(axis = 0).index, y = new_df.mean(axis = 0).values, mode = 'lines', row=1, col=2)
    fig.update_layout(template="plotly_dark", width=900,
    height=500, title_text=" Global Gender Gap Progress in the last Decade")

    return fig

def viz3():
    gap_index['text'] = gap_index['Country'] + '<br>' + \
      gap_index['2010'].astype(str)
    gap_index['texts'] = gap_index['Country'] + '<br>' + \
        gap_index['2019'].astype(str)

    fig = make_subplots(rows=2, cols=1,specs=[[{"type": "Choropleth", "rowspan": 1}], [{"type": "Choropleth", "rowspan": 1}]],vertical_spacing = 0.05,subplot_titles=("2019", "2010"), )

    fig.add_choropleth(
        locations=gap_index['Country'], # Spatial coordinates
        z = gap_index['2019'], # Data to be color-coded
        locationmode='country names',# set of locations match entries in `locations`
        hoverinfo = 'text',
        text=gap_index['texts'], # hover text
        coloraxis = "coloraxis",
        reversescale=True,
        marker_line_color='white', # line markers between states
         row=1, col=1,
    )

    fig.add_choropleth(
        locations=gap_index['Country'], # Spatial coordinates
        z = gap_index['2010'], # Data to be color-coded
        locationmode='country names',# set of locations match entries in `locations`
        hoverinfo = 'text',
        text=gap_index['text'], # hover text
        marker_line_color='white',
        coloraxis = "coloraxis",
        reversescale=True, # line markers between states
       row=2, col=1
    )
    fig.update_layout(coloraxis = {'colorscale':'viridis', 'reversescale': True},

        title_text = 'World Gender Gap Index by Countries - Now and 2010',
        geo = dict(
            scope='world',
            projection=go.layout.geo.Projection(type = 'equirectangular'),
            showlakes=True,
            showframe=False,
            showcoastlines=False,# lakes
            lakecolor='rgb(255, 255, 255)', ),
        geo2 = dict(
            scope='world',
            projection=go.layout.geo.Projection(type = 'equirectangular'),
            showlakes=False,
            showframe=False,
            showcoastlines=False,# lakes
            lakecolor='rgb(255, 255, 255)',),
                      width=900,height=900,autosize=False,  margin=go.layout.Margin(
            l=10,
            r=10,
            b=20,
            t=100,
            pad=0
        )
    )
    return fig


def body():
    st.image("images/logo3.png",use_column_width=True)
    st.write("""The visualisation was based on the recent research paper the world forum
   published this year which revolved around gender gap index. \n\n The first Global Gender Gap Report was published in 2006 by the World Economic Forum which included about 114 countries.
   As at this years report, over 140 countries were included. \n\n
   The Global Gender Gap Index is an index designed to measure gender equality. Index ranks countries according to calculated gender gap between women and men in four key areas: \n\n
   ♟ **Economic participation and opportunity** – outcomes on salaries, participation levels and access to high-skilled employment \n
   ♟ **Educational attainment** – outcomes on access to basic and higher level education \n
   ♟ **Political empowerment** – outcomes on representation in decision-making structures \n
   ♟ **Health and survival** – outcomes on life expectancy and sex ratio. \n
   The index ranges between 0 and 1 where 1 means perfect gender equality and 0 mean no gender equality.
   You can find all data sources and more info via [Wikipedia](https://en.wikipedia.org/wiki/Global_Gender_Gap_Report) and [WEF report](https://en.wikipedia.org/wiki/Global_Gender_Gap_Report)
   Using Plotly, I was about to answer two questions \n
   ♟ _**Has the world index as a whole improved in the last decade?**_ \n
   ♟ _**How has individual countries fared currently compared to 2010 and are the countries overall geting better or worse?**_
    """)

    st.header("Data Exploration")
    if st.checkbox("See how the data looks like"):
        st.dataframe(gap_index.iloc[:,1:].head())
        st.write(gap_index.shape)
        st.text('Please note that all index has been approxiated to 2 decimal places')
    if st.checkbox('World index distribution in the last decade'):
        fig = viz1()
        st.plotly_chart(fig)
        st.text("""
                   Key Insight
                   🔹2019 seems to be the best year so far for the world as whole
                   in terms of gender equality.

                 """)
        if st.checkbox('See more'):
            choice = st.radio('What would you like to see?',('Source Code','Chart with different y axes'))
            if choice == 'Source Code':
                st.code(code_1)
            elif choice == 'Chart with different y axes':
                fi = viz2()
                st.plotly_chart(fi)
                st.text('N:B Also the Average index would also not approximated in this chart')

    if st.checkbox('Countries Indices in 2010 and Now'):
        map = viz3()
        st.plotly_chart(map)
        st.text("""
                   Insights \n
                   🔹At first glance at both charts, it would seem that the world as a whole is going 'bluer'
                     i.e tending towards 1.
                   🔹The Scandanavia regions tend to be doing better than the rest of the world in terms of gender
                     equality.
                   🔹The Northern Africa and middle east region, although have progressed in the last decade, are
                     still the worst compared to the rest of the world.
                   🔹As at the last report, Iceland have the highest score of 0.88 and Yemen with the lowest
                     score of 0.49.
                   🔹 Not all countries are been captured yet. But more countries now, compared to 2010

                """)
        if st.checkbox('Check code'):
            st.code(code_2)
    st.write('You can find the repo [here](https://github.com/anitaokoh/Streamlit_Python_Viz_App)')


if __name__ == "__main__":
    main()
