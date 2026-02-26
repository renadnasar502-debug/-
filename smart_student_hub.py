import streamlit as st
from datetime import datetime
import random

# إعدادات الصفحة
st.set_page_config(
    page_title="منصة الطالب الذكي",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تطبيق CSS احترافي للألوان الجميلة والتوافق مع الجوال
st.markdown("""
    <style>
        /* إعدادات الاتجاه العام */
        [data-testid="stAppViewContainer"], [data-testid="stSidebar"], .main {
            direction: rtl;
            text-align: right;
        }
        
        /* ألوان الخلفية الجميلة (تدرج هادئ) */
        .stApp {
            background: linear-gradient(to bottom, #fdfbfb 0%, #ebedee 100%);
        }
        
        /* تنسيق العنوان الرئيسي */
        h1 {
            color: #6B46C1; /* بنفسجي جميل */
            text-align: center;
            font-weight: 700;
            padding: 20px 0;
            font-size: calc(1.5rem + 1.5vw); /* حجم خط مرن يناسب الجوال والكمبيوتر */
        }
        
        /* تنسيق العناوين الفرعية */
        h2, h3 {
            color: #805AD5;
            text-align: center;
            margin-top: 15px;
        }
        
        /* بطاقات المعلومات (مرنة وتناسب الجوال) */
        .info-card {
            background-color: white;
            padding: 1.5rem;
            border-radius: 15px;
            border: 1px solid #E9D8FD;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(107, 70, 193, 0.05);
            transition: transform 0.2s;
        }
        
        .info-card:hover {
            transform: translateY(-5px);
            border-color: #B794F4;
        }
        
        /* تنسيق الروابط كأزرار أنيقة */
        .custom-link {
            display: block;
            background-color: #9F7AEA;
            color: white !important;
            padding: 12px;
            text-decoration: none !important;
            border-radius: 10px;
            text-align: center;
            margin: 8px 0;
            font-weight: 500;
            transition: 0.3s;
        }
        
        .custom-link:hover {
            background-color: #805AD5;
            box-shadow: 0 4px 12px rgba(128, 90, 213, 0.3);
        }
        
        /* تحسين مظهر القائمة الجانبية */
        [data-testid="stSidebar"] {
            background-color: #FAF5FF;
            border-left: 2px solid #E9D8FD;
        }
        
        /* جعل الجداول متوافقة مع الجوال */
        .stTable {
            overflow-x: auto;
            display: block;
        }
        
        /* تنسيق رسائل التحفيز */
        .motivation-box {
            background-color: #FFF5F7; /* وردي هادئ */
            color: #9B2C2C;
            padding: 20px;
            border-radius: 15px;
            border-right: 5px solid #F687B3;
            text-align: center;
            font-size: 1.1rem;
            margin: 20px 0;
        }

        /* تعديل المسافات لتناسب الجوال */
        @media (max-width: 768px) {
            .main .block-container {
                padding: 1rem;
            }
            h1 {
                font-size: 1.8rem;
            }
        }
    </style>
""", unsafe_allow_html=True)

# شريط التنقل الجانبي
st.sidebar.markdown("<h2 style='text-align: center; color: #6B46C1;'>القائمة</h2>", unsafe_allow_html=True)
page = st.sidebar.radio(
    "انتقلي إلى:",
    ["🏠 الرئيسية", "📅 الجدول الدراسي", "🔗 روابط مفيدة", "💡 نصائح دراسية"]
)

# ============ الصفحة الرئيسية ============
if page == "🏠 الرئيسية":
    st.markdown("<h1>منصة الطالب الذكي</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #718096;'>مرحباً بكِ في مساحتكِ الخاصة للتنظيم والإبداع</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # استخدام columns التي تتحول تلقائياً لصفوف في الجوال
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown("""
        <div class='info-card'>
            <h3>التعليم</h3>
            <p style='text-align: center;'>مصادر تعليمية متنوعة لتطوير مهاراتكِ</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class='info-card'>
            <h3>التنظيم</h3>
            <p style='text-align: center;'>نظمي مهامكِ الدراسية بكل سهولة</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class='info-card'>
            <h3>النجاح</h3>
            <p style='text-align: center;'>حققي أهدافكِ الدراسية بذكاء</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # معلومات سريعة
    c1, c2 = st.columns(2)
    with c1:
        st.info(f"📅 اليوم: {datetime.now().strftime('%A')}")
    with c2:
        st.success(f"⏰ الوقت: {datetime.now().strftime('%H:%M')}")

# ============ الجدول الدراسي ============
elif page == "📅 الجدول الدراسي":
    st.markdown("<h1>جدولكِ الدراسي</h1>", unsafe_allow_html=True)
    
    schedule_data = {
        "الحصة": ["1", "2", "3", "4"],
        "الأحد": ["رياضيات", "علوم", "عربي", "إنجليزي"],
        "الاثنين": ["إنجليزي", "رياضيات", "علوم", "دراسات"],
        "الثلاثاء": ["دراسات", "عربي", "رياضيات", "دين"],
        "الأربعاء": ["دين", "حاسب", "دراسات", "رياضيات"],
        "الخميس": ["علوم", "رياضيات", "عربي", "فنية"]
    }
    
    st.table(schedule_data)
    
    st.markdown("---")
    st.markdown("<h3>إضافة مهمة جديدة</h3>", unsafe_allow_html=True)
    t_name = st.text_input("اسم المهمة:")
    if st.button("حفظ المهمة"):
        if t_name: st.success(f"تم حفظ المهمة: {t_name}")

# ============ الروابط المفيدة ============
elif page == "🔗 روابط مفيدة":
    st.markdown("<h1>روابط تهمكِ</h1>", unsafe_allow_html=True)
    
    links = {
        "منصة مدرستي": "https://schools.madrasati.sa",
        "قناة عين التعليمية": "https://www.einarabic.com",
        "بوابة عين": "https://ien.edu.sa",
        "موقع حلول": "https://hulul.online"
    }
    
    for name, url in links.items():
        st.markdown(f"<a href='{url}' class='custom-link' target='_blank'>{name}</a>", unsafe_allow_html=True)

# ============ نصائح دراسية ============
elif page == "💡 نصائح دراسية":
    st.markdown("<h1>نصائح وإلهام</h1>", unsafe_allow_html=True)
    
    motivations = [
        "أنتِ قادرة على تحقيق المستحيل بإصراركِ",
        "كل خطوة صغيرة تقربكِ من حلمكِ الكبير",
        "العلم نور يضيء لكِ دروب المستقبل",
        "ثقي بنفسكِ، فأنتِ مبدعة ومتميزة"
    ]
    
    st.markdown(f"<div class='motivation-box'>{random.choice(motivations)}</div>", unsafe_allow_html=True)
    
    tips = [
        ("نظمي وقتكِ", "خصصي وقتاً لكل مادة وخذي فترات راحة"),
        ("اختاري مكاناً هادئاً", "الهدوء يساعد على التركيز وسرعة الفهم"),
        ("اشربي الماء", "الماء ينشط الذاكرة ويحافظ على حيويتكِ")
    ]
    
    for title, desc in tips:
        st.markdown(f"""
        <div class='info-card'>
            <h4>{title}</h4>
            <p style='text-align: center;'>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# التذييل
st.markdown("---")
st.markdown("<p style='text-align: center; color: #A0AEC0; font-size: 0.8rem;'>منصة الطالب الذكي © 2025 | تم تطويرها بواسطة طالبة مبدعة</p>", unsafe_allow_html=True)
