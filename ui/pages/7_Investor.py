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
    "WhollyWare — The household staple plan that pays you back."
)

# Hero
st.html("""
<div style='background:linear-gradient(160deg,#06131C 0%,#0F2236 60%,#06131C 100%);
            border-radius:16px;padding:52px 44px 44px;color:white;margin-bottom:2rem;'>
  <p style='font-size:0.7rem;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;
            color:#7FB8D4;margin-bottom:14px;'>WhollyWare | Sentir Solutions LLC | Charlottesville, VA</p>
  <h1 style='font-size:2.8rem;font-weight:800;color:#fff;margin:0 0 12px;line-height:1.1;'>
    The simplest vertical.<br>The largest to win.
  </h1>
  <p style='font-size:1.05rem;color:rgba(255,255,255,0.72);max-width:600px;line-height:1.65;margin-bottom:2rem;'>
    Every household buys paper towels, laundry detergent, and dish soap every single week
    on autopilot, at whatever price their usual store charges. No comparison. No planning.
    WhollyWare is the first tool that changes that, honestly and without compromise.
  </p>
  <div style='display:flex;gap:18px;flex-wrap:wrap;'>
    <div style='background:rgba(255,255,255,0.06);border:1px solid rgba(127,184,212,0.25);
                border-radius:10px;padding:18px 24px;min-width:140px;flex:1;'>
      <div style='font-size:1.9rem;font-weight:800;color:#E87C2A;'>$200B+</div>
      <div style='font-size:0.75rem;color:rgba(255,255,255,0.5);margin-top:5px;'>US household staples market</div>
    </div>
    <div style='background:rgba(255,255,255,0.06);border:1px solid rgba(127,184,212,0.25);
                border-radius:10px;padding:18px 24px;min-width:140px;flex:1;'>
      <div style='font-size:1.9rem;font-weight:800;color:#E87C2A;'>$800+</div>
      <div style='font-size:0.75rem;color:rgba(255,255,255,0.5);margin-top:5px;'>Average household overspend per year</div>
    </div>
    <div style='background:rgba(255,255,255,0.06);border:1px solid rgba(127,184,212,0.25);
                border-radius:10px;padding:18px 24px;min-width:140px;flex:1;'>
      <div style='font-size:1.9rem;font-weight:800;color:#E87C2A;'>82%</div>
      <div style='font-size:0.75rem;color:rgba(255,255,255,0.5);margin-top:5px;'>Of households never comparison-shop staples</div>
    </div>
    <div style='background:rgba(255,255,255,0.06);border:1px solid rgba(127,184,212,0.25);
                border-radius:10px;padding:18px 24px;min-width:140px;flex:1;'>
      <div style='font-size:1.9rem;font-weight:800;color:#E87C2A;'>$0</div>
      <div style='font-size:0.75rem;color:rgba(255,255,255,0.5);margin-top:5px;'>Paid placements. Ever. Structural guarantee.</div>
    </div>
  </div>
</div>
""")

# Platform foundation
st.html("""
<div style='background:linear-gradient(135deg,#112A40 0%,#1A3D5C 100%);
            border-radius:12px;padding:2.25rem;margin-bottom:1.5rem;'>
  <p style='font-size:0.7rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;
            color:#7FB8D4;margin-bottom:0.75rem;'>Platform Foundation</p>
  <blockquote style='font-family:Fraunces,serif;font-weight:300;font-size:1.2rem;
                     font-style:italic;color:#FFFFFF;line-height:1.6;margin:0 0 1rem;'>
    "WhollyWare does not start from scratch. It inherits the same constraint engine, circular
     ingestion pipeline, and Found Money math already validated by WhollyFare -- the meal planning
     brand that is running in a live pilot household right now."
  </blockquote>
  <p style='color:rgba(255,255,255,0.5);font-size:0.82rem;line-height:1.6;margin:0;'>
    WhollyFare is in active pilot -- Tim Hislop family, four Charlottesville grocers, weekly receipts.
    The engine works. The platform compounds. WhollyWare is the second brand on an already-proven foundation.
  </p>
</div>
""")

# Why Now
st.html("""
<div style='margin-bottom:1rem;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#2E6B8C;margin-bottom:6px;'>Why Now</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.5rem;color:#1A3D5C;margin:0 0 0.5rem;'>
    Three forces making this the right moment.
  </h2>
</div>
""")

