# ⚡ WeatherVibe - Premium Weather Application

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-2.0+-green.svg" alt="Flask Version">
  <img src="https://img.shields.io/badge/License-MIT-red.svg" alt="License">
</div>

<div align="center">
  <h3>🌤️ A stunning, modern weather application with UI/UX design</h3>
  <p><strong>Built by:</strong> <a href="https://github.com/IshanNaikele">Ishan Naikele</a> (@IshanNaikele)</p>
</div>

---

## 🌟 Features

 

### 🌍 **Weather Features**
- **Real-time weather data** from OpenWeatherMap API
- **Comprehensive weather metrics** (temperature, humidity, pressure, wind)
- **Weather icons** with floating animations
- **Wind direction indicators** with rotating arrows
- **Responsive error handling** with user-friendly messages

### 🔧 **Technical Excellence**
- **Performance optimized** with requestAnimationFrame
- **Mobile-first approach** with progressive enhancement
- **Clean, maintainable code** structure

---
 


## 🛠️ Tech Stack

### **Backend**
- **Python 3.8+** - Core programming language
- **Flask 2.0+** - Lightweight web framework
- **Requests** - HTTP library for API calls
- **Python-dotenv** - Environment variable management

### **Frontend**
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with animations
 
### **APIs & Services**
- **OpenWeatherMap API** - Real-time weather data
- **Google Fonts** - Professional typography

---

## 📦 Installation & Setup

### **Prerequisites**
- Python 3.8 or higher
- OpenWeatherMap API key (free)

### **1. Clone Repository**
```bash
git clone https://github.com/IshanNaikele/weather-app.git
cd weather-app
```

### **2. Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Environment Setup**
Create a `.env` file in the root directory:
```env
OPENWEATHER_API_KEY=your_api_key_here
```

**Get your free API key:**
1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Generate your API key
4. Add it to your `.env` file

### **5. Run Application**
```bash
python app.py
```

Visit `http://localhost:5000` to view the application.

---

## 📁 Project Structure

```
weather-app/
│
├── app.py                 # Flask application & API logic
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (create this)
├── .gitignore           # Git ignore rules
│
├── templates/
│   └── index.html       # Main HTML template with advanced CSS/JS
│
│
└── README.md           # Project documentation
```

---

## 🔧 Configuration

### **Environment Variables**
| Variable | Description | Required |
|----------|-------------|----------|
| `OPENWEATHER_API_KEY` | Your OpenWeatherMap API key | Yes |
| `FLASK_ENV` | Flask environment (development/production) | No |
| `SECRET_KEY` | Flask secret key (auto-generated) | No |

### **API Rate Limits**
- **Free Tier:** 1,000 calls/day, 60 calls/minute
- **Paid Tiers:** Higher limits available

---

 
 

  
## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 About the Developer

**Ishan Naikele** - Full Stack Developer
- 🌐 **GitHub:** [@IshanNaikele](https://github.com/IshanNaikele)
- 📧 **Email:** [Contact Me](mailto:ishannaikele23@gmail.com)
- 💼 **LinkedIn:** [Connect with me](https://www.linkedin.com/in/ishan-naikele-b759562b0/))

### **Skills Demonstrated in This Project:**
- **Backend Development:** Python, Flask, API Integration
- **Frontend Development:** HTML ,CSS 
  
 
 

---

<div align="center">
  <h3>⭐ If you found this project helpful, please give it a star!</h3>
  <p>Made with ❤️ by <strong>Ishan Naikele</strong></p>
</div>
