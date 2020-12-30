import streamlit as st
import pandas as pd
import plotly
import plotly.express as px
from other_app_py_files.year_wrapup_viz import create_fig as fig_annot
from other_app_py_files.year_wrapup_viz_without_annotation import create_fig as fig_no_annot
import numpy as np
from chart_studio.plotly import image as py
# from PIL import Image as PILImage
import base64

#App data
emotions_list = ['Ecstatic','Happy', 'Content','Ok' ,'Frustrated', 'Sad', 'Depressed']
emotion_scale = [7, 6, 5, 4, 3, 2, 1]
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
month_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
emotion_index_map = dict(zip(emotion_scale, emotions_list))


def map_index_with_emotion(data_list):
    """
    Gets the emotion equivalent to the ratings
    Args: The user rating imput
    Return: a list of the emotions
    """
    user_emotion = []
    for element in data_list:
        results = emotion_index_map[element]
        user_emotion.append(results)
    return user_emotion

def create_df(data_list):
    """
    Creates a dataframe containing the user rating an demotion as well as the month name and index
    Args: The user input
    Return: A dataframe
    """
    new_list = [1 if ele == 0 else ele for ele in data_list]
    user_emotion = map_index_with_emotion(new_list)
    df = pd.DataFrame(zip(month_index, month_list,user_emotion,new_list), columns = ['Month_Index','Month', 'Emotion', 'Emotion_Scale'])
    return df

def get_highlight_month(df,function):
    """
    Gets details about the highlighted months for annotation
    Args: The dataframe and a function used for the dataframe
    Return: A list containg the highlighted months and month indice, emotion and rating
    """
    data= df[df['Emotion_Scale']==function]
    data_month_list = data['Month'].tolist()
    emotion_highlight = data['Emotion'].tolist()[0]
    emotion_index = data['Emotion_Scale'].tolist()
    month_index = data['Month_Index'].to_list()
    month_content = [data_month_list, emotion_highlight, emotion_index, month_index]
    return month_content



def get_best_and_worst_months(df):
    """
    Gets details on the best month(s) and worst month(s) using the get_highlighted_month function
    Args: Dataframe
    Return: two list variables of details on the worst and best month(s)
    """
    min_month_content = get_highlight_month(df,df['Emotion_Scale'].min())
    max_month_content = get_highlight_month(df,df['Emotion_Scale'].max())
    return min_month_content, max_month_content

def get_coordinates(month_content,data, text):
    """
    Gets the coordinate locations of the chart annoations
    Args: details on the highlighed month and the text summary from the user
    Return: A list of the x , y coordinates as well as the text from the user
    """
    y_coordinates = month_content[2][month_content[0].index(data)]
    x_coordinates = month_content[3][month_content[0].index(data)]
    coordinates_content = [x_coordinates,y_coordinates,text]
    return coordinates_content

def get_annotations_coordinates(max_month_content, min_month_content, min_text, max_text, min_data, max_data):
    """
    Gets the coordinates of the best and worst month. Just one.
    Args: The details of the best and worst months as well as their corresponding summaries from the user.
    Return: The coordinates of the best and worst month
    """
    min_content = get_coordinates(min_month_content, min_data,min_text)
    max_content = get_coordinates(max_month_content, max_data,max_text)
    return min_content,max_content


