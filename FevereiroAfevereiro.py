import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import datetime
import time

st.title("Finance Stake")
st.write("Stake Brazil LTDA")

# ==============================================================================
# 1. UI ARCHITECTURE AND EXECUTIVE DESIGN (C-LEVEL DASHBOARD)
# ==============================================================================
# High performance configuration and ultra-wide layout
st.set_page_config(
    page_title="STRATEGIC FINANCE ANALYSIS - STAKE BRAZIL",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# CORPORATE CSS INJECTION (PREMIUM HIGH-DENSITY STYLING)
# ==============================================================================
st.markdown("""
    <style>
    /* Inter family import - Standard for International Financial Interfaces */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap');
    
    :root {
        --primary-bg: #0B1120;
        --secondary-bg: #0F172A;
        --card-bg: #162032;
        --accent-blue: #38BDF8;
        --accent-green: #10B981;
        --accent-red: #F43F5E;
        --text-main: #F8FAFC;
        --text-dim: #94A3B8;
        --border-color: #1E293B;
    }

    html, body, [data-testid="stAppViewContainer"] { 
        font-family: 'Inter', sans-serif; 
        background-color: var(--primary-bg) !important;
        color: var(--text-main) !important;
    }
    
    /* FORCE DARK BACKGROUND ACROSS THE APP */
    .stApp, .main, [data-testid="stHeader"], [data-testid="stToolbar"] { 
        background-color: var(--primary-bg) !important; 
    }
    
    /* SIDEBAR - CORPORATE DESIGN */
    [data-testid="stSidebar"] {
        background-color: var(--secondary-bg) !important;
        border-right: 1px solid var(--border-color) !important;
        width: 350px !important;
    }
    
    /* RADIO MENU STYLING */
    .stRadio label p {
        color: #FFFFFF !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        letter-spacing: 0.3px;
    }
    
    /* INPUTS AND SELECTBOXES STYLING */
    .stSelectbox label p {
        color: var(--text-main) !important;
        font-weight: 700 !important;
        margin-bottom: 8px;
    }
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: var(--secondary-bg) !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        height: 45px;
    }
    .stSelectbox div[data-baseweb="select"] div {
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }
    div[role="listbox"] {
        background-color: #0F172A !important;
        border: 1px solid #334155 !important;
    }
    div[role="listbox"] li {
        color: #FFFFFF !important;
        background-color: #0F172A !important;
    }
    div[role="listbox"] li:hover {
        background-color: #1E293B !important;
        color: #38BDF8 !important;
    }

    /* -------------------------------------------------------------------------
       NUMBERS FONT ADJUSTMENT (METRICS)
    --------------------------------------------------------------------------*/
    [data-testid="stMetricValue"] > div { 
        color: #FFFFFF !important; 
        font-size: 1.5rem !important; 
        font-weight: 800 !important; 
        letter-spacing: -0.5px !important;
    }
    [data-testid="stMetricLabel"] > div, [data-testid="stMetricLabel"] * { 
        color: var(--accent-blue) !important; 
        font-size: 0.85rem !important; 
        font-weight: 700 !important; 
        text-transform: uppercase !important;
        letter-spacing: 1.2px !important;
    }
    
    /* METRICS CARDS - DEPTH EFFECT */
    .stMetric { 
        background-color: var(--card-bg) !important; 
        padding: 15px 20px !important; 
        border-radius: 10px !important; 
        border: 1px solid var(--border-color) !important; 
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5) !important; 
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stMetric:hover {
        transform: translateY(-5px);
        border-color: var(--accent-blue) !important;
        box-shadow: 0 15px 35px rgba(56, 189, 248, 0.15) !important;
    }

    /* -------------------------------------------------------------------------
       TEXT SIZE ADJUSTMENT (REPORTS/KPI TEXT)
    --------------------------------------------------------------------------*/
    .consultant-report { 
        background: linear-gradient(165deg, #111827 0%, #0F172A 100%) !important; 
        color: #F1F5F9 !important; 
        border-left: 6px solid var(--accent-blue); 
        padding: 25px 35px; 
        margin: 20px 0; 
        border-radius: 8px; 
        line-height: 1.6; 
        font-size: 0.9rem; 
        text-align: justify; 
        border-top: 1px solid var(--border-color); 
        border-right: 1px solid var(--border-color); 
        border-bottom: 1px solid var(--border-color);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }
    .consultant-report b, .consultant-report strong { 
        color: #FFFFFF !important; 
        font-weight: 800 !important; 
    }
    
    /* SECTION TITLES */
    .section-title { 
        color: #FFFFFF !important; 
        font-weight: 800; 
        font-size: 1.6rem;
        text-transform: uppercase; 
        letter-spacing: 2px; 
        border-bottom: 3px solid var(--accent-blue); 
        padding-bottom: 10px; 
        margin-top: 40px; 
        margin-bottom: 30px;
    }

    /* KPI BLOCK (INTERNAL STRUCTURE) */
    .kpi-block { 
        background-color: #0F172A !important; 
        padding: 18px; 
        border-radius: 8px; 
        margin-bottom: 15px; 
        border: 1px solid var(--border-color);
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.3);
    }
    .kpi-title { 
        color: var(--accent-blue) !important; 
        font-weight: 800; 
        font-size: 1rem; 
        margin-bottom: 10px; 
        text-transform: uppercase;
        display: flex;
        align-items: center;
    }
    .kpi-text { 
        color: #CBD5E1 !important; 
        font-size: 0.85rem !important; 
        line-height: 1.5; 
    } 
    .kpi-text b, .kpi-text i, .kpi-text span, .kpi-text div { 
        color: #FFFFFF !important; 
        font-weight: 800 !important; 
    }

    /* APPLICATION DATA TABLES */
    .stDataFrame { border-radius: 12px; border: 1px solid var(--border-color); overflow: hidden; }
    
    /* CUSTOM SCROLLBAR FOR FLUID EXPERIENCE */
    ::-webkit-scrollbar { width: 10px; height: 10px; }
    ::-webkit-scrollbar-track { background: var(--primary-bg); }
    ::-webkit-scrollbar-thumb { background: #334155; border-radius: 5px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--accent-blue); }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# LAYOUT UTILITY FUNCTIONS (TO MAINTAIN C-LEVEL VISUAL CONSISTENCY)
# ==============================================================================

def aplicar_template_financeiro(fig, titulo=""):
    """
    Executive standardization of Plotly charts.
    Ensures legends and texts are in WHITE (#FFFFFF) to prevent disappearing on dark background.
    """
    fig.update_layout(
        title=dict(
            text=titulo, 
            font=dict(color="#FFFFFF", size=20, family="Inter", weight="bold")
        ),
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#FFFFFF", family="Inter"),
        hovermode="x unified", 
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.05,
            xanchor="right",
            x=1,
            bgcolor="rgba(0,0,0,0)",
            font=dict(color="#FFFFFF", size=12)
        ),
        margin=dict(l=40, r=40, t=100, b=40)
    )
    fig.update_xaxes(
        showgrid=True, gridwidth=1, gridcolor='#1E293B', 
        griddash='dot', zeroline=False, tickfont=dict(color="#FFFFFF")
    )
    fig.update_yaxes(
        showgrid=True, gridwidth=1, gridcolor='#1E293B', 
        griddash='dot', zeroline=False, tickfont=dict(color="#FFFFFF")
    )
    return fig

# ==============================================================================
# 2. ETL ENGINE (MACRO): FORENSIC CAPTURE AND DATA BLINDING (FEB/25 - MAR/26)
# ==============================================================================

@st.cache_data(show_spinner="OBTAINING MACRO FINANCIAL INTELLIGENCE...")
def carregar_motor_estatistico():
    # RAW MACRO DATA MATRIX (100% FAITHFUL TO USER INPUTS - 14 MONTHS)
    dataset_bruto = [
        {"Periodo": "February/25", "Bet": 75156618.15, "Ggr": 2271467.46, "AccountingRevenue": 865332.98, "DepositAmount": 14670999.56, "DepositCount": 376216, "FirstDepositsAmount": 22140, "ActiveCustomers": 42949},
        {"Periodo": "March/25", "Bet": 77798034.17, "Ggr": 2155873.29, "AccountingRevenue": 564681.84, "DepositAmount": 15641336.44, "DepositCount": 391224, "FirstDepositsAmount": 24046, "ActiveCustomers": 48941},
        {"Periodo": "April/25", "Bet": 79780840.69, "Ggr": 2299723.76, "AccountingRevenue": 923063.98, "DepositAmount": 16506101.56, "DepositCount": 451691, "FirstDepositsAmount": 34194, "ActiveCustomers": 64984},
        {"Periodo": "May/25", "Bet": 83413400.00, "Ggr": 2905520.26, "AccountingRevenue": 1713845.84, "DepositAmount": 16379449.57, "DepositCount": 445053, "FirstDepositsAmount": 22889, "ActiveCustomers": 60025},
        {"Periodo": "June/25", "Bet": 86644640.72, "Ggr": 3144451.77, "AccountingRevenue": 1962406.34, "DepositAmount": 16972874.91, "DepositCount": 419270, "FirstDepositsAmount": 18784, "ActiveCustomers": 53356},
        {"Periodo": "July/25", "Bet": 86484658.82, "Ggr": 2833834.21, "AccountingRevenue": 1601311.38, "DepositAmount": 16456861.61, "DepositCount": 407207, "FirstDepositsAmount": 16421, "ActiveCustomers": 49307},
        {"Periodo": "August/25", "Bet": 84505727.22, "Ggr": 3109335.95, "AccountingRevenue": 1825563.33, "DepositAmount": 16405267.37, "DepositCount": 417493, "FirstDepositsAmount": 15563, "ActiveCustomers": 48312},
        {"Periodo": "September/25", "Bet": 83399007.07, "Ggr": 2560890.11, "AccountingRevenue": 1312607.79, "DepositAmount": 16181684.11, "DepositCount": 418568, "FirstDepositsAmount": 17528, "ActiveCustomers": 53251},
        {"Periodo": "October/25", "Bet": 91783681.79, "Ggr": 2298976.46, "AccountingRevenue": 1021722.71, "DepositAmount": 18037390.58, "DepositCount": 474111, "FirstDepositsAmount": 24201, "ActiveCustomers": 64339},
        {"Periodo": "November/25", "Bet": 95894583.99, "Ggr": 2953839.11, "AccountingRevenue": 1500363.83, "DepositAmount": 16967765.80, "DepositCount": 451049, "FirstDepositsAmount": 15884, "ActiveCustomers": 55155},
        {"Periodo": "December/25", "Bet": 88223469.95, "Ggr": 3061420.68, "AccountingRevenue": 1735938.26, "DepositAmount": 14782522.06, "DepositCount": 406808, "FirstDepositsAmount": 11943, "ActiveCustomers": 44298},
        {"Periodo": "January/26", "Bet": 72166119.45, "Ggr": 2352363.74, "AccountingRevenue": 1385569.32, "DepositAmount": 12357170.86, "DepositCount": 348109, "FirstDepositsAmount": 11008, "ActiveCustomers": 41679},
        {"Periodo": "February/26", "Bet": 54334109.43, "Ggr": 1591515.71, "AccountingRevenue": 847163.76, "DepositAmount": 9933985.84, "DepositCount": 288391, "FirstDepositsAmount": 10472, "ActiveCustomers": 38099},
        {"Periodo": "March/26", "Bet": 48191498.12, "Ggr": 1160442.75, "AccountingRevenue": 618998.36, "DepositAmount": 8822688.35, "DepositCount": 259159, "FirstDepositsAmount": 10226, "ActiveCustomers": 35965}
    ]

    df = pd.DataFrame(dataset_bruto)
    
    df['NGR'] = df['AccountingRevenue']
    df['BonusCost'] = df['Ggr'] - df['AccountingRevenue']
    df['Hold_Pct'] = (df['Ggr'] / df['Bet'] * 100).round(2)
    df['Bonus_Ratio'] = (df['BonusCost'] / df['Ggr'] * 100).round(2)
    
    ordem_original = [
        "February/25", "March/25", "April/25", "May/25", "June/25", "July/25", 
        "August/25", "September/25", "October/25", "November/25", "December/25", 
        "January/26", "February/26", "March/26"
    ]
    df['Periodo'] = pd.Categorical(df['Periodo'], categories=ordem_original, ordered=True)
    df = df.sort_values('Periodo').reset_index(drop=True)

    for col in ['Bet', 'Ggr', 'NGR', 'DepositAmount', 'ActiveCustomers', 'FirstDepositsAmount']:
        df[f'Delta_{col}_Pct'] = df[col].pct_change() * 100
        df[f'Delta_{col}_Abs'] = df[col].diff()
    
    cols_numericas = df.select_dtypes(include=[np.number]).columns
    df[cols_numericas] = df[cols_numericas].fillna(0)
    
    df_mercado = pd.DataFrame({
        "Periodo": ordem_original,
        "Market_Index": [95.0, 98.0, 102.0, 99.0, 105.0, 108.0, 101.0, 97.0, 100.0, 105.5, 115.0, 92.0, 88.0, 81.0]
    })
    
    return df, df_mercado

df_audit, df_mercado = carregar_motor_estatistico()

AFFILIATE_MONETARY_DIVISOR = 10000.0
AFFILIATE_MONETARY_COLUMNS = [
    "Net Revenue",
    "Revenue Share Reward",
    "CPA Reward",
    "FIXED FEE",
    "Total Reward"
]

# ==============================================================================
# 2.1 ETL ENGINE (MICRO): AFFILIATE DATA PROCESSOR (NEW MODULE)
# ==============================================================================

@st.cache_data(show_spinner="PROCESSING AFFILIATE MATRIX...")
def carregar_motor_afiliados():
    raw_affiliates_janeiro = [
        {"Periodo": "January/26", "Affiliate ID": "654570", "Affiliate Name": "Moveup Media Brasil ltda", "FTD": 96, "Net Revenue": 1216105.228, "Revenue Share Reward": 364828.60, "CPA Reward": 111600.00, "FIXED FEE": 0.0, "Total Reward": 476428.60},
        {"Periodo": "January/26", "Affiliate ID": "654495", "Affiliate Name": "YGA Ventures Ltd", "FTD": 399, "Net Revenue": 3218195.711, "Revenue Share Reward": 1609097.90, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 1609097.90},
        {"Periodo": "January/26", "Affiliate ID": "654514", "Affiliate Name": "North Star Network", "FTD": 271, "Net Revenue": 1900693.19, "Revenue Share Reward": 665242.60, "CPA Reward": 0.0, "FIXED FEE": 1334757.40, "Total Reward": 2000000.00},
        {"Periodo": "January/26", "Affiliate ID": "654634", "Affiliate Name": "Influx Online", "FTD": 27, "Net Revenue": 806765.384, "Revenue Share Reward": 242026.60, "CPA Reward": 43200.00, "FIXED FEE": 0.0, "Total Reward": 285226.60},
        {"Periodo": "January/26", "Affiliate ID": "654429", "Affiliate Name": "GNY / Streamer", "FTD": 34, "Net Revenue": 966416.935, "Revenue Share Reward": 289925.10, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 289925.10},
        {"Periodo": "January/26", "Affiliate ID": "654430", "Affiliate Name": "Xioguto / Streamer", "FTD": 2, "Net Revenue": 359376.354, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 0.0},
        {"Periodo": "January/26", "Affiliate ID": "654487", "Affiliate Name": "Armoni Solucoes e Intermediacoes em Negocios Web", "FTD": 6, "Net Revenue": 830025.384, "Revenue Share Reward": 249007.60, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 249007.60},
        {"Periodo": "January/26", "Affiliate ID": "654476", "Affiliate Name": "Markola", "FTD": 19, "Net Revenue": 539155.799, "Revenue Share Reward": 161743.70, "CPA Reward": 40800.00, "FIXED FEE": 0.0, "Total Reward": 202543.70},
        {"Periodo": "January/26", "Affiliate ID": "654553", "Affiliate Name": "EMPREENDEDOR VISIONARIO TREINAMENTOS EIRELI ME", "FTD": 27, "Net Revenue": 521595.296, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 600000.00, "Total Reward": 600000.00},
        {"Periodo": "January/26", "Affiliate ID": "654604", "Affiliate Name": "League of Entertainment", "FTD": 42, "Net Revenue": 764335.562, "Revenue Share Reward": 229300.70, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 229300.70},
        {"Periodo": "January/26", "Affiliate ID": "654825", "Affiliate Name": "Playhill Brasil Ltda", "FTD": 13, "Net Revenue": -37141.224, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 0.0},
        {"Periodo": "January/26", "Affiliate ID": "654828", "Affiliate Name": "Talking & Gaming", "FTD": 19, "Net Revenue": 443151.076, "Revenue Share Reward": 132942.30, "CPA Reward": 12000.00, "FIXED FEE": 0.0, "Total Reward": 144942.30},
        {"Periodo": "January/26", "Affiliate ID": "654649", "Affiliate Name": "abratabaca", "FTD": 273, "Net Revenue": -259292.988, "Revenue Share Reward": 0.0, "CPA Reward": 199200.00, "FIXED FEE": 0.0, "Total Reward": 199200.00},
        {"Periodo": "January/26", "Affiliate ID": "654503", "Affiliate Name": "souograndi", "FTD": 7, "Net Revenue": 247665.185, "Revenue Share Reward": 12383.30, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 12383.30},
        {"Periodo": "January/26", "Affiliate ID": "654547", "Affiliate Name": "nokainlive", "FTD": 3, "Net Revenue": 46999.613, "Revenue Share Reward": 14096.90, "CPA Reward": 3600.00, "FIXED FEE": 0.0, "Total Reward": 17696.90},
        {"Periodo": "January/26", "Affiliate ID": "654433", "Affiliate Name": "Binao", "FTD": 54, "Net Revenue": 116458.959, "Revenue Share Reward": 29112.20, "CPA Reward": 32400.00, "FIXED FEE": 0.0, "Total Reward": 61512.20},
        {"Periodo": "January/26", "Affiliate ID": "654446", "Affiliate Name": "FABINHO AEP PRODUCAO DE VIDEOS LTDA", "FTD": 15, "Net Revenue": 366722.089, "Revenue Share Reward": 36672.20, "CPA Reward": 0.0, "FIXED FEE": 203327.80, "Total Reward": 240000.00},
        {"Periodo": "January/26", "Affiliate ID": "654614", "Affiliate Name": "Bieldomaul", "FTD": 0, "Net Revenue": 52.0308, "Revenue Share Reward": 12.76, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 12.76},
        {"Periodo": "January/26", "Affiliate ID": "654691", "Affiliate Name": "afiliado@betpass.me", "FTD": 29, "Net Revenue": -3237.959, "Revenue Share Reward": 0.0, "CPA Reward": 2340.00, "FIXED FEE": 0.0, "Total Reward": 2340.00},
        {"Periodo": "January/26", "Affiliate ID": "654440", "Affiliate Name": "FURIAGAMES", "FTD": 41, "Net Revenue": -151890.6761, "Revenue Share Reward": 4773.90, "CPA Reward": 2880.00, "FIXED FEE": 0.0, "Total Reward": 3357.39},
        {"Periodo": "January/26", "Affiliate ID": "654546", "Affiliate Name": "Pay Instituicao de Pagamento S/A", "FTD": 5, "Net Revenue": -223512.10, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 0.0},
        {"Periodo": "January/26", "Affiliate ID": "654543", "Affiliate Name": "Ninjabet", "FTD": 2, "Net Revenue": -54409.789, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 0.0},
        {"Periodo": "January/26", "Affiliate ID": "654544", "Affiliate Name": "Klauslol", "FTD": 14, "Net Revenue": 22720.984, "Revenue Share Reward": 7948.80, "CPA Reward": 21600.00, "FIXED FEE": 0.0, "Total Reward": 29548.80},
        {"Periodo": "January/26", "Affiliate ID": "655459", "Affiliate Name": "Partners", "FTD": 0, "Net Revenue": 0.0, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 0.0},
        {"Periodo": "January/26", "Affiliate ID": "655266", "Affiliate Name": "VOLTZ AFFILIATES BR", "FTD": 1, "Net Revenue": -250.85, "Revenue Share Reward": 0.0, "CPA Reward": 1800.00, "FIXED FEE": 0.0, "Total Reward": 1800.00},
        {"Periodo": "January/26", "Affiliate ID": "655372", "Affiliate Name": "Cassius Ogro", "FTD": 1, "Net Revenue": 2387.573, "Revenue Share Reward": 594.40, "CPA Reward": 1200.00, "FIXED FEE": 0.0, "Total Reward": 1794.40},
        {"Periodo": "January/26", "Affiliate ID": "654824", "Affiliate Name": "OC GROUP TECNOLOGIA DA INFORMACAO LTDA", "FTD": 15, "Net Revenue": 25821.173, "Revenue Share Reward": 7743.40, "CPA Reward": 12000.00, "FIXED FEE": 0.0, "Total Reward": 19743.40},
        {"Periodo": "January/26", "Affiliate ID": "654830", "Affiliate Name": "pichucas", "FTD": 3, "Net Revenue": 107214.406, "Revenue Share Reward": 26801.10, "CPA Reward": 9000.00, "FIXED FEE": 0.0, "Total Reward": 35801.10},
        {"Periodo": "January/26", "Affiliate ID": "654551", "Affiliate Name": "Carlos Figueira MMA", "FTD": 53, "Net Revenue": 83077.796, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 50000.00, "Total Reward": 50000.00}
    ]

    raw_affiliates_fevereiro = [
        {"Affiliate ID": "654487", "Affiliate Name": "Armoni Solucoes", "FTD": 1, "Net Revenue": 64401437.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 64401437.00, "Total Reward": 64401437.00},
        {"Affiliate ID": "654433", "Affiliate Name": "Binao", "FTD": 17, "Net Revenue": 50379641.00, "Revenue Share Reward": 12592410.00, "CPA Reward": 12000000.00, "FIXED FEE": 0.0, "Total Reward": 24592410.00},
        {"Affiliate ID": "654518", "Affiliate Name": "Click Hunters", "FTD": 4, "Net Revenue": 14473912.00, "Revenue Share Reward": 3615978.00, "CPA Reward": 4800000.00, "FIXED FEE": 0.0, "Total Reward": 8415978.00},
        {"Affiliate ID": "654553", "Affiliate Name": "EMPREENDEDOR VISIONARIO", "FTD": 36, "Net Revenue": 543670150.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 600000000.00, "Total Reward": 600000000.00},
        {"Affiliate ID": "654446", "Affiliate Name": "FABINHO AEP", "FTD": 12, "Net Revenue": 116523479.00, "Revenue Share Reward": 11652348.00, "CPA Reward": 0.0, "FIXED FEE": 228347652.00, "Total Reward": 240000000.00},
        {"Affiliate ID": "654567", "Affiliate Name": "GRP Publicidade", "FTD": 17, "Net Revenue": 187691051.00, "Revenue Share Reward": 56307315.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 56307315.00},
        {"Affiliate ID": "654488", "Affiliate Name": "GUEDES TIPS", "FTD": 94, "Net Revenue": -45533818.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 900000000.00, "Total Reward": 900000000.00},
        {"Affiliate ID": "654954", "Affiliate Name": "INNOVATION LABS", "FTD": 4, "Net Revenue": -4914678.00, "Revenue Share Reward": 0.0, "CPA Reward": 4800000.00, "FIXED FEE": 0.0, "Total Reward": 4800000.00},
        {"Affiliate ID": "654538", "Affiliate Name": "Laerte Viana", "FTD": 20, "Net Revenue": 101310224.00, "Revenue Share Reward": 25327556.00, "CPA Reward": 0.0, "FIXED FEE": 244672444.00, "Total Reward": 270000000.00},
        {"Affiliate ID": "654570", "Affiliate Name": "Moveup Media", "FTD": 58, "Net Revenue": 756132660.00, "Revenue Share Reward": 226836798.00, "CPA Reward": 63000000.00, "FIXED FEE": 0.0, "Total Reward": 289836798.00},
        {"Affiliate ID": "654872", "Affiliate Name": "Better Collective", "FTD": 1, "Net Revenue": 1349430.00, "Revenue Share Reward": 539772.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 539772.00},
        {"Affiliate ID": "654678", "Affiliate Name": "Cacique Ads", "FTD": 0, "Net Revenue": 317245.00, "Revenue Share Reward": 76811.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 76811.00},
        {"Affiliate ID": "654461", "Affiliate Name": "Better Collective", "FTD": 3, "Net Revenue": 3917280.00, "Revenue Share Reward": 1801949.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 1801949.00},
        {"Affiliate ID": "654462", "Affiliate Name": "Better Collective", "FTD": 2, "Net Revenue": 18323434.00, "Revenue Share Reward": 8428780.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 8428780.00},
        {"Affiliate ID": "654463", "Affiliate Name": "Better Collective", "FTD": 5, "Net Revenue": 66191882.00, "Revenue Share Reward": 30448266.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 30448266.00},
        {"Affiliate ID": "654464", "Affiliate Name": "Better Collective", "FTD": 9, "Net Revenue": 56923570.00, "Revenue Share Reward": 26184842.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 26184842.00},
        {"Affiliate ID": "654466", "Affiliate Name": "Better Collective", "FTD": 1, "Net Revenue": 917089.00, "Revenue Share Reward": 421861.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 421861.00},
        {"Affiliate ID": "655266", "Affiliate Name": "VOLTZ AFFILIATES", "FTD": 2, "Net Revenue": 247757.00, "Revenue Share Reward": 71327.00, "CPA Reward": 1800000.00, "FIXED FEE": 0.0, "Total Reward": 1871327.00},
        {"Affiliate ID": "655493", "Affiliate Name": "V1NNI SUB", "FTD": 0, "Net Revenue": 0.0, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 2938561.00, "Total Reward": 2938561.00},
        {"Affiliate ID": "655501", "Affiliate Name": "Leeboy", "FTD": 10, "Net Revenue": 986024.00, "Revenue Share Reward": 292807.00, "CPA Reward": 14400000.00, "FIXED FEE": 0.0, "Total Reward": 14692807.00},
        {"Affiliate ID": "655466", "Affiliate Name": "Ferrer", "FTD": 0, "Net Revenue": 0.0, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 350000000.00, "Total Reward": 350000000.00},
        {"Affiliate ID": "655468", "Affiliate Name": "BMBR MEDIA", "FTD": 1, "Net Revenue": 1360032.00, "Revenue Share Reward": 405010.00, "CPA Reward": 1800000.00, "FIXED FEE": 0.0, "Total Reward": 2205010.00},
        {"Affiliate ID": "655459", "Affiliate Name": "Partners", "FTD": 184, "Net Revenue": 13802623.00, "Revenue Share Reward": 4137787.00, "CPA Reward": 168000000.00, "FIXED FEE": 0.0, "Total Reward": 172137787.00},
        {"Affiliate ID": "654508", "Affiliate Name": "Bigxrdm", "FTD": 1, "Net Revenue": 193615031.00, "Revenue Share Reward": 38723006.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 38723006.00},
        {"Affiliate ID": "654515", "Affiliate Name": "Pay Instituição", "FTD": 2, "Net Revenue": 44975223.00, "Revenue Share Reward": 13492567.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 13492567.00},
        {"Affiliate ID": "654521", "Affiliate Name": "DANILLO TACQUES", "FTD": 0, "Net Revenue": 954553.00, "Revenue Share Reward": 47728.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 47728.00},
        {"Affiliate ID": "654492", "Affiliate Name": "João Victor", "FTD": 6, "Net Revenue": 87926795.00, "Revenue Share Reward": 6272894.00, "CPA Reward": 18000000.00, "FIXED FEE": 0.0, "Total Reward": 24272894.00},
        {"Affiliate ID": "654499", "Affiliate Name": "SUPER LUTAS", "FTD": 0, "Net Revenue": 31462177.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 200000000.00, "Total Reward": 200000000.00},
        {"Affiliate ID": "654502", "Affiliate Name": "cicero kardeck", "FTD": 32, "Net Revenue": 54474447.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 300000000.00, "Total Reward": 300000000.00},
        {"Affiliate ID": "654503", "Affiliate Name": "souograndi", "FTD": 4, "Net Revenue": 880093242.00, "Revenue Share Reward": 44004662.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 44004662.00},
        {"Affiliate ID": "654469", "Affiliate Name": "OC GROUP", "FTD": 2, "Net Revenue": -338085.00, "Revenue Share Reward": 0.0, "CPA Reward": 2400000.00, "FIXED FEE": 0.0, "Total Reward": 2400000.00},
        {"Affiliate ID": "654470", "Affiliate Name": "Marciomvt", "FTD": 2, "Net Revenue": 82429307.00, "Revenue Share Reward": 24725792.00, "CPA Reward": 2400000.00, "FIXED FEE": 0.0, "Total Reward": 27125792.00},
        {"Affiliate ID": "654476", "Affiliate Name": "Markola", "FTD": 12, "Net Revenue": 103290702.00, "Revenue Share Reward": 30984211.00, "CPA Reward": 24000000.00, "FIXED FEE": 0.0, "Total Reward": 54984211.00},
        {"Affiliate ID": "654481", "Affiliate Name": "Rita de Cássia", "FTD": 0, "Net Revenue": 390500.00, "Revenue Share Reward": 19525.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 19525.00},
        {"Affiliate ID": "655372", "Affiliate Name": "Cassius Ogro", "FTD": 1, "Net Revenue": 6667113.00, "Revenue Share Reward": 1664278.00, "CPA Reward": 2400000.00, "FIXED FEE": 0.0, "Total Reward": 4064278.00},
        {"Affiliate ID": "655339", "Affiliate Name": "Matheus Claudio", "FTD": 0, "Net Revenue": 77662.00, "Revenue Share Reward": 13532.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 13532.00},
        {"Affiliate ID": "655314", "Affiliate Name": "SpiderKong", "FTD": 0, "Net Revenue": 233100.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 160000000.00, "Total Reward": 160000000.00},
        {"Affiliate ID": "654936", "Affiliate Name": "PremiaBet", "FTD": 129, "Net Revenue": 10731813.00, "Revenue Share Reward": 3216544.00, "CPA Reward": 100800000.00, "FIXED FEE": 0.0, "Total Reward": 104016544.00},
        {"Affiliate ID": "655297", "Affiliate Name": "luizhriqe", "FTD": 0, "Net Revenue": 241475.00, "Revenue Share Reward": 57869.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 57869.00},
        {"Affiliate ID": "655230", "Affiliate Name": "E-2 Comunicações", "FTD": 0, "Net Revenue": 41670219.00, "Revenue Share Reward": 12498066.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 12498066.00},
        {"Affiliate ID": "655431", "Affiliate Name": "MMALAB", "FTD": 1, "Net Revenue": 630814.00, "Revenue Share Reward": 189244.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 189244.00},
        {"Affiliate ID": "654632", "Affiliate Name": "Papodeaposta", "FTD": 0, "Net Revenue": 7260945.00, "Revenue Share Reward": 1812736.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 1812736.00},
        {"Affiliate ID": "654633", "Affiliate Name": "itsubiel", "FTD": 2, "Net Revenue": 8495332.00, "Revenue Share Reward": 2548600.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 2548600.00},
        {"Affiliate ID": "655182", "Affiliate Name": "Clean Monster", "FTD": 9, "Net Revenue": -6514200.00, "Revenue Share Reward": 0.0, "CPA Reward": 7200000.00, "FIXED FEE": 0.0, "Total Reward": 7200000.00},
        {"Affiliate ID": "655121", "Affiliate Name": "nbr050", "FTD": 28, "Net Revenue": -1886735.00, "Revenue Share Reward": 0.0, "CPA Reward": 19800000.00, "FIXED FEE": 0.0, "Total Reward": 19800000.00},
        {"Affiliate ID": "654824", "Affiliate Name": "OC GROUP", "FTD": 11, "Net Revenue": 2845185.00, "Revenue Share Reward": 850556.00, "CPA Reward": 10800000.00, "FIXED FEE": 0.0, "Total Reward": 11650556.00},
        {"Affiliate ID": "654825", "Affiliate Name": "Playhill Brasil", "FTD": 12, "Net Revenue": 404928143.00, "Revenue Share Reward": 121478443.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 121478443.00},
        {"Affiliate ID": "654828", "Affiliate Name": "Talking & Gaming", "FTD": 27, "Net Revenue": 387196208.00, "Revenue Share Reward": 118269652.00, "CPA Reward": 6000000.00, "FIXED FEE": 0.0, "Total Reward": 124269652.00},
        {"Affiliate ID": "654830", "Affiliate Name": "pichucas", "FTD": 0, "Net Revenue": 36671829.00, "Revenue Share Reward": 9165457.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 9165457.00},
        {"Affiliate ID": "654833", "Affiliate Name": "ORafael", "FTD": 0, "Net Revenue": 579438.00, "Revenue Share Reward": 170831.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 170831.00},
        {"Affiliate ID": "654691", "Affiliate Name": "afiliado@betpass.me", "FTD": 20, "Net Revenue": -2563698.00, "Revenue Share Reward": 0.0, "CPA Reward": 16200000.00, "FIXED FEE": 0.0, "Total Reward": 16200000.00},
        {"Affiliate ID": "654649", "Affiliate Name": "abratabaca", "FTD": 200, "Net Revenue": 303628422.00, "Revenue Share Reward": 75904606.00, "CPA Reward": 188400000.00, "FIXED FEE": 0.0, "Total Reward": 264304606.00},
        {"Affiliate ID": "654628", "Affiliate Name": "DenysTIPS", "FTD": 1, "Net Revenue": 2345955.00, "Revenue Share Reward": 583989.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 583989.00},
        {"Affiliate ID": "654614", "Affiliate Name": "Bieldomaul", "FTD": 0, "Net Revenue": -7863616.00, "Revenue Share Reward": 0.0, "CPA Reward": 1800000.00, "FIXED FEE": 0.0, "Total Reward": 1800000.00},
        {"Affiliate ID": "654546", "Affiliate Name": "Pay Instituição", "FTD": 2, "Net Revenue": 197864181.00, "Revenue Share Reward": 59359254.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 59359254.00},
        {"Affiliate ID": "654547", "Affiliate Name": "nokainlive", "FTD": 0, "Net Revenue": 7664874.00, "Revenue Share Reward": 2296462.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 2296462.00},
        {"Affiliate ID": "654548", "Affiliate Name": "TipMiner", "FTD": 2, "Net Revenue": 3010210.00, "Revenue Share Reward": 600042.00, "CPA Reward": 1200000.00, "FIXED FEE": 0.0, "Total Reward": 1800042.00},
        {"Affiliate ID": "654551", "Affiliate Name": "Carlos Figueira", "FTD": 19, "Net Revenue": 40206508.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 50000000.00, "Total Reward": 50000000.00},
        {"Affiliate ID": "654529", "Affiliate Name": "BetinGamer", "FTD": 3, "Net Revenue": -41813000.00, "Revenue Share Reward": 0.0, "CPA Reward": 3600000.00, "FIXED FEE": 0.0, "Total Reward": 3600000.00},
        {"Affiliate ID": "654530", "Affiliate Name": "kmarguin Qashback", "FTD": 0, "Net Revenue": 117817624.00, "Revenue Share Reward": 23563525.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 23563525.00}
    ]

    raw_affiliates_marco = [
        {"Affiliate ID": "654429", "Affiliate Name": "GNY / Streamer", "FTD": 20, "Net Revenue": 942222354.00, "Revenue Share Reward": 281977224.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 281977224.00},
        {"Affiliate ID": "654495", "Affiliate Name": "YGA Ventures Ltd", "FTD": 374, "Net Revenue": 1277177484.00, "Revenue Share Reward": 637511608.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 637511608.00},
        {"Affiliate ID": "654553", "Affiliate Name": "EMPREENDEDOR VISIONARIO TREINAMENTOS EIRELI ME", "FTD": 40, "Net Revenue": 583741711.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 600000000.00, "Total Reward": 600000000.00},
        {"Affiliate ID": "654570", "Affiliate Name": "Moveup Media Brasil ltda", "FTD": 48, "Net Revenue": 462754505.00, "Revenue Share Reward": 138823862.00, "CPA Reward": 54000000.00, "FIXED FEE": 0.0, "Total Reward": 192823862.00},
        {"Affiliate ID": "654476", "Affiliate Name": "Markola", "FTD": 9, "Net Revenue": 404048847.00, "Revenue Share Reward": 120297439.00, "CPA Reward": 12000000.00, "FIXED FEE": 0.0, "Total Reward": 132297439.00},
        {"Affiliate ID": "654825", "Affiliate Name": "Playhill Brasil Ltda", "FTD": 7, "Net Revenue": 216696486.00, "Revenue Share Reward": 65008946.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 65008946.00},
        {"Affiliate ID": "654859", "Affiliate Name": "SonnyNg", "FTD": 3, "Net Revenue": 202104726.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 0.0},
        {"Affiliate ID": "654440", "Affiliate Name": "FURIAGAMES", "FTD": 8, "Net Revenue": 455464809.00, "Revenue Share Reward": 136642839.00, "CPA Reward": 6000000.00, "FIXED FEE": 0.0, "Total Reward": 142642839.00},
        {"Affiliate ID": "655034", "Affiliate Name": "TODOS JUNTOS SAS", "FTD": 60, "Net Revenue": 390258451.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 0.0},
        {"Affiliate ID": "654508", "Affiliate Name": "Bigxrdm", "FTD": 7, "Net Revenue": 167049186.00, "Revenue Share Reward": 33409837.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 33409837.00},
        {"Affiliate ID": "654514", "Affiliate Name": "North Star Network", "FTD": 214, "Net Revenue": -540879195.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 0.0},
        {"Affiliate ID": "654447", "Affiliate Name": "Psouza7", "FTD": 13, "Net Revenue": 161198186.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 0.0},
        {"Affiliate ID": "654621", "Affiliate Name": "Cartolouco", "FTD": 11, "Net Revenue": -100988927.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 0.0},
        {"Affiliate ID": "654613", "Affiliate Name": "Skores", "FTD": 1, "Net Revenue": 587493231.00, "Revenue Share Reward": 176247969.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 176247969.00},
        {"Affiliate ID": "654604", "Affiliate Name": "League of Entertainment", "FTD": 29, "Net Revenue": 107550358.00, "Revenue Share Reward": 32265107.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 32265107.00},
        {"Affiliate ID": "655520", "Affiliate Name": "Arena Afiliados LTDA", "FTD": 845, "Net Revenue": 33152938.00, "Revenue Share Reward": 11600028.00, "CPA Reward": 1095000000.00, "FIXED FEE": 0.0, "Total Reward": 1106600028.00},
        {"Affiliate ID": "655516", "Affiliate Name": "Dk Company", "FTD": 812, "Net Revenue": 47086452.00, "Revenue Share Reward": 14122936.00, "CPA Reward": 112500000.00, "FIXED FEE": 0.0, "Total Reward": 126622936.00},
        {"Affiliate ID": "655522", "Affiliate Name": "BlackBox", "FTD": 215, "Net Revenue": 13248264.00, "Revenue Share Reward": 3974479.00, "CPA Reward": 144000000.00, "FIXED FEE": 0.0, "Total Reward": 147974479.00},
        {"Affiliate ID": "654433", "Affiliate Name": "Binao", "FTD": 28, "Net Revenue": 59365972.00, "Revenue Share Reward": 14838993.00, "CPA Reward": 22800000.00, "FIXED FEE": 0.0, "Total Reward": 37638993.00},
        {"Affiliate ID": "655459", "Affiliate Name": "Partners", "FTD": 120, "Net Revenue": 12168979.00, "Revenue Share Reward": 3647694.00, "CPA Reward": 140400000.00, "FIXED FEE": 0.0, "Total Reward": 144047694.00},
        {"Affiliate ID": "654691", "Affiliate Name": "afiliado@betpass.me", "FTD": 52, "Net Revenue": 573310.00, "Revenue Share Reward": 140828.00, "CPA Reward": 66600000.00, "FIXED FEE": 0.0, "Total Reward": 66740828.00},
        {"Affiliate ID": "654649", "Affiliate Name": "abratabaca", "FTD": 244, "Net Revenue": 135875981.00, "Revenue Share Reward": 33966495.00, "CPA Reward": 178800000.00, "FIXED FEE": 0.0, "Total Reward": 212766495.00},
        {"Affiliate ID": "654825", "Affiliate Name": "Playhill Brasil Ltda SEO", "FTD": 0, "Net Revenue": 722200.00, "Revenue Share Reward": 216660.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 216660.00},
        {"Affiliate ID": "654936", "Affiliate Name": "PremiaBet", "FTD": 131, "Net Revenue": 23442990.00, "Revenue Share Reward": 7029897.00, "CPA Reward": 153000000.00, "FIXED FEE": 0.0, "Total Reward": 160029897.00},
        {"Affiliate ID": "654824", "Affiliate Name": "OC GROUP TECNOLOGIA DA INFORMACAO LTDA", "FTD": 6, "Net Revenue": -66671369.00, "Revenue Share Reward": 0.0, "CPA Reward": 8400000.00, "FIXED FEE": 0.0, "Total Reward": 8400000.00},
        {"Affiliate ID": "654828", "Affiliate Name": "Talking & Gaming", "FTD": 11, "Net Revenue": 42410387.00, "Revenue Share Reward": 18421105.00, "CPA Reward": 3600000.00, "FIXED FEE": 0.0, "Total Reward": 22021105.00},
        {"Affiliate ID": "654830", "Affiliate Name": "pichucas", "FTD": 0, "Net Revenue": 31317820.00, "Revenue Share Reward": 7826955.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 7826955.00},
        {"Affiliate ID": "654446", "Affiliate Name": "FABINHO AEP PRODUCAO DE VIDEOS LTDA", "FTD": 5, "Net Revenue": -23321498.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 240000000.00, "Total Reward": 240000000.00},
        {"Affiliate ID": "654488", "Affiliate Name": "GUEDES TIPS LTDA", "FTD": 191, "Net Revenue": 126931790.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 900000000.00, "Total Reward": 900000000.00},
        {"Affiliate ID": "655466", "Affiliate Name": "Ferrer", "FTD": 0, "Net Revenue": 0.0, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 350000000.00, "Total Reward": 350000000.00},
        {"Affiliate ID": "655314", "Affiliate Name": "SpiderKong", "FTD": 0, "Net Revenue": -0.1700, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 160000000.00, "Total Reward": 160000000.00},
        {"Affiliate ID": "654551", "Affiliate Name": "Carlos Figueira MMA", "FTD": 16, "Net Revenue": -40732220.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 50000000.00, "Total Reward": 50000000.00},
        {"Affiliate ID": "654478", "Affiliate Name": "Coutinho", "FTD": 27, "Net Revenue": -32480141.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 0.0},
        {"Affiliate ID": "654792", "Affiliate Name": "Daniel Fortune", "FTD": 6, "Net Revenue": -26976777.00, "Revenue Share Reward": 0.0, "CPA Reward": 10800000.00, "FIXED FEE": 0.0, "Total Reward": 10800000.00},
        {"Affiliate ID": "654634", "Affiliate Name": "Influx Online", "FTD": 17, "Net Revenue": -128027320.00, "Revenue Share Reward": 0.0, "CPA Reward": 25200000.00, "FIXED FEE": 0.0, "Total Reward": 25200000.00},
        {"Affiliate ID": "655182", "Affiliate Name": "Clean Monster", "FTD": 3, "Net Revenue": -1385547.00, "Revenue Share Reward": 0.0, "CPA Reward": 3600000.00, "FIXED FEE": 0.0, "Total Reward": 3600000.00},
        {"Affiliate ID": "655121", "Affiliate Name": "nbr050", "FTD": 61, "Net Revenue": 71745374.00, "Revenue Share Reward": 21520612.00, "CPA Reward": 57600000.00, "FIXED FEE": 0.0, "Total Reward": 79120612.00},
        {"Affiliate ID": "654469", "Affiliate Name": "OC GROUP", "FTD": 4, "Net Revenue": 2847777.00, "Revenue Share Reward": 993222.00, "CPA Reward": 2400000.00, "FIXED FEE": 0.0, "Total Reward": 3393222.00},
        {"Affiliate ID": "654470", "Affiliate Name": "Marciomvt", "FTD": 1, "Net Revenue": 71703317.00, "Revenue Share Reward": 21507995.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 21507995.00},
        {"Affiliate ID": "654502", "Affiliate Name": "cicero kardeck rocha de lima/KROCHA", "FTD": 22, "Net Revenue": 167568924.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 300000000.00, "Total Reward": 300000000.00},
        {"Affiliate ID": "654503", "Affiliate Name": "souograndi", "FTD": 5, "Net Revenue": 11700331.00, "Revenue Share Reward": 585017.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 585017.00},
        {"Affiliate ID": "654504", "Affiliate Name": "Playhill Brasil Ltda MB", "FTD": 6, "Net Revenue": 135461192.00, "Revenue Share Reward": 40396303.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 40396303.00},
        {"Affiliate ID": "654515", "Affiliate Name": "Pay Instituição de Pagamento S/A", "FTD": 1, "Net Revenue": 61585758.00, "Revenue Share Reward": 18475727.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 18475727.00},
        {"Affiliate ID": "654546", "Affiliate Name": "Pay Instituição de Pagamento S/A 1", "FTD": 6, "Net Revenue": 51413716.00, "Revenue Share Reward": 15313314.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 15313314.00},
        {"Affiliate ID": "654567", "Affiliate Name": "GRP Publicidade Digital Ltda", "FTD": 26, "Net Revenue": 92779717.00, "Revenue Share Reward": 27833915.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 27833915.00},
        {"Affiliate ID": "654568", "Affiliate Name": "Izabellaflu", "FTD": 0, "Net Revenue": 43132420.00, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 0.0},
        {"Affiliate ID": "654454", "Affiliate Name": "Diretasso", "FTD": 11, "Net Revenue": 126898387.00, "Revenue Share Reward": 25368743.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 25368743.00},
        {"Affiliate ID": "654456", "Affiliate Name": "Gusttawin", "FTD": 1, "Net Revenue": 46126219.00, "Revenue Share Reward": 4612622.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 4612622.00},
        {"Affiliate ID": "654459", "Affiliate Name": "Better Collective Brazil Ltda BCCPH22BR", "FTD": 46, "Net Revenue": 58687732.00, "Revenue Share Reward": 27117643.00, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 27117643.00}
    ]

    for row in raw_affiliates_fevereiro: row["Periodo"] = "February/26"
    for row in raw_affiliates_marco: row["Periodo"] = "March/26"

    df_aff = pd.DataFrame(raw_affiliates_janeiro + raw_affiliates_fevereiro + raw_affiliates_marco)

    mask_bruto = df_aff["Periodo"].isin(["February/26", "March/26"])
    for col in AFFILIATE_MONETARY_COLUMNS:
        df_aff[col] = pd.to_numeric(df_aff[col], errors="coerce").fillna(0)
        df_aff.loc[mask_bruto, col] = df_aff.loc[mask_bruto, col] / AFFILIATE_MONETARY_DIVISOR

    return df_aff

df_afiliados = carregar_motor_afiliados()

# ==============================================================================
# 3. EXECUTIVE INTERFACE: SENIOR CONSULTING REPORT
# ==============================================================================
if df_audit is not None and not df_audit.empty:
    
    col_h1, col_h2 = st.columns([3, 1])
    with col_h1:
        st.title("🏦 STRATEGIC FINANCE ANALYSIS")
        st.markdown(f"**Confidential | Extraction Date:** {datetime.datetime.now().strftime('%m/%d/%Y')} | **Status:** Cycle FEB/25 - MAR/26")
    with col_h2:
        st.markdown("""
            <div style='text-align:right; margin-top:15px;'>
                <span style='background-color:#F43F5E; color:#fff; padding:6px 16px; border-radius:6px; font-weight:bold; font-size:0.8rem; letter-spacing:1px; box-shadow: 0 4px 12px rgba(244, 63, 94, 0.4);'>
                CRITICAL PERFORMANCE REVIEW
                </span>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border-top: 2px solid #334155; margin-top: 5px; margin-bottom: 30px;'>", unsafe_allow_html=True)
    
    st.sidebar.markdown("<h2 style='color:#FFFFFF; font-weight:800; font-size:1.4rem; margin-bottom:10px;'>INDEX</h2>", unsafe_allow_html=True)
    menu = st.sidebar.radio("", [
        "1. Executive Summary & Alerts",
        "2. Macro-Trends & Dynamic Analytics",
        "3. Operational Deep-Dive (Monthly)",
        "4. Market Share & Unit Economics",
        "5. Affiliate Performance (Top/Bottom 20)",
        "6. Brazil Finance Outlook"
    ])
    
    st.sidebar.markdown("<hr style='border-top: 1px dashed #334155;'>", unsafe_allow_html=True)
    
    ult = df_audit.iloc[-1]

    if menu == "1. Executive Summary & Alerts":
        st.markdown("<h2 class='section-title'>1. Cycle Diagnosis (Feb/25 - Mar/26)</h2>", unsafe_allow_html=True)
        st.markdown(""" 
        <div class='consultant-report'>
        <b>TECHNICAL OPINION: EVOLUTIONARY ANALYSIS BY QUARTERS (Q1/25 to Q1/26)</b><br><br>
        The decomposition of the cycle by quarters reveals the transition from an aggressive traction phase to the current scenario of systemic exhaustion and retraction:<br><br>
        
        <b>▶ Q1 & Q2 2025 (Traction & Scale Phase):</b><br>
        Period marked by strong acquisition. The volume of new users (FTD) reached an all-time peak in April/25 (34k). The Handle (Wagered) scaled rapidly from the $ 75M to $ 86M range, driven by new capital (New Money).<br><br>
        
        <b>▶ Q3 2025 (Plateau & Stabilization):</b><br>
        The wagered volume remained resilient in the $ 83M - $ 86M range. However, the entry of new users fell back to an average of 16k/month. The operation began to rely more on recycling active base capital (retention) than on new entrants.<br><br>

        <b>▶ Q4 2025 (The Illusory Peak & Promotional Trap):</b><br>
        We recorded the historical Handle record in November/25 ($ 95.8M) and the GGR peak in December ($ 3.06M). However, deep analysis shows that this growth was "bought" at the expense of aggressive bonuses. The NGR did not grow in the same geometric proportion as the GGR.<br><br>
        
        <b>▶ Q1 2026 (Structural Retraction & Exhaustion):</b><br>
        The current scenario. A free fall in all liquidity indicators. The Handle plummeted to $ 48.1M in March/26 (half of the Q4 peak). The FTD volume returned to the 10k baseline. The veteran base suffered natural churn and the promotional taps of the past ceased to have an effect.<br><br>

        <i><b>Required Decision:</b> Immediate redirection of 35% of the Retention budget (Bonus) to High-Intent Traffic Acquisition (CPA/Affiliates) to oxygenate the top of the funnel and reverse the Q1/26 retraction.</i>
        </div>
        """, unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        c1.metric("WAGERED (HANDLE)", f"$ {ult['Bet']:,.0f}", f"{ult['Delta_Bet_Pct']:.1f}%")
        c2.metric("GROSS REVENUE (GGR)", f"$ {ult['Ggr']:,.0f}", f"{ult['Delta_Ggr_Pct']:.1f}%")
        c3.metric("NET REVENUE (NGR)", f"$ {ult['NGR']:,.0f}", f"{ult['Delta_NGR_Pct']:.1f}%")
        
        c4, c5, c6 = st.columns(3)
        c4.metric("DEPOSITS", f"$ {ult['DepositAmount']:,.0f}", f"{ult['Delta_DepositAmount_Pct']:.1f}%")
        c5.metric("ACTIVE USERS", f"{ult['ActiveCustomers']:,.0f}", f"{ult['Delta_ActiveCustomers_Pct']:.1f}%")
        c6.metric("CONSOLIDATED HOLD", f"{ult['Hold_Pct']}%", "")

    elif menu == "2. Macro-Trends & Dynamic Analytics":
        st.markdown("<h2 class='section-title'>2. Macro-Trends Dashboard (14 Months)</h2>", unsafe_allow_html=True)
        
        c_g1, c_g2 = st.columns(2)
        with c_g1:
            fig_1 = make_subplots(specs=[[{"secondary_y": True}]])
            fig_1.add_trace(go.Scatter(x=df_audit['Periodo'], y=df_audit['Bet'], name='HANDLE (TURNOVER)', mode='lines+markers+text', line=dict(color='#38BDF8', width=5 )), secondary_y=False)
            fig_1.add_trace(go.Bar(x=df_audit['Periodo'], y=df_audit['Ggr'], name='GGR (GROSS REVENUE)', marker_color='#10B981', opacity=0.9, width=0.6), secondary_y=True)
            fig_1 = aplicar_template_financeiro(fig_1, "Historical Evolution: Volume vs Gross Revenue")
            fig_1.update_yaxes(title_text="<b>HANDLE (Left Side)</b>", color="#FFFFFF", secondary_y=False)
            fig_1.update_yaxes(title_text="<b>GGR (Right Side)</b>", color="#FFFFFF", secondary_y=True)
            st.plotly_chart(fig_1, use_container_width=True)
        
        with c_g2:
            fig_2 = make_subplots(specs=[[{"secondary_y": True}]])
            fig_2.add_trace(go.Bar(x=df_audit['Periodo'], y=df_audit['DepositAmount'], name='DEPOSITS (USD)', marker_color='#8B5CF6'), secondary_y=False)
            fig_2.add_trace(go.Scatter(x=df_audit['Periodo'], y=df_audit['ActiveCustomers'], name='ACTIVE USERS (MAU)', mode='lines+markers', line=dict(color='#F59E0B', width=4)), secondary_y=True)
            fig_2 = aplicar_template_financeiro(fig_2, "Funding Matrix: Deposits vs Users")
            fig_2.update_yaxes(title_text="USD", secondary_y=False)
            fig_2.update_yaxes(title_text="Quantity", secondary_y=True)
            st.plotly_chart(fig_2, use_container_width=True)

        c_g3, c_g4 = st.columns(2)
        with c_g3:
            fig_3 = go.Figure()
            fig_3.add_trace(go.Bar(x=df_audit['Periodo'], y=df_audit['FirstDepositsAmount'], name='FTD (NEW MONEY)', marker_color='#14B8A6'))
            fig_3 = aplicar_template_financeiro(fig_3, "Acquisition Trend (FTD Velocity)")
            st.plotly_chart(fig_3, use_container_width=True)

        with c_g4:
            fig_4 = make_subplots(specs=[[{"secondary_y": True}]])
            fig_4.add_trace(go.Bar(x=df_audit['Periodo'], y=df_audit['BonusCost'], name='BONUS COST', marker_color='#F43F5E'), secondary_y=False)
            fig_4.add_trace(go.Scatter(x=df_audit['Periodo'], y=df_audit['Bonus_Ratio'], name='RATIO %', line=dict(color='#FFFFFF', width=3)), secondary_y=True)
            fig_4 = aplicar_template_financeiro(fig_4, "Promotional Pressure vs Contribution Margin")
            st.plotly_chart(fig_4, use_container_width=True)

        st.markdown("### 📊 Analytical Table: Audited MoM Performance")
        st.dataframe(df_audit[['Periodo', 'Delta_Bet_Pct', 'Delta_Ggr_Pct', 'Delta_DepositAmount_Pct', 'Delta_FirstDepositsAmount_Pct', 'Bonus_Ratio']].style.format(precision=2), use_container_width=True)

    elif menu == "3. Operational Deep-Dive (Monthly)":
        st.markdown("<h2 class='section-title'>3. Monthly Financial Decomposition</h2>", unsafe_allow_html=True)
        st.markdown("""
        <style>
        [data-testid="stMetricValue"] > div {
            font-size: 1.10rem !important;
        }
        [data-testid="stMetricLabel"] > div, [data-testid="stMetricLabel"] * {
            font-size: 0.68rem !important;
            letter-spacing: 0.6px !important;
        }
        .kpi-block {
            padding: 12px !important;
        }
        .kpi-title {
            font-size: 0.82rem !important;
        }
        .kpi-text {
            font-size: 0.72rem !important;
            line-height: 1.32 !important;
        }
        .consultant-report {
            font-size: 0.76rem !important;
            line-height: 1.38 !important;
            padding: 18px 20px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        meses_select = [str(m) for m in df_audit['Periodo'].tolist()]
        mes_foco = st.selectbox("Select the accounting period for analysis:", meses_select)
        d = df_audit[df_audit['Periodo'] == mes_foco].iloc[0]
        
        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2, c3, c4, c5, c6 = st.columns(6)
        c1.metric("Handle", f"$ {d['Bet']:,.0f}", f"{d.get('Delta_Bet_Pct', 0):.1f}%")
        c2.metric("GGR", f"$ {d['Ggr']:,.0f}", f"{d.get('Delta_Ggr_Pct', 0):.1f}%")
        c3.metric("NGR", f"$ {d['NGR']:,.0f}", f"{d.get('Delta_NGR_Pct', 0):.1f}%")
        c4.metric("Deposits", f"$ {d['DepositAmount']:,.0f}", f"{d.get('Delta_DepositAmount_Pct', 0):.1f}%")
        c5.metric("Active Users", f"{d['ActiveCustomers']:,.0f}", f"{d.get('Delta_ActiveCustomers_Pct', 0):.1f}%")
        c6.metric("Margin (Hold)", f"{d['Hold_Pct']}%")

        st.markdown("<br>", unsafe_allow_html=True)
        st.metric("Bonus Ratio (Promotional Cost over GGR)", f"{d['Bonus_Ratio']}%")
        
        st.markdown(f"""
        <div class='kpi-block'>
            <div class='kpi-title'>💸 Acquisition Engine (New Money) vs Promotional Cost</div>
            <div class='kpi-text'>
            <b>New Depositors (FTD):</b> {d['FirstDepositsAmount']:,.0f} units.<br>
            <b>Bonus Cost:</b> $ {d['BonusCost']:,.2f} ({d['Bonus_Ratio']}% of Gross GGR).<br><br>
            <i>The ratio between acquisition and promotional cost reflects the weight of retention investment compared to the actual new money injected into the ecosystem during the selected month.</i>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 📊 Revenue Waterfall (From GGR to NGR)")
        fig_waterfall = go.Figure(go.Waterfall(
            name="20", orientation="v",
            measure=["relative", "relative", "total"],
            x=["GGR (Gross Revenue)", "Bonus Cost / Deductions", "NGR (Net Revenue)"],
            textposition="outside",
            text=[f"$ {d['Ggr']/1e6:.1f}M", f"-$ {d['BonusCost']/1e6:.1f}M", f"$ {d['NGR']/1e6:.1f}M"],
            y=[d['Ggr'], -d['BonusCost'], d['NGR']],
            connector={"line": {"color": "rgb(63, 63, 63)", "width": 2}},
            decreasing={"marker": {"color": "#F43F5E"}},
            increasing={"marker": {"color": "#10B981"}},
            totals={"marker": {"color": "#38BDF8"}}
        ))
        fig_waterfall = aplicar_template_financeiro(fig_waterfall, f"Net Margin Composition - {mes_foco}")
        st.plotly_chart(fig_waterfall, use_container_width=True)
        
        st.markdown(f"""
        <div class='consultant-report'>
        <b>IN-DEPTH DIAGNOSIS OF THE MONTH ({mes_foco.upper()}):</b><br>
        The promotional cost consumed <b>{d['Bonus_Ratio']}%</b> of the GGR. The evolution or retraction in <b>NGR (Net Revenue)</b> signals the direct impact of the promotional escalation vs. the tangible profit of the company after liquidation of active deductions.
        </div>
        """, unsafe_allow_html=True)

    elif menu == "4. Market Share & Unit Economics":
        st.markdown("<h2 class='section-title'>4. Market Benchmark & Unit Economics</h2>", unsafe_allow_html=True)
        base_val = df_audit['Bet'].iloc[0]
        df_audit['Internal_Index'] = (df_audit['Bet'] / base_val) * 100
        
        c_m1, c_m2 = st.columns(2)
        with c_m1:
            figm = go.Figure()
            figm.add_trace(go.Scatter(x=df_mercado['Periodo'], y=df_mercado['Market_Index'], name='MARKET BENCHMARK', line=dict(dash='dot', color='#8B5CF6')))
            figm.add_trace(go.Scatter(x=df_audit['Periodo'], y=df_audit['Internal_Index'], name='OUR OPERATION', line=dict(color='#38BDF8', width=5)))
            st.plotly_chart(aplicar_template_financeiro(figm, "Retraction Index vs National Proxy (Base 100)"), use_container_width=True)
        with c_m2:
            df_jogos = pd.DataFrame({
                "Game": ["Aviator (Spribe)", "Fortune Tiger (PG Soft)", "Brazilian Roulette", "Mines (Original)", "Gates of Olympus"],
                "Volume (%)": [31.5, 24.2, 18.0, 12.3, 8.5],
                "Color": ['#38BDF8', '#10B981', '#F59E0B', '#F43F5E', '#8B5CF6']
            })
            figj = px.bar(df_jogos, x="Volume (%)", y="Game", orientation='h', color="Game", color_discrete_sequence=df_jogos['Color'].tolist())
            st.plotly_chart(aplicar_template_financeiro(figj, "Revenue Capillarity by Core Provider"), use_container_width=True)

        st.markdown("""
        <div class='consultant-report'>
        <b>MARKET SHARE VERDICT:</b><br>
        The dynamics of the iGaming market in Brazil in 2026 are in a phase of regulatory consolidation. We note that the National Market Proxy follows clear seasonal cycles. However, the divergence in our curve confirms the thesis of "Market Share Loss due to Ad-Spend Deficiency".<br><br>
        <b>PROVIDER SCRUTINY:</b><br>
        <b>1. Spribe:</b> Daily engagement anchor. <br>
        <b>2. PG Soft:</b> Retail tractor (Fortune Tiger) with a colossal volume of micro-bets.<br>
        <b>3. Evolution:</b> VIP Dining Room. The psychological factor boosts profitability close to 8.5%.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='kpi-block'>
            <div class='kpi-title'>📚 Methodology & Data Source</div>
            <div class='kpi-text'>
            <b>Benchmark Source:</b> National B2B iGaming Proxy, built from market traffic aggregators (e.g., SimilarWeb, SEMrush) and anonymized sector reports in Brazil, cross-referenced with internal transactional logs.<br><br>
            <b>Internal Index Formula (Retraction Index):</b><br>
            <i>Internal Index = (Current Month Handle / Base Month Handle) * 100</i><br>
            This allows us to compare the operation's rate of decline or growth relative to the macro market oscillation, without absolute financial bias.
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif menu == "5. Affiliate Performance (Top/Bottom 20)":
        st.markdown("<h2 class='section-title'>5. Affiliate Analysis</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class='consultant-report'>
        <b>B2B PARTNERS AUDIT:</b><br>
        This module ranks the capital efficiency of partners (Affiliates). 
        The <b>Net Revenue</b> indicator was isolated to identify which partners are generating financial margin versus those that are merely consuming resources via "FIXED FEE" and delivering traffic without retention.
        </div>
        """, unsafe_allow_html=True)

        if not df_afiliados.empty:
            periodos_afiliados = [str(p) for p in df_afiliados["Periodo"].dropna().unique().tolist()]
            periodo_foco = st.selectbox("Select the affiliate period:", periodos_afiliados, index=0)
            df_periodo = df_afiliados[df_afiliados["Periodo"] == periodo_foco].copy()

            st.markdown(
                f"<div class='kpi-block'><div class='kpi-title'>Period under analysis</div><div class='kpi-text'>All tables and charts below refer to <b>{periodo_foco}</b>.</div></div>",
                unsafe_allow_html=True
            )

            df_sorted = df_periodo.sort_values(by="Net Revenue", ascending=False)
            top_20 = df_sorted.head(20).copy()
            bottom_20 = df_sorted.tail(20).sort_values(by="Net Revenue", ascending=True).copy()
            top_20["NGR Affiliate"] = top_20["Net Revenue"]
            bottom_20["NGR Affiliate"] = bottom_20["Net Revenue"]

            format_dict = {
                "NGR Affiliate": "$ {:,.2f}",
                "Net Revenue": "$ {:,.2f}",
                "Revenue Share Reward": "$ {:,.2f}",
                "CPA Reward": "$ {:,.2f}",
                "FIXED FEE": "$ {:,.2f}",
                "Total Reward": "$ {:,.2f}"
            }

            st.markdown(f"<h3 style='color:#10B981; margin-top:20px; font-weight:800;'>🏆 TOP 20 AFFILIATES - {periodo_foco} (HIGHEST NET REVENUE GENERATED)</h3>", unsafe_allow_html=True)
            st.dataframe(top_20.style.format(format_dict), use_container_width=True)

            st.markdown(f"<br><h3 style='color:#F43F5E; margin-top:20px; font-weight:800;'>⚠️ BOTTOM 20 AFFILIATES - {periodo_foco} (LOSS OR LOW EFFICIENCY)</h3>", unsafe_allow_html=True)
            st.dataframe(bottom_20.style.format(format_dict), use_container_width=True)
            
            st.markdown("<h3 style='color:#FFFFFF; margin-top:26px; font-weight:800;'>📈 AFFILIATE NGR AND ACQUISITION COST</h3>", unsafe_allow_html=True)

            top_20_chart = top_20.sort_values(by="NGR Affiliate", ascending=False)
            top_20_chart["Affiliate Label"] = top_20_chart["Affiliate Name"].astype(str).str.slice(0, 22)
            fig_aff_top = go.Figure()
            fig_aff_top.add_trace(go.Bar(
                x=top_20_chart['Affiliate Label'],
                y=top_20_chart['CPA Reward'],
                name='CPA Reward (Cost)',
                marker_color='#F59E0B',
                hovertemplate='<b>%{x}</b><br>CPA: $ %{y:,.2f}<extra></extra>'
            ))
            fig_aff_top.add_trace(go.Bar(
                x=top_20_chart['Affiliate Label'],
                y=top_20_chart['FIXED FEE'],
                name='FIXED FEE (Additional Cost)',
                marker_color='#8B5CF6',
                hovertemplate='<b>%{x}</b><br>FIXED FEE: $ %{y:,.2f}<extra></extra>'
            ))
            fig_aff_top.add_trace(go.Scatter(
                x=top_20_chart['Affiliate Label'],
                y=top_20_chart['NGR Affiliate'],
                name='NGR Affiliate',
                mode='lines+markers',
                marker=dict(color='#10B981', size=7),
                line=dict(color='#10B981', width=3),
                hovertemplate='<b>%{x}</b><br>NGR: $ %{y:,.2f}<extra></extra>'
            ))

            fig_aff_top.update_layout(
                barmode='stack',
                height=560,
                xaxis=dict(tickangle=-35, automargin=True, tickfont=dict(size=10)),
                yaxis=dict(tickfont=dict(size=10))
            )
            fig_aff_top = aplicar_template_financeiro(fig_aff_top, f"Acquisition Cost Analysis + NGR (Top 20) - {periodo_foco}")
            st.plotly_chart(fig_aff_top, use_container_width=True)

            bottom_20_chart = bottom_20.sort_values(by="NGR Affiliate", ascending=True)
            bottom_20_chart["Affiliate Label"] = bottom_20_chart["Affiliate Name"].astype(str).str.slice(0, 22)
            fig_aff_bottom = go.Figure()
            fig_aff_bottom.add_trace(go.Bar(
                x=bottom_20_chart['Affiliate Label'],
                y=bottom_20_chart['CPA Reward'],
                name='CPA Reward (Cost)',
                marker_color='#F59E0B',
                hovertemplate='<b>%{x}</b><br>CPA: $ %{y:,.2f}<extra></extra>'
            ))
            fig_aff_bottom.add_trace(go.Bar(
                x=bottom_20_chart['Affiliate Label'],
                y=bottom_20_chart['FIXED FEE'],
                name='FIXED FEE (Additional Cost)',
                marker_color='#8B5CF6',
                hovertemplate='<b>%{x}</b><br>FIXED FEE: $ %{y:,.2f}<extra></extra>'
            ))
            fig_aff_bottom.add_trace(go.Scatter(
                x=bottom_20_chart['Affiliate Label'],
                y=bottom_20_chart['NGR Affiliate'],
                name='NGR Affiliate',
                mode='lines+markers',
                marker=dict(color='#F43F5E', size=7),
                line=dict(color='#F43F5E', width=3),
                hovertemplate='<b>%{x}</b><br>NGR: $ %{y:,.2f}<extra></extra>'
            ))

            fig_aff_bottom.update_layout(
                barmode='stack',
                height=560,
                xaxis=dict(tickangle=-35, automargin=True, tickfont=dict(size=10)),
                yaxis=dict(tickfont=dict(size=10))
            )
            fig_aff_bottom = aplicar_template_financeiro(fig_aff_bottom, f"Acquisition Cost Analysis + NGR (Bottom 20) - {periodo_foco}")
            st.plotly_chart(fig_aff_bottom, use_container_width=True)

    elif menu == "6. Brazil Finance Outlook":
        st.markdown("<h2 class='section-title'>6. Brazil Finance Strategic Outlook</h2>", unsafe_allow_html=True)
        st.markdown(""" 
        <div class='consultant-report'>
        <b>EXECUTIVE SUMMARY ON BRAZILIAN OPERATIONS</b><br><br>
        
        <b>1. General Sentiment: Structural Concern.</b><br>
        The Brazil Finance team identifies that the operation is entering a <b>dangerous cycle of marginal returns</b>. While Gross Revenue (GGR) showed resilience during late 2025, the Net Profitability (NGR) is being systematically hollowed out by inefficient promotional spending and toxic retention models.<br><br>

        <b>2. Critical Pain Points:</b><br>
        • <b>Acquisition Collapse:</b> The 70% drop in FTD volume since the peak of April 2025 proves our current marketing channels are exhausted and failing to deliver new capital.<br>
        • <b>Bonus Dependency:</b> We are essentially "subsidizing" a legacy base that no longer brings fresh capital to the platform, generating an unreal inflation in Wagered volume without translating to bottom-line profit.<br>
        • <b>Affiliate Inefficiency:</b> A significant portion of the CPA and Fixed Fee budget is being consumed by partners delivering negative or zero Net Revenue.<br><br>

        <b>3. Strategy for Immediate Improvement:</b><br>
        • <b>Budget Pivot:</b> Immediate 35% cut in broad, unconditional bonus campaigns. This capital MUST be aggressively reinvested into SEO, High-Intent CPA, and Tier-1 Influencers.<br>
        • <b>Restructure Promotions:</b> Transition strictly to "Stake-Back" or loyalty models where bonuses are only released based on actual fiduciary turnover, eliminating Bonus Hunters.<br>
        • <b>Affiliate Purge:</b> Renegotiate or terminate contracts with the Bottom 20 Affiliates operating on Fixed Fees with negative NGR yields. Shift focus to pure RevShare agreements.
        </div>
        """, unsafe_allow_html=True)

else:
    st.error("❌ LOAD FAILURE: The Data Engine did not detect the blinded base.")

def log_system_access_telemetry():
    pass

def handle_high_concurrency_requests():
    pass

# End of script
