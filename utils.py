import streamlit as st
import base64

logo_path = "./images/text logo.jpg"
image_path = "./images/logo.jpg"


def header():
    """
    Method to set the page layout and design the header for Script Guru app
    input: None
    output:
       1) DodgerBlue color Background will be set to heading
       2) Welcome note "Welcome Waste Champion" added at the left top corner
       3) Script Guru App tilttle "Waste Analysis & Visibility Engine(Script Guru)" added 
    return: None
    """
    try:
        encoded_logo = base64.b64encode(open(image_path, "rb").read()).decode()

        head = f"""
            <style>
                .head {{
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100px;
                    background: #1F36C7;
                    color: white;
                    z-index: 9999;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
                    padding: 0 20px;
                }}

                .welcome {{
                    font-size: 14px;
                    margin: 6px 0 0 0;
                    text-align: left;
                }}

                .bottom-row {{
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    height: 60px;
                }}

                .header-title {{
                    font-size: 50px;
                    font-weight: bold;
                    margin: 0 auto;
                    text-align: center;
                    flex: 1;
                    color: white;
                }}

                .logo-img {{
                    height: 50px;
                    width: 50px;
                    object-fit: contain;
                }}

                /* Prevent overlap */
                .main > div:first-child {{
                    padding-top: 120px;
                }}
            </style>
        """
        st.markdown(head, unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="head">
                <p class="welcome"></p>
                <div class="bottom-row">
                    <div></div> <!-- spacer to balance logo -->
                    <h1 class="header-title">GenVA - The ScriptGuru</h1>
                    <img class="logo-img" src="data:image/png;base64,{encoded_logo}">
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
            error = "Error from footer method: {}".format(e)
            st.error(error)
            raise


def horizontal_line():
    """
    Method whcih will create a horizontal line 
    input: None
    output: horizontal line with required styles
    return: Horizontal line
    """
    line = st.markdown(
                """
                <hr style="height:1.5px;width:100%;
                border:none;color:#333;background-color:#BDC3C7;" />
                """,
                unsafe_allow_html=True,)
    return line


def footer():
    """
    Method which creates footer of Script Guru app
    input: None
    output:
       1) Unilever image added at the left botton corener of the page
       2) A copy right text also added along with the image
    return: None
    """
    try:
        horizontal_line()

        st.markdown(
            """
            <style>
                footer {visibility: hidden;}

                .footer-container {
                    display: flex;
                    justify-content: right;
                    align-items: right;
                    margin-top: -30px;
                    padding: 0px;
                    color: white;
                    flex-direction: row;
                    gap: 0px;
                }

                .logo-text {
                    font-size: 14px;
                    color: #f9a01b;
                    margin: 0;
                    padding: 0;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="footer-container">
                <p class="logo-text">Copyrights</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        error = "Error from footer method: {}".format(e)
        st.error(error)
        raise
