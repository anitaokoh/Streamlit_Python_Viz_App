import streamlit as st
import gendergap
import youtube_earnings
import SessionState


# query_params = st.experimental_set_query_params()
# app_check = st.experimental_get_query_params()

# session_state = SessionState.get(first_query_params=query_params)
# first_query_params = session_state.first_query_params

# app_check = {k: v[0] if isinstance(v, list) else v for k, v in app_check.items()}


# # the controller of the homepage
# def main():
#     createlayout()
#     side_bar_homepage()

#the homepage side bar
def side_bar_homepage():
    st.sidebar.title("About Author")
    st.sidebar.info("""Hi, I am Anita Okoh.  I enjoy learning about data science with python.
    This includes using python to visualize data. I also enjoy converting my pain-points into useful products.
    You can connect with me via [LinkedIn](https://www.linkedin.com/in/anita-okoh/) and [Github](https://github.com/anitaokoh)""")
    html_temp1 = """
    [![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/H2H12Z70I)
    """

    st.sidebar.markdown(html_temp1)


# the content of the homepage
def homepage():
    st.image("images/logo1.png",use_column_width=True)
    st.markdown("> Visualization gives you answers to questions you didn’t know you had")
    st.write("""
            When attempting to predict something using data, visualization seems to  be a small means to an end
            and I tend not to spend as much time as I want to visualizing the _"crap out of the data"_.
             """)
    st.write("""
             Whenever I want to indulge in data visualization, my default tend to be using tableau and this is not very often.
             This year, (2020), I have decided to give visualization a little more focus and also visualize using python more. \n
             By the end of the year, It would be great to see
             - If I can completely switch to using just python visualization libraries
             - How much I have improved in this aspect in terms of diving into library documentations,
             understanding the different libraries strengths and weakness etc

             Below are some of the tools I would be exploring:
            """)
    st.image("images/logo2.png",use_column_width=True)
    st.write("""
            Each visualization experiment will be based on a topic. **Since the main goal of this platform is to improve my visualization skill using only python**,
            there may be less words (or story) than there are charts. However, there would be links for more info about the data used.

            To see the visualizations, click on the icon on the top left of this page and navigate through the available visualizations
            which would be updated from time to time. Just in case you are interested in mimicking my visualizations, there would be a source code
            along with each visualization or you can watch this [Github repo](https://github.com/anitaokoh/Streamlit_Python_Viz_App) to get updated as soon as the next visualization drops.
            """)
    st.markdown("<div align='center'><br>"
                "<img src='https://img.shields.io/badge/MADE%20WITH-PYTHON%20-red?style=for-the-badge'"
                "alt='API stability' height='25'/>"
                "<img src='https://img.shields.io/badge/HOSTED%20ON-Heroku-blue?style=for-the-badge'"
                "alt='API stability' height='25'/>"
                "<img src='https://img.shields.io/badge/POWERED%20BY-Streamlit-green?style=for-the-badge'"
                "alt='API stability' height='25'/></div>", unsafe_allow_html=True)

#the layout of the whole app
def createlayout():
    st.sidebar.title("Menu")
    query_params = st.experimental_get_query_params()
    app_check = st.experimental_get_query_params()

    session_state = SessionState.get(first_query_params=query_params)
    first_query_params = session_state.first_query_params

    app_check = {k: v[0] if isinstance(v, list) else v for k, v in app_check.items()}
    page_list = ["Homepage", "Gender Gap", "Popular YouTubers"]
    default_radio = int(app_check["selectbox"]) if "selectbox" in app_check else 0
    app_mode = st.sidebar.selectbox("Please select a page", page_list,index = default_radio)
    if app_mode:
        app_check["selectbox"] = str(app_mode)
        st.experimental_set_query_params(**app_check)
#     app_mode = st.sidebar.selectbox("Please select a page", ["Homepage", "Gender Gap", "Popular YouTubers"])
        if app_mode == 'Homepage':
            homepage()
        elif app_mode == "Gender Gap":
            gendergap.load_page()
        elif app_mode == "Popular YouTubers":
            youtube_earnings.load_page()
        
        
 # the controller of the homepage
def main():
    createlayout()
    side_bar_homepage()


if __name__ == "__main__":
    main()
