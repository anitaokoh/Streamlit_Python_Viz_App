import pandas as pd
import plotly
import plotly.express as px



def create_fig(df,emotions_list,emotion_scale):
    """
    Creates a Plotly cutomized line chart without annotations
    Args: The user input and emotion scale measures
    Return: A Plotly figure
    """
    #Create the line  chart
    fig = px.line(df, x="Month_Index", y="Emotion_Scale",width=1020,  template="simple_white")

    #Customize the hover tooltp and line in the chart
    fig.update_traces(mode='lines+markers', hovertemplate=None)

    # Adjust the position of the chart using margin
    # Change the background to white using paper_bgcolor
    # Create a reference line using Shape
    # Customize the Chart Title using title
    #Upload the logo below using image
    # Add annotations to the min and max score using annotation

    fig.update_layout(
        margin=dict(l=2, r=2, t=40, b=40),paper_bgcolor="White",
    shapes=[
    dict(
    type= 'line',
    yref= 'y', y0= 4, y1= 4,   
    xref= 'paper', x0= 0, x1= 7,
    line=dict(
                        color="Black",
                        width=2,
                        dash="dash"),

    )

    ], 
    title={
            'text': "MY 2020 IN A WRAP",
            'y':0.99,
            'x':0.55,
            'xanchor': 'center',
            'yanchor': 'top',
            'font':dict(
                family="Arial",
                size=30,
                color='#000000')
    },
    images = [dict(
            source="https://raw.githubusercontent.com/anitaokoh/Streamlit_Python_Viz_App/master/images/image.png",
            xref="paper", yref="paper",
            x=0.94, y=-0.07,
            sizex=0.1, sizey=0.09,
            xanchor="center", yanchor="top"
        )]

    )

    #Customize the x-axis labels
    fig.update_xaxes(showline=True, linewidth=2, linecolor='black', title = '<b>Month</b>',
        ticktext=list(df['Month']),
        tickvals=list(df['Month_Index']),
    )

    #Customize the y-axis labels
    fig.update_yaxes(range=[0, 8],
        showline=True, linewidth=2, linecolor='black',title = '<b>Emotion Summary</b>',
        ticktext= emotions_list,
        tickvals= emotion_scale
        ,showgrid=True
    )
    return fig

if __name__ == "__main__":
    create_fig(df, emotions_list,emotion_scale)
