import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Liyi, Wang
##### *CV* 
''')



st.markdown('## Contact', unsafe_allow_html=True)
st.info('''
- Contact Number: +66 63 650 8798 
- meensky54@gmail.com.
- Location: Bangkok.
- CV link: https://share.streamlit.io/goodjira/cvliyi/main
''')

#####################
# Navigation
#https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css
#https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css
#https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
#st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">')
#<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
#<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark"  style="background-color: #4A9DF8;">
  <a class="navbar-brand"  target="_blank">Liyi, Wang</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">SKILLS</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#professional-certificates">PROFESSIONAL CERTIFICATES</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)





#####################
st.markdown('''
## WORK EXPERIENCE
''')

st.markdown('**BUSINESS INSIGHTS ANALYST**, BECIS (Bangkok),                 Dec20-Now')
st.markdown('**The only `business (data) analyst` supporting whole organization across `8` countries in different green energy product lines in terms of `data platform`, `database`, `BI reports`, and `data insights`.**')
st.markdown('''
- Build a reliable platform using Bubble.io, Power Apps for all departments in the organization e.g. Business Development, Operation, Finance, Project Management, Engineering.
- Define and collect required information and maintain database. eg. web scraping, MySQL, Microsoft dataverse, Microsoft dataflow.
- Build sustainable Power BI reports e.g. company-wide KPI, Sales Pipeline, Operating reports.
- Analyze data and provide business insights to top management using Power BI and Python.
- Migrate different platforms into a single Customer Relationship Management (Dynamics 365 CRM) platform as well as maintain the platform.
- Proactively look for new approaches to constantly improve current workflows and systems.  
''')

st.markdown('**DATA ANALYST**, Jinpao Precision (Samutprakarn),                 Oct19-Nov20')
st.markdown('**Data analyst in Finance department**')
st.markdown('''
- Prepare company???s financial reports (using SQL and Power BI)
- ERP system debugging
- Analyze factory-related data to improve efficiency and find opportunities (using SQL and Python) e.g. analysis of factory workers??? production time, factory revenue and cost analysis, working-process optimization, etc.
''')

st.markdown('**ACTUARIAL OFFICER**, HonTai Life Insurance (Taipei),                 Jun16-May18')
st.markdown('**Actuarial role with focus on Asset Liability Management **')
st.markdown('''
- Expense and overriding analysis.
- Actuarial pricing assumption setting.
- Prophet actuarial models maintenance.
- Cash flow projection and testing for asset and liability modeling.
- Actuarial Assistant (AA) report (report about life insurance company's assets and liabilities) 
- Risk-based Capital (RBC) projection - industry review
''')

st.markdown('**ACTUARIAL OFFICER**, Chaoyang Life Insurance (Taipei),                 Aug15-Jun16')
st.markdown('**Actuarial role with focus on Actuarial Statistics**')
st.markdown('''
- Experience study review (analyze statistical data such as mortality, accident, sickness, disability and construct probability tables to forecast risk and liability for payment of future benefits) 
- Insurance pricing assumption setting 
- MG-ALFA actuarial models maintenance 
- Cash flow projection and testing for asset and liability modeling 
- Actuarial Assistant (AA) report (report about life insurance company's assets and liabilities) 
- Own Risk and Solvency Assessment (ORSA) report
''')

#####################
st.markdown('''
## EDUCATION
''')

st.markdown('MSc in **Statistics and Actuarial Science** ,Sep12-Jun14')
st.markdown('''
- `MSc in Feng Chia University (Taiwan)`
- Example of courses taken: Actuarial mathematics, Loss model, Credibility theory, Regression analysis, Time series analysis.
''')

st.markdown('BSc in **Applied Mathematics**, Sep08-Jun12')
st.markdown('''
- `National Kaohsiung Normal University (Taiwan)`
''')

#####################
st.markdown('''
## SKILLS
''')

st.markdown('''
##### Languages
''')
st.text('    - Mandarin (native speaker)')
st.text('    - English (IELTS 5.5)')
st.text('    - Thai (beginner)')

st.markdown('''
##### Programming
''')
st.text('    - Microsoft Power Platform (Power BI, Power Automate, Power Apps, Power Agent)')
st.text('    - Microsoft Dynamics 365')
st.text('    - AWS (RDS, Lambda, EC2, SageMaker, S3)')
st.text('    - Microsoft Dataverse')
st.text('    - Bubble.io')
st.text('    - Python')
st.text('    - SQL(MySQL, Oracle, MS SQL server)')
st.text('    - Microsoft Office (Excel, Power Point, Word)')
#st.text('    - Power BI')
st.text('    - Zapier')
st.text('    - Prophet')
st.text('    - MG-ALFA')
st.text('    - SAS Data Step')


#####################
st.markdown('''
## PROFESSIONAL CERTIFICATES
''')
st.markdown('''
##### Data science
''')
st.markdown('''
    - Practical Data Science Specialization by AWS (online) https://www.coursera.org/account/accomplishments/specialization/certificate/BJP2VR6HAF94
    - IBM Data Science Professional Certificate (online)  
    - Python for Everybody Specialization https://www.coursera.org/account/accomplishments/specialization/certificate/WFQVSP7W8R64
''')

st.markdown('''
##### Actuarial
''')
st.markdown('''
      - SOA Exam FM (financial mathematics)
      - SOA Exam P (probability)                                 
      - VEE Economics
      - VEE Corporate Finance
      - VEE Applied Statistics
''')
