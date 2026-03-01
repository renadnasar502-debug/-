import streamlit as st
from datetime import datetime
import random

# إعدادات الصفحة
st.set_page_config(
    page_title="منصة الطالب الذكي - رنيم محمد الزبيدي",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# رابط شعار منصة مدرستي الموثوق
MADRASATI_LOGO = "https://www.moe.gov.sa/ar/education/general-education/PublishingImages/madrasati.png"

# تطبيق CSS احترافي بألوان فاتحة وقوية وواضحة
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap' );
        [data-testid="stAppViewContainer"], [data-testid="stSidebar"], .main {{
            direction: rtl;
            text-align: right;
            font-family: 'Cairo', sans-serif;
        }}
        .stApp {{ background-color: #F7FAFC; }}
        .header-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 40px;
            background: #FFFFFF;
            border-radius: 30px;
            box-shadow: 0 10px 30px rgba(107, 70, 193, 0.1);
            margin-bottom: 40px;
            border-bottom: 8px solid #6B46C1;
        }}
        .logo-img {{ max-width: 280px; margin-bottom: 20px; }}
        h1 {{ color: #4C51BF; font-weight: 900; font-size: calc(2.5rem + 1.5vw); margin: 10px 0; }}
        .info-card {{
            background: #FFFFFF;
            padding: 30px;
            border-radius: 25px;
            margin-bottom: 25px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
            border-top: 6px solid #9F7AEA;
        }}
        .stTable {{ background-color: white; border-radius: 20px; overflow: hidden; }}
        thead tr th {{ background-color: #6B46C1 !important; color: white !important; font-weight: 900 !important; text-align: center !important; }}
        tbody tr td {{ text-align: center !important; font-weight: 600 !important; color: #2D3748 !important; }}
        .custom-link {{
            display: block;
            background: linear-gradient(90deg, #6B46C1 0%, #805AD5 100%);
            color: white !important;
            padding: 20px;
            text-decoration: none !important;
            border-radius: 18px;
            text-align: center;
            margin: 15px 0;
            font-weight: 700;
            font-size: 1.3rem;
        }}
        .motivation-box {{
            background: #FAF5FF;
            color: #553C9A;
            padding: 35px;
            border-radius: 25px;
            border-right: 12px solid #B794F4;
            text-align: center;
            font-size: 1.6rem;
            font-weight: 800;
            margin: 35px 0;
        }}
        .footer {{
            text-align: center;
            padding: 50px;
            margin-top: 80px;
            background: white;
            border-radius: 40px 40px 0 0;
            border-top: 5px solid #6B46C1;
        }}
    </style>
""", unsafe_allow_html=True)

# الهيدر والشعار
st.markdown(f"""
    <div class="header-container">
        <img src="{MADRASATI_LOGO}" class="logo-img" onerror="this.src='https://www.moe.gov.sa/ar/education/general-education/PublishingImages/madrasati.png'" alt="منصة مدرستي">
        <h2 style="margin-bottom: 5px; text-align: center;">المدرسة الخامسة والثمانون المتوسطة</h2>
        <h3 style="color: #805AD5; margin-top: 0; text-align: center;">وزارة التعليم - المملكة العربية السعودية</h3>
        <h1>منصة الطالب الذكي</h1>
    </div>
""", unsafe_allow_html=True )

# شريط التنقل الجانبي
st.sidebar.markdown("<h2 style='text-align: center; color: #6B46C1;'>📌 القائمة</h2>", unsafe_allow_html=True)
page = st.sidebar.radio("اختاري القسم:", ["🏠 الرئيسية", "📅 الجدول الدراسي", "🔗 روابط تعليمية", "💡 نصائح وإلهام"])

# ============ الصفحة الرئيسية ============
if page == "🏠 الرئيسية":
    st.markdown("<h2 style='text-align: center;'>مرحباً بكِ يا رنيم في مدرستكِ الرقمية</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown("<div class='info-card'><h3 style='text-align: center;'>📚 التعليم</h3><p style='text-align: center;'>دروسكِ ومصادركِ التعليمية في مكان واحد</p></div>", unsafe_allow_html=True)
    with col2: st.markdown("<div class='info-card'><h3 style='text-align: center;'>⏰ التنظيم</h3><p style='text-align: center;'>نظمي وقتكِ الدراسي وحققي أهدافكِ اليومية</p></div>", unsafe_allow_html=True)
    with col3: st.markdown("<div class='info-card'><h3 style='text-align: center;'>🏆 التميز</h3><p style='text-align: center;'>كوني الطالبة المتميزة التي تفتخر بها المدرسة</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1: st.info(f"📅 اليوم: {datetime.now().strftime('%A')}")
    with c2: st.success(f"⏰ الوقت: {datetime.now().strftime('%H:%M')}")
    with c3: st.warning("🎯 الصف: الثاني متوسط")

# ============ الجدول الدراسي ============
elif page == "📅 الجدول الدراسي":
    st.markdown("<h2 style='text-align: center;'>📅 الجدول الدراسي للمرحلة المتوسطة</h2>", unsafe_allow_html=True)
    schedule_data = {
        "الحصة": ["الأولى", "الثانية", "الثالثة", "الرابعة", "الخامسة", "السادسة"],
        "الأحد": ["لغتي الخالدة", "الرياضيات", "العلوم", "الدراسات الإسلامية", "التربية البدنية", "المهارات الرقمية"],
        "الاثنين": ["الرياضيات", "العلوم", "اللغة الإنجليزية", "الدراسات الاجتماعية", "التفكير الناقد", "لغتي الخالدة"],
        "الثلاثاء": ["العلوم", "الرياضيات", "الدراسات الإسلامية", "المهارات الحياتية", "لغتي الخالدة", "اللغة الإنجليزية"],
        "الأربعاء": ["لغتي الخالدة", "الرياضيات", "العلوم", "الدراسات الإسلامية", "اللغة الإنجليزية", "التربية الفنية"],
        "الخميس": ["الرياضيات", "العلوم", "لغتي الخالدة", "الدراسات الاجتماعية", "اللغة الإنجليزية", "المهارات الرقمية"]
    }
    st.table(schedule_data)
    st.markdown("---")
    t_name = st.text_input("ما هي المهمة التي تودين إنجازها اليوم؟")
    if st.button("إضافة للمفكرة"):
        if t_name: st.balloons(); st.success(f"رائع يا رنيم! تمت إضافة: {t_name}")

# ============ الروابط التعليمية ============
elif page == "🔗 روابط تعليمية":
    st.markdown("<h2 style='text-align: center;'>🔗 روابط تعليمية هامة</h2>", unsafe_allow_html=True)
    links = { "📱 منصة مدرستي الرسمية": "https://schools.madrasati.sa", "📺 قناة عين التعليمية": "https://www.youtube.com/user/ien_channel", "🌐 بوابة عين الإثرائية": "https://ien.edu.sa", "📖 موقع حلول التعليمي": "https://hulul.online" }
    for name, url in links.items( ): st.markdown(f"<a href='{url}' class='custom-link' target='_blank'>{name}</a>", unsafe_allow_html=True)

# ============ نصائح وإلهام ============
elif page == "💡 نصائح وإلهام":
    st.markdown("<h2 style='text-align: center;'>🌟 كلمات محفزة لكِ يا رنيم</h2>", unsafe_allow_html=True)
    motivations = ["رنيم.. طالبة المدرسة 85 المبدعة، مستقبلكِ مشرق!", "كل يوم تدرسين فيه هو خطوة نحو القمة.", "العلم هو السلاح الأقوى لتغيير العالم.", "ثقي بنفسكِ، فأنتِ نجمة في سماء الإبداع."]
    st.markdown(f"<div class='motivation-box'>{random.choice(motivations)}</div>", unsafe_allow_html=True)
    tips = [("🎯 ركزي في حصصكِ", "الاستماع الجيد للمعلمة يوفر عليكِ الوقت."), ("🧘 نظمي وقتكِ", "اجعلي لكل مادة وقتاً وخذي فترات راحة."), ("💧 اهتمي بصحتكِ", "الغذاء الصحي والنوم المبكر وقود عقلكِ.")]
    for title, desc in tips: st.markdown(f"<div class='info-card'><h4 style='color: #6B46C1; text-align: center;'>{title}</h4><p style='text-align: center;'>{desc}</p></div>", unsafe_allow_html=True)

# التذييل
st.markdown(f"""
    <div class="footer">
        <p>🎓 منصة الطالب الذكي © 2025</p>
        <p>المدرسة الخامسة والثمانون المتوسطة</p>
        <p>تم تطويرها بكل فخر بواسطة المبدعة: <span style="color: #6B46C1; font-size: 1.5rem;">رنيم محمد الزبيدي</span></p>
        <p style="font-size: 1rem; color: #718096;">مشروع مسابقة البرمجة الرقمية - الصف الثاني متوسط</p>
    </div>
""", unsafe_allow_html=True)
