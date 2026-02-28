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

# رابط شعار منصة مدرستي (رابط رسمي أو موثوق)
MADRASATI_LOGO = "https://schools.madrasati.sa/img/madrasati-logo.png"

# تطبيق CSS احترافي بألوان قوية وجذابة وتصميم عصري
st.markdown(f"""
    <style>
        /* إعدادات الاتجاه العام */
        [data-testid="stAppViewContainer"], [data-testid="stSidebar"], .main {{
            direction: rtl;
            text-align: right;
        }}
        
        /* ألوان خلفية قوية وجذابة */
        .stApp {{
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }}
        
        /* تنسيق الهيدر والشعار */
        .header-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
            background: white;
            border-radius: 20px;
            box-shadow: 0 10px 25px rgba(107, 70, 193, 0.1);
            margin-bottom: 30px;
            border-bottom: 5px solid #6B46C1;
        }}
        
        .logo-img {{
            max-width: 180px;
            margin-bottom: 15px;
        }}
        
        h1 {{
            color: #4C51BF; /* بنفسجي قوي */
            text-align: center;
            font-weight: 800;
            font-size: calc(2rem + 1.5vw);
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }}
        
        /* تنسيق البطاقات بألوان فاتحة وجذابة */
        .info-card {{
            background: white;
            padding: 2rem;
            border-radius: 20px;
            border: none;
            margin-bottom: 1.5rem;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
            border-top: 5px solid #9F7AEA;
        }}
        
        .info-card:hover {{
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(107, 70, 193, 0.15);
        }}
        
        /* أزرار روابط قوية */
        .custom-link {{
            display: block;
            background: linear-gradient(90deg, #6B46C1 0%, #805AD5 100%);
            color: white !important;
            padding: 15px;
            text-decoration: none !important;
            border-radius: 12px;
            text-align: center;
            margin: 10px 0;
            font-weight: 600;
            font-size: 1.1rem;
            transition: 0.3s;
            box-shadow: 0 4px 15px rgba(107, 70, 193, 0.3);
        }}
        
        .custom-link:hover {{
            transform: scale(1.02);
            box-shadow: 0 6px 20px rgba(107, 70, 193, 0.4);
        }}
        
        /* رسائل التحفيز بلون وردي جذاب */
        .motivation-box {{
            background: linear-gradient(135deg, #FFF5F7 0%, #FED7E2 100%);
            color: #9B2C2C;
            padding: 25px;
            border-radius: 20px;
            border-right: 8px solid #F687B3;
            text-align: center;
            font-size: 1.3rem;
            font-weight: 600;
            margin: 25px 0;
            box-shadow: 0 5px 15px rgba(246, 135, 179, 0.2);
        }}

        /* تذييل الصفحة باسم الطالبة */
        .footer {{
            text-align: center;
            padding: 30px;
            margin-top: 50px;
            background: white;
            border-radius: 20px 20px 0 0;
            box-shadow: 0 -5px 20px rgba(0,0,0,0.05);
            border-top: 3px solid #6B46C1;
        }}
        
        .footer p {{
            color: #4A5568;
            font-weight: 600;
            margin: 5px 0;
        }}

        /* تنسيق الجداول */
        .stTable {{
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }}
    </style>
""", unsafe_allow_html=True)

# الهيدر والشعار
st.markdown(f"""
    <div class="header-container">
        <img src="{MADRASATI_LOGO}" class="logo-img" alt="شعار مدرستي">
        <h1>منصة الطالب الذكي</h1>
    </div>
""", unsafe_allow_html=True)

# شريط التنقل الجانبي
st.sidebar.markdown("<h2 style='text-align: center; color: #6B46C1;'>📌 التنقل</h2>", unsafe_allow_html=True)
page = st.sidebar.radio(
    "انتقلي إلى القسم المطلوب:",
    ["🏠 الصفحة الرئيسية", "📅 الجدول الدراسي", "🔗 الروابط التعليمية", "💡 نصائح وإلهام"]
)

