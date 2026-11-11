# 📊 Website Traffic Analysis Dashboard

An interactive **Website Traffic Analysis Dashboard** built using Python, Pandas, NumPy, Plotly and Streamlit. This project analyzes website visitor behavior, traffic sources, user engagement and conversion performance through data analysis and interactive visualizations.

The dashboard helps understand how visitors interact with a website and identifies the best-performing traffic sources.

## 🚀 Live Demo

**Live Dashboard:** https://website-traffic-analysis.streamlit.app/

**GitHub Repository:** https://github.com/Rajlaxmi-1307/Website-Traffic-Analysis

---

## 🎯 Project Objectives

- Analyze website traffic and visitor behavior.
- Understand different website traffic sources.
- Identify user engagement patterns.
- Analyze page views and session duration.
- Study bounce rates and conversion rates.
- Identify the best-performing traffic source.
- Build an interactive dashboard using Streamlit.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Pandas | Data Cleaning and Analysis |
| NumPy | Numerical Operations |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Plotly | Interactive Charts |
| Streamlit | Dashboard Development |
| Jupyter Notebook | Exploratory Data Analysis |
| Git & GitHub | Version Control |

## 📂 Project Structure

```text
Website_Traffic_Analysis/
│
├── dashboard/
│   └── app.py
│
├── dataset/
│   ├── website_wata.csv
│   └── cleaned_website_traffic.csv
│
├── notebooks/
│   └── EDA.ipynb
│
├── visualizations/
│
├── .gitignore
│
└── requirements.txt
```

## 📊 Dataset Information

The project uses a website traffic dataset containing **2,000 records and 7 columns** after data cleaning.

### Dataset Columns

| Column | Description |
|---|---|
| Page Views | Number of pages viewed by visitors |
| Session Duration | Time spent by visitors on the website |
| Bounce Rate | Percentage of visitors leaving without further interaction |
| Time on Page | Time spent on individual pages |
| Previous Visits | Number of previous visits |
| Conversion Rate | Visitor conversion performance |
| Traffic Source | Source from which visitors arrive |

## 🔍 Exploratory Data Analysis (EDA)

The following analysis was performed using Python:

1. Data Loading and Understanding
2. Data Cleaning and Preprocessing
3. Handling Missing Values
4. Checking Duplicate Records
5. Statistical Analysis
6. Traffic Source Distribution
7. Session Duration Analysis
8. Page Views Analysis
9. Bounce Rate Analysis
10. Conversion Rate Analysis
11. Correlation Analysis
12. Best Traffic Source Identification

## 📈 Dashboard Features

The Streamlit dashboard provides:

- **Interactive Traffic Source Filter:** Filter website performance by traffic source.
- **KPI Cards:** Display total sessions, page views, average session duration, conversion rate and bounce rate.
- **Traffic Source Distribution:** Visualize traffic from Organic, Paid, Referral, Social and Direct sources.
- **Page Views Analysis:** Analyze website page-view patterns.
- **Session Duration Analysis:** Compare visitor engagement.
- **Bounce Rate Analysis:** Understand visitor exit behavior.
- **Conversion Analysis:** Evaluate conversion performance.
- **Best Traffic Source:** Identify the highest-performing traffic source.

## 📌 Key Insights

Based on the analysis performed:

- Total website sessions: **2,000**
- Total page views: **9,901**
- Average session duration: **3.02**
- Average conversion rate: **98.2%**
- Average bounce rate: **28.5%**

### Traffic Source Distribution

| Traffic Source | Percentage |
|---|---:|
| Organic | 39.3% |
| Paid | 21.4% |
| Referral | 15.0% |
| Social | 13.5% |
| Direct | 10.8% |

### Best Performing Traffic Source

**Referral Traffic**

- Highest average conversion rate: 0.988
- Average session duration: 3.13

Referral traffic achieved the highest conversion rate in the analysis.

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### Step 1: Clone the Repository

```bash
git clone https://github.com/Rajlaxmi-1307/Website-Traffic-Analysis.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Website-Traffic-Analysis
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate Virtual Environment

For Windows:

```bash
.venv\Scripts\activate
```

### Step 5: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 6: Run the Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

### Step 7: Open the Dashboard

Open the local URL displayed in your terminal:

```text
http://localhost:8501
```

## 🌐 Deployment

The project is deployed using **Streamlit Community Cloud**.

Live Application:

https://website-traffic-analysis.streamlit.app/

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Python programming and data analysis.
- Data cleaning and preprocessing.
- Exploratory Data Analysis (EDA).
- Data visualization and interpretation.
- Working with Pandas and NumPy.
- Building interactive dashboards using Streamlit.
- Managing projects using Git and GitHub.
- Deploying Python applications online.

## 👩‍💻 Author

**Rajlaxmi Patil**

GitHub: https://github.com/Rajlaxmi-1307

---

⭐ If you find this project useful, consider giving the repository a star!

**Thank you for visiting my project!**