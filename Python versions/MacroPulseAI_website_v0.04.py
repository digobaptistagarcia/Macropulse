# stream_test1
import streamlit as st
import pandas as pd
# import plotly.express as px

# st.title("MacroPulse AI")
# st.text("The Future of Economic Intelligence Starts Here.")


# Title and Introduction
st.title("MacroPulse AI")
st.text("The Future of Economic Intelligence Starts Here.")
    

# Creating tabs
tab_about, tab_cases, tab_solutions, tab_contact, tab_articles = st.tabs([
    "About Us", "Successful Cases", "Our Solutions", "Contact Us", "Articles"
])

# Content for About Us tab
with tab_about:
    st.header("About Us")
    st.write("Learn more about our company, mission, and values.")

# Content for Successful Cases tab
with tab_cases:
    # st.header("Successful Cases")
    st.write("Explore our past successes and case studies.")
    st.subheader("Pesquisa_agricola do brasil")
    st.write('lalalal lelelele lololo')
    

    st.subheader("Movimentação portuaria no br")
    st.write('lalalal lelelele lololo')

    st.subheader("Cnpj's do brasil")
    st.write('lalalal lelelele lololo')
    

    st.subheader("Armazenagem no")
    st.write('lalalal lelelele lololo')
    
    
# Content for Our Solutions tab
with tab_solutions:
    st.header("Our Solutions")
    st.write("Discover the solutions we offer to our clients.")

    #------------start
        
    if st.button("AI-Powered Economic Analysis"):
        st.markdown('MacroPulse AI harnesses advanced artificial intelligence to extract valuable insights from unstructured economic data, including financial reports, news articles, and market signals. By analyzing vast amounts of text and numerical data in real time, our models detect hidden patterns, sentiment shifts, and emerging trends that impact the global economy. This automated approach eliminates manual inefficiencies, allowing businesses, investors, and policymakers to make data-driven decisions with unparalleled accuracy and speed.')

    if st.button("Real-Time Macro Trends"):
        st.write('Economic conditions change rapidly, and staying ahead requires access to up-to-date information. MacroPulse AI continuously monitors key macroeconomic indicators—such as GDP growth, inflation, employment rates, and market sentiment—aggregating data from multiple sources to provide a comprehensive real-time view. With automated alerts, live dashboards, and AI-driven analysis, users can instantly respond to economic shifts, capitalize on opportunities, and mitigate potential risks.')

  
    #------------end 

# Content for Contact Us tab
with tab_contact:
    st.header("Contact Us")
    st.write("Get in touch with us for inquiries and support.")
    st.markdown("""We’d love to hear from you!
                Whether you have questions, want to learn more about our platform, or are interested in starting a partnership, don’t hesitate to get in touch.
                
Email: contact@macropulse.ai
 """)

# Content for Articles tab
with tab_articles:
    st.header("Articles")
    st.write("Read the latest insights and industry news.")

# # Sidebar com botões
# with st.sidebar:
#     st.header("Menu")
#     page = st.radio("Escolha uma opção:", 
#                     ["AI-Powered Economic Analysis", "Real-Time Macro Trends", "Actionable Insights", "Successful Examples"])

# # Página principal (conteúdo muda com base na escolha do usuário)
# if page == "AI-Powered Economic Analysis":
#     st.image("./imagens/fundo_de_tela.png")
#     st.markdown("""
#         **MacroPulse AI harnesses advanced artificial intelligence to extract valuable insights from unstructured economic data**, 
#         including financial reports, news articles, and market signals. By analyzing vast amounts of text and numerical data in real 
#         time, our models detect hidden patterns, sentiment shifts, and emerging trends that impact the global economy. This automated 
#         approach eliminates manual inefficiencies, allowing businesses, investors, and policymakers to make data-driven decisions 
#         with unparalleled accuracy and speed.
#     """)


# elif page == "Real-Time Macro Trends":
#     st.image("./imagens/fundo_de_tela2.png")
#     st.write("""
#         **Economic conditions change rapidly, and staying ahead requires access to up-to-date information.** MacroPulse AI continuously 
#         monitors key macroeconomic indicators—such as GDP growth, inflation, employment rates, and market sentiment—aggregating data 
#         from multiple sources to provide a comprehensive real-time view. With automated alerts, live dashboards, and AI-driven analysis, 
#         users can instantly respond to economic shifts, capitalize on opportunities, and mitigate potential risks.
#     """)

# elif page == "Actionable Insights":
#     st.image("./imagens/fundo_de_tela3.png")
#     st.write("""
#         **MacroPulse AI seamlessly integrates into existing financial and economic analysis workflows through API-ready solutions**, 
#         enabling users to access real-time data directly within their preferred platforms. Whether incorporated into business intelligence 
#         tools, investment models, or policy research systems, our solution eliminates data silos and enhances collaboration. With a focus on 
#         flexibility and ease of use, professionals can leverage MacroPulse AI’s insights without requiring extensive technical expertise.
#     """)

