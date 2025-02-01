# 📈 Stock Alert System with Twilio SMS

This Python-based Stock Alert System tracks daily stock price changes and sends SMS notifications via **Twilio** if the price fluctuation exceeds **1%**. It also fetches related news articles to provide more context.

---

## 📷 SMS Notification Preview
Below is a dummy image illustrating how the stock alert message appears on a phone:

![Image](https://github.com/user-attachments/assets/4e61c813-568e-42fb-88ed-24861f9bd547)
---

## 🚀 Features
✅ Fetches real-time stock price changes from **Alpha Vantage API**  
✅ Retrieves relevant news articles from **NewsAPI**  
✅ Sends SMS notifications via **Twilio** when the stock price changes significantly  
✅ Includes **🔻 (red down) & 🟢 (green up) emojis** for price movement indication  
✅ Displays **headline and brief summary** of top 3 related news articles  

---

## 🛠 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/stock-alert-twilio.git
cd stock-alert-twilio