wn1, wn2, wn3 = st.columns(3, gap="medium")
why_now = [
    (wn1, "Household goods inflation",
     "US household staple prices rose 28%+ between 2020-2024. Consumers are actively looking for savings tools for non-perishables for the first time. Demand is real and measurable."),
    (wn2, "Retailer circular data is accessible",
     "Target, Walmart, Kroger, Costco, Dollar General -- all publish weekly circulars. The data pipeline that powers WhollyFare works identically for household goods."),
    (wn3, "AI makes unit-price parsing tractable",
     "8 rolls vs. 12 rolls vs. 20 rolls vs. 24 rolls -- LLM-assisted extraction normalizes unit pricing across all formats automatically. This was not reliable 24 months ago."),
]
for col, title, body in why_now:
    with col:
        st.html(f"""
        <div style='background:#fff;border-radius:10px;padding:1.4rem 1.2rem;
                    border:1px solid #D0DDE8;border-top:4px solid #2E6B8C;
                    box-shadow:0 2px 10px rgba(0,0,0,0.05);'>
          <div style='font-size:0.92rem;font-weight:700;color:#1A3D5C;margin-bottom:6px;'>{title}</div>
          <div style='font-size:0.83rem;color:#5C6B78;line-height:1.6;'>{body}</div>
        </div>
        """)

st.html("<div style='height:1.5rem;'></div>")

# Sincere Strategy
st.html("""
<div style='margin-bottom:1rem;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#2E6B8C;margin-bottom:6px;'>The Sincere Strategy</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.5rem;color:#1A3D5C;margin:0 0 0.5rem;'>
    Six commitments competitors cannot copy.
  </h2>
  <p style='color:#5C6B78;font-size:0.9rem;max-width:620px;line-height:1.7;'>
    Every Wholly brand is governed by the Sincere Strategy -- a set of non-negotiable principles
    that require competitors to destroy their own revenue model to adopt.
  </p>
</div>
""")

s1, s2 = st.columns(2, gap="medium")
sincere = [
    ("No paid placements",
     "Honey, Rakuten, and Ibotta are paid by brands to surface their products. WhollyWare recommendations are pure -- no CPG company can pay to appear. Adopting this rule would destroy their affiliate revenue."),
    ("Ingredient constraints first",
     "Fragrance-free, dye-free, allergy-safe -- constraints run before the price optimizer. If a product fails the household requirements, it never appears. No exceptions for any price point."),
    ("Net savings, always",
     "We show gas costs alongside grocery savings. The honest net number is structurally bad for competitors who want the gross savings headline to look impressive."),
    ("Radical transparency",
     "Every product filtered out is shown to the user with the reason. No black boxes. Users see exactly why a specific item did not make the list."),
    ("Local-first, real circulars",
     "Plans built from your local stores' actual weekly circulars -- not national price estimates or partnered inventory feeds. If it's not on sale at your Target this week, it does not appear."),
    ("User data ownership",
     "Household preferences and constraint data is yours. WhollyWare does not sell it, share it with CPG brands, or use it for targeting. Subscription revenue only."),
]
for i, (title, body) in enumerate(sincere):
    col = s1 if i % 2 == 0 else s2
    with col:
        st.html(f"""
        <div style='background:#fff;border:1px solid #D0DDE8;border-left:4px solid #2E6B8C;
                    border-radius:6px;padding:1.1rem 1.4rem;margin-bottom:0.85rem;'>
          <div style='font-size:0.92rem;font-weight:700;color:#1A3D5C;margin-bottom:4px;'>{title}</div>
          <div style='font-size:0.83rem;color:#5C6B78;line-height:1.65;'>{body}</div>
        </div>
        """)

st.html("""
<div style='background:#EFF6FA;border:1px solid #B0D4E8;border-radius:10px;
            padding:14px 22px;margin-top:4px;font-size:0.88rem;color:#1A3D5C;font-weight:600;line-height:1.55;'>
  Honey and Rakuten cannot adopt the Sincere Strategy without eliminating their affiliate revenue stream.
  That is not a policy difference -- it is a structural moat.
</div>
""")

st.html("<div style='height:1.5rem;'></div>")

# Competitive moat
st.html("""
<div style='margin-bottom:1rem;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#2E6B8C;margin-bottom:6px;'>Competitive Landscape</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.5rem;color:#1A3D5C;margin:0 0 0.5rem;'>
    Why the existing tools cannot do this honestly.
  </h2>
</div>
""")

m1, m2 = st.columns(2, gap="medium")
moat_items = [
    ("Honey and Rakuten are paid by the brands they recommend",
     "Every discount they surface has an affiliate fee behind it. A brand that does not pay does not appear. WhollyWare zero-placement rule makes this structurally impossible -- and makes every recommendation trustworthy."),
    ("Unit pricing in household goods is deliberately opaque",
     "8 rolls for $5.99 vs. 20 rolls for $12.99 -- the math is designed to be hard to do at the shelf. WhollyWare normalizes every format to per-unit cost and surfaces the comparison that actually matters."),
    ("Amazon subscribe and save is one store, always",
     "Subscribe and Save locks you into Amazon pricing with no visibility into what the same product costs at Target or Costco this week. WhollyWare is cross-store, always, with actual circular data."),
    ("No existing tool filters on ingredient or sensitivity first",
     "A fragrance-sensitive household buying the wrong detergent is overpaying twice -- at the shelf and in irritation. WhollyWare runs household constraints before the price comparison. No competitor does this."),
]
for i, (title, body) in enumerate(moat_items):
    col = m1 if i % 2 == 0 else m2
    with col:
        st.html(f"""
        <div style='background:#FFFFFF;border:1px solid #D0DDE8;border-left:3px solid #4A94BB;
                    border-radius:6px;padding:1.25rem 1.5rem;margin-bottom:1rem;'>
          <h4 style='font-size:0.92rem;font-weight:600;color:#1A3D5C;margin-bottom:0.4rem;'>{title}</h4>
          <p style='font-size:0.85rem;color:#5C6B78;line-height:1.75;margin:0;'>{body}</p>
        </div>
        """)