def get_table_download_link(data):
    """
    Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    # figure = data.to_image(format="png")
    figure =  py.get(data)
    b64 = base64.b64encode(figure).decode()  
    href = f'<a href="data:file/image;base64,{b64}" download="My 2020 in a wrap.png">Download chart</a>'
    return href






def viz_page():
    """
    Get a downloadable Chart image of the months' ratings for the year by calling the above functions.
    Args: 
    Return: A download link to the wrap up chart
    """
    #the first part
    max_width_str = f"max-width: 1030px;"
    st.markdown(f"""<style>.reportview-container .main .block-container{{{max_width_str}}}</style>""",unsafe_allow_html=True)
    st.image('images/logo5.png',use_column_width=True)
    st.subheader('How has your 2020 been?')
    with st.beta_expander('See more/less Content'):
        st.markdown("""<p>Although 2020 has been been a chaotic memorable year for a lot of people , it has had some good memorable moments.</p> 
        <p>This web app is to help guide to reflect on moments you have had and  summarize each month with an emotion you felt the strongest.</p>
        <p> You can summarize each month based on the following 7 emotions: <strong>Ecstatic, Happy, Content, Ok, Frustrated, Sad</strong> and <strong>Depressed</strong> </p>
         """,unsafe_allow_html=True)
    # the second part for the ratings
    if st.checkbox('Start'):
        st.write("""
        Rate each month of this year on a scale of 1-7. Remember to scale each month on the following emotion and scale number:\n
        **Ecstatic = 7, Happy = 6, Content = 5, Ok = 4 , Frustrated = 3, Sad = 2 and finally, Depressed is a 1**.
        """)
        col1, col2 = st.beta_columns(2)
        data_input1 = []
        data_input2 =[]
        col1.subheader('First Half of the Year')
        col2.subheader('Second Half of the Year')
        for element in month_list[:6]:
            element = col1.slider(element, 0, 7,key='col1')
            data_input1.append(element)
            
        for element in month_list[6:]:
            element = col2.slider(element, 0, 7,key='col2')
            data_input2.append(element) 
        emotion_scale_data = data_input1+data_input2
        df = create_df(emotion_scale_data)
        # the third part for the Viz
        if st.checkbox('Next'):
            # to decide if Viz with or with annotation
            choose_annotation = st.radio("Would you like to add annotation highlights to your best and worst months?",('Yes, I have some words to say', 'No, visualize straight away'))
            # the annotation part
            if choose_annotation == 'Yes, I have some words to say':
    
                with st.beta_expander('More'):
                
                    min_month_content,max_month_content = get_best_and_worst_months(df)
                    st.subheader('Give a brief Highlight summary of your best and worth months below')
                    st.write(f"In your best month(s), you were **{max_month_content[1].lower()}**. And in your worst month(s), you were **{min_month_content[1].lower()}** .")
                    title, option = st.beta_columns(2)
                    max_month = title.selectbox("Choose the best month you would like to highlight",max_month_content[0])
                    min_month = title.selectbox("Choose the worst month you would like to highlight",min_month_content[0])
                    max_text = option.text_input('Summary Highlight (5 words max)', key='First')

                    
                    min_text= option.text_input('Summary Highlight (5 words max)', key='second')
    

                    if st.checkbox('Verify text'):
                        for min_t,max_t in {min_text:max_text}.items():
                            if len(min_t.split()) > 5 or len(max_t.split()) > 5:
                                st.warning(f'Either "{min_t}"  or "{max_t}" is more than 5 words. Please summarize further ')
                            elif len(min_t.split()) < 1  or len(max_t.split()) < 1:
                                st.warning(f'One of the Text boxes is empty. Please write a summary or go back and click the button above to visualize straightaway ')
                            else:
                                if st.checkbox('Ready to Visualize'):
                        
                                    min_content,max_content = get_annotations_coordinates(max_month_content, min_month_content, min_text, max_text, min_month, max_month)
                                    
                            
                                #the annotated chart
                                    fig = fig_annot(df, emotions_list,emotion_scale, min_content, max_content)
                                    st.plotly_chart(fig,use_container_width=True, config={'displayModeBar': False})
                                    # if st.button('Export Vizualization image'):
                                    #     st.text('Ready to Download')
                                    #     st.markdown(get_table_download_link(fig), unsafe_allow_html=True)

           # the non-annotated chart
            else: 
                with st.beta_expander('See Chart'):  

                    fig = fig_no_annot(df, emotions_list,emotion_scale)


                    
                    st.plotly_chart(fig,use_container_width=True)
            
                    
                    if st.button('Export Vizualization image'):
                        st.text('Ready to Download')
                        st.markdown(get_table_download_link(fig), unsafe_allow_html=True)




if __name__ == "__main__":
    viz_page()
