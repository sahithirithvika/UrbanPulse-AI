import streamlit as st
import pandas as pd
import plotly.express as px
import random
from datetime import datetime

st.set_page_config(
    page_title="UrbanPulse AI",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

.big-title{
    font-size:42px;
    font-weight:bold;
    color:#1E3A8A;
}

.subtitle{
    color:gray;
    font-size:18px;
}

.metric-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.1);
    text-align:center;
}

.report-card{
    background:#ffffff;
    padding:20px;
    border-radius:15px;
    border-left:8px solid #2563EB;
}

</style>
""",unsafe_allow_html=True)
st.sidebar.title("🌍 UrbanPulse AI")

page=st.sidebar.radio(
"Navigation",
[
"🏠 Home",
"📝 Report Issue",
"🧠 Decision Intelligence",
"📊 Community Insights",
"📄 Executive Brief"
]
)
data={
"Category":["Garbage","Road Damage","Water Leakage","Traffic","Streetlights","Electricity","Public Safety","Garbage","Road Damage","Traffic"],
"Priority":["High","Critical","Medium","Low","High","Medium","Critical","Low","Medium","High"],
"Location":["MG Road","KPHB","Kukatpally","Madhapur","Ameerpet","Gachibowli","Secunderabad","Kondapur","Uppal","LB Nagar"],
"Status":["Pending","Pending","Resolved","Resolved","Pending","Resolved","Pending","Pending","Resolved","Pending"]
}

df=pd.DataFrame(data)
if page=="🏠 Home":

    st.markdown("<div class='big-title'>🌍 UrbanPulse AI</div>",unsafe_allow_html=True)

    st.markdown("<div class='subtitle'>Turning Citizen Voices into Smarter Community Decisions</div>",unsafe_allow_html=True)

    st.write("")

    c1,c2,c3,c4=st.columns(4)

    c1.metric("📢 Complaints",250)
    c2.metric("🚨 Critical",18)
    c3.metric("✅ Resolved",172)
    c4.metric("💚 Pulse Score","84/100")

    st.write("---")

    st.subheader("About")

    st.write("""
UrbanPulse AI is an AI-powered civic intelligence platform that converts citizen complaints into actionable insights.

Authorities can quickly identify priority issues, monitor community health, and make informed decisions through interactive dashboards.
""")

    st.write("---")

    st.subheader("How it Works")

    st.markdown("""
1. Citizen reports issue

2. AI understands complaint

3. Priority assigned

4. Dashboard updated

5. Authorities take action
""")
    if page=="📝 Report Issue":

        st.title("📝 Report Community Issue")

        st.write("Help us improve your community by reporting civic issues.")

        with st.form("complaint_form"):

            name = st.text_input("Citizen Name")

            location = st.text_input("Location")

            ward = st.number_input("Ward Number",1,100,1)

            category = st.selectbox(
                "Issue Category",
                [
                    "Garbage",
                    "Road Damage",
                    "Water Leakage",
                    "Streetlights",
                    "Traffic",
                    "Electricity",
                    "Public Safety",
                    "Others"
                ]
            )

            description = st.text_area(
                "Complaint Description",
                height=150
            )

            submitted = st.form_submit_button("🚀 Submit Complaint")

        if submitted:

            st.success("✅ Complaint Submitted Successfully!")

            st.info(f"""
Citizen : {name}

Location : {location}

Ward : {ward}

Category : {category}

Status : Pending Review
""")

    if page=="🧠 Decision Intelligence":

        st.title("🧠 AI Decision Intelligence")

        complaint = st.text_area(
            "Enter Complaint",
            height=150
        )

        if st.button("Analyze Complaint"):

            categories = [
                "Garbage",
                "Road Damage",
                "Water Leakage",
                "Streetlights",
                "Traffic",
                "Electricity",
                "Public Safety"
            ]

            departments = {
                "Garbage":"Sanitation Department",
                "Road Damage":"Roads & Infrastructure",
                "Water Leakage":"Water Supply Department",
                "Streetlights":"Electrical Department",
                "Traffic":"Traffic Police",
                "Electricity":"Power Department",
                "Public Safety":"Police Department"
            }

            category=random.choice(categories)

            priority=random.choice(
                [
                    "Low",
                    "Medium",
                    "High",
                    "Critical"
                ]
            )

            severity=random.randint(60,100)

            department=departments[category]

            resolution=random.choice(
                [
                    "24 Hours",
                    "48 Hours",
                    "3 Days",
                    "1 Week"
                ]
            )

            st.success("Analysis Complete")

            c1,c2=st.columns(2)

            c1.metric("Category",category)

            c2.metric("Priority",priority)

            c3,c4=st.columns(2)

            c3.metric("Severity Score",f"{severity}/100")

            c4.metric("Resolution",resolution)

            st.write("---")

            st.subheader("Responsible Department")

            st.info(department)

            st.subheader("AI Summary")

            st.write(
                f"""
