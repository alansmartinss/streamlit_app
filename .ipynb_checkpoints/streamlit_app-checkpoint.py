
import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import stripe

# Chave secreta do Stripe (substitua pela sua chave de testes ou produção)
stripe.api_key = 'sk_test_sua_chave_secreta_aqui'

# Usuários de exemplo para autenticação
users = {
    "joao": {"name": "João Silva", "password": "123"},
    "maria": {"name": "Maria Souza", "password": "abc"}
}

authenticator = stauth.Authenticate(
    list(users.keys()),
    [user["name"] for user in users.values()],
    [user["password"] for user in users.values()],
    cookie_name='streamlit_auth',
    key='abcdef',
    cookie_expiry_days=1
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    st.success(f'Bem-vindo, {name}!')
    uploaded_file = st.file_uploader("Faça upload do seu arquivo CSV", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        num_linhas = len(df)
        st.write(f"O arquivo tem {num_linhas} linhas.")
        preco_por_linha = 0.01
        valor_total = num_linhas * preco_por_linha
        st.write(f"Total a pagar: R${valor_total:.2f}")

        if st.button("Pagar com Stripe"):
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'brl',
                        'product_data': {
                            'name': 'Processamento de CSV',
                        },
                        'unit_amount': int(preco_por_linha * 100),  # centavos
                    },
                    'quantity': num_linhas,
                }],
                mode='payment',
                success_url='http://localhost:8501/?success=true',
                cancel_url='http://localhost:8501/?canceled=true',
            )
            st.markdown(f"[Clique aqui para pagar]({session.url})", unsafe_allow_html=True)

    query_params = st.experimental_get_query_params()
    if query_params.get("success"):
        st.success("Pagamento confirmado com sucesso!")
        st.write("### Relatório do CSV")
        st.write(f"Número total de linhas: {num_linhas}")
        st.dataframe(df.head())
    elif query_params.get("canceled"):
        st.warning("Pagamento cancelado.")

elif authentication_status is False:
    st.error("Usuário ou senha inválidos.")
elif authentication_status is None:
    st.warning("Por favor, digite seu login.")
