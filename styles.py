import streamlit as st
import base64

fav_icon_path = "./images/newFav Icon.jpg"


def page_config():
    """
    Method to design the page intial structure 
    input: None
    output: 
        1) Sets the page configuration
        2) Adds Script GUru title to the application 
        3) Adds "Food Waste Warriors" image as fav icon for the application
        4) Streamlit pre designed Header will be hidden
        5) Margin will be set for the streamlit Page content
        6) Design the button design for entire Script GUru app
    return: None
    """
    try:
        st.set_page_config( layout="wide", page_title = "ScriptGuru", page_icon=fav_icon_path)
        page_design = '''
                    <style>
                        body{
                            border:None;
                        }
                        .appview-container .main .block-container{
                            padding-right: 0rem;
                            margin-top: 0rem;
                        }
                        [data-testid = "stVerticalBlock"]{
                            margin-top: -20px;
                            margin-left: -45px;
                            margin-right: 0px;
                        }
                        /* Sidebar alignment */
                        section[data-testid="stSidebar"] {
                            margin-top: 100px;
                            padding-top: 1rem;
                            background-color: #f9f9f9; /* optional */
                        }

                        /* Optional: remove sidebar header spacing */
                        section[data-testid="stSidebar"] {
                            padding-top: 0.5rem;  /* or match your header’s spacing */
                            padding-left: 1rem;
                        }
                       .stTabs [data-baseweb="tab-list"] {
                            gap: 10px;
                        }

                        .stTabs [data-baseweb="tab"] {
                            height: 50px;
                            white-space: pre-wrap;
                            background-color: #F0F2F6;
                            border-radius: 4px 4px 0px 0px;
                            gap: 1px;
                            padding-top: 0px;
                            padding-bottom: 10px;
                        }

                        .stTabs [aria-selected="true"] {
                            background-color: #1F36C7;
                        }
                        [data-testid = "stHeader"]{
                            display:none;
                        }
                        div.stButton > button:first-child{
                            background-color:#005eef;
                            color:white;
                            font-size:15px;
                        }
                        div.stDownloadButton > button:first-child{
                            background-color:#005eef;
                            color:white;
                            font-size:15px;
                        }
                        div[data-testid="metric-container"] {
                            background-color: rgba(28, 131, 225, 0.1);
                            border: 1px solid rgba(28, 131, 225, 0.1);
                            padding: 5% 5% 5% 10%;
                            border-radius: 5px;
                            color: rgb(30, 103, 119);
                            overflow-wrap: break-word;
                            }
                        div.block-container {padding-top:0rem;}
                    </style>
                    '''
        st.markdown(page_design, unsafe_allow_html=True)
    except Exception as e:
        error = "Error from page_config method: {}".format(e)
        st.error(error)
        raise

def homepage_tile_styles(header:str,sline:list,colour:str,image:str = " "):
    """
    Method to create the tile structure for home section
    input: Tile Header, Tile data, Tile color
    output: Tiles will be created with defined header,data,image and style
    return: None
    """
    try:
        tile_style ="""
                    <style>
                        .tile{
                            color: #000000;
                            font-size: 18px;
                            padding-bottom: 18px;
                            padding-top: 18px;
                        } 
                    </style>       
                    """
        st.markdown(tile_style,unsafe_allow_html=True)
        if image != " ":
            tile_content = f"""
                            <div>
                                <p class = "tile", style='background-color: {colour};'>
                                    <span style = 'font-size: 20px; 
                                        font-weight: bold;'>{header}</span>
                                    <BR>
                                    <span style='font-size: 18px; 
                                        margin-top: 0;'>{sline[0]}</span>
                                    <BR>
                                    <BR>
                                    <span style='font-size: 18px; 
                                        margin-top: 0;'>{sline[1]}</span>
                                </p>
                                <img width="500", height ="200" src="data:image/png;base64,
                                    {base64.b64encode(open(image, "rb").read()).decode()}">
                            <div>
                        """
        else:
            tile_content = f"""
                            <div>
                                <p class = "tile", style='background-color: {colour};'>
                                    <span style = 'font-size: 20px; 
                                        font-weight: bold;'>{header}</span>
                                    <BR>
                                    <span style='font-size: 18px; 
                                        margin-top: 0;'>{sline[0]}</span>
                                    <BR>
                                    <BR>
                                    <span style='font-size: 18px; 
                                        margin-top: 0;'>{sline[1]}</span>
                                    <BR>
                                </p>
                            <div>
                        """
        st.markdown(tile_content, unsafe_allow_html=True)
    except Exception as e:
        error = "Error from homepage_tile_styles method: {}".format(e)
        st.error(error)
        raise