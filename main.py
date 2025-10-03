# flashy_mid_autumn.py
import streamlit as st
from datetime import datetime
import uuid

st.set_page_config(
    page_title="🌕 Mid-Autumn Festival — Flashy Edition",
    page_icon="🌕",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- App state ----------
if "wishes" not in st.session_state:
    st.session_state.wishes = []
if "gallery" not in st.session_state:
    st.session_state.gallery = []

# ---- Next Mid-Autumn date (you can change this next year) ----
FESTIVAL_DT = datetime(2025, 10, 6)  # 2025-10-06 (15th day of 8th lunar month)
days_to_go = (FESTIVAL_DT.date() - datetime.now().date()).days
is_today = days_to_go == 0

# ---------- Global CSS & Fonts ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;800&family=Plus+Jakarta+Sans:wght@400;600&display=swap');

:root{
  --gold:#FFEAA6;
  --amber:#ffb24d;
  --ink:#0a0d1a;
  --sky1:#1b223b;
  --sky2:#0b0f21;
}

html, body, [data-testid="stAppViewContainer"]{
  background: radial-gradient(1200px 600px at 50% -20%, var(--sky1), var(--sky2) 60%, var(--ink) 100%) !important;
  color: #eaeaf2;
  font-family: "Plus Jakarta Sans", system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
}

/* Sticky top nav */
.top-nav{
  position: sticky; top: 0; z-index: 9999;
  backdrop-filter: blur(8px);
  background: rgba(3,5,12,.35);
  border-bottom: 1px solid rgba(255,255,255,.08);
  padding: 10px 12px; border-radius: 0 0 12px 12px;
}
.top-nav a{
  color: var(--gold) !important; text-decoration:none; margin-right: 18px;
  font-weight:600;
}
.top-nav a:hover{ text-decoration: underline }

/* Section headers */
.section h2{
  font-family: "Playfair Display", serif;
  font-weight: 800;
  color: var(--gold);
  text-shadow: 0 10px 38px rgba(0,0,0,.55);
  margin: 8px 0 14px 0;
  font-size: clamp(24px, 3.2vw, 40px);
}

/* Glass cards */
.glass{
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 16px;
  backdrop-filter: blur(8px);
  padding: 16px;
  box-shadow: 0 18px 48px rgba(0,0,0,.35);
}

/* Nice inputs/buttons */
input, textarea{
  border-radius: 12px !important;
}
button[kind="secondary"]{
  border-radius: 12px !important;
}

/* Make headings prettier */
h1, .hero-title h1{ font-family: "Playfair Display", serif; }

/* Reduce default container padding a bit */
.block-container{ padding-top: 0 !important; }
</style>
""", unsafe_allow_html=True)

# ---------- Sticky NAV ----------
st.markdown("""
<div class="top-nav">
  <a href="#hero">Hero</a>
  <a href="#legend">Legend</a>
  <a href="#gallery">Gallery</a>
  <a href="#wishes">Lantern Wishes</a>
  <a href="#recipes">Mooncakes</a>
  <a href="#countdown">Countdown</a>
</div>
""", unsafe_allow_html=True)

# ---------- HERO (full canvas, ornate) ----------
# hero_html = f"""
# <div id="hero"></div>
# <div style="position:relative;width:100%;height:72vh;max-height:840px;overflow:hidden;border-radius:18px;box-shadow:0 30px 80px rgba(0,0,0,.55)">
#   <!-- Stars (animated) -->
#   <div style="
#     position:absolute;inset:0;pointer-events:none;
#     background-image:
#       radial-gradient(1px 1px at 10% 20%, rgba(255,255,255,.8) 48%, transparent 51%),
#       radial-gradient(1.2px 1.2px at 30% 80%, rgba(255,255,255,.7) 48%, transparent 51%),
#       radial-gradient(1.5px 1.5px at 70% 35%, rgba(255,255,255,.8) 48%, transparent 51%),
#       radial-gradient(1px 1px at 85% 60%, rgba(255,255,255,.9) 48%, transparent 51%);
#     background-repeat:no-repeat; animation: twinkle 7s ease-in-out infinite;
#   "></div>

#   <style>
#   @keyframes twinkle{{0%,100%{{opacity:.7}}50%{{opacity:1}}}}
#   @keyframes moonGlow{{from{{filter:saturate(.95) brightness(.95) drop-shadow(0 0 22px #ffd98a)}}to{{filter:saturate(1.15) brightness(1.05) drop-shadow(0 0 36px #ffd98a)}}}}
#   @keyframes sway{{from{{transform:rotate(-6deg)}}to{{transform:rotate(5deg)}}}}
#   @keyframes drift{{from{{background-position:0 0}}to{{background-position:1200px 0}}}}
#   @keyframes drift2{{from{{background-position:0 0}}to{{background-position:900px 0}}}}
#   </style>

#   <!-- Glowing moon -->
#   <div style="
#     position:absolute;top:9%;left:50%;transform:translateX(-50%);
#     width:min(28vmax,300px); aspect-ratio:1/1; border-radius:50%;
#     background: radial-gradient(60% 60% at 45% 40%, #fff6d3 0%, #ffeaa6 35%, #ffd56b 60%, #f2b85a 75%, #e7a64f 100%);
#     animation: moonGlow 5s ease-in-out infinite alternate;
#   "></div>

#   <!-- Parallax clouds -->
#   <div style="
#     position:absolute;inset:0;bottom:-30px;opacity:.75;pointer-events:none;
#     background-repeat:repeat-x;background-size:1200px 300px;animation:drift 70s linear infinite;
#     background-image:url('data:image/svg+xml;utf8,\
#     <svg xmlns=\\\"http://www.w3.org/2000/svg\\\" width=\\\"1200\\\" height=\\\"300\\\" viewBox=\\\"0 0 1200 300\\\">\
#       <defs><linearGradient id=\\\"cg\\\" x1=\\\"0\\\" x2=\\\"0\\\" y1=\\\"0\\\" y2=\\\"1\\\">\
#         <stop offset=\\\"0%\\\" stop-color=\\\"#ffffff\\\" stop-opacity=\\\"0.7\\\"/>\
#         <stop offset=\\\"100%\\\" stop-color=\\\"#d7e7ff\\\" stop-opacity=\\\"0.0\\\"/>\
#       </linearGradient></defs>\
#       <g fill=\\\"url(#cg)\\\">\
#         <ellipse cx=\\\"120\\\" cy=\\\"120\\\" rx=\\\"120\\\" ry=\\\"55\\\"/>\
#         <ellipse cx=\\\"260\\\" cy=\\\"135\\\" rx=\\\"140\\\" ry=\\\"60\\\"/>\
#         <ellipse cx=\\\"420\\\" cy=\\\"120\\\" rx=\\\"110\\\" ry=\\\"50\\\"/>\
#         <ellipse cx=\\\"600\\\" cy=\\\"140\\\" rx=\\\"160\\\" ry=\\\"70\\\"/>\
#         <ellipse cx=\\\"820\\\" cy=\\\"125\\\" rx=\\\"140\\\" ry=\\\"60\\\"/>\
#         <ellipse cx=\\\"1020\\\" cy=\\\"130\\\" rx=\\\"160\\\" ry=\\\"70\\\"/>\
#       </g></svg>');
#   "></div>
#   <div style="
#     position:absolute;inset:0;bottom:-6px;opacity:.55;pointer-events:none;
#     background-repeat:repeat-x;background-size:900px 240px;animation:drift2 95s linear infinite reverse;
#     background-image:inherit;
#   "></div>

#   <!-- Ornate swinging lanterns (SVG) -->
#   {"".join([
#     f'''<svg viewBox="0 0 72 120" style="position:absolute;top:56%;left:{x}%;width:74px;height:120px;transform-origin:top center;animation:sway {dur}s ease-in-out {delay}s infinite alternate;filter:drop-shadow(0 0 18px rgba(255,180,80,.55));">
#           <line x1="36" y1="0" x2="36" y2="10" stroke="#b05816" stroke-width="4"/>
#           <rect x="10" y="10" rx="14" width="52" height="70" fill="url(#g{i})" stroke="#b05816" stroke-width="3"/>
#           <rect x="22" y="82" rx="2" width="28" height="8" fill="#b05816"/>
#           <line x1="36" y1="90" x2="36" y2="112" stroke="#b05816" stroke-width="3"/>
#           <path d="M36 112 l-6 8 h12 z" fill="#e6792e"/>
#           <defs><linearGradient id="g{i}" x1="0" y1="0" x2="0" y2="1">
#              <stop offset="0%" stop-color="#ffd37c"/><stop offset="60%" stop-color="#ff9f45"/><stop offset="100%" stop-color="#e6792e"/>
#           </linearGradient></defs>
#         </svg>'''
#     for i, (x, dur, delay) in enumerate([(12,3.6,.2),(28,3.2,.5),(46,3.9,.1),(66,3.4,.8),(82,3.7,.3)], start=1)
#   ])}

#   <!-- Title -->
#   <div class="hero-title" style="position:absolute;top:48%;left:50%;transform:translate(-50%,-50%);text-align:center;">
#     <h1 style="font-size:clamp(36px,6vw,72px);margin:0 0 6px 0;color:var(--gold);letter-spacing:.5px;">Happy Mid-Autumn Festival</h1>
#     <p style="margin:0;font-size:clamp(16px,2.4vw,22px);opacity:.96">Reunion under the full moon · Lanterns · Mooncakes</p>
#     <p style="margin-top:10px;opacity:.88">
#       {"🎉 It’s today! Chúc Tết Trung Thu vui vẻ!" if is_today else f"⏳ Countdown: <strong>{days_to_go}</strong> day{'s' if days_to_go!=1 else ''} to go"}
#     </p>
#   </div>
# </div>
# """
# st.components.v1.html(hero_html, height=720, scrolling=False)

# Build dynamic bits first
lantern_svgs = "".join([
    f'''<svg viewBox="0 0 72 120" style="position:absolute;top:56%;left:{x}%;width:74px;height:120px;transform-origin:top center;animation:sway {dur}s ease-in-out {delay}s infinite alternate;filter:drop-shadow(0 0 18px rgba(255,180,80,.55));">
          <line x1="36" y1="0" x2="36" y2="10" stroke="#b05816" stroke-width="4"/>
          <rect x="10" y="10" rx="14" width="52" height="70" fill="url(#g{i})" stroke="#b05816" stroke-width="3"/>
          <rect x="22" y="82" rx="2" width="28" height="8" fill="#b05816"/>
          <line x1="36" y1="90" x2="36" y2="112" stroke="#b05816" stroke-width="3"/>
          <path d="M36 112 l-6 8 h12 z" fill="#e6792e"/>
          <defs><linearGradient id="g{i}" x1="0" y1="0" x2="0" y2="1">
             <stop offset="0%" stop-color="#ffd37c"/><stop offset="60%" stop-color="#ff9f45"/><stop offset="100%" stop-color="#e6792e"/>
          </linearGradient></defs>
        </svg>'''
    for i, (x, dur, delay) in enumerate([(12,3.6,.2),(28,3.2,.5),(46,3.9,.1),(66,3.4,.8),(82,3.7,.3)], start=1)
])

countdown_text = None

if is_today:
    countdown_text = "🎉 It’s today! Chúc Tết Trung Thu vui vẻ!"
else:
    plural = "s" if days_to_go != 1 else ""
    countdown_text = f"⏳ Countdown: <strong>{days_to_go}</strong> day{plural} to go"

# Use a NORMAL triple-quoted string (not f""") so CSS braces don’t blow up
hero_html = """
<div id="hero"></div>
<div style="position:relative;width:100%;height:72vh;max-height:840px;overflow:hidden;border-radius:18px;box-shadow:0 30px 80px rgba(0,0,0,.55)">
  <!-- Stars (animated) -->
  <div style="
    position:absolute;inset:0;pointer-events:none;
    background-image:
      radial-gradient(1px 1px at 10% 20%, rgba(255,255,255,.8) 48%, transparent 51%),
      radial-gradient(1.2px 1.2px at 30% 80%, rgba(255,255,255,.7) 48%, transparent 51%),
      radial-gradient(1.5px 1.5px at 70% 35%, rgba(255,255,255,.8) 48%, transparent 51%),
      radial-gradient(1px 1px at 85% 60%, rgba(255,255,255,.9) 48%, transparent 51%);
    background-repeat:no-repeat; animation: twinkle 7s ease-in-out infinite;
  "></div>

  <style>
  @keyframes twinkle {0%,100%{opacity:.7} 50%{opacity:1}}
  @keyframes moonGlow {from{filter:saturate(.95) brightness(.95) drop-shadow(0 0 22px #ffd98a)} to{filter:saturate(1.15) brightness(1.05) drop-shadow(0 0 36px #ffd98a)}}
  @keyframes sway {from{transform:rotate(-6deg)} to{transform:rotate(5deg)}}
  @keyframes drift {from{background-position:0 0} to{background-position:1200px 0}}
  @keyframes drift2 {from{background-position:0 0} to{background-position:900px 0}}

  /* <<< make all hero text yellow >>> */
  .hero-title, .hero-title * { color:#FFEAA6 !important; }
  </style>

  <!-- Glowing moon -->
  <div style="
    position:absolute;top:9%;left:50%;transform:translateX(-50%);
    width:min(28vmax,300px); aspect-ratio:1/1; border-radius:50%;
    background: radial-gradient(60% 60% at 45% 40%, #fff6d3 0%, #ffeaa6 35%, #ffd56b 60%, #f2b85a 75%, #e7a64f 100%);
    animation: moonGlow 5s ease-in-out infinite alternate;
  "></div>

  <!-- Parallax clouds -->
  <div style="
    position:absolute;inset:0;bottom:-30px;opacity:.75;pointer-events:none;
    background-repeat:repeat-x;background-size:1200px 300px;animation:drift 70s linear infinite;
    background-image:url('data:image/svg+xml;utf8,\
    <svg xmlns=\\\"http://www.w3.org/2000/svg\\\" width=\\\"1200\\\" height=\\\"300\\\" viewBox=\\\"0 0 1200 300\\\">\
      <defs><linearGradient id=\\\"cg\\\" x1=\\\"0\\\" x2=\\\"0\\\" y1=\\\"0\\\" y2=\\\"1\\\">\
        <stop offset=\\\"0%\\\" stop-color=\\\"#ffffff\\\" stop-opacity=\\\"0.7\\\"/>\
        <stop offset=\\\"100%\\\" stop-color=\\\"#d7e7ff\\\" stop-opacity=\\\"0.0\\\"/>\
      </linearGradient></defs>\
      <g fill=\\\"url(#cg)\\\">\
        <ellipse cx=\\\"120\\\" cy=\\\"120\\\" rx=\\\"120\\\" ry=\\\"55\\\"/>\
        <ellipse cx=\\\"260\\\" cy=\\\"135\\\" rx=\\\"140\\\" ry=\\\"60\\\"/>\
        <ellipse cx=\\\"420\\\" cy=\\\"120\\\" rx=\\\"110\\\" ry=\\\"50\\\"/>\
        <ellipse cx=\\\"600\\\" cy=\\\"140\\\" rx=\\\"160\\\" ry=\\\"70\\\"/>\
        <ellipse cx=\\\"820\\\" cy=\\\"125\\\" rx=\\\"140\\\" ry=\\\"60\\\"/>\
        <ellipse cx=\\\"1020\\\" cy=\\\"130\\\" rx=\\\"160\\\" ry=\\\"70\\\"/>\
      </g></svg>');
  "></div>
  <div style="
    position:absolute;inset:0;bottom:-6px;opacity:.55;pointer-events:none;
    background-repeat:repeat-x;background-size:900px 240px;animation:drift2 95s linear infinite reverse;
    background-image:inherit;
  "></div>

  <!-- Ornate swinging lanterns (SVG) -->
  {{LANTERNS}}

  <!-- Title -->
  <div class="hero-title" style="position:absolute;top:48%;left:50%;transform:translate(-50%,-50%);text-align:center;">
    <h1 style="font-size:clamp(36px,6vw,72px);margin:0 0 6px 0;letter-spacing:.5px;"> Happy Mid-Autumn Festival</h1>
    <p style="margin:0;font-size:clamp(16px,2.4vw,22px);opacity:.96">Reunion under the full moon · Lanterns · Mooncakes</p>
    <p style="margin-top:10px;opacity:.88">
      {{COUNTDOWN}}
    </p>
  </div>
</div>
"""

# Substitute placeholders, then render
hero_html = hero_html.replace("{{LANTERNS}}", lantern_svgs).replace("{{COUNTDOWN}}", countdown_text)
st.components.v1.html(hero_html, height=720, scrolling=False)

# ---------- Legend / Story ----------
st.markdown('<div class="section" id="legend"><h2>Legend • Sự tích chị Hằng & thỏ ngọc</h2></div>', unsafe_allow_html=True)
st.markdown("""
Ngày xửa ngày xưa, cung thủ Hậu Nghệ đã cứu thế giới bằng cách bắn hạ thêm nhiều mặt trời.
Vợ ông, Hằng Nga, đã uống một loại thuốc trường sinh bất lão và bay lên mặt trăng, nơi Thỏ Ngọc giã thuốc.
Các gia đình tụ họp dưới trăng tròn với đèn lồng và bánh trung thu để ăn mừng ngày đoàn tụ và tri ân.
""")

# ---------- Lantern Wishes (floating) ----------
st.markdown('<div class="section" id="wishes"><h2>Lantern Wishes • Đèn lồng điều ước</h2></div>', unsafe_allow_html=True)
wish = st.text_input("Type your wish and send it up with a lantern:", placeholder="Health, peace, luck…")
if st.button("Send Wish 🏮") and wish.strip():
    st.session_state.wishes.append((uuid.uuid4().hex, wish.strip()))

# Build floating lantern stage
lanterns = []
for i, (_, text) in enumerate(st.session_state.wishes[-10:]):
    delay = 0.35 * i
    left = 12 + (i * 9) % 76
    lanterns.append(f"""
      <div style="position:absolute;bottom:-70px;left:{left}%;transform:translateX(-50%);
                  animation: rise 11s linear {delay}s forwards;">
        <svg viewBox="0 0 72 120" width="72" height="120" style="filter:drop-shadow(0 0 16px rgba(255,180,80,.6))">
          <rect x="10" y="10" rx="14" width="52" height="70" fill="url(#lg)" stroke="#b05816" stroke-width="3"/>
          <rect x="22" y="82" rx="2" width="28" height="8" fill="#b05816"/>
          <line x1="36" y1="90" x2="36" y2="112" stroke="#b05816" stroke-width="3"/>
          <path d="M36 112 l-7 9 h14 z" fill="#e6792e"/>
          <defs><linearGradient id="lg" x1="0" y1="0" x2="0" y2="1">
             <stop offset="0%" stop-color="#ffd37c"/><stop offset="60%" stop-color="#ff9f45"/><stop offset="100%" stop-color="#e6792e"/>
          </linearGradient></defs>
        </svg>
        <div style="text-align:center;margin-top:6px;
                    color:#FFEAA6; font-weight:700;
                    font-family:'Plus Jakarta Sans', sans-serif;
                    max-width:160px">{text}</div>
      </div>
    """)

stage = f"""
<style>
@keyframes rise {{
  0%   {{ transform: translate(-50%, 0) scale(.92); opacity:0 }}
  10%  {{ opacity:1 }}
  100% {{ transform: translate(-50%, -360px) scale(1.08); opacity:.18 }}
}}
</style>
<div class="glass" style="position:relative;height:360px;overflow:hidden;border-radius:16px">
  {''.join(lanterns)}
</div>
"""
st.components.v1.html(stage, height=380, scrolling=False)

# ---------- Mooncake Recipes ----------
st.markdown('<div class="section" id="recipes"><h2>Mooncake Recipes • Bánh Trung Thu</h2></div>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
cards = [
    ("Traditional Lotus Seed", "Lotus paste + salted egg yolk; fragrant golden crust."),
    ("Snow Skin (No-bake)", "Chewy mochi-like skin; try custard, matcha or durian."),
    ("Red Bean & Black Sesame", "Nutty, aromatic filling; perfect with hot tea."),
]
for (title, desc), col in zip(cards, (c1,c2,c3)):
    with col:
        st.markdown(f"""
        <div class="glass" style="transition:transform .25s ease,box-shadow .25s ease">
          <div style="display:flex; align-items:center; gap:12px;">
            <div style="font-size:28px;animation:spinCake 7s linear infinite">🥮</div>
            <div><strong>{title}</strong><br><span style="opacity:.9">{desc}</span></div>
          </div>
        </div>
        <style>@keyframes spinCake{{from{{transform:rotate(0)}}to{{transform:rotate(360deg)}}}}</style>
        """, unsafe_allow_html=True)

# ---------- Countdown ----------

st.markdown('<div class="section" id="countdown"><h2>Countdown • Đếm ngược</h2></div>', unsafe_allow_html=True)
if is_today:
    st.success("🎉 **Happy Mid-Autumn today!** Enjoy the full moon with your family! 🌕")
else:
    st.info(f"⏳ **{days_to_go}** day{'s' if days_to_go!=1 else ''} until the next Mid-Autumn Festival (Oct 6, 2025).")

