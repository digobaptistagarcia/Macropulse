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
    
    st.markdown(""" At MacroPulse AI, we are revolutionizing how businesses, investors, and policymakers access and interpret economic data. Our mission is to harness the power of artificial intelligence to unlock valuable insights from unstructured data sources, including financial reports, news, and market signals. We provide real-time macroeconomic analysis, predictive forecasting, and seamless data integration, helping our clients stay ahead in an ever-changing economic landscape. With a team of experienced economists, data scientists, and AI experts, we are committed to delivering actionable intelligence that empowers smarter decision-making, reduces uncertainty, and drives growth.

We believe that economic analysis shouldn’t be slow, complex, or reactive. That’s why we use cutting-edge AI to streamline the process, offering solutions that are not only accurate but also accessible and customizable for any professional. Whether you're a global investor, a government policymaker, or an economist, MacroPulse AI transforms raw data into actionable insights, helping you navigate the complexities of the global economy with confidence.

""")
    st.header("What we do")
    st.markdown(""" MacroPulse AI specializes in turning unstructured economic data into real-time, actionable insights. Our AI models analyze vast amounts of information—from financial reports to market signals—to provide a comprehensive view of macroeconomic conditions. We continuously track key indicators like GDP, inflation, employment rates, and market trends to keep you ahead of the curve. Our platform offers real-time updates, predictive analytics, and data-driven forecasting, enabling smarter decision-making and more accurate economic planning.

We also prioritize seamless integration with your existing systems. Our API-ready solutions ensure that our insights fit effortlessly into your workflow, whether you're a business leader, an investor, or a policymaker. By providing both real-time data feeds and predictive models, we empower you to make proactive, informed decisions that minimize risk and maximize opportunity. Our focus is on simplicity, speed, and precision, ensuring that complex economic data is easy to understand and act upon.""")
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
        
    st.title("AI-Powered Economic Analysis")
    st.markdown('MacroPulse AI harnesses advanced artificial intelligence to extract valuable insights from unstructured economic data, including financial reports, news articles, and market signals. By analyzing vast amounts of text and numerical data in real time, our models detect hidden patterns, sentiment shifts, and emerging trends that impact the global economy. This automated approach eliminates manual inefficiencies, allowing businesses, investors, and policymakers to make data-driven decisions with unparalleled accuracy and speed.')

    st.title("Real-Time Macro Trends")
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
