# import streamlit as st


# st.set_page_config(
#         page_title="Trading App",
#         page_icon=":heavy_dollar_sign:",
#         layout="wide",
#     )
# st.title("Trading Guide App :bar_chart:")

# st.subheader("We provide the Greatest platform for you to collect all information prior to investing in stocks.")

# st.image("app.png")

# st.markdown("## We provide the following services")

# st.markdown("#### :one: Stock Information")
# st.write("Through this page, you can see all the information about stock. ")

# st.markdown("#### :two: Stock Analysis")
# st.write("You can explore analysis of stocks  closing prices for the next 30 days based on historical stock data . Use this tool to gain valuable insights into market trends and make informed investment decisions.")

# # st.markdown('#### :three: CAPM Return')
# # st.write("Discover how the Capital Asset Pricing Model (CAPM) calculates the expected return of different stocks asset based on its risk and market performance")

# # st.markdown('#### :four: CAPM Beta')
# # st.write("Calculates Beta and Expected Return for Individual Stocks.")

import streamlit as st
from auth import login, register

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Trading App",
    page_icon=":heavy_dollar_sign:",
    layout="wide",
)

# ---------------- SESSION ----------------
if "user" not in st.session_state:
    st.session_state["user"] = None

if "redirect_to_login" not in st.session_state:
    st.session_state["redirect_to_login"] = False


# ---------------- AUTH SYSTEM ----------------
if st.session_state["user"] is None:

    st.title("🔐 Welcome to Trading App")

    # 👇 REDIRECT LOGIC
    if st.session_state["redirect_to_login"]:
        menu = "Login"
        st.session_state["redirect_to_login"] = False
    else:
        menu = st.sidebar.selectbox("Menu", ["Login", "Register"])

    if menu == "Login":
        login()
    else:
        register()


# ---------------- MAIN APP ----------------
else:
    st.sidebar.success(f"Welcome {st.session_state['user']} 👋")

    if st.sidebar.button("Logout"):
        st.session_state["user"] = None
        st.rerun()

    # ----------- YOUR ORIGINAL UI -----------
    st.title("Trading Guide App :bar_chart:")

    st.subheader(
        "We provide the Greatest platform for you to collect all information prior to investing in stocks."
    )

    st.image("app.png")

    st.markdown("## We provide the following services")

    st.markdown("#### :one: Stock Information")
    st.write("Through this page, you can see all the information about stock. ")

    st.markdown("#### :two: Stock Analysis")
    st.write(
        "You can explore analysis of stocks closing prices for the next 30 days based on historical stock data. Use this tool to gain valuable insights into market trends and make informed investment decisions."
    )

    # st.markdown('#### :three: CAPM Return')
    # st.write("Discover how the Capital Asset Pricing Model (CAPM) calculates the expected return of different stocks asset based on its risk and market performance")

    # st.markdown('#### :four: CAPM Beta')
    # st.write("Calculates Beta and Expected Return for Individual Stocks.")