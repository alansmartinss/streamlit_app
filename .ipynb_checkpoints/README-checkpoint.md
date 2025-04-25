# 💳 Streamlit CSV Payment App

This project demonstrates an interactive web application built with **Streamlit** and **Python**, focusing on the integration of **pay-per-row data processing**. The system simulates a billing model based on the number of rows in a `.csv` file, ideal for use cases such as:

- On-demand data processing services  
- APIs with usage-based billing  
- Payment gateway integration demos  

---

## 🚀 Features

- **User authentication** via `streamlit-authenticator`
- **CSV file upload** with row count and preview
- **Dynamic pricing calculation** based on number of rows (R$0.01 per row)
- **Stripe Checkout integration** for secure payment processing
- **Post-payment report** showing a sample of uploaded data

---

## 🧠 Technologies Used

- **[Streamlit](https://streamlit.io/)** – Web app framework for Python
- **[Pandas](https://pandas.pydata.org/)** – Data manipulation and analysis
- **[Stripe API](https://stripe.com/docs/api)** – Online payment platform
- **[streamlit-authenticator](https://github.com/mkhorasani/Streamlit-Authenticator)** – Simple authentication for Streamlit

---

## 🗂️ Project Structure

```
my_app/
├── streamlit_app.py            # Main application file
├── requirements.txt            # Project dependencies
└── .streamlit/
    └── config.toml             # Streamlit server configuration
```

---

## ⚙️ How to Run Locally

1. Clone the repository or copy the files into a folder:

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run streamlit_app.py
```

4. Access at `http://localhost:8501`

---

## 💰 Payment Integration

The app uses **Stripe Checkout** to handle transactions. The total amount is calculated based on the number of rows in the uploaded `.csv` file, charged at R$0.01 per row.

> ⚠️ To enable full functionality, replace the Stripe test key with your valid one:
```python
stripe.api_key = 'sk_test_your_secret_key_here'
```

---

## 📈 Use Case Scenarios

This project can easily be adapted for:

- SaaS tools with volume-based billing
- Prototypes of platforms monetized by data uploads
- Training and demonstration of payment API integration

---

## 📌 Future Improvements

- Integration with Mercado Pago for Brazilian market
- Database storage of uploads and payments
- Billing dashboard per user
- Email-based authentication using secure backend (Firebase/Auth0/etc)

---

## 👤 Author

**Alan Martins**  
📧 Email: alansmartinss@hotmail.com   
🔗 [LinkedIn](https://www.linkedin.com/in/alansmartinss)