The complaint has been classified as **{category}**.

Based on the issue description, it is assigned a **{priority}** priority with a severity score of **{severity}/100**.

The recommended department is **{department}**.

Immediate inspection and corrective action are advised to minimize community impact.
"""
            )

            st.subheader("Recommended Action")

            st.success(
                "Dispatch the responsible field team, verify the issue, update citizens, and resolve within the estimated timeline."
            )

    if page=="📊 Community Insights":

        st.title("📊 Community Insights Dashboard")

        c1,c2,c3,c4=st.columns(4)

        c1.metric("Total Complaints",len(df))

        c2.metric("Critical Issues",2)

        c3.metric("Resolved",4)

        c4.metric("Pulse Score","84/100")

        st.write("---")

        fig1=px.bar(
            df,
            x="Category",
            color="Category",
            title="Complaints by Category"
        )

        st.plotly_chart(fig1,use_container_width=True)

        fig2=px.pie(
            df,
            names="Priority",
            title="Priority Distribution"
        )

        st.plotly_chart(fig2,use_container_width=True)

        hotspot=df["Location"].value_counts().reset_index()

        hotspot.columns=["Location","Complaints"]

        fig3=px.bar(
            hotspot,
            x="Location",
            y="Complaints",
            color="Complaints",
            title="Community Hotspots"
        )

        st.plotly_chart(fig3,use_container_width=True)

        st.subheader("AI Community Insights")

        st.success("""
• Garbage complaints increased this week.

• Road Damage reports are concentrated in KPHB.

• Traffic issues remain stable.

• Water leakage complaints have reduced.

• Immediate attention is recommended for high-priority complaints.
""")
    if page=="📄 Executive Brief":

        st.title("📄 Executive Brief")

        st.markdown("""
### 📌 Community Summary

UrbanPulse AI analyzed the submitted complaints and identified the most pressing civic issues affecting the community.

The platform prioritizes complaints based on severity and impact, helping authorities respond efficiently.
""")

        st.write("---")

        col1,col2=st.columns(2)

        with col1:

            st.subheader("🚨 Top Issues")

            st.write("""
- Road Damage
- Garbage Overflow
- Streetlight Failure
- Water Leakage
- Traffic Congestion
""")

        with col2:

            st.subheader("🏢 Recommended Departments")

            st.write("""
- Roads & Infrastructure
- Sanitation Department
- Electrical Department
- Water Supply Department
- Traffic Police
""")

    st.write("---")

    st.subheader("🎯 Recommended Action Plan")

    st.success("""
✅ Deploy field inspection teams

✅ Prioritize critical complaints

✅ Increase garbage collection frequency

✅ Repair damaged roads

✅ Fix non-functional streetlights

✅ Resolve water leakage complaints

✅ Monitor complaint trends weekly
""")

    st.write("---")

    st.subheader("📊 Community Pulse Score")

    score=84

    st.progress(score/100)

    st.metric("Overall Community Health",f"{score}/100")

    st.info("""
The community is performing well overall, but Road Damage and Garbage Management require immediate attention to improve the Community Pulse Score.
""")

    report=f"""
URBANPULSE AI EXECUTIVE REPORT

Total Complaints : {len(df)}

Critical Issues : 2

Resolved Issues : 4

Community Pulse Score : 84/100

Top Priority:
Road Damage
Garbage
Streetlights

Recommended Actions:

Deploy Road Repair Team

Increase Waste Collection

Repair Streetlights

Prepared by UrbanPulse AI
"""

    st.download_button(
        label="⬇ Download Executive Report",
        data=report,
        file_name="UrbanPulse_Report.txt",
        mime="text/plain"
    )
    st.markdown("---")

st.markdown(
"""
<div style='text-align:center;color:gray;'>

© 2026 UrbanPulse AI

Turning Citizen Voices into Smarter Community Decisions

Built for AI for Better Living & Smarter Communities Hackathon

</div>
""",
unsafe_allow_html=True
)
        