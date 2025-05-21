import streamlit as st
st.header("Our Solutions")
st.write("Discover the solutions we offer to our clients.")

#------------start
    
st.title("AI-Powered Economic Analysis")
st.markdown('MacroPulse AI harnesses advanced artificial intelligence to extract valuable insights from unstructured economic data, including financial reports, news articles, and market signals. By analyzing vast amounts of text and numerical data in real time, our models detect hidden patterns, sentiment shifts, and emerging trends that impact the global economy. This automated approach eliminates manual inefficiencies, allowing businesses, investors, and policymakers to make data-driven decisions with unparalleled accuracy and speed.')

st.title("Real-Time Macro Trends")
st.write('Economic conditions change rapidly, and staying ahead requires access to up-to-date information. MacroPulse AI continuously monitors key macroeconomic indicators—such as GDP growth, inflation, employment rates, and market sentiment—aggregating data from multiple sources to provide a comprehensive real-time view. With automated alerts, live dashboards, and AI-driven analysis, users can instantly respond to economic shifts, capitalize on opportunities, and mitigate potential risks.')


# Seu link de pagamento do Stripe
# Substitua este link pelo link real do seu produto no Stripe
# STRIPE_PAYMENT_LINK = "https://buy.stripe.com/test_YOUR_STRIPE_PAYMENT_LINK_HERE" 
STRIPE_PAYMENT_LINK = "https://buy.stripe.com/test_eVq9AT0MsbJ98GCaJf5Rm00"

# st.set_page_config(layout="centered")

st.title("Compre nosso Produto Incrível!")

# st.write(
#     """
#     Este é um exemplo de como integrar um link de pagamento do Stripe em seu aplicativo Streamlit.
#     Basta clicar no botão abaixo para ser redirecionado para a página de checkout seguro do Stripe.
#     """
# )

# Adicione uma imagem do produto (opcional)
# st.image("caminho/para/sua/imagem_do_produto.png", caption="Nosso Produto")

st.subheader("Preço: R$ 99,99")

# Opção 1: Botão de pagamento
if st.button("Comprar Agora (via Stripe)"):
    st.markdown(f'<a href="{STRIPE_PAYMENT_LINK}" target="_blank">Clique aqui para ir para o pagamento</a>', unsafe_allow_html=True)
    st.info("Você será redirecionado para a página de pagamento seguro do Stripe.")

st.markdown("---")

# Opção 2: Link de pagamento direto (pode ser usado como alternativa ao botão)
st.write("Ou, se preferir, acesse o link de pagamento diretamente:")
st.markdown(f"[Link de Pagamento Stripe]({STRIPE_PAYMENT_LINK})")

st.info("Para este exemplo funcionar, substitua `test_YOUR_STRIPE_PAYMENT_LINK_HERE` pelo seu link de pagamento real do Stripe.")   

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# import streamlit as st
# import time

# # Substitua com seu link de pagamento real do Stripe
# STRIPE_PAYMENT_LINK = "https://buy.stripe.com/YOUR_STRIPE_PAYMENT_LINK"  # Coloque o link de pagamento do Stripe aqui

# # Substitua com o URL do arquivo que você deseja que o usuário baixe após o pagamento
# DOWNLOAD_URL = "https://your-website.com/seu_arquivo.csv"  # Coloque o URL do arquivo para download aqui

# def main():
#     st.title("Apoie e Baixe seus Dados")
#     st.write("Clique no botão abaixo para apoiar e receber seus dados.")

#     if st.button("Apoiar e Baixar Dados"):
#         # Simula o direcionamento para o Stripe e o processo de pagamento
#         st.info("Redirecionando para o pagamento...")
#         time.sleep(2)  # Simula o tempo de redirecionamento

#         # Aqui, você normalmente integraria com a API do Stripe para processar o pagamento
#         # Se o pagamento for bem-sucedido, você exibiria o link de download

#         # Simula um pagamento bem-sucedido
#         pagamento_bem_sucedido = True  # Mude para False para testar o cenário de falha

#         if pagamento_bem_sucedido:
#             st.success("Pagamento realizado com sucesso! Clique no link abaixo para baixar seus dados.")
#             st.markdown(f'<a href="{DOWNLOAD_URL}" target="_blank" style="display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; border-radius: 5px;">Baixar Dados</a>', unsafe_allow_html=True)
#         else:
#             st.error("Ocorreu um erro ao processar o pagamento. Por favor, tente novamente.")

# if __name__ == "__main__":
#     main()