# elif page == "Successful Examples":
#     st.image("./imagens/fundo_de_tela4.png")
#     st.write("""
#         **By applying machine learning and deep learning techniques, MacroPulse AI offers predictive analytics that forecast economic trends** 
#         with high accuracy. Our models analyze historical data, real-time indicators, and external factors—such as geopolitical events and 
#         policy shifts—to identify early signals of economic changes. This proactive intelligence empowers businesses, investors, and policymakers 
#         to anticipate market fluctuations, optimize resource allocation, and make strategic decisions with confidence.
#     """)

# with st.sidebar:
# # Define buttons and show content based on the button clicked
#     if st.button("AI-Powered Economic Analysis"):
#         st.image("./imagens/fundo_de_tela.png")
#         st.markdown("""
#             **MacroPulse AI harnesses advanced artificial intelligence to extract valuable insights from unstructured economic data**, 
#             including financial reports, news articles, and market signals. By analyzing vast amounts of text and numerical data in real 
#             time, our models detect hidden patterns, sentiment shifts, and emerging trends that impact the global economy. This automated 
#             approach eliminates manual inefficiencies, allowing businesses, investors, and policymakers to make data-driven decisions 
#             with unparalleled accuracy and speed.
#         """)

#     if st.button("Real-Time Macro Trends"):
#         st.image("./imagens/fundo_de_tela2.png")
#         st.write("""
#             **Economic conditions change rapidly, and staying ahead requires access to up-to-date information.** MacroPulse AI continuously 
#             monitors key macroeconomic indicators—such as GDP growth, inflation, employment rates, and market sentiment—aggregating data 
#             from multiple sources to provide a comprehensive real-time view. With automated alerts, live dashboards, and AI-driven analysis, 
#             users can instantly respond to economic shifts, capitalize on opportunities, and mitigate potential risks.
#         """)

#     if st.button("Actionable Insights"):
#         st.image("./imagens/fundo_de_tela3.png")
#         st.write("""
#             **MacroPulse AI seamlessly integrates into existing financial and economic analysis workflows through API-ready solutions**, 
#             enabling users to access real-time data directly within their preferred platforms. Whether incorporated into business intelligence 
#             tools, investment models, or policy research systems, our solution eliminates data silos and enhances collaboration. With a focus on 
#             flexibility and ease of use, professionals can leverage MacroPulse AI’s insights without requiring extensive technical expertise.
#         """)

#     if st.button("Successful Examples"):
#         st.image("./imagens/fundo_de_tela4.png")
#         st.write("""
#             **By applying machine learning and deep learning techniques, MacroPulse AI offers predictive analytics that forecast economic trends** 
#             with high accuracy. Our models analyze historical data, real-time indicators, and external factors—such as geopolitical events and 
#             policy shifts—to identify early signals of economic changes. This proactive intelligence empowers businesses, investors, and policymakers 
#             to anticipate market fluctuations, optimize resource allocation, and make strategic decisions with confidence.
#         """)

# st.image("./soja - area colhida.png")


# st.selectbox("I am a Bussines or person", ["Bussines", "person"])


# st.multiselect("Buy", ["milk", "apples", "potatoes"])

# if st.button("AI-Powered Economic Analysis"):
#     st.markdown('MacroPulse AI harnesses advanced artificial intelligence to extract valuable insights from unstructured economic data, including financial reports, news articles, and market signals. By analyzing vast amounts of text and numerical data in real time, our models detect hidden patterns, sentiment shifts, and emerging trends that impact the global economy. This automated approach eliminates manual inefficiencies, allowing businesses, investors, and policymakers to make data-driven decisions with unparalleled accuracy and speed.')

# if st.button("Real-Time Macro Trends"):
#     st.write('Economic conditions change rapidly, and staying ahead requires access to up-to-date information. MacroPulse AI continuously monitors key macroeconomic indicators—such as GDP growth, inflation, employment rates, and market sentiment—aggregating data from multiple sources to provide a comprehensive real-time view. With automated alerts, live dashboards, and AI-driven analysis, users can instantly respond to economic shifts, capitalize on opportunities, and mitigate potential risks.')

# if st.button("Actionable Insights"):
#     st.write('MacroPulse AI seamlessly integrates into existing financial and economic analysis workflows through API-ready solutions, enabling users to access real-time data directly within their preferred platforms. Whether incorporated into business intelligence tools, investment models, or policy research systems, our solution eliminates data silos and enhances collaboration. With a focus on flexibility and ease of use, professionals can leverage MacroPulse AI’s insights without requiring extensive technical expertise.')

# if st.button("Sucessfull Examples"):
#     st.write('By applying machine learning and deep learning techniques, MacroPulse AI offers predictive analytics that forecast economic trends with high accuracy. Our models analyze historical data, real-time indicators, and external factors—such as geopolitical events and policy shifts—to identify early signals of economic changes. This proactive intelligence empowers businesses, investors, and policymakers to anticipate market fluctuations, optimize resource allocation, and make strategic decisions with confidence.')


    



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

