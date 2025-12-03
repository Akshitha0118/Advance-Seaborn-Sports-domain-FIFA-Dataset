# Advance-Seaborn-Sports-domain-FIFA-Dataset
# ⚽ FIFA Player Analysis Dashboard — Streamlit

### 📌 Project Overview
This interactive dashboard provides **Exploratory Data Analysis (EDA)** on the FIFA dataset using **Streamlit**.  
Users can explore player performances, filter players by attributes, compare players, visualize rating trends, and even build a **Best XI team** automatically based on overall ratings.

---

## 🚀 Features
| Module | Description |
|--------|-------------|
| 🔍 Filters | Filter by Position, Nationality, Club, Age & Overall Rating |
| 📄 Overview | Dataset metadata & raw table preview |
| 📊 Univariate Analysis | Distribution plots for Overall & Age |
| 🔗 Bivariate Analysis | Scatter plot of Age vs Overall (with position groups) |
| 🔥 Correlation | Heatmap to analyze relationships between player attributes |
| 🏆 Best XI Team | Auto-select top player per position based on Overall rating |
| ⚔ Player Comparison | Side-by-side comparison of any two players |

---

## 🖥️ Tech Stack
| Library | Purpose |
|--------|---------|
| Streamlit | Dashboard UI |
| Pandas | Data processing |
| Seaborn | Statistical visualizations |
| Matplotlib | Plot rendering |
| CSS | Custom UI styling |

---

## 📌 Key Insights from FIFA Dataset
✔ Majority of players fall within a **balanced age distribution**, indicating a good mix of young & experienced players.  
✔ **Overall rating distribution is right-skewed**, meaning fewer highly elite players compared to average ones.  
✔ **Positive correlation** observed between **Age and Overall rating**, but younger players often have **higher potential**.  
✔ Top rated players are concentrated in popular clubs and well-known football nations.  
✔ Best XI team based on ratings includes high-ranking players across each position, reflecting **real-world football balance**.  
✔ The **Player Comparison** feature highlights:
- Age and rating differences
- Wage & market value comparison
- Potential growth insight

---

## 🏁 Conclusion
This FIFA dashboard provides:
- A strong foundation for **football analytics**
- A dynamic tool for **talent scouting & performance interpretation**
- A useful interface for **sports data analysis learning**

📌 It can be extended to:
- Player market value prediction
- Similar player recommendation system
- Player performance forecasting using machine learning

---

## ▶️ How to Run the App
```bash
pip install -r requirements.txt
streamlit run app.py
