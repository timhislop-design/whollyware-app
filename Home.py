"""
Home.py — WhollyWare Landing Page
Run with:  streamlit run Home.py
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

import streamlit as st
import ui.style as style

st.set_page_config(
    page_title="WhollyWare — Household Staples, Smarter",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

style.inject()

# ══════════════════════════════════════════════════════════════════════════════
# TOP NAV BAR
# ══════════════════════════════════════════════════════════════════════════════
style.brand_nav()

# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='position:relative;overflow:hidden;
            background:linear-gradient(140deg,#112A40 0%,#1A3D5C 55%,#2E6B8C 100%);
            border-radius:18px;padding:54px 52px 50px;margin-bottom:20px;'>

  <!-- Decorative house+check icon, right side -->
  <svg style='position:absolute;right:60px;top:50%;transform:translateY(-55%);
              opacity:0.12;pointer-events:none;'
       width="200" height="200" viewBox="0 0 48 48" fill="none"
       xmlns="http://www.w3.org/2000/svg">
    <polyline points="4,24 24,6 44,24" stroke="white" stroke-width="2.5"
              stroke-linecap="round" stroke-linejoin="round"/>
    <rect x="10" y="23" width="28" height="20" rx="1" stroke="white"
          stroke-width="2.2" fill="none"/>
    <rect x="18" y="30" width="12" height="13" rx="1" stroke="white"
          stroke-width="1.8" fill="none"/>
  </svg>

  <!-- Badge -->
  <div style='display:inline-flex;align-items:center;gap:7px;
              background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.18);
              border-radius:20px;padding:5px 14px;margin-bottom:20px;'>
    <span style='width:7px;height:7px;background:#4A94BB;border-radius:50%;
                 display:inline-block;'></span>
    <span style='font-size:0.72rem;font-weight:600;letter-spacing:0.1em;
                 text-transform:uppercase;color:rgba(255,255,255,0.85);'>
      Household price intelligence &nbsp;·&nbsp; Sincere savings
    </span>
  </div>

  <!-- Headline -->
  <h1 style='font-family:Fraunces,serif;font-weight:300;font-size:clamp(1.9rem,3.5vw,2.9rem);
             color:#FFFFFF;line-height:1.2;margin:0 0 14px;max-width:560px;'>
    Stop overpaying for<br />the things you buy<br /><em style='color:#7FB8D4;'>every single week.</em>
  </h1>

  <p style='font-size:1.05rem;color:rgba(255,255,255,0.75);max-width:500px;
            line-height:1.8;margin-bottom:28px;'>
    WhollyWare cross-compares prices for paper towels, laundry detergent,
    cleaning supplies, and every household staple — across every store you
    actually shop at. Net savings, honestly shown.
  </p>

  <!-- Tagline -->
  <div style='display:inline-block;background:rgba(232,124,42,0.18);
              border:1px solid rgba(232,124,42,0.35);border-radius:8px;
              padding:10px 20px;margin-bottom:28px;'>
    <span style='font-family:Fraunces,serif;font-style:italic;font-size:1.1rem;
                 color:#F4A96A;font-weight:300;'>
      The household staple plan that pays you back.
    </span>
  </div>

  <div style='display:flex;gap:12px;flex-wrap:wrap;'>
    <a href="#" style='display:inline-block;background:#E87C2A;color:#FFFFFF;
                       text-decoration:none;font-size:0.9rem;font-weight:600;
                       padding:12px 28px;border-radius:8px;letter-spacing:0.02em;'>
      Join the Waitlist
    </a>
    <a href="https://sentir-solutions.com" target="_blank"
       style='display:inline-block;background:rgba(255,255,255,0.1);color:#FFFFFF;
              border:1px solid rgba(255,255,255,0.25);text-decoration:none;
              font-size:0.9rem;font-weight:400;padding:12px 24px;border-radius:8px;'>
      About Sentir Solutions →
    </a>
  </div>
</div>
""")

# ══════════════════════════════════════════════════════════════════════════════
# HOW IT WORKS — 3-step
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='margin-bottom:8px;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#2E6B8C;margin-bottom:6px;'>How It Works</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.8rem;
             color:#1A3D5C;margin:0 0 6px;'>Three steps to household savings.</h2>
  <p style='color:#5C6B78;font-size:0.95rem;max-width:520px;'>
    WhollyWare does the comparison work so you don't have to.
  </p>
