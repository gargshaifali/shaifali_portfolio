"""Generate Shaifali Garg's updated resume PDF (mirrors the portfolio site)."""
from fpdf import FPDF

# ---- Theme (matches the portfolio) ----
INK = (26, 26, 46)
SOFT = (74, 74, 104)
ACCENT = (37, 117, 252)      # blue
TEAL = (18, 136, 124)
LIGHT = (245, 247, 251)

BULLET = "\u2022"


class Resume(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(150, 150, 160)
        self.cell(0, 8, f"Shaifali Garg  |  Page {self.page_no()}", align="C")

    # -- building blocks --
    def section_title(self, text):
        self.ln(2.5)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(*ACCENT)
        self.cell(0, 7, text.upper(), new_x="LMARGIN", new_y="NEXT")
        y = self.get_y()
        self.set_draw_color(*ACCENT)
        self.set_line_width(0.5)
        self.line(self.l_margin, y, self.w - self.r_margin, y)
        self.ln(2)

    def job(self, role, dates, org):
        self.set_font("Helvetica", "B", 10.5)
        self.set_text_color(*INK)
        w = self.w - self.l_margin - self.r_margin
        self.cell(w - 32, 5.5, role, new_x="RIGHT")
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*TEAL)
        self.cell(32, 5.5, dates, align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "I", 9.5)
        self.set_text_color(*SOFT)
        self.cell(0, 5, org, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.5)

    def bullet(self, text):
        self.set_font("Helvetica", "", 9.3)
        self.set_text_color(*SOFT)
        x = self.get_x()
        y = self.get_y()
        # draw a small filled circle as the bullet marker
        self.set_fill_color(*ACCENT)
        self.ellipse(x + 0.6, y + 1.7, 1.4, 1.4, style="F")
        self.set_x(x + 4)
        self.multi_cell(self.w - self.l_margin - self.r_margin - 4, 4.6, text)
        self.ln(0.4)

    def labelled(self, label, text):
        self.set_font("Helvetica", "B", 9.3)
        self.set_text_color(*INK)
        self.write(4.6, f"{label}: ")
        self.set_font("Helvetica", "", 9.3)
        self.set_text_color(*SOFT)
        self.multi_cell(0, 4.6, text)
        self.ln(1.2)


pdf = Resume(format="A4")
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_margins(15, 12, 15)
pdf.add_page()

