"""
style.py — WhollyWare brand styles
Steel blue palette. inject() must be called on every page after st.set_page_config().
"""

import streamlit as st

# ── Brand tokens ──────────────────────────────────────────────────────────────
DARK    = "#1A3D5C"   # deep steel blue — primary
MID     = "#2E6B8C"   # mid steel blue
ACCENT  = "#4A94BB"   # accent blue
LIGHT   = "#7FB8D4"   # light accent
BG      = "#F2F6FA"   # cool cream — background
FOUND   = "#E87C2A"   # Found Money orange — shared across all Wholly brands

BRAND_NAME    = "WhollyWare™"
BRAND_DOMAIN  = "wholly-ware.com"
TAGLINE       = "The household staple plan that pays you back."
PARENT_URL    = "https://sentir-solutions.com"


def inject():
    """Inject global CSS — call once per page after st.set_page_config()."""
    st.html(f"""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;1,9..144,300&family=Inter:wght@300;400;500;600&display=swap');

      :root {{
        --ww-dark:   {DARK};
        --ww-mid:    {MID};
        --ww-accent: {ACCENT};
        --ww-light:  {LIGHT};
        --ww-bg:     {BG};
        --ww-found:  {FOUND};
      }}

      /* ── Page background ── */
      [data-testid="stAppViewContainer"] > .main {{
        background: var(--ww-bg) !important;
      }}
      .block-container {{ padding-top: 0.5rem !important; }}

      /* ── Hide default Streamlit nav ── */
      [data-testid="stSidebarNav"] {{ display: none !important; }}
      header[data-testid="stHeader"] {{ display: none !important; }}

      /* ── Card hover lift ── */
      .ww-card {{
        transition: transform 0.18s ease, box-shadow 0.18s ease !important;
      }}
      .ww-card:hover {{
        transform: translateY(-4px) !important;
        box-shadow: 0 14px 40px rgba(26,61,92,0.14) !important;
      }}

      /* ── Pricing tier cards ── */
      .ww-tier {{
        background: #FFFFFF;
        border: 1px solid #D0DDE8;
        border-top: 3px solid var(--ww-accent);
        border-radius: 10px;
        padding: 1.75rem;
        height: 100%;
      }}

      .ww-tier.featured {{
        border-top-color: var(--ww-dark);
        box-shadow: 0 4px 20px rgba(26,61,92,0.12);
      }}

      .ww-tier-price {{
        font-family: 'Fraunces', serif;
        font-size: 2.2rem;
        font-weight: 300;
        color: var(--ww-dark);
        line-height: 1;
        margin: 0.5rem 0 0.25rem;
      }}

      .ww-tier-name {{
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: var(--ww-accent);
        margin-bottom: 0.25rem;
      }}

      .ww-tier-desc {{
        font-size: 0.88rem;
        color: #5C6B78;
        line-height: 1.7;
        margin-top: 0.75rem;
      }}

      /* ── Found Money badge ── */
      .ww-found-badge {{
        display: inline-block;
        background: var(--ww-found);
        color: #FFFFFF;
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        padding: 3px 10px;
        border-radius: 20px;
      }}

      /* ── Sincere pill ── */
      .ww-sincere {{
        display: inline-block;
        background: rgba(26,61,92,0.08);
        color: var(--ww-dark);
        font-size: 0.72rem;
        font-weight: 500;
        padding: 4px 12px;
        border-radius: 20px;
        border: 1px solid rgba(26,61,92,0.15);
        margin: 2px;
      }}

      /* ── Stat card ── */
      .ww-stat {{
        background: #FFFFFF;
        border: 1px solid #D0DDE8;
        border-left: 3px solid var(--ww-found);
        padding: 1.25rem 1.5rem;
        border-radius: 6px;
      }}

      .ww-stat-num {{
        font-family: 'Fraunces', serif;
        font-size: 2.2rem;
        font-weight: 300;
        color: var(--ww-dark);
        line-height: 1;
      }}

      .ww-stat-label {{
        font-size: 0.82rem;
        color: #5C6B78;
        margin-top: 0.3rem;
        line-height: 1.5;
      }}
    </style>
    """)


def page_header(title: str, subtitle: str = ""):
    """Standard interior page header."""
    sub_html = f"<p style='color:#7FB8D4;font-size:0.95rem;margin-top:0.5rem;'>{subtitle}</p>" if subtitle else ""
    st.html(f"""
    <div style='background:linear-gradient(135deg,{DARK} 0%,{MID} 100%);
                padding:2.5rem 2rem 2rem;border-radius:12px;margin-bottom:1.5rem;'>
      <p style='font-size:0.7rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;
                color:{LIGHT};margin-bottom:0.5rem;'>WhollyWare™</p>
      <h1 style='font-family:Fraunces,serif;font-weight:300;font-size:2rem;
                 color:#FFFFFF;margin:0;line-height:1.2;'>{title}</h1>
      {sub_html}
    </div>
    """)


def brand_nav():
    """Minimal top nav bar for all pages."""
    st.html(f"""
    <div style='display:flex;align-items:center;gap:10px;margin-bottom:16px;
                padding:10px 18px;background:#FFFFFF;
                border-radius:10px;border:1px solid #D0DDE8;'>
      <svg width="28" height="28" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <polyline points="8,24 24,10 40,24" stroke="{DARK}" stroke-width="2.5"
                  stroke-linecap="round" stroke-linejoin="round"/>
        <rect x="13" y="23" width="22" height="18" rx="1" stroke="{DARK}"
              stroke-width="2.2" fill="none"/>
        <rect x="20" y="30" width="8" height="11" rx="1" stroke="{DARK}"
              stroke-width="1.8" fill="none"/>
        <circle cx="34" cy="14" r="7" fill="{ACCENT}"/>
        <polyline points="30.5,14 33,16.5 37.5,11.5" stroke="white"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <span style='font-size:1rem;font-weight:700;color:{DARK};'>WhollyWare™</span>
      <span style='color:#C0CDD8;margin:0 4px;'>·</span>
      <span style='font-size:0.8rem;color:#666;'>a
        <a href="{PARENT_URL}" target="_blank"
           style="color:{MID};font-weight:600;text-decoration:none;">Sentir Solutions</a>® Company</span>
    </div>
    """)