</div>
""")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.html("""
    <div class='ww-card' style='background:#FFFFFF;border:1px solid #D0DDE8;border-top:3px solid #1A3D5C;
                                border-radius:10px;padding:1.75rem;height:100%;'>
      <div style='font-family:Fraunces,serif;font-size:2rem;font-weight:300;
                  color:#D0DDE8;margin-bottom:1rem;'>01</div>
      <h3 style='font-size:1.05rem;font-weight:600;color:#1A3D5C;margin-bottom:0.6rem;'>
        Tell us your stores
      </h3>
      <p style='font-size:0.88rem;color:#5C6B78;line-height:1.75;'>
        Enter your zip code. WhollyWare finds your nearest Target, Walmart, Costco,
        Kroger, and Dollar General — filters to what's actually reachable.
      </p>
    </div>
    """)

with col2:
    st.html("""
    <div class='ww-card' style='background:#FFFFFF;border:1px solid #D0DDE8;border-top:3px solid #2E6B8C;
                                border-radius:10px;padding:1.75rem;height:100%;'>
      <div style='font-family:Fraunces,serif;font-size:2rem;font-weight:300;
                  color:#D0DDE8;margin-bottom:1rem;'>02</div>
      <h3 style='font-size:1.05rem;font-weight:600;color:#1A3D5C;margin-bottom:0.6rem;'>
        We pull the weekly circulars
      </h3>
      <p style='font-size:0.88rem;color:#5C6B78;line-height:1.75;'>
        Every week, WhollyWare ingests store sale circulars and compares
        unit prices across brands, sizes, and stores — automatically.
      </p>
    </div>
    """)

with col3:
    st.html("""
    <div class='ww-card' style='background:#FFFFFF;border:1px solid #D0DDE8;border-top:3px solid #4A94BB;
                                border-radius:10px;padding:1.75rem;height:100%;'>
      <div style='font-family:Fraunces,serif;font-size:2rem;font-weight:300;
                  color:#D0DDE8;margin-bottom:1rem;'>03</div>
      <h3 style='font-size:1.05rem;font-weight:600;color:#1A3D5C;margin-bottom:0.6rem;'>
        See your Found Money
      </h3>
      <p style='font-size:0.88rem;color:#5C6B78;line-height:1.75;'>
        Your personalized household shopping list, organized by store,
        with net savings shown — gas costs included. The number in your pocket.
      </p>
    </div>
    """)

st.html("<div style='height:2rem;'></div>")

# ══════════════════════════════════════════════════════════════════════════════
# PRICING TIERS
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='margin-bottom:8px;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#2E6B8C;margin-bottom:6px;'>Pricing</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.8rem;
             color:#1A3D5C;margin:0 0 6px;'>Start free. Pay for what you use.</h2>
  <p style='color:#5C6B78;font-size:0.95rem;max-width:520px;'>
    No ads. No affiliate deals. No data sales. Revenue is subscriptions only —
    the Sincere Strategy in practice.
  </p>
</div>
""")

t1, t2, t3, t4 = st.columns(4, gap="medium")

tiers = [
    ("Price Finder", "Free", "forever",
     "Cross-store unit price comparison. Weekly savings report. Always free.",
     False),
    ("Staple Tracker", "$5/mo", "per household",
     "Your recurring staples tracked automatically. Buy-off alerts when your brand goes on sale.",
     False),
    ("Health Guard", "$12/mo", "per household",
     "Hard ingredient filters — fragrance-free, dye-free, allergy-safe. Never trades health for savings.",
     True),
    ("Full Household", "$19/mo", "per household",
     "Full staple history, pantry tracking, coupon vault, and multi-store trip optimizer.",
     False),
]

for col, (name, price, period, desc, featured) in zip([t1, t2, t3, t4], tiers):
    featured_style = "border-top-color:#1A3D5C;box-shadow:0 4px 20px rgba(26,61,92,0.12);" if featured else ""
    featured_badge = "<span style='font-size:0.68rem;background:#1A3D5C;color:white;padding:2px 8px;border-radius:10px;margin-left:6px;'>Popular</span>" if featured else ""
    with col:
        st.html(f"""
        <div class='ww-card ww-tier' style='background:#FFFFFF;border:1px solid #D0DDE8;
                                             border-top:3px solid #4A94BB;border-radius:10px;
                                             padding:1.75rem;{featured_style}'>
          <p class='ww-tier-name'>{name}{featured_badge}</p>
          <div class='ww-tier-price'>{price}</div>
          <p style='font-size:0.78rem;color:#8A9CAA;'>{period}</p>
          <p class='ww-tier-desc'>{desc}</p>
        </div>
        """)