# ============ الصفحة الرئيسية ============
if page == "🏠 الصفحة الرئيسية":
    st.markdown("<h2 style='text-align: center;'>مرحباً بكِ في مساحتكِ الإبداعية</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='info-card'>
            <h3 style='text-align: center;'>📚 التعليم</h3>
            <p style='text-align: center;'>استكشفي عالم المعرفة وطوري مهاراتكِ الرقمية</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class='info-card'>
            <h3 style='text-align: center;'>⏰ التنظيم</h3>
            <p style='text-align: center;'>نظمي وقتكِ ومهامكِ الدراسية بكل سهولة ويسر</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class='info-card'>
            <h3 style='text-align: center;'>🏆 النجاح</h3>
            <p style='text-align: center;'>حققي أهدافكِ وطموحاتكِ لتكوني فخراً لوطنكِ</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # معلومات سريعة جذابة
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info(f"📅 اليوم: {datetime.now().strftime('%A')}")
    with c2:
        st.success(f"⏰ الوقت: {datetime.now().strftime('%H:%M')}")
    with c3:
        st.warning("🎯 المستوى: الثاني متوسط")

# ============ الجدول الدراسي ============
elif page == "📅 الجدول الدراسي":
    st.markdown("<h2 style='text-align: center;'>📅 جدولكِ الدراسي الأسبوعي</h2>", unsafe_allow_html=True)
    
    schedule_data = {
        "الحصة": ["الأولى", "الثانية", "الثالثة", "الرابعة"],
        "الأحد": ["الرياضيات", "العلوم", "اللغة العربية", "اللغة الإنجليزية"],
        "الاثنين": ["اللغة الإنجليزية", "الرياضيات", "العلوم", "الدراسات الاجتماعية"],
        "الثلاثاء": ["الدراسات الاجتماعية", "اللغة العربية", "الرياضيات", "التربية الإسلامية"],
        "الأربعاء": ["التربية الإسلامية", "المهارات الرقمية", "الدراسات الاجتماعية", "الرياضيات"],
        "الخميس": ["العلوم", "الرياضيات", "اللغة العربية", "التربية الفنية"]
    }
    
    st.table(schedule_data)
    
    st.markdown("---")
    st.markdown("<h3>📝 مفكرة المهام السريعة</h3>", unsafe_allow_html=True)
    t_name = st.text_input("ما هي المهمة التي تودين إنجازها اليوم؟")
    if st.button("إضافة للمفكرة"):
        if t_name: st.balloons(); st.success(f"رائع يا رنيم! تمت إضافة: {t_name}")

# ============ الروابط التعليمية ============
elif page == "🔗 الروابط التعليمية":
    st.markdown("<h2 style='text-align: center;'>🔗 روابط تعليمية هامة</h2>", unsafe_allow_html=True)
    
    links = {
        "📱 منصة مدرستي": "https://schools.madrasati.sa",
        "📺 قناة عين التعليمية": "https://www.einarabic.com",
        "🌐 بوابة عين الإثرائية": "https://ien.edu.sa",
        "📖 موقع حلول التعليمي": "https://hulul.online",
        "🎓 منصة إدراك": "https://www.edraak.org"
    }
    
    for name, url in links.items():
        st.markdown(f"<a href='{url}' class='custom-link' target='_blank'>{name}</a>", unsafe_allow_html=True)

# ============ نصائح وإلهام ============
elif page == "💡 نصائح وإلهام":
    st.markdown("<h2 style='text-align: center;'>🌟 كلمات ملهمة لكِ</h2>", unsafe_allow_html=True)
    
    motivations = [
        "رنيم.. أنتِ قادرة على تحقيق المستحيل بإصراركِ وعزيمتكِ!",
        "كل يوم تدرسين فيه هو خطوة نحو مستقبلكِ المشرق بإذن الله.",
        "العلم هو السلاح الأقوى لتغيير العالم.. استمري في الإبداع.",
        "ثقي بنفسكِ وبقدراتكِ، فأنتِ نجمة في سماء التميز.",
        "النجاح هو مجموع خطوات صغيرة تتكرر كل يوم.. لا تتوقفي!"
    ]
    
    st.markdown(f"<div class='motivation-box'>{random.choice(motivations)}</div>", unsafe_allow_html=True)
    
    tips = [
        ("🎯 حددي أهدافكِ", "اكتبي ما تودين تحقيقه كل صباح لتكوني أكثر تركيزاً."),
        ("🧘 استرخي قليلاً", "الراحة بين المذاكرة تجدد نشاط عقلكِ وتزيد من استيعابكِ."),
        ("💧 حافظي على صحتكِ", "شرب الماء والغذاء الصحي هما وقود عقلكِ المبدع.")
    ]
    
    for title, desc in tips:
        st.markdown(f"""
        <div class='info-card'>
            <h4 style='color: #6B46C1;'>{title}</h4>
            <p style='text-align: center;'>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# التذييل الاحترافي باسم الطالبة
st.markdown(f"""
    <div class="footer">
        <p>🎓 منصة الطالب الذكي © 2025</p>
        <p>تم تطويرها بواسطة المبدعة: <span style="color: #6B46C1; font-size: 1.2rem;">رنيم محمد الزبيدي</span></p>
        <p style="font-size: 0.8rem; color: #A0AEC0;">مشروع مسابقة البرمجة الرقمية - الصف الثاني متوسط</p>
    </div>
""", unsafe_allow_html=True)
