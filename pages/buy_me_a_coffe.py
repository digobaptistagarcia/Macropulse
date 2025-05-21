import streamlit as st

# --- Configurações da Página ---
st.set_page_config(
    page_title="Me Ofereça um Café!",
    page_icon="☕",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Seu Link de Pagamento do Stripe ---
# IMPORTANTE: SUBSTITUA ESTE LINK PELO SEU LINK DE PAGAMENTO REAL DO STRIPE!
STRIPE_PAYMENT_LINK = "https://buy.stripe.com/test_YOUR_STRIPE_PAYMENT_LINK_HERE" 
# Exemplo de um link real: "https://buy.stripe.com/565778899011223344"

# --- Título e Mensagem de Boas-Vindas ---
st.title("☕ Me Ofereça um Café!")

st.write(
    """
    Olá! Se você gostou do meu trabalho, do meu conteúdo ou se de alguma forma fui útil para você, 
    consideraria me oferecer um café? 
    
    É uma pequena forma de mostrar seu apoio e me ajuda a continuar criando e compartilhando!
    """
)

st.write("---")

# --- Opções de Apoio (Simulando "Tiers" ou "Valores Sugeridos") ---

st.subheader("Escolha o seu apoio:")

# Opção 1: Um café
st.markdown("### Um Café Pequeno - R$ 10,00")
st.write("Apenas o suficiente para um bom expresso.")
if st.button("Comprar um Café Pequeno", key="small_coffee"):
    st.markdown(f'<a href="{STRIPE_PAYMENT_LINK}" target="_blank" style="display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; border-radius: 5px;">Apoiar com R$ 10,00</a>', unsafe_allow_html=True)
    st.success("Você será redirecionado para o Stripe para completar a doação.")

st.markdown("---")

# Opção 2: Um café médio
st.markdown("### Um Café Grande - R$ 25,00")
st.write("Para aqueles dias longos de codificação ou criação de conteúdo.")
if st.button("Comprar um Café Grande", key="large_coffee"):
    st.markdown(f'<a href="{STRIPE_PAYMENT_LINK}" target="_blank" style="display: inline-block; padding: 10px 20px; background-color: #2196F3; color: white; text-align: center; text-decoration: none; border-radius: 5px;">Apoiar com R$ 25,00</a>', unsafe_allow_html=True)
    st.success("Você será redirecionado para o Stripe para completar a doação.")

st.markdown("---")

# Opção 3: Um pacote de café (mais generoso)
st.markdown("### Pacote de Café - R$ 50,00")
st.write("Muito obrigado! Este apoio me ajuda a cobrir custos de ferramentas e tempo.")
if st.button("Comprar um Pacote de Café", key="coffee_package"):
    st.markdown(f'<a href="{STRIPE_PAYMENT_LINK}" target="_blank" style="display: inline-block; padding: 10px 20px; background-color: #FF9800; color: white; text-align: center; text-decoration: none; border-radius: 5px;">Apoiar com R$ 50,00</a>', unsafe_allow_html=True)
    st.success("Você será redirecionado para o Stripe para completar a doação.")

st.markdown("---")

# --- Agradecimento e Nota Importante ---
st.write(
    """
    **Muito obrigado pelo seu apoio!** Cada café faz uma grande diferença e me motiva a continuar.
    """
)

st.info(
    "**Nota Importante:** Para este aplicativo funcionar, você deve **substituir o valor de `STRIPE_PAYMENT_LINK`** no código pelo seu link de pagamento real do Stripe. "
    "Se você quiser oferecer diferentes valores (R$ 10, R$ 25, R$ 50) e que o Stripe reflita isso, você precisará criar um link de pagamento separado no Stripe para cada valor ou usar o modo de checkout com preço selecionável, que é mais avançado."
)

st.write("Feito com ❤️ no Streamlit.")