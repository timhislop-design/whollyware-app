"""
7_Investor.py — WhollyWare Investor Brief
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import streamlit as st
import ui.style as style

st.set_page_config(
    page_title="WhollyWare — Investor Brief",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

style.inject()
style.brand_nav()
style.page_header(
    "Investor Brief",
    "WhollyWare™ — The household staple plan that pays you back."
)

# ── Market opportunity ────────────────────────────────────────────────────────
st.html("""
<div style='margin-bottom:1.5rem;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#2E6B8C;margin-bottom:6px;'>The Opportunity</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.7rem;
             color:#1A3D5C;margin:0 0 0.75rem;'>
    The simplest vertical to build.<br />The largest to win.
  </h2>
  <p style='color:#5C6B78;font-size:0.95rem;max-width:620px;line-height:1.8;'>
    Household non-perishables — paper towels, laundry detergent, dish soap, cleaning
    supplies, batteries — are the category every household buys on autopilot.
    No planning logic, no expiration dates, no meal constraints.
    Pure price comparison, done right for the first time.
  </p>
</div>
""")

c1, c2, c3, c4 = st.columns(4, gap="medium")

stats = [
    ("$200B+", "US household staples market — the single largest CPG category"),
    ("$800+",  "Average household overspend per year vs. optimal store selection"),
    ("82%",    "Of households don't comparison-shop staples — they default to habit"),
    ("$19/mo", "Full Household tier price vs. $800+/yr in recoverable savings"),
]

for col, (num, label) in zip([c1, c2, c3, c4], stats):
    with col:
        st.html(f"""
        <div class='ww-stat'>
          <div class='ww-stat-num'>{num}</div>
          <div class='ww-stat-label'>{label}</div>
        </div>
        """)

st.html("<div style='height:1.5rem;'></div>")

# ── Platform thesis ───────────────────────────────────────────────────────────
st.html("""
<div style='background:linear-gradient(135deg,#112A40 0%,#1A3D5C 100%);
            border-radius:12px;padding:2.25rem;margin-bottom:1.5rem;'>
  <p style='font-size:0.7rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;
            color:#7FB8D4;margin-bottom:0.75rem;'>Platform Thesis</p>
  <blockquote style='font-family:Fraunces,serif;font-weight:300;font-size:1.25rem;
                     font-style:italic;color:#FFFFFF;line-height:1.6;margin:0;'>
    "WhollyWare is the second brand on the Sincere Strategy® platform — the same
     constraint engine and price-intelligence layer that powers WhollyFare,
     applied to the category with the highest repurchase frequency and the
     lowest consumer price awareness in retail."
  </blockquote>
  <p style='color:rgba(255,255,255,0.4);font-size:0.8rem;margin-top:1rem;'>
    — Sentir Solutions® founding thesis
  </p>
</div>
""")

# ── Competitive moat ─────────────────────────────────────────────────────────
st.html("""
<div style='margin-bottom:1rem;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#2E6B8C;margin-bottom:6px;'>The Moat</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.5rem;
             color:#1A3D5C;margin:0 0 0.5rem;'>
    Why competitors can't copy the Sincere Strategy.
  </h2>