st.html("<div style='height:2rem;'></div>")

# ══════════════════════════════════════════════════════════════════════════════
# SINCERE STRATEGY CALLOUT
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='background:linear-gradient(135deg,#112A40 0%,#1A3D5C 100%);
            border-radius:14px;padding:2.5rem;margin-bottom:20px;'>
  <p style='font-size:0.7rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;
            color:#7FB8D4;margin-bottom:1rem;'>The Sincere Strategy®</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.6rem;
             color:#FFFFFF;margin:0 0 1rem;line-height:1.3;'>
    WhollyWare is built on one rule:<br />
    <em style='color:#7FB8D4;'>your interests, always first.</em>
  </h2>
  <div style='display:flex;flex-wrap:wrap;gap:8px;margin-top:1.25rem;'>
    <span class='ww-sincere' style='background:rgba(255,255,255,0.08);color:rgba(255,255,255,0.8);border-color:rgba(255,255,255,0.12);'>
      Zero paid placements — ever
    </span>
    <span class='ww-sincere' style='background:rgba(255,255,255,0.08);color:rgba(255,255,255,0.8);border-color:rgba(255,255,255,0.12);'>
      Health filters are hard rules, not suggestions
    </span>
    <span class='ww-sincere' style='background:rgba(255,255,255,0.08);color:rgba(255,255,255,0.8);border-color:rgba(255,255,255,0.12);'>
      Net savings shown — gas costs included
    </span>
    <span class='ww-sincere' style='background:rgba(255,255,255,0.08);color:rgba(255,255,255,0.8);border-color:rgba(255,255,255,0.12);'>
      Your data is never sold or targeted
    </span>
    <span class='ww-sincere' style='background:rgba(255,255,255,0.08);color:rgba(255,255,255,0.8);border-color:rgba(255,255,255,0.12);'>
      Subscription-only revenue
    </span>
  </div>
  <p style='color:rgba(255,255,255,0.5);font-size:0.8rem;margin-top:1.5rem;'>
    A <a href="https://sentir-solutions.com" target="_blank"
         style="color:#7FB8D4;text-decoration:none;font-weight:500;">Sentir Solutions®</a> company ·
    whollyware.com · Coming 2026
  </p>
</div>
""")

# ══════════════════════════════════════════════════════════════════════════════
# WAITLIST CTA
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='background:#FFFFFF;border:1px solid #D0DDE8;border-radius:14px;
            padding:2.5rem;text-align:center;margin-bottom:20px;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.16em;text-transform:uppercase;
            color:#2E6B8C;margin-bottom:0.75rem;'>Coming Soon — 2026</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.8rem;
             color:#1A3D5C;margin:0 0 0.75rem;'>
    Be first to know when WhollyWare launches.
  </h2>
  <p style='color:#5C6B78;font-size:0.95rem;max-width:460px;margin:0 auto 1.5rem;'>
    We're building WhollyWare now — after WhollyFare's pilot proves the model.
    Join the waitlist and we'll reach out when your area goes live.
  </p>
  <a href="mailto:tim.hislop@gmail.com?subject=WhollyWare%20Waitlist"
     style='display:inline-block;background:#E87C2A;color:#FFFFFF;text-decoration:none;
            font-size:0.9rem;font-weight:600;padding:12px 32px;border-radius:8px;'>
    Join the Waitlist →
  </a>
</div>
""")

# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='text-align:center;padding:1.5rem;color:#8A9CAA;font-size:0.8rem;'>
  WhollyWare™ · A <a href="https://sentir-solutions.com" target="_blank"
  style="color:#2E6B8C;text-decoration:none;">Sentir Solutions®</a> Company ·
  Charlottesville, VA ·
  <a href="mailto:tim.hislop@gmail.com" style="color:#2E6B8C;text-decoration:none;">
    tim.hislop@gmail.com
  </a>
</div>
""")