st.html("<div style='height:1.5rem;'></div>")

# Why Tim
st.html("""
<div style='background:linear-gradient(160deg,#06131C,#0F2236);border:1px solid #2E6B8C;
            border-radius:12px;padding:2rem 2.25rem;margin-bottom:1.5rem;'>
  <p style='font-size:0.7rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;
            color:#7FB8D4;margin-bottom:0.75rem;'>The Founder</p>
  <p style='font-family:Fraunces,serif;font-weight:300;font-size:1.1rem;
            font-style:italic;color:#FFFFFF;line-height:1.6;margin:0 0 1rem;'>
    "I am not building WhollyWare because someone told me there was a market opportunity.
     I am building it because I run WhollyFare for my own family every Sunday,
     and I know exactly how the same engine applies to every other aisle in that store."
  </p>
  <p style='color:rgba(255,255,255,0.55);font-size:0.83rem;line-height:1.65;margin:0;'>
    Tim Hislop -- Founder, Sentir Solutions LLC -- Full-time at ECS -- Building nights and weekends --
    Charlottesville, VA pilot running now. The constraint engine that powers WhollyFare powers WhollyWare.
    The code is the same. The vertical is bigger.
  </p>
</div>
""")

# Roadmap
st.html("""
<div style='margin-bottom:1rem;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#2E6B8C;margin-bottom:6px;'>Roadmap</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.5rem;color:#1A3D5C;margin:0;'>
    WhollyWare launches after WhollyFare proves the model.
  </h2>
</div>
""")

r1, r2, r3 = st.columns(3, gap="medium")
phases = [
    ("Phase 1 -- Prerequisite", "#D0DDE8",
     "WhollyFare pilot completes 8 weeks of real household savings data. The Sincere Strategy engine is validated in the perishables vertical. The platform foundation is proven."),
    ("Phase 2 -- WhollyWare Launch", "#1A3D5C",
     "WhollyWare builds on the same engine -- circular ingestion, unit-price normalization, trip cost math -- stripped of meal planning complexity. Faster to build, higher purchase frequency."),
    ("Phase 3 -- National Scale", "#2E6B8C",
     "Target, Walmart, Costco, Kroger, Amazon, Dollar General. Automated circular parsing. 50,000+ households. Market Insights data product. $2M+ ARR. The Sincere Strategy brand owns a category."),
]
for col, (title, color, desc) in zip([r1, r2, r3], phases):
    with col:
        st.html(f"""
        <div style='background:#FFFFFF;border:1px solid #D0DDE8;border-top:4px solid {color};
                    border-radius:10px;padding:1.5rem;'>
          <h4 style='font-size:0.9rem;font-weight:600;color:#1A3D5C;margin-bottom:0.6rem;'>{title}</h4>
          <p style='font-size:0.85rem;color:#5C6B78;line-height:1.75;margin:0;'>{desc}</p>
        </div>
        """)

st.html("<div style='height:1.5rem;'></div>")

# Close
st.html("""
<div style='background:#F2F6FA;border:1px solid #D0DDE8;border-radius:12px;padding:2.25rem;text-align:center;'>
  <h3 style='font-family:Fraunces,serif;font-weight:300;font-size:1.4rem;color:#1A3D5C;margin:0 0 0.6rem;'>
    WhollyWare is happening. The platform is proven.
  </h3>
  <p style='color:#5C6B78;font-size:0.88rem;max-width:480px;margin:0 auto 1.25rem;line-height:1.7;'>
    WhollyFare is in pilot now. The engine works. WhollyWare is the same engine applied
    to the largest CPG category in retail. Investment inquiries cover the full Sentir Solutions portfolio.
  </p>
  <a href="mailto:tim.hislop@gmail.com?subject=WhollyWare%20Investor%20Inquiry"
     style='display:inline-block;background:#1A3D5C;color:#FFFFFF;text-decoration:none;
            font-size:0.9rem;font-weight:600;padding:11px 28px;border-radius:8px;'>
    tim.hislop@gmail.com
  </a>
  <p style='color:#8A9CAA;font-size:0.78rem;margin-top:1rem;'>
    Full portfolio at
    <a href="https://sentir-solutions.com" target="_blank" style="color:#2E6B8C;text-decoration:none;">
      sentir-solutions.com
    </a>
  </p>
</div>
""")
