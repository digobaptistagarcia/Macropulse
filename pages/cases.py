import streamlit as st



# Creating tabs
tab_silos_geoloc , pesq_agr, port_mov, tab_csult_socio, tab_articles = st.tabs([
     "Armazenagem", "Pesquisa_agricola do brasil", "Movimentação portuaria",     "Consulta_socio", "Articles"
])


with tab_silos_geoloc:
    import pandas as pd
    import plotly.express as px

    # Load data
    
    diretorio = r'C:\Users\digob\OneDrive\Área de Trabalho\PROJECTS\Silos Geo Loc'
    # caminho_completo = diretorio + '\\Base_completa.xlsx'
    df = pd.read_excel(diretorio + '\\Base_completa.xlsx')
    
    # df = pd.read_excel('/C:\Users\digob\OneDrive\Área de Trabalho\PROJECTS\Silos Geo Loc/Base_completa.xlsx')

    df = df[['CDA', 'Armazenador', 'Endereço', 'Município', 'UF', 'Tipo', 'Telefone',
            'Email', 'Capacidade (t)', 'lat_ok1', 'Long_ok1']]
    df.columns = ['CDA', 'Armazenador', 'Endereco', 'Municipio', 'UF', 'Tipo', 'Telefone',
                'Email', 'Capacidade (t)', 'latitude', 'longitude']

    # Define dropdown options including "All"
    dropdown_options = ['All'] + df['UF'].unique().tolist()

    # Sidebar
    st.title("Grain Storage Capacity in Brazil")
    st.markdown("""Explore grain storage facilities in Brazil by state and capacity.             
                Grains such as soybeans and  corn are fundamental to both food security and economic development nowadays. As one of the world’s top agricultural producers, Brazil depends on efficient grain storage systems to preserve crop quality, reduce post-harvest losses, and ensure a stable supply throughout the year. Understanding the country’s storage capacity is essential to identifying gaps in infrastructure, optimizing logistics, and supporting farmers who rely on adequate storage to negotiate better prices and manage production risks.
                Grain storage also plays a strategic role in national planning. It helps balance market fluctuations, strengthens food reserves, and supports international trade. Without sufficient and well-managed storage, even the most productive harvests can go to waste or flood the market at low prices. Therefore, analyzing grain storage capacity is not just a technical concern—it’s a key factor in promoting sustainability, economic resilience, and long-term food security in Brazil and beyond.""")
    st.markdown("""             
                Because Brazil typically produces two grain crops per year—most commonly a soybean and corn rotation—the country faces a significant storage deficit. In some states, the lack of capacity is so severe that grains are often piled outside silos, exposed to weather and potential losses. Mapping the location of silos reveals much more than just storage infrastructure—it provides insight into the flow of grain to export ports and the economic development that occurs along key transportation routes. It’s also important to note that the majority of grain is transported by trucks, with limited use of railways, which increases logistics costs and pressure on road infrastructure. Today, Brazil’s northern ports are responsible for approximately 50pp of grain exports, highlighting a shift in export dynamics and the growing importance of northern logistics corridors.
                """)

    selected_states = st.multiselect("Select state(s)", dropdown_options, default='All')
    selected_capacity = st.slider("Select capacity range", min_value=0, max_value=300000, value=(0, 300000), step=5000)

    # Filter data based on user inputs
    filtered_df = df.copy()
    if 'All' not in selected_states:
        filtered_df = filtered_df[filtered_df['UF'].isin(selected_states)]

    filtered_df = filtered_df[(filtered_df['Capacidade (t)'] >= selected_capacity[0]) & (filtered_df['Capacidade (t)'] <= selected_capacity[1])]

    # Scatter mapbox figure
    scatter_fig = px.scatter_mapbox(
        filtered_df,
        lat='latitude',
        lon='longitude',
        hover_name='Armazenador',
        size='Capacidade (t)',
        color='Capacidade (t)',
        color_continuous_scale='Viridis',
        hover_data={'latitude': True, 'longitude': True, 'Capacidade (t)': True},
        zoom=3
    )
    scatter_fig.update_layout(
        mapbox_style='carto-positron',
        mapbox_zoom=4,
        mapbox_center={'lat': -15, 'lon': -55},
        title='Scatter Map of Silos',
        height=600
    )

    # Histogram graph
    histogram_fig = px.histogram(filtered_df, x='Capacidade (t)', nbins=80, title='Histogram of Capacity',
                                color_discrete_sequence=['darkblue'])  # color of histogram bars)
    histogram_fig.update_xaxes(title_text='Capacity (t)')
    histogram_fig.update_yaxes(title_text='Frequency')
    histogram_fig.update_layout(template='plotly_white')

    # Bar graph
    bar_data = filtered_df.groupby('UF')['Capacidade (t)'].sum().reset_index()
    bar_data = bar_data.sort_values(by='Capacidade (t)', ascending=False)  # Sort by capacity in descending order
    bar_fig = px.bar(bar_data, x='UF', y='Capacidade (t)', title='Capacity per State',
                    color_discrete_sequence=['darkblue'])
    bar_fig.update_layout(template='plotly_white')

    # Display charts
    st.plotly_chart(scatter_fig)
    st.plotly_chart(histogram_fig)
    st.plotly_chart(bar_fig)


# Content for About Us tab
with pesq_agr:
    st.header("Pesquisa_agricola do brasil")
    st.write("Learn more about our company, mission, and values.")

# Content for Successful Cases tab
with port_mov:
    # st.header("Successful Cases")
    st.write("Explore our past successes and case studies.")
    st.subheader("Pesquisa_agricola do brasil")
    st.write('lalalal lelelele lololo')
    

    st.subheader("Movimentação portuaria no br")
    st.write('lalalal lelelele lololo')

with tab_csult_socio:
    st.header('Consulte um CNPJ:')
    st.number_input('digite o cnpj:')

    
    st.subheader('Como o site funciona:')
    st.markdown("""
Como o site funciona:

A plataforma realiza a busca de informações públicas relacionadas a empresas e seus sócios.
O usuário pode acessar dados como nome, CNPJ, endereço e outras informações legais de uma empresa ou sociedade.
Existem diferentes modalidades de consulta, com detalhes pagos para acesso a informações mais completas ou atualizadas. """)