# stream_test1
import streamlit as st
import pandas as pd
# import plotly.express as px

st.title("MacroPulse AI")
st.text("The Future of Economic Intelligence Starts Here.")



if st.button("AI-Powered Economic Analysis"):
    st.write('MacroPulse AI harnesses advanced artificial intelligence to extract valuable insights from unstructured economic data, including financial reports, news articles, and market signals. By analyzing vast amounts of text and numerical data in real time, our models detect hidden patterns, sentiment shifts, and emerging trends that impact the global economy. This automated approach eliminates manual inefficiencies, allowing businesses, investors, and policymakers to make data-driven decisions with unparalleled accuracy and speed.')

if st.button("Real-Time Macro Trends"):
    st.write('Economic conditions change rapidly, and staying ahead requires access to up-to-date information. MacroPulse AI continuously monitors key macroeconomic indicators—such as GDP growth, inflation, employment rates, and market sentiment—aggregating data from multiple sources to provide a comprehensive real-time view. With automated alerts, live dashboards, and AI-driven analysis, users can instantly respond to economic shifts, capitalize on opportunities, and mitigate potential risks.')

if st.button("Actionable Insights"):
    st.write('MacroPulse AI seamlessly integrates into existing financial and economic analysis workflows through API-ready solutions, enabling users to access real-time data directly within their preferred platforms. Whether incorporated into business intelligence tools, investment models, or policy research systems, our solution eliminates data silos and enhances collaboration. With a focus on flexibility and ease of use, professionals can leverage MacroPulse AI’s insights without requiring extensive technical expertise.')

if st.button("Sucessfull Examples"):
    st.write('By applying machine learning and deep learning techniques, MacroPulse AI offers predictive analytics that forecast economic trends with high accuracy. Our models analyze historical data, real-time indicators, and external factors—such as geopolitical events and policy shifts—to identify early signals of economic changes. This proactive intelligence empowers businesses, investors, and policymakers to anticipate market fluctuations, optimize resource allocation, and make strategic decisions with confidence.')



# st.title("My title")
# st.header("My header")
# st.subheader("My sub")
# st.selectbox("this is a test")
# st.markdown(style, unsafe_allow_html=True)

# st.set_page_config(layout='wide')
# df = pd.read_csv('diamonds.csv',nrows=100)
# df.head(2)
# col1, col2  = st.columns(2)
# col3, col4, col5 = st.columns(3)
# st.markdown(style, unsafe_allow_html=True)
# fig_date = px.bar(df , x='cut' , y = 'price', title='preço por corte')
# col1.plotly_chart(fig_date)

