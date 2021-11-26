# Core Pkgs
import streamlit as st
import streamlit.components.v1 as stc
from src.painel import set_dashboard
# from crontab import CronTab
# import pyautogui, time
import pandas as pd
from datetime import datetime, timedelta

def load_css(file_name):
    print('load_css')
    # with open(file_name) as f:
    #     st.markdown('<style>{}</style>'.format(f.read()),
    #                 unsafe_allow_html=True)

def load_icon(icon_name):
    print('load_icon')
    # st.markdown('<i class="material-icons">{}</i>'.format(icon_name),
    #             unsafe_allow_html=True)

def render_html():
    html_div = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px;font-size:{}px">
    <h1 style="color:white;text-align:center;">Analise e segmentacao de mercado </h1>
    <h1 style="color:white;text-align:center;">Dashboard!! </h1>
    </div>
    """
    return html_div

def set_config():
    st.set_page_config(
    page_title='Analise e segmentacao de mercado Dashboard', 
    page_icon='📊', 
    layout='wide')

def set_menu():
    menu = ["Dashboard", "Ajustes", "Ajuda"]
    choice = st.sidebar.selectbox("Escolha uma opção:", menu)

	# Dashboard
    if choice == "Dashboard":
        # st.subheader("Home Page")
        set_dashboard()
       
    # Ajustes
    elif choice == "Ajustes":
        st.subheader("App Custom_Settings")

		# Define and Initialize State
        if 'fontsize' not in st.session_state:
            st.session_state['fontsize'] = 12

        f1, f2 = st.columns(2)

        with f1:
			# Create a button for fxn/cb fxn
            font_increment = st.button('Increase Font')
            if font_increment:
                st.session_state['fontsize'] += 5


        with f2:
			# Create a button for fxn/cb fxn
            font_decrement = st.button('Decrease Font')
            if font_decrement:
                st.session_state['fontsize'] -= 5	

		# Results
        st.write("Current Font Size",st.session_state.fontsize)
        stc.html(render_html().format(st.session_state.fontsize))

    # Ajuda
    else:
        st.subheader("Ajuda")
        st.info("Analise e segmentacao de mercado")
        st.success("msg ...!")
        new_date=datetime.now().strftime("%Y-%m-%d")
        date_relatorio = pd.to_datetime(new_date) - timedelta(days=1)
        st.text(date_relatorio)
        

def atualize():
    try:
        new_date=datetime.now().strftime("%Y-%m-%d")
        date_relatorio = pd.to_datetime(new_date) - timedelta(days=1)
        print(date_relatorio)
        st.info("Relatorio para a data: {}".format(date_relatorio))
    except:
        pyautogui.hotkey("ctrl","F5")  

def main():
    """ Main App """
    set_config()
    set_menu()
    st.title("Analise e segmentacao de mercado DashBoard")
      
if __name__ == '__main__':
	main()
    
