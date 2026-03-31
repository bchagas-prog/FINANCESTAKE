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

st.write("App rodando 🚀")
# ==============================================================================
# 1. ARQUITETURA DE UI E DESIGN EXECUTIVO (C-LEVEL DASHBOARD)
# ==============================================================================
# Configuração de alta performance e layout ultra-wide
st.set_page_config(
    page_title="STRATEGIC FINANCE ANALYSIS - STAKE BRAZIL",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# INJEÇÃO DE CSS CORPORATIVO (ESTILIZAÇÃO PREMIUM DE ALTA DENSIDADE)
# ==============================================================================
st.markdown("""
    <style>
    /* Importação da família Inter - Padrão de Interfaces Financeiras Internacionais */
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
    
    /* FORÇAR FUNDO ESCURO EM TODA A APLICAÇÃO */
    .stApp, .main, [data-testid="stHeader"], [data-testid="stToolbar"] { 
        background-color: var(--primary-bg) !important; 
    }
    
    /* BARRA LATERAL (SIDEBAR) - DESIGN CORPORATIVO */
    [data-testid="stSidebar"] {
        background-color: var(--secondary-bg) !important;
        border-right: 1px solid var(--border-color) !important;
        width: 350px !important;
    }
    
    /* ESTILIZAÇÃO DO MENU DE RÁDIO NA SIDEBAR */
    .stRadio label p {
        color: #FFFFFF !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        letter-spacing: 0.3px;
    }
    
    /* ESTILIZAÇÃO DE INPUTS E SELECTBOXES */
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
       AJUSTE DE FONTE DOS NÚMEROS (METRICS)
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
    
    /* CARTÕES DE MÉTRICAS - EFEITO DE PROFUNDIDADE */
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
       AJUSTE DE TAMANHO DO TEXTO (REPORTS/KPI TEXT)
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
    
    /* TÍTULOS DE SEÇÃO */
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

    /* KPI BLOCK (ESTRUTURA INTERNA DO RAIO-X) */
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

    /* TABELAS DE DADOS DA APLICAÇÃO */
    .stDataFrame { border-radius: 12px; border: 1px solid var(--border-color); overflow: hidden; }
    
    /* SCROLLBAR CUSTOMIZADA PARA EXPERIÊNCIA FLUIDA */
    ::-webkit-scrollbar { width: 10px; height: 10px; }
    ::-webkit-scrollbar-track { background: var(--primary-bg); }
    ::-webkit-scrollbar-thumb { background: #334155; border-radius: 5px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--accent-blue); }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# FUNÇÕES DE UTILITÁRIO DE LAYOUT (PARA MANTER CONSISTÊNCIA VISUAL C-LEVEL)
# ==============================================================================

def aplicar_template_financeiro(fig, titulo=""):
    """
    Padronização executiva de gráficos Plotly.
    Garante legendas e textos em BRANCO (#FFFFFF) para evitar sumiço em fundo escuro.
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
# 2. MOTOR ETL (MACRO): CAPTURA FORENSE E BLINDAGEM DE DADOS (FEV/25 - MAR/26)
# ==============================================================================

@st.cache_data(show_spinner="OBTENDO INTELIGÊNCIA FINANCEIRA MACRO...")
def carregar_motor_estatistico():
    # MATRIZ BRUTA DE DADOS MACRO (100% FIEL AOS INPUTS DO USUÁRIO - 14 MESES)
    dataset_bruto = [
        {"Periodo": "Fevereiro/25", "Bet": 433154903.03, "Ggr": 12817805.08, "AccountingRevenue": 4793123.37, "BonusCost": 8024681.71, "DepositAmount": 84614542.14, "DepositCount": 376216, "FirstDepositsAmount": 5452035.47, "ActiveCustomers": 93713},
        {"Periodo": "Março/25", "Bet": 449776319.50, "Ggr": 12474456.69, "AccountingRevenue": 3461593.98, "BonusCost": 9012862.71, "DepositAmount": 90369274.57, "DepositCount": 391222, "FirstDepositsAmount": 6343221.86, "ActiveCustomers": 71182},
        {"Periodo": "Abril/25", "Bet": 461386592.20, "Ggr": 13319801.53, "AccountingRevenue": 4767018.58, "BonusCost": 8552782.95, "DepositAmount": 95452676.79, "DepositCount": 451684, "FirstDepositsAmount": 7045320.18, "ActiveCustomers": 89597},
        {"Periodo": "Maio/25", "Bet": 472787703.86, "Ggr": 16467641.86, "AccountingRevenue": 9721186.45, "BonusCost": 6746455.41, "DepositAmount": 92833122.69, "DepositCount": 444984, "FirstDepositsAmount": 4664941.54, "ActiveCustomers": 88803},
        {"Periodo": "Junho/25", "Bet": 480912914.30, "Ggr": 17463526.94, "AccountingRevenue": 10911182.44, "BonusCost": 6552344.50, "DepositAmount": 94196541.68, "DepositCount": 419129, "FirstDepositsAmount": 5982397.35, "ActiveCustomers": 76894},
        {"Periodo": "Julho/25", "Bet": 477529960.43, "Ggr": 15638347.67, "AccountingRevenue": 8808137.85, "BonusCost": 6830209.82, "DepositAmount": 90861644.43, "DepositCount": 407201, "FirstDepositsAmount": 4994592.87, "ActiveCustomers": 105552},
        {"Periodo": "Agosto/25", "Bet": 460638534.40, "Ggr": 16950966.87, "AccountingRevenue": 9966733.22, "BonusCost": 6984233.65, "DepositAmount": 89384216.75, "DepositCount": 417421, "FirstDepositsAmount": 4243819.63, "ActiveCustomers": 94685},
        {"Periodo": "Setembro/25", "Bet": 447766137.68, "Ggr": 13775941.23, "AccountingRevenue": 7097767.01, "BonusCost": 6678174.22, "DepositAmount": 86888335.77, "DepositCount": 418562, "FirstDepositsAmount": 5519619.07, "ActiveCustomers": 111437},
        {"Periodo": "Outubro/25", "Bet": 494759539.00, "Ggr": 12388762.29, "AccountingRevenue": 5478265.27, "BonusCost": 6910497.02, "DepositAmount": 97196004.80, "DepositCount": 474100, "FirstDepositsAmount": 7122170.31, "ActiveCustomers": 89808},
        {"Periodo": "Novembro/25", "Bet": 500831546.18, "Ggr": 15464720.24, "AccountingRevenue": 7763157.75, "BonusCost": 7701562.49, "DepositAmount": 89005331.10, "DepositCount": 442831, "FirstDepositsAmount": 4213036.44, "ActiveCustomers": 76702},
        {"Periodo": "Dezembro/25", "Bet": 469903667.46, "Ggr": 16397186.75, "AccountingRevenue": 9144726.01, "BonusCost": 7252460.74, "DepositAmount": 80648625.03, "DepositCount": 406783, "FirstDepositsAmount": 2442483.58, "ActiveCustomers": 76537},
        {"Periodo": "Janeiro/26", "Bet": 386563548.21, "Ggr": 12642884.23, "AccountingRevenue": 7468767.08, "BonusCost": 5174117.15, "DepositAmount": 66159171.03, "DepositCount": 348104, "FirstDepositsAmount": 2157301.62, "ActiveCustomers": 77882},
        {"Periodo": "Fevereiro/26", "Bet": 282974008.65, "Ggr": 8252592.58, "AccountingRevenue": 4378511.90, "BonusCost": 3874080.68, "DepositAmount": 51737038.31, "DepositCount": 288391, "FirstDepositsAmount": 1849641.42, "ActiveCustomers": 67932},
        {"Periodo": "Março/26", "Bet": 252135263.60, "Ggr": 6100445.57, "AccountingRevenue": 3265798.25, "BonusCost": 2834647.32, "DepositAmount": 46144497.75, "DepositCount": 258837, "FirstDepositsAmount": 1805797.30, "ActiveCustomers": 64863}
    ]

    df = pd.DataFrame(dataset_bruto)
    
    df['NGR'] = df['AccountingRevenue']
    df['Hold_Pct'] = (df['Ggr'] / df['Bet'] * 100).round(2)
    df['Bonus_Ratio'] = (df['BonusCost'] / df['Ggr'] * 100).round(2)
    df['FTD_Ratio'] = (df['FirstDepositsAmount'] / df['DepositAmount'] * 100).round(2)
    df['ARPU'] = (df['Ggr'] / df['ActiveCustomers']).round(2)
    df['Retention_Index'] = (df['DepositCount'] / df['ActiveCustomers']).round(2)
    df['Ticket_Medio_Dep'] = (df['DepositAmount'] / df['DepositCount']).round(2)
    
    ordem_original = [
        "Fevereiro/25", "Março/25", "Abril/25", "Maio/25", "Junho/25", "Julho/25", 
        "Agosto/25", "Setembro/25", "Outubro/25", "Novembro/25", "Dezembro/25", 
        "Janeiro/26", "Fevereiro/26", "Março/26"
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
# 2.1 MOTOR ETL (MICRO): PROCESSADOR DE DADOS DE AFILIADOS JANEIRO (NOVO MÓDULO)
# ==============================================================================

@st.cache_data(show_spinner="PROCESSANDO MATRIZ DE AFILIADOS...")
def carregar_motor_afiliados():
    raw_affiliates_janeiro = [
        {"Periodo": "Janeiro/26", "Affiliate ID": "654570", "Affiliate Name": "Moveup Media Brasil ltda", "FTD": 96, "Net Revenue": 1216105.228, "Revenue Share Reward": 364828.60, "CPA Reward": 111600.00, "FIXED FEE": 0.0, "Total Reward": 476428.60},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654495", "Affiliate Name": "YGA Ventures Ltd", "FTD": 399, "Net Revenue": 3218195.711, "Revenue Share Reward": 1609097.90, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 1609097.90},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654514", "Affiliate Name": "North Star Network", "FTD": 271, "Net Revenue": 1900693.19, "Revenue Share Reward": 665242.60, "CPA Reward": 0.0, "FIXED FEE": 1334757.40, "Total Reward": 2000000.00},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654634", "Affiliate Name": "Influx Online", "FTD": 27, "Net Revenue": 806765.384, "Revenue Share Reward": 242026.60, "CPA Reward": 43200.00, "FIXED FEE": 0.0, "Total Reward": 285226.60},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654429", "Affiliate Name": "GNY / Streamer", "FTD": 34, "Net Revenue": 966416.935, "Revenue Share Reward": 289925.10, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 289925.10},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654430", "Affiliate Name": "Xioguto / Streamer", "FTD": 2, "Net Revenue": 359376.354, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 0.0},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654487", "Affiliate Name": "Armoni Solucoes e Intermediacoes em Negocios Web", "FTD": 6, "Net Revenue": 830025.384, "Revenue Share Reward": 249007.60, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 249007.60},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654476", "Affiliate Name": "Markola", "FTD": 19, "Net Revenue": 539155.799, "Revenue Share Reward": 161743.70, "CPA Reward": 40800.00, "FIXED FEE": 0.0, "Total Reward": 202543.70},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654553", "Affiliate Name": "EMPREENDEDOR VISIONARIO TREINAMENTOS EIRELI ME", "FTD": 27, "Net Revenue": 521595.296, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 600000.00, "Total Reward": 600000.00},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654604", "Affiliate Name": "League of Entertainment", "FTD": 42, "Net Revenue": 764335.562, "Revenue Share Reward": 229300.70, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 229300.70},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654825", "Affiliate Name": "Playhill Brasil Ltda", "FTD": 13, "Net Revenue": -37141.224, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 0.0},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654828", "Affiliate Name": "Talking & Gaming", "FTD": 19, "Net Revenue": 443151.076, "Revenue Share Reward": 132942.30, "CPA Reward": 12000.00, "FIXED FEE": 0.0, "Total Reward": 144942.30},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654649", "Affiliate Name": "abratabaca", "FTD": 273, "Net Revenue": -259292.988, "Revenue Share Reward": 0.0, "CPA Reward": 199200.00, "FIXED FEE": 0.0, "Total Reward": 199200.00},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654503", "Affiliate Name": "souograndi", "FTD": 7, "Net Revenue": 247665.185, "Revenue Share Reward": 12383.30, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 12383.30},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654547", "Affiliate Name": "nokainlive", "FTD": 3, "Net Revenue": 46999.613, "Revenue Share Reward": 14096.90, "CPA Reward": 3600.00, "FIXED FEE": 0.0, "Total Reward": 17696.90},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654433", "Affiliate Name": "Binao", "FTD": 54, "Net Revenue": 116458.959, "Revenue Share Reward": 29112.20, "CPA Reward": 32400.00, "FIXED FEE": 0.0, "Total Reward": 61512.20},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654446", "Affiliate Name": "FABINHO AEP PRODUCAO DE VIDEOS LTDA", "FTD": 15, "Net Revenue": 366722.089, "Revenue Share Reward": 36672.20, "CPA Reward": 0.0, "FIXED FEE": 203327.80, "Total Reward": 240000.00},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654614", "Affiliate Name": "Bieldomaul", "FTD": 0, "Net Revenue": 52.0308, "Revenue Share Reward": 12.76, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 12.76},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654691", "Affiliate Name": "afiliado@betpass.me", "FTD": 29, "Net Revenue": -3237.959, "Revenue Share Reward": 0.0, "CPA Reward": 2340.00, "FIXED FEE": 0.0, "Total Reward": 2340.00},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654440", "Affiliate Name": "FURIAGAMES", "FTD": 41, "Net Revenue": -151890.6761, "Revenue Share Reward": 4773.90, "CPA Reward": 2880.00, "FIXED FEE": 0.0, "Total Reward": 3357.39},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654546", "Affiliate Name": "Pay Instituicao de Pagamento S/A", "FTD": 5, "Net Revenue": -223512.10, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 0.0},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654543", "Affiliate Name": "Ninjabet", "FTD": 2, "Net Revenue": -54409.789, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 0.0},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654544", "Affiliate Name": "Klauslol", "FTD": 14, "Net Revenue": 22720.984, "Revenue Share Reward": 7948.80, "CPA Reward": 21600.00, "FIXED FEE": 0.0, "Total Reward": 29548.80},
        {"Periodo": "Janeiro/26", "Affiliate ID": "655459", "Affiliate Name": "Partners", "FTD": 0, "Net Revenue": 0.0, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 0.0, "Total Reward": 0.0},
        {"Periodo": "Janeiro/26", "Affiliate ID": "655266", "Affiliate Name": "VOLTZ AFFILIATES BR", "FTD": 1, "Net Revenue": -250.85, "Revenue Share Reward": 0.0, "CPA Reward": 1800.00, "FIXED FEE": 0.0, "Total Reward": 1800.00},
        {"Periodo": "Janeiro/26", "Affiliate ID": "655372", "Affiliate Name": "Cassius Ogro", "FTD": 1, "Net Revenue": 2387.573, "Revenue Share Reward": 594.40, "CPA Reward": 1200.00, "FIXED FEE": 0.0, "Total Reward": 1794.40},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654824", "Affiliate Name": "OC GROUP TECNOLOGIA DA INFORMACAO LTDA", "FTD": 15, "Net Revenue": 25821.173, "Revenue Share Reward": 7743.40, "CPA Reward": 12000.00, "FIXED FEE": 0.0, "Total Reward": 19743.40},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654830", "Affiliate Name": "pichucas", "FTD": 3, "Net Revenue": 107214.406, "Revenue Share Reward": 26801.10, "CPA Reward": 9000.00, "FIXED FEE": 0.0, "Total Reward": 35801.10},
        {"Periodo": "Janeiro/26", "Affiliate ID": "654551", "Affiliate Name": "Carlos Figueira MMA", "FTD": 53, "Net Revenue": 83077.796, "Revenue Share Reward": 0.0, "CPA Reward": 0.0, "FIXED FEE": 50000.00, "Total Reward": 50000.00}
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

    for row in raw_affiliates_fevereiro:
        row["Periodo"] = "Fevereiro/26"
    for row in raw_affiliates_marco:
        row["Periodo"] = "Março/26"

    df_aff = pd.DataFrame(raw_affiliates_janeiro + raw_affiliates_fevereiro + raw_affiliates_marco)

    # Corrige as bases brutas que vieram multiplicadas por 10.000.
    mask_bruto = df_aff["Periodo"].isin(["Fevereiro/26", "Março/26"])
    for col in AFFILIATE_MONETARY_COLUMNS:
        df_aff[col] = pd.to_numeric(df_aff[col], errors="coerce").fillna(0)
        df_aff.loc[mask_bruto, col] = df_aff.loc[mask_bruto, col] / AFFILIATE_MONETARY_DIVISOR

    return df_aff

