import streamlit as st

st.markdown("""
<h3>📊 Pesquisa Agrícola Mensal (PAM) – IBGE</h3>

<p>A <strong>Pesquisa Agrícola Mensal (PAM)</strong> é realizada pelo <strong>IBGE</strong> com o objetivo de acompanhar, mês a mês, o desempenho das principais lavouras brasileiras.</p>

<h4>🎯 Objetivos</h4>
<ul>
  <li>Estimar a <strong>área plantada e colhida</strong>;</li>
  <li>Monitorar a <strong>produção agrícola e rendimento médio</strong>;</li>
  <li>Atualizar <strong>projeções ao longo do ano-safra</strong>.</li>
</ul>

<h4>🌱 Produtos Monitorados</h4>
<p>A PAM acompanha as principais culturas temporárias e permanentes do Brasil, como:</p>
<ul>
  <li>Soja</li>
  <li>Milho</li>
  <li>Arroz</li>
  <li>Feijão</li>
  <li>Cana-de-açúcar</li>
  <li>Café</li>
  <li>Laranja</li>
  <li>Trigo, entre outros</li>
</ul>

<h4>🛰️ Metodologia</h4>
<p>Os dados são coletados pelas Unidades Estaduais do IBGE, com apoio de <em>Comissões Municipais e Estaduais de Estatística Agropecuária</em>, formadas por especialistas, cooperativas e órgãos públicos.</p>

<h4>📅 Diferença entre PAM e PAM-PROD</h4>
<ul>
  <li><strong>PAM (Mensal):</strong> dados preliminares e contínuos sobre a produção agrícola.</li>
  <li><strong>PAM-PROD (Anual):</strong> consolida os dados definitivos por município.</li>
</ul>

<p>🔍 Para mais informações, acesse o site do <a href="https://www.ibge.gov.br/estatisticas/economicas/agricultura-e-pecuaria.html" target="_blank">IBGE</a>.</p>
""", unsafe_allow_html=True)