# ---- Header ----
pdf.set_font("Helvetica", "B", 24)
pdf.set_text_color(*INK)
pdf.cell(0, 10, "SHAIFALI GARG", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 11)
pdf.set_text_color(*ACCENT)
pdf.cell(0, 6, "Analytical Thinker  |  Quantitative Researcher  |  BI Manager",
         new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(*SOFT)
pdf.cell(0, 5.5, "shaifaligarg2024@gmail.com   |   gecgithub01.walmart.com/s0g0em7",
         new_x="LMARGIN", new_y="NEXT")

# ---- Summary ----
pdf.section_title("Professional Summary")
pdf.set_font("Helvetica", "", 9.3)
pdf.set_text_color(*SOFT)
pdf.multi_cell(0, 4.6, (
    "Analytical thinker with strong mathematical foundations and ten years tackling complex "
    "problems across quantitative disciplines, from supply chain optimization to predictive "
    "modeling. Cross-disciplinary expertise grounded in business analytics. Proven ability to "
    "rapidly learn new domains and apply rigorous analytical frameworks. Strong communicator "
    "translating complex quantitative concepts for interdisciplinary teams. Curiosity-driven "
    "researcher committed to leveraging analytical expertise to build impactful AI systems."
))

# ---- Core Competencies ----
pdf.section_title("Core Competencies")
pdf.set_font("Helvetica", "", 9.3)
pdf.set_text_color(*SOFT)
pdf.multi_cell(0, 4.6, (
    "Math Modeling, Statistical Analysis, Problem Solving, Quantitative Research, "
    "Facilities Services Management, Predictive Analytics, Machine Learning, Rapid Learning, "
    "Hypothesis Testing, Regression Analysis, Time Series, Neural Networks"
))

# ---- Work Experience ----
pdf.section_title("Work Experience")

pdf.job("Manager, Business Intelligence and Reporting", "2022 - Present",
        "Facilities Services, Walmart Inc, Bentonville, USA")
for b in [
    "Created new processes and workflows in Phoenix (Quickbase) that help run the business and "
    "finance across all POs, maintaining financial changes in data directly from SAP.",
    "Lead cross-disciplinary teams, fostering collaborative problem-solving and a continuous "
    "learning culture.",
    "Translate complex quantitative insights into clear, actionable recommendations for "
    "executive leadership.",
    "Design advanced analytical solutions leveraging statistical methods, predictive modeling, "
    "and ML algorithms.",
    "Demonstrate rapid learning agility by mastering new domains, tools, and methodologies.",
    "Manage complex BI and reporting solutions by researching potential solutions and making "
    "recommendations to meet end-user objectives; updating business data; creating visual "
    "prototypes and design documentation; monitoring solutions and troubleshooting issues; "
    "completing dashboard and reporting specifications; and creating reports and visualizations "
    "to effectively communicate results.",
    "Manage the implementation of BI solution roadmaps by developing written and oral "
    "presentations for diverse audiences (management, customers, suppliers, BI and analytics "
    "staff); ensuring solution testing and validation; ensuring requirements are met to support "
    "implementations; overseeing upgrades and release schedules for BI and database products; "
    "reviewing the impact of changes before and after implementation; and communicating project "
    "results and updates to senior leadership.",
    "Provide supervision and development opportunities for associates by hiring and training on "
    "modern tools such as Code Puppy and Copilot; mentoring; assigning duties; providing "
    "recognition; and ensuring diversity awareness.",
    "Create and revise complex BI and reporting solutions by identifying business requirements "
    "and validating gathered information; collaborating with subject matter experts, data "
    "experts, and other BI and analytics experts; coordinating the evaluation of customer and "
    "supplier solutions; making recommendations to meet end-user objectives; designing and "
    "conducting analysis and reporting solutions; writing detailed dashboard and reporting "
    "specifications; documenting and revising data collection processes; and creating reports "
    "and visualizations to effectively communicate results.",
    "Understand current customer BI and reporting needs by managing production of scheduled "
    "reports; managing reporting databases to ensure accuracy and completeness of data; "
    "maintaining materials for state-of-the-art user interfaces that enable business users to "
    "interpret trends and exceptions; providing guidance and direction to stakeholders; and "
    "identifying gaps and opportunities in BI and reporting solutions.",
]:
    pdf.bullet(b)

pdf.job("Senior Data Analyst", "2022", "Supply Chain, Walmart Inc, Bentonville, USA")
for b in [
    "Developed 20+ dashboards translating complex data patterns into clear visualizations for "
    "diverse stakeholders.",
    "Applied time series forecasting models for transportation demand, balancing complexity "
    "with applicability.",
    "Elevated customer satisfaction from 60% to 95% through rigorous root cause analysis and "
    "systematic frameworks.",
    "Tackled inventory optimization for 1,500+ SKUs using mathematical modeling and constraint "
    "optimization.",
]:
    pdf.bullet(b)

pdf.job("Business Analyst Intern", "2022", "Aezion Inc, Dallas, USA")
for b in [
    "Applied quantitative risk analysis to $2B programs using Monte Carlo simulations.",
    "Achieved 20% supply chain cost reduction through analytical insights.",
]:
    pdf.bullet(b)

pdf.job("Research Analyst", "2021", "Southern Methodist University, Dallas, USA")
for b in [
    "Developed mathematical models in Python quantifying marketing impact on consumer behavior.",
    "Built neural network models predicting performing arts attendance during COVID-19 "
    "unprecedented conditions.",
    "Created an interactive web application (RShiny & SQL) enabling exploration of complex "
    "predictive models.",
]:
    pdf.bullet(b)

pdf.job("R&D Quality Assurance Manager", "2020 - 2021",
        "Dassault Systemes Solutions Lab, Pune, India")
for b in [
    "Led a team of 7 automating analytical workflows (Power BI), achieving 10% revenue increase.",
    "Defined 100+ KPIs for 6 product launches, establishing rigorous quantitative measurement "
    "frameworks.",
    "Created dashboards translating complex clinical trial data into accessible insights for "
    "medical stakeholders.",
]:
    pdf.bullet(b)

pdf.job("Senior Consultant", "2019 - 2020", "Publicis Sapient, Gurgaon, India")
for b in [
    "Performed EDA using advanced statistical techniques (Q-Q plots, correlation analysis).",
    "Conducted rigorous root cause analysis improving software quality.",
]:
    pdf.bullet(b)

pdf.job("QA Analyst", "2018 - 2019", "Capgemini, Pune, India")
for b in [
    "Led an analytical team developing quantitative models for media supply chain optimization.",
    "Performed EDA on financial loan data, uncovering behavioral patterns and risk factors.",
]:
    pdf.bullet(b)

pdf.job("Senior Data Analyst", "2014 - 2018", "Infosys Ltd, Pune, India")
for b in [
    "Applied hypothesis testing, regression, and correlation for strategic business decisions.",
    "Performed linear programming and sensitivity analysis for resource optimization.",
]:
    pdf.bullet(b)

# ---- Projects ----
pdf.section_title("Analytical Projects")
projects = [
    ("Phoenix (Quickbase) Finance Platform",
     "Designed new processes and workflows in Phoenix (Quickbase) to run business and finance "
     "operations across all POs, maintaining financial changes in data sourced directly from SAP."),
    ("Code Puppy Diaries (Live)",
     "A living project exploring AI-assisted development with Code Puppy - experiments, "
     "automations, and learnings, versioned and shared on Walmart Enterprise GitHub "
     "(gecgithub01.walmart.com/s0g0em7/Code-Puppy-Diaries-live)."),
    ("EOL Electrical Analysis (Multi-Agent)",
     "Automated end-of-life electrical analysis - picks stores one by one, finds the latest "
     "diagram model from a shared folder, downloads it, converts it into a readable Excel form, "
     "and pushes the data into Phoenix (Quickbase), all orchestrated by 4 parallel Quickbase agents."),
    ("Power Automate Ticketing Bot",
     "Built an automation bot in Power Automate that copies comments from an email and pastes "
     "them into the DRT associated with a ticket, saving roughly 7 hours every day."),
    ("Statistical Decision Modeling",
     "Applied hypothesis testing, multiple regression, and correlation for a multi-million dollar "
     "acquisition evaluation (Sleep Cool Mattress)."),
    ("Consumer Behavior Analysis",
     "Analyzed large-scale Six Flags data identifying behavioral patterns; built interactive "
     "Tableau dashboards."),
    ("Optimization Modeling",
     "Performed linear programming & sensitivity analysis for LEGO production planning and "
     "resource allocation."),
]
for name, desc in projects:
    pdf.labelled(name, desc)

# ---- Education ----
pdf.section_title("Education")
pdf.job("MS in Business Analytics (GPA: 3.7/4.0)", "2021 - 2022",
        "Southern Methodist University, Dallas, USA")
pdf.bullet("Coursework: Statistical Analysis, ML, Predictive Modeling, Decision Optimization, "
           "Time Series.")
pdf.job("BS in Computer Science & Engineering", "2010 - 2014", "Lingaya's University, India")
pdf.bullet("Foundation: Algorithms, Data Structures, Computational Math, Database Systems.")

# ---- Technical Skills ----
pdf.section_title("Technical Skills & Methodologies")
pdf.labelled("Programming & Tools",
             "Python (NumPy, Pandas, Scikit-learn), R (Statistical Analysis), SQL, Tableau, "
             "Power BI, GCP BigQuery, Alteryx, Dataiku, Excel (Advanced Analytics), Code Puppy, "
             "Git, AI Innovation Lab, Wibey, VS Code")
pdf.labelled("Analytical Methods",
             "Hypothesis Testing, Regression (Linear, Logistic, Multiple), Time Series (ARIMA, "
             "Prophet), Neural Networks, Decision Trees, Clustering, Monte Carlo Simulation, "
             "Linear Programming, Sensitivity Analysis, Root Cause Analysis, A/B Testing, EDA")
pdf.labelled("Domains",
             "Supply Chain, Healthcare, Finance, Social Media, Performing Arts, Retail, "
             "Facilities Services, Walmart Power")

# ---- Certifications ----
pdf.section_title("Certifications & Commitment")
pdf.bullet("Certifications: Dataiku Core Designer | Bloomberg Market Concepts | Python Data "
           "Science Toolkit (DataCamp) | Data Analytics in R | Lean Six Sigma Yellow Belt (AIGPE)")
pdf.bullet("Continuous Learning: Rapidly mastered new platforms (Dataiku, Alteryx), demonstrating "
           "intellectual curiosity and adaptability.")
pdf.bullet("Cross-Disciplinary Impact: Applied expertise across supply chain, healthcare, finance, "
           "social media, performing arts, and facilities services.")
pdf.bullet("Collaborative Excellence: Effective communication with technical teams, business "
           "stakeholders, and academic researchers.")

pdf.output("assets/Shaifali_Garg_Resume.pdf")
print("Resume PDF written to assets/Shaifali_Garg_Resume.pdf")