df_afiliados = carregar_motor_afiliados()

# ==============================================================================
# 3. INTERFACE EXECUTIVA: O RELATÓRIO DE CONSULTORIA SÊNIOR
# ==============================================================================
if df_audit is not None and not df_audit.empty:
    
    col_h1, col_h2 = st.columns([3, 1])
    with col_h1:
        st.title("🏦 FINANCE ANALYSIS")
        st.markdown(f"**Confidencial | Data da Extração:** {datetime.datetime.now().strftime('%d/%m/%Y')} | **Status:** Ciclo FEV/25 - MAR/26")
    with col_h2:
        st.markdown("""
            <div style='text-align:right; margin-top:15px;'>
                <span style='background-color:#F43F5E; color:#fff; padding:6px 16px; border-radius:6px; font-weight:bold; font-size:0.8rem; letter-spacing:1px; box-shadow: 0 4px 12px rgba(244, 63, 94, 0.4);'>
                CRITICAL PERFORMANCE REVIEW
                </span>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border-top: 2px solid #334155; margin-top: 5px; margin-bottom: 30px;'>", unsafe_allow_html=True)
    
    st.sidebar.markdown("<h2 style='color:#FFFFFF; font-weight:800; font-size:1.4rem; margin-bottom:10px;'>ESTRATÉGIA</h2>", unsafe_allow_html=True)
    menu = st.sidebar.radio("", [
        "1. Executive Summary & Alerts",
        "2. Macro-Trends & Dynamic Analytics",
        "3. Raio-X Operacional (Mês a Mês)",
        "4. Capital Efficiency & Elasticity",
        "5. Market Share & Unit Economics",
        "6. Roadmap Strategy: 90 Days",
        "7. Technical Mathematical Repository",
        "8. Scenario Simulator (Predictive)",
        "9. Anomaly & Fraud Detection",
        "10. Affiliate Performance (Top/Bottom 20)"
    ])
    
    st.sidebar.markdown("<hr style='border-top: 1px dashed #334155;'>", unsafe_allow_html=True)
    
    ult = df_audit.iloc[-1]
    st.sidebar.markdown("### ⚡ Live Pulse (Last Cycle)")
    st.sidebar.metric("FTD Velocity", f"R$ {ult['FirstDepositsAmount']/1e6:.2f}M", f"{ult['Delta_FirstDepositsAmount_Pct']:.1f}%")
    st.sidebar.metric("Hold Yield", f"{ult['Hold_Pct']}%", f"{ult['Hold_Pct'] - df_audit.iloc[-2]['Hold_Pct']:.2f}%")

    if menu == "1. Executive Summary & Alerts":
        st.markdown("<h2 class='section-title'>1. Diagnóstico do Ciclo (Fev/25 - Mar/26)</h2>", unsafe_allow_html=True)
        st.markdown(""" 
        <div class='consultant-report'>
        <b>PARECER TÉCNICO: ESTADO DE EXAUSTÃO ESTRUTURAL</b><br><br>
        A análise Comportamental dos 14 meses de dados consolidados aponta para um cenário onde a operação atingiu seu <b>ponto de saturação tática em Outubro/2025</b>. A partir de então, verificamos um decréscimo severo no vetor de oxigenação da base (FTD).<br><br>
        <b>Os 3 Pilares do Problema Atual:</b><br>
        <ul style="margin-top: 10px; margin-bottom: 10px;">
            <li><b>O Colapso do FTD (New Money):</b> A aquisição de capital inédito despencou. Passamos de uma média de R$ 6M para R$ 1.8M em Março/26. A plataforma deixou de trazer tráfego fresco, dependendo da reciclagem de veteranos.</li>
            <li><b>A Armadilha do Bônus (Bonus Trap):</b> Para frear a perda de jogadores (Churn), a operação abriu as torneiras de bonificação de forma incondicional. O <i>Bonus Ratio</i> explodiu para níveis insustentáveis, devorando o GGR.</li>
            <li><b>Canibalização de Orçamento:</b> O capital que deveria estar sendo investido em CPA e afiliados (Aquisição) está sendo queimado em bônus para sustentar uma base que não deposita mais dinheiro real fiduciário.</li>
        </ul>
        <i><b>Decisão Requerida:</b> Redirecionamento imediato de 35% do orçamento de Retenção (Bônus) para Aquisição de Tráfego de Alta Intenção (Google/SEO/Influenciadores Tier-1) para quebrar o teto de faturamento atual.</i>
        </div>
        """, unsafe_allow_html=True)
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("FTD (MARÇO/26)", f"R$ {ult['FirstDepositsAmount']:,.0f}", f"{ult['Delta_FirstDepositsAmount_Pct']:.1f}%")
        c2.metric("GGR (RECEITA BRUTA)", f"R$ {ult['Ggr']:,.0f}", f"{ult['Delta_Ggr_Pct']:.1f}%")
        c3.metric("HOLD CONSOLIDADO", f"{ult['Hold_Pct']}%", f"{ult['Hold_Pct']-3:.2f}% vs Meta")
        c4.metric("MAU (ATIVOS)", f"{ult['ActiveCustomers']:,.0f}", f"{ult['Delta_ActiveCustomers_Pct']:.1f}%")

    elif menu == "2. Macro-Trends & Dynamic Analytics":
        st.markdown("<h2 class='section-title'>2. Dashboard Macro-Trends (14 Meses)</h2>", unsafe_allow_html=True)
        
        c_g1, c_g2 = st.columns(2)
        with c_g1:
            fig_1 = make_subplots(specs=[[{"secondary_y": True}]])
            fig_1.add_trace(go.Scatter(x=df_audit['Periodo'], y=df_audit['Bet'], name='HANDLE (LIQUIDEZ)', mode='lines+markers+text', line=dict(color='#38BDF8', width=5)), secondary_y=False)
            fig_1.add_trace(go.Bar(x=df_audit['Periodo'], y=df_audit['Ggr'], name='GGR (RECEITA BRUTA)', marker_color='#10B981', opacity=0.9, width=0.6), secondary_y=True)
            fig_1 = aplicar_template_financeiro(fig_1, "Evolução do Histórico: Volume x Receita Bruta")
            fig_1.update_yaxes(title_text="<b>HANDLE (Lado Esquerdo)</b>", color="#FFFFFF", secondary_y=False)
            fig_1.update_yaxes(title_text="<b>GGR (Lado Direito)</b>", color="#FFFFFF", secondary_y=True)
            st.plotly_chart(fig_1, use_container_width=True)
        
        with c_g2:
            fig_2 = make_subplots(specs=[[{"secondary_y": True}]])
            fig_2.add_trace(go.Bar(x=df_audit['Periodo'], y=df_audit['DepositAmount'], name='DEPÓSITOS (R$)', marker_color='#8B5CF6'), secondary_y=False)
            fig_2.add_trace(go.Scatter(x=df_audit['Periodo'], y=df_audit['ActiveCustomers'], name='ATIVOS (MAU)', mode='lines+markers', line=dict(color='#F59E0B', width=4)), secondary_y=True)
            fig_2 = aplicar_template_financeiro(fig_2, "Matriz de Captação: Depósitos x Usuários")
            fig_2.update_yaxes(title_text="R$", secondary_y=False)
            fig_2.update_yaxes(title_text="Quantidade", secondary_y=True)
            st.plotly_chart(fig_2, use_container_width=True)

        c_g3, c_g4 = st.columns(2)
        with c_g3:
            fig_3 = go.Figure()
            fig_3.add_trace(go.Bar(x=df_audit['Periodo'], y=df_audit['FirstDepositsAmount'], name='FTD (NEW MONEY)', marker_color='#14B8A6'))
            fig_3 = aplicar_template_financeiro(fig_3, "Tendência de Captação (FTD Velocity)")
            st.plotly_chart(fig_3, use_container_width=True)

        with c_g4:
            fig_4 = make_subplots(specs=[[{"secondary_y": True}]])
            fig_4.add_trace(go.Bar(x=df_audit['Periodo'], y=df_audit['BonusCost'], name='CUSTO BÔNUS', marker_color='#F43F5E'), secondary_y=False)
            fig_4.add_trace(go.Scatter(x=df_audit['Periodo'], y=df_audit['Bonus_Ratio'], name='RATIO %', line=dict(color='#FFFFFF', width=3)), secondary_y=True)
            fig_4 = aplicar_template_financeiro(fig_4, "Pressão Promocional vs Margem de Contribuição")
            st.plotly_chart(fig_4, use_container_width=True)

        st.markdown("### 📊 Tabela Analítica: Performance MoM Auditada")
        st.dataframe(df_audit[['Periodo', 'Delta_Bet_Pct', 'Delta_Ggr_Pct', 'Delta_DepositAmount_Pct', 'Delta_FirstDepositsAmount_Pct', 'Bonus_Ratio']].style.format(precision=2), use_container_width=True)

    elif menu == "3. Raio-X Operacional (Mês a Mês)":
        st.markdown("<h2 class='section-title'>3. Decomposição Financeira por Ciclo Fiscal</h2>", unsafe_allow_html=True)
        meses_select = [str(m) for m in df_audit['Periodo'].tolist()]
        mes_foco = st.selectbox("Selecione o período contábil de análise:", meses_select)
        d = df_audit[df_audit['Periodo'] == mes_foco].iloc[0]
        
        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2, c3, c4, c5, c6 = st.columns(6)
        c1.metric("Handle (Giro)", f"R$ {d['Bet']:,.0f}", f"{d.get('Delta_Bet_Pct', 0):.1f}%")
        c2.metric("GGR (Bruto)", f"R$ {d['Ggr']:,.0f}", f"{d.get('Delta_Ggr_Pct', 0):.1f}%")
        c3.metric("NGR (Líquido)", f"R$ {d['NGR']:,.0f}", f"{d.get('Delta_NGR_Pct', 0):.1f}%")
        c4.metric("Depósitos", f"R$ {d['DepositAmount']:,.0f}", f"{d.get('Delta_DepositAmount_Pct', 0):.1f}%")
        c5.metric("Base Ativa", f"{d['ActiveCustomers']:,.0f}", f"{d.get('Delta_ActiveCustomers_Pct', 0):.1f}%")
        c6.metric("Hold %", f"{d['Hold_Pct']}%")

        st.markdown("<br>", unsafe_allow_html=True)
        c7, c8, c9, c10 = st.columns(4)
        c7.metric("Ticket Médio (Depósito)", f"R$ {d['Ticket_Medio_Dep']:,.2f}")
        c8.metric("ARPU (Receita por Usuário)", f"R$ {d['ARPU']:,.2f}")
        c9.metric("FTD Ratio (New Money)", f"{d['FTD_Ratio']}%")
        c10.metric("Bonus Ratio (Custo)", f"{d['Bonus_Ratio']}%")
        
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.markdown(f"""
            <div class='kpi-block'>
                <div class='kpi-title'>📍 Elasticidade de Produto (Handle vs Hold)</div>
                <div class='kpi-text'>
                Volume Registrado: R$ {d['Bet']:,.2f}. <br>
                <b>Parecer:</b> O Hold de {d['Hold_Pct']}% está dentro do padrão ouro da indústria iGaming. O faturamento não está caindo por defeito no jogo, mas por falta de volume de apostadores.
                <br><br><b>ARPU:</b> Cada jogador ativo gerou R$ {d['ARPU']:,.2f} de receita bruta neste ciclo.
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_t2:
            st.markdown(f"""
            <div class='kpi-block'>
                <div class='kpi-title'>💸 Motor de Aquisição (New Money)</div>
                <div class='kpi-text'>
                Injeção de FTD: R$ {d['FirstDepositsAmount']:,.2f}. <br>
                <b>Parecer:</b> O FTD Ratio de {d['FTD_Ratio']}% é insuficiente para o equilíbrio do churn. O caixa está sendo financiado por capital reciclado.
                <br><br><b>Custo de Bônus:</b> A plataforma queimou R$ {d['BonusCost']:,.2f} ({d['Bonus_Ratio']}% do GGR) para segurar a base atual.
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### 📊 Cascata de Receita (De GGR para NGR)")
        fig_waterfall = go.Figure(go.Waterfall(
            name="20", orientation="v",
            measure=["relative", "relative", "total"],
            x=["GGR (Receita Bruta)", "Custo de Bônus / Deduções", "NGR (Receita Líquida)"],
            textposition="outside",
            text=[f"R$ {d['Ggr']/1e6:.1f}M", f"-R$ {d['BonusCost']/1e6:.1f}M", f"R$ {d['NGR']/1e6:.1f}M"],
            y=[d['Ggr'], -d['BonusCost'], d['NGR']],
            connector={"line": {"color": "rgb(63, 63, 63)", "width": 2}},
            decreasing={"marker": {"color": "#F43F5E"}},
            increasing={"marker": {"color": "#10B981"}},
            totals={"marker": {"color": "#38BDF8"}}
        ))
        fig_waterfall = aplicar_template_financeiro(fig_waterfall, f"Composição de Margem Líquida - {mes_foco}")
        st.plotly_chart(fig_waterfall, use_container_width=True)
        
        st.markdown(f"""
        <div class='consultant-report'>
        <b>DIAGNÓSTICO APROFUNDADO DO MÊS ({mes_foco.upper()}):</b><br>
        • A eficiência de retenção está refletida no Ticket Médio de <b>R$ {d['Ticket_Medio_Dep']:,.2f}</b> por depósito realizado na plataforma.<br>
        • A relação entre a receita gerada pelo usuário e o capital "devolvido" como estímulo (Retention Ad-Spend) revela um sacrifício de margem brutal de <b>{d['Bonus_Ratio']}%</b>.<br>
        • Para que a operação (NGR) volte a apresentar crescimento sustentável sem depender de alta volatilidade (Hold estourando), a taxa de <b>New Money (FTD Ratio)</b> precisa obrigatoriamente cruzar a barreira de segurança de 15%. Atualmente encontra-se em {d['FTD_Ratio']}%, o que força o time de CRM a sangrar a margem líquida para tentar engajar usuários com alto índice de fadiga.
        </div>
        """, unsafe_allow_html=True)

    elif menu == "4. Capital Efficiency & Elasticity":
        st.markdown("<h2 class='section-title'>4. Teoria da Elasticidade Aplicada</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class='consultant-report'>
        <b>ANÁLISE DE SENSIBILIDADE DO FLUXO DE CAIXA:</b><br><br>
        O cruzamento dos dados de 2025 com o Q1/2026 revela um fenômeno de <b>Fadiga de Retenção</b>. <br><br>
        <b>1. Elasticidade de Aquisição Inelástica:</b> A nossa curva de FTDs despencou, indicando que a injeção de capital novo não está respondendo ao estímulo. Mantivemos contas altas de Afiliados, mas a quantidade demandada de novos depósitos é inelástica ao gasto atual.<br><br>
        <b>2. Elasticidade de Retenção Altamente Sensível:</b> A base veterana condicionou o jogo ao bônus. No entanto, o bônus não gera mais ROI, pois não há FTD suficiente para substituir o capital que "vaza" no churn natural.
        </div>
        """, unsafe_allow_html=True)

    elif menu == "5. Market Share & Unit Economics":
        st.markdown("<h2 class='section-title'>5. Benchmark de Mercado e Unit Economics</h2>", unsafe_allow_html=True)
        base_val = df_audit['Bet'].iloc[0]
        df_audit['Internal_Index'] = (df_audit['Bet'] / base_val) * 100
        
        c_m1, c_m2 = st.columns(2)
        with c_m1:
            figm = go.Figure()
            figm.add_trace(go.Scatter(x=df_mercado['Periodo'], y=df_mercado['Market_Index'], name='BENCHMARK MERCADO', line=dict(dash='dot', color='#8B5CF6')))
            figm.add_trace(go.Scatter(x=df_audit['Periodo'], y=df_audit['Internal_Index'], name='NOSSA OPERAÇÃO', line=dict(color='#38BDF8', width=5)))
            st.plotly_chart(aplicar_template_financeiro(figm, "Índice de Retração vs Proxy Nacional (Base 100)"), use_container_width=True)
        with c_m2:
            df_jogos = pd.DataFrame({
                "Jogo": ["Aviator (Spribe)", "Fortune Tiger (PG Soft)", "Roleta Brasileira", "Mines (Original)", "Gates of Olympus"],
                "Volume (%)": [31.5, 24.2, 18.0, 12.3, 8.5],
                "Cor": ['#38BDF8', '#10B981', '#F59E0B', '#F43F5E', '#8B5CF6']
            })
            figj = px.bar(df_jogos, x="Volume (%)", y="Jogo", orientation='h', color="Jogo", color_discrete_sequence=df_jogos['Cor'].tolist())
            st.plotly_chart(aplicar_template_financeiro(figj, "Capilaridade de Faturamento por Provedor Base"), use_container_width=True)

        st.markdown("""
        <div class='consultant-report'>
        <b>VEREDITO DO MARKET SHARE:</b><br>
        A dinâmica do mercado iGaming no Brasil em 2026 está em fase de consolidação regulatória. Notamos que o Proxy de Mercado Nacional acompanha ciclos sazonais claros. Contudo, a divergência na nossa curva confirma a tese de "Perda de Market Share por Deficiência de Ad-Spend".<br><br>
        <b>ESCRUTÍNIO POR PROVEDOR:</b><br>
        <b>1. Spribe:</b> Âncora de engajamento diário. <br>
        <b>2. PG Soft:</b> Trator do varejo (Fortune Tiger) com volume colossal de micro-apostas.<br>
        <b>3. Evolution:</b> Sala de Jantar VIP. O fator psicológico impulsiona rentabilidade perto de 8.5%.
        </div>
        """, unsafe_allow_html=True)

    elif menu == "6. Roadmap Strategy: 90 Days":
        st.markdown("<h2 class='section-title'>6. Action Plan: Intervenção C-Level</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class='consultant-report'>
        <b>FASE 1: CHOQUE DE AQUISIÇÃO E REDE DE AFILIADOS (Dias 1 a 30) - Estancar a Hemorragia</b><br>
        • <b>Desvio de Orçamento:</b> Corte radical de 35% na verba passiva de Bônus. Injetar em tráfego SEO/Google.<br>
        • <b>Meta de CPA:</b> Elevar o FTD de volta ao patamar de segurança acima de R$ 3,5M mensais.<br>
        • Migrar parceiros de afiliados para RevShare sobre NGR puro.<br><br>
        <b>FASE 2: REFATORAÇÃO DO CRM E FIM DO BONUS TRAP (Dias 31 a 60)</b><br>
        • Banir bônus incondicionais que alimentam "Bonus Hunters".<br>
        • Gamificação: Implementar Rakebacks pagos apenas sobre o volume apostado fiduciário.<br><br>
        <b>FASE 3: BLINDAGEM DO PRODUTO (Dias 61 a 90)</b><br>
        • <b>Regra de Ouro:</b> Não tocar no Hold! Diretórios sob pressão tendem a aumentar o Hold, o que aceleraria o churn. A crise é de Tráfego, não de Produto. Mantenha o RTP.
        </div>
        """, unsafe_allow_html=True)

    elif menu == "7. Technical Mathematical Repository":
        st.markdown("<h2 class='section-title'>7. Repositório de Métricas e Indexadores</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class='consultant-report'>
        <b>MODELAGEM MATEMÁTICA (iGAMING STANDARDS):</b> Este repositório documenta o racional algébrico utilizado.
        </div>
        """, unsafe_allow_html=True)
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            st.markdown("### 📐 1. Hold Margin (Margem Bruta)")
            st.latex(r"Hold Margin = \left( \frac{GGR}{Bet} \right) \times 100")
            st.markdown("### 💰 2. NGR (Net Gaming Revenue)")
            st.latex(r"NGR = GGR - (Bonus + Fees + Taxes)")
        with col_f2:
            st.markdown("### 🚀 3. FTD Ratio (Tração de Novo Capital)")
            st.latex(r"FTD Ratio = \left( \frac{Volume FTD}{Total Deposits} \right) \times 100")
            st.markdown("### 👤 4. ARPU (Average Revenue Per User)")
            st.latex(r"ARPU = \frac{GGR}{MAU}")

    elif menu == "8. Scenario Simulator (Predictive)":
        st.markdown("<h2 class='section-title'>8. Simulador de Decisão Financeira (What-If?)</h2>", unsafe_allow_html=True)
        with st.expander("COMO FUNCIONA O ALGORITMO PREDITIVO?"):
            st.markdown("""
            O simulador aplica um coeficiente de **Elasticidade Cruzada**. Ele assume que a redução de Bônus causa uma queda 
            parcial no Giro (Handle), mas se o capital for reinvestido em CPA (Aquisição), o faturamento líquido (NGR) pode 
            recuperar a curva de crescimento positiva.
            """)
        c_s1, c_s2 = st.columns([1, 2])
        with c_s1:
            st.markdown("### 🛠️ Parâmetros de Ajuste")
            red_b = st.slider("Reduzir Bônus em (%):", 0, 100, 40)
            invest_cpa = st.number_input("Injetar em Aquisição (R$):", value=1500000)
            mult_acq = st.slider("Multiplicador de Conversão (CAC/LTV):", 1.0, 5.0, 2.5)
            
            ggr_base = ult['Ggr']
            bonus_base = ult['BonusCost']
            novo_bonus = bonus_base * (1 - red_b/100)
            novo_ftd = invest_cpa * (mult_acq / 2)
            novo_ggr = (ggr_base * 0.8) + (novo_ftd * 0.4) 
            novo_ngr = novo_ggr - novo_bonus
            vitoria = novo_ngr - ult['NGR']
        
        with c_s2:
            fig_sim = go.Figure()
            fig_sim.add_trace(go.Bar(name='Cenário Atual', x=['NGR'], y=[ult['NGR']], marker_color='#64748B'))
            fig_sim.add_trace(go.Bar(name='Cenário Simulado', x=['NGR'], y=[novo_ngr], marker_color='#10B981'))
            fig_sim = aplicar_template_financeiro(fig_sim, "Projeção de Incremento em NGR Real")
            st.plotly_chart(fig_sim, use_container_width=True)
            
            if vitoria > 0:
                st.success(f"💹 **SINAL VERDE:** Esta estratégia geraria um lucro extra de **R$ {vitoria:,.2f}**.")
            else:
                st.error(f"⚠️ **SINAL VERMELHO:** A redução de bônus é muito agressiva para a taxa de conversão atual.")

    elif menu == "9. Anomaly & Fraud Detection Engine":
        st.markdown("<h2 class='section-title'>9. Monitoramento de Anomalias Estatísticas</h2>", unsafe_allow_html=True)
        df_audit['Z_Score_Bonus'] = (df_audit['BonusCost'] - df_audit['BonusCost'].mean()) / df_audit['BonusCost'].std()
        df_audit['Z_Score_FTD'] = (df_audit['FirstDepositsAmount'] - df_audit['FirstDepositsAmount'].mean()) / df_audit['FirstDepositsAmount'].std()
        df_audit['Z_Score_NGR'] = (df_audit['NGR'] - df_audit['NGR'].mean()) / df_audit['NGR'].std()
        
        fig_anom = px.scatter(df_audit, x='Periodo', y='BonusCost', color='Z_Score_Bonus', size='Ggr',
                             title="Audit Trail: Detecção de Over-Bonification",
                             color_continuous_scale=px.colors.diverging.RdYlGn_r)
        st.plotly_chart(aplicar_template_financeiro(fig_anom), use_container_width=True)

        meses_criticos_bonus = df_audit[df_audit['Z_Score_Bonus'].abs() > 1.5][['Periodo', 'BonusCost', 'Bonus_Ratio', 'Z_Score_Bonus']].copy()
        meses_criticos_bonus = meses_criticos_bonus.sort_values(by='Z_Score_Bonus', ascending=False)

        c_a1, c_a2, c_a3 = st.columns(3)
        c_a1.metric("Picos de Bônus", f"{(df_audit['Z_Score_Bonus'] > 1.5).sum():,.0f}")
        c_a2.metric("Quedas de FTD", f"{(df_audit['Z_Score_FTD'] < -1.0).sum():,.0f}")
        c_a3.metric("Meses com NGR Atípico", f"{(df_audit['Z_Score_NGR'].abs() > 1.0).sum():,.0f}")

        if not meses_criticos_bonus.empty:
            st.markdown("### 🔎 Meses Prioritários para Auditoria")
            st.dataframe(
                meses_criticos_bonus.style.format({
                    "BonusCost": "R$ {:,.2f}",
                    "Bonus_Ratio": "{:,.2f}%",
                    "Z_Score_Bonus": "{:,.2f}"
                }),
                use_container_width=True
            )
        
        st.markdown("""
        <div class='consultant-report'>
        <b>AUDITORIA FORENSE:</b><br>
        Esta seção aponta meses em que bônus, captação de capital novo e receita líquida saíram da faixa estatística esperada.<br><br>
        <b>Como interpretar:</b><br>
        • <b>Z-Score de Bônus alto:</b> evidencia excesso promocional e risco de compra artificial de volume.<br>
        • <b>Z-Score de FTD muito baixo:</b> mostra retração de capital novo e aumento da dependência de reciclagem da base antiga.<br>
        • <b>Z-Score de NGR fora do padrão:</b> indica distorção relevante de margem líquida, positiva ou negativa.<br><br>
        <b>Encaminhamento gerencial:</b><br>
        • auditar origem do tráfego e campanhas do período;<br>
        • revisar se o bônus foi direcionado para retenção saudável ou para sustentar comportamento improdutivo;<br>
        • comparar o mês anômalo com os pares anteriores e posteriores para medir recorrência;<br>
        • validar com risco e CRM se houve abuso, cluster de jogadores oportunistas ou deterioração de cohort quality.
        </div>
        """, unsafe_allow_html=True)

    elif menu == "10. Affiliate Performance (Top/Bottom 20)":
        st.markdown("<h2 class='section-title'>10. Módulo Forense de Afiliados</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class='consultant-report'>
        <b>AUDITORIA DE PARCEIROS B2B:</b><br>
        Este módulo ranqueia a eficiência de capital dos parceiros (Afiliados). 
        Foi isolado o indicador de <b>Net Revenue (Receita Líquida Real)</b> para identificar quais parceiros estão gerando margem financeira versus aqueles que estão apenas consumindo recursos via "FIXED FEE" e entregando tráfego sem retenção.
        </div>
        """, unsafe_allow_html=True)

        if not df_afiliados.empty:
            periodos_afiliados = [str(p) for p in df_afiliados["Periodo"].dropna().unique().tolist()]
            periodo_foco = st.selectbox("Selecione o período de afiliados:", periodos_afiliados, index=0)
            df_periodo = df_afiliados[df_afiliados["Periodo"] == periodo_foco].copy()

            st.markdown(
                f"<div class='kpi-block'><div class='kpi-title'>Período em análise</div><div class='kpi-text'>Todas as tabelas e gráficos abaixo referem-se a <b>{periodo_foco}</b>.</div></div>",
                unsafe_allow_html=True
            )

            df_sorted = df_periodo.sort_values(by="Net Revenue", ascending=False)
            top_20 = df_sorted.head(20).copy()
            bottom_20 = df_sorted.tail(20).sort_values(by="Net Revenue", ascending=True).copy()
            top_20["NGR Afiliado"] = top_20["Net Revenue"]
            bottom_20["NGR Afiliado"] = bottom_20["Net Revenue"]

            format_dict = {
                "NGR Afiliado": "R$ {:,.2f}",
                "Net Revenue": "R$ {:,.2f}",
                "Revenue Share Reward": "R$ {:,.2f}",
                "CPA Reward": "R$ {:,.2f}",
                "FIXED FEE": "R$ {:,.2f}",
                "Total Reward": "R$ {:,.2f}"
            }

            # CORREÇÃO: Utilizando formatação nativa do Streamlit para evitar erros de ausência do Matplotlib
            st.markdown(f"<h3 style='color:#10B981; margin-top:20px; font-weight:800;'>🏆 TOP 20 AFILIADOS - {periodo_foco} (MAIOR RECEITA LÍQUIDA GERADA)</h3>", unsafe_allow_html=True)
            st.dataframe(top_20.style.format(format_dict), use_container_width=True)

            st.markdown(f"<br><h3 style='color:#F43F5E; margin-top:20px; font-weight:800;'>⚠️ BOTTOM 20 AFILIADOS - {periodo_foco} (PREJUÍZO OU BAIXA EFICIÊNCIA)</h3>", unsafe_allow_html=True)
            st.dataframe(bottom_20.style.format(format_dict), use_container_width=True)
            
            st.markdown("<h3 style='color:#FFFFFF; margin-top:26px; font-weight:800;'>📈 NGR DOS AFILIADOS E CUSTO DE AQUISIÇÃO</h3>", unsafe_allow_html=True)

            top_20_chart = top_20.sort_values(by="NGR Afiliado", ascending=False)
            top_20_chart["Affiliate Label"] = top_20_chart["Affiliate Name"].astype(str).str.slice(0, 22)
            fig_aff_top = go.Figure()
            fig_aff_top.add_trace(go.Bar(
                x=top_20_chart['Affiliate Label'],
                y=top_20_chart['CPA Reward'],
                name='CPA Reward (Custo)',
                marker_color='#F59E0B',
                hovertemplate='<b>%{x}</b><br>CPA: R$ %{y:,.2f}<extra></extra>'
            ))
            fig_aff_top.add_trace(go.Bar(
                x=top_20_chart['Affiliate Label'],
                y=top_20_chart['FIXED FEE'],
                name='FIXED FEE (Custo Adicional)',
                marker_color='#8B5CF6',
                hovertemplate='<b>%{x}</b><br>FIXED FEE: R$ %{y:,.2f}<extra></extra>'
            ))
            fig_aff_top.add_trace(go.Scatter(
                x=top_20_chart['Affiliate Label'],
                y=top_20_chart['NGR Afiliado'],
                name='NGR Afiliado',
                mode='lines+markers',
                marker=dict(color='#10B981', size=7),
                line=dict(color='#10B981', width=3),
                hovertemplate='<b>%{x}</b><br>NGR: R$ %{y:,.2f}<extra></extra>'
            ))

            fig_aff_top.update_layout(
                barmode='stack',
                height=560,
                xaxis=dict(tickangle=-35, automargin=True, tickfont=dict(size=10)),
                yaxis=dict(tickfont=dict(size=10))
            )
            fig_aff_top = aplicar_template_financeiro(fig_aff_top, f"Análise de Custo de Aquisição + NGR (Top 20) - {periodo_foco}")
            st.plotly_chart(fig_aff_top, use_container_width=True)

            bottom_20_chart = bottom_20.sort_values(by="NGR Afiliado", ascending=True)
            bottom_20_chart["Affiliate Label"] = bottom_20_chart["Affiliate Name"].astype(str).str.slice(0, 22)
            fig_aff_bottom = go.Figure()
            fig_aff_bottom.add_trace(go.Bar(
                x=bottom_20_chart['Affiliate Label'],
                y=bottom_20_chart['CPA Reward'],
                name='CPA Reward (Custo)',
                marker_color='#F59E0B',
                hovertemplate='<b>%{x}</b><br>CPA: R$ %{y:,.2f}<extra></extra>'
            ))
            fig_aff_bottom.add_trace(go.Bar(
                x=bottom_20_chart['Affiliate Label'],
                y=bottom_20_chart['FIXED FEE'],
                name='FIXED FEE (Custo Adicional)',
                marker_color='#8B5CF6',
                hovertemplate='<b>%{x}</b><br>FIXED FEE: R$ %{y:,.2f}<extra></extra>'
            ))
            fig_aff_bottom.add_trace(go.Scatter(
                x=bottom_20_chart['Affiliate Label'],
                y=bottom_20_chart['NGR Afiliado'],
                name='NGR Afiliado',
                mode='lines+markers',
                marker=dict(color='#F43F5E', size=7),
                line=dict(color='#F43F5E', width=3),
                hovertemplate='<b>%{x}</b><br>NGR: R$ %{y:,.2f}<extra></extra>'
            ))

            fig_aff_bottom.update_layout(
                barmode='stack',
                height=560,
                xaxis=dict(tickangle=-35, automargin=True, tickfont=dict(size=10)),
                yaxis=dict(tickfont=dict(size=10))
            )
            fig_aff_bottom = aplicar_template_financeiro(fig_aff_bottom, f"Análise de Custo de Aquisição + NGR (Bottom 20) - {periodo_foco}")
            st.plotly_chart(fig_aff_bottom, use_container_width=True)

else:
    st.error("❌ FALHA NA CARGA: O Motor de Dados não detectou a base blindada.")

def log_system_access_telemetry():
    pass

def handle_high_concurrency_requests():
    pass

# Fim de script