</div>
""")

m1, m2 = st.columns(2, gap="medium")

moat_items = [
    ("Zero paid placements",
     "Rakuten, Honey, Ibotta, and every competitor monetizes via brand sponsorships and affiliate commissions. Adopting the Sincere Strategy would destroy their revenue model — they literally cannot do it."),
    ("Health-first constraint engine",
     "We run allergen and ingredient filters before the optimizer. A brand cannot pay to appear in a filtered-out category. No existing price-comparison tool makes this guarantee."),
    ("Net savings, always",
     "We show gas costs and trip costs alongside grocery savings. Showing the honest net number is structurally bad for competitors who want the gross savings headline to look impressive."),
    ("Subscription-only revenue",
     "No ads, no data sales, no affiliate fees. This is a feature, not a limitation — households trust a product that has no incentive to mislead them."),
]

for i, (title, body) in enumerate(moat_items):
    col = m1 if i % 2 == 0 else m2
    with col:
        st.html(f"""
        <div style='background:#FFFFFF;border:1px solid #D0DDE8;border-left:3px solid #4A94BB;
                    border-radius:6px;padding:1.25rem 1.5rem;margin-bottom:1rem;'>
          <h4 style='font-size:0.92rem;font-weight:600;color:#1A3D5C;margin-bottom:0.4rem;'>
            {title}
          </h4>
          <p style='font-size:0.85rem;color:#5C6B78;line-height:1.75;margin:0;'>{body}</p>
        </div>
        """)

st.html("<div style='height:1.5rem;'></div>")

# ── Roadmap ───────────────────────────────────────────────────────────────────
st.html("""
<div style='margin-bottom:1rem;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#2E6B8C;margin-bottom:6px;'>Roadmap</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.5rem;
             color:#1A3D5C;margin:0;'>WhollyWare launches after WhollyFare proves the model.</h2>
</div>
""")

r1, r2, r3 = st.columns(3, gap="medium")

phases = [
    ("Phase 1 — Prerequisite", "#D0DDE8",
     "WhollyFare pilot completes 8 weeks of real household savings data. The Sincere Strategy engine is validated in the perishables vertical first."),
    ("Phase 2 — WhollyWare Launch", "#1A3D5C",
     "WhollyWare builds on the same engine — circular ingestion, unit-price normalization, trip cost math — stripped of meal planning complexity. Faster to build, higher frequency purchases."),
    ("Phase 3 — National Scale", "#2E6B8C",
     "Target, Walmart, Costco, Kroger, Amazon, Dollar General. Automated circular parsing. 50,000+ households. Market Insights data product (public). $2M+ ARR."),
]

for col, (title, color, desc) in zip([r1, r2, r3], phases):
    with col:
        st.html(f"""
        <div style='background:#FFFFFF;border:1px solid #D0DDE8;
                    border-top:4px solid {color};border-radius:10px;padding:1.5rem;'>
          <h4 style='font-size:0.9rem;font-weight:600;color:#1A3D5C;margin-bottom:0.6rem;'>
            {title}
          </h4>
          <p style='font-size:0.85rem;color:#5C6B78;line-height:1.75;margin:0;'>{desc}</p>
        </div>
        """)

st.html("<div style='height:1.5rem;'></div>")

# ── Contact ───────────────────────────────────────────────────────────────────
st.html("""
<div style='background:#F2F6FA;border:1px solid #D0DDE8;border-radius:12px;
            padding:2.25rem;text-align:center;'>
  <h3 style='font-family:Fraunces,serif;font-weight:300;font-size:1.5rem;
             color:#1A3D5C;margin:0 0 0.75rem;'>
    Interested in the WhollyWare opportunity?
  </h3>
  <p style='color:#5C6B78;font-size:0.9rem;max-width:420px;margin:0 auto 1.25rem;'>
    WhollyWare is part of the Sentir Solutions® portfolio. Investment inquiries
    cover the full platform — WhollyFare, WhollyWare, WhollyPaws, and WhollyCare.
  </p>
  <a href="mailto:tim.hislop@gmail.com?subject=WhollyWare%20Investor%20Inquiry"
     style='display:inline-block;background:#1A3D5C;color:#FFFFFF;text-decoration:none;
            font-size:0.9rem;font-weight:600;padding:11px 28px;border-radius:8px;'>
    tim.hislop@gmail.com
  </a>
  <p style='color:#8A9CAA;font-size:0.78rem;margin-top:1rem;'>
    See the full portfolio at
    <a href="https://sentir-solutions.com" target="_blank"
       style="color:#2E6B8C;text-decoration:none;">sentir-solutions.com</a>
  </p>
</div>
""")
