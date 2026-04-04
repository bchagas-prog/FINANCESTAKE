import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import warnings

warnings.filterwarnings('ignore')

# ==============================================================================
# 1. UI & CORPORATE DESIGN
# ==============================================================================
st.set_page_config(page_title="OPERAÇÃO Q1 2026 - AUDITORIA", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    html, body, [data-testid="stAppViewContainer"] { font-family: 'Inter', sans-serif; background-color: #0B1120 !important; color: #F8FAFC !important; }
    [data-testid="stSidebar"] { background-color: #0F172A !important; border-right: 1px solid #1E293B !important; }
    .kpi-card { background: linear-gradient(145deg, #162032, #0F172A); padding: 20px; border-radius: 12px; border: 1px solid #1E293B; box-shadow: 0 4px 6px rgba(0,0,0,0.3); transition: transform 0.2s;}
    .kpi-card:hover { transform: translateY(-3px); border-color: #38BDF8; }
    .kpi-title { color: #94A3B8; font-size: 0.85rem; text-transform: uppercase; font-weight: 800; letter-spacing: 1px; margin-bottom: 8px; }
    .kpi-value { color: #FFFFFF; font-size: 1.8rem; font-weight: 800; }
    .kpi-sub { color: #38BDF8; font-size: 0.85rem; font-weight: 600; margin-top: 5px; }
    .kpi-red { color: #F43F5E !important; }
    .kpi-green { color: #10B981 !important; }
    .report-text { background-color: #111827; padding: 20px; border-left: 4px solid #38BDF8; border-radius: 4px; font-size: 0.95rem; line-height: 1.6; margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);}
    .section-title { color: #FFFFFF !important; font-weight: 800; font-size: 1.4rem; text-transform: uppercase; letter-spacing: 2px; border-bottom: 2px solid #38BDF8; padding-bottom: 8px; margin-top: 30px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

def aplicar_template_financeiro(fig, titulo=""):
    fig.update_layout(
        title=dict(text=titulo, font=dict(color="#FFFFFF", size=18, family="Inter", weight="bold")),
        template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#FFFFFF", family="Inter"),
        hovermode="x unified",
        margin=dict(l=20, r=20, t=60, b=20)
    )
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#1E293B', griddash='dot', zeroline=False)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#1E293B', griddash='dot', zeroline=False)
    return fig

# Funções de Estilização que NÃO precisam de matplotlib
def color_negative_red(val):
    color = '#F43F5E' if val < 0 else '#10B981'
    return f'color: {color}'

# ==============================================================================
# 2. ETL: MOTOR DE DADOS EMBUTIDO (HARDCODED Q1 2026)
# ==============================================================================
@st.cache_data(show_spinner="Carregando dados Q1 2026...")
def carregar_dados_q1_2026():
    dados_q1 = [
        {"Login": "igalech59", "Date Created": "18/01/2026", "Period Deposit Amount": 0.00, "Bonus Total": 2404.85, "Period Turnover": 89597.50, "GGR": -4731.62, "Balance": 0.00},
        {"Login": "Tambapet", "Date Created": "04/01/2026", "Period Deposit Amount": 123.00, "Bonus Total": 2077.03, "Period Turnover": 1238.50, "GGR": -536.15, "Balance": 0.00},
        {"Login": "Douglas Siviero", "Date Created": "02/01/2026", "Period Deposit Amount": 1746.33, "Bonus Total": 2542.70, "Period Turnover": 7853.38, "GGR": -1588.63, "Balance": 0.00},
        {"Login": "anobre46", "Date Created": "03/01/2026", "Period Deposit Amount": 1930.80, "Bonus Total": 721.60, "Period Turnover": 5039.30, "GGR": -2454.50, "Balance": 0.00},
        {"Login": "Tgardoni", "Date Created": "21/01/2026", "Period Deposit Amount": 0.00, "Bonus Total": 703.76, "Period Turnover": 223705.00, "GGR": -16320.00, "Balance": 50.00},
        {"Login": "José1237", "Date Created": "03/01/2026", "Period Deposit Amount": 500.00, "Bonus Total": 671.66, "Period Turnover": 1122.35, "GGR": -471.55, "Balance": 0.00},
        {"Login": "Rosiane1970", "Date Created": "27/03/2026", "Period Deposit Amount": 4000.00, "Bonus Total": 0.00, "Period Turnover": 0.00, "GGR": 4000.00, "Balance": 0.00},
        {"Login": "marceelorezende", "Date Created": "10/01/2026", "Period Deposit Amount": 10897.00, "Bonus Total": 0.00, "Period Turnover": 57574.60, "GGR": 12398.17, "Balance": 0.40},
        {"Login": "Gatadasorte", "Date Created": "27/03/2026", "Period Deposit Amount": 270.00, "Bonus Total": 0.00, "Period Turnover": 1633.80, "GGR": 269.76, "Balance": 0.24},
        {"Login": "Roner1997", "Date Created": "27/03/2026", "Period Deposit Amount": 250.00, "Bonus Total": 0.00, "Period Turnover": 0.00, "GGR": 250.00, "Balance": 0.00},
        {"Login": "Paloma8341", "Date Created": "27/03/2026", "Period Deposit Amount": 1700.00, "Bonus Total": 0.00, "Period Turnover": 0.00, "GGR": 1700.00, "Balance": 0.00},
        {"Login": "RebecaRamos", "Date Created": "27/03/2026", "Period Deposit Amount": 750.00, "Bonus Total": 0.00, "Period Turnover": 0.00, "GGR": 750.00, "Balance": 0.00},
        {"Login": "Gremio049", "Date Created": "27/03/2026", "Period Deposit Amount": 2160.00, "Bonus Total": 0.00, "Period Turnover": 0.00, "GGR": 2160.00, "Balance": 0.00},
        {"Login": "eltonmassashi", "Date Created": "27/03/2026", "Period Deposit Amount": 150.00, "Bonus Total": 0.00, "Period Turnover": 368.90, "GGR": 149.94, "Balance": 0.06},
        {"Login": "Arthurarauj", "Date Created": "27/03/2026", "Period Deposit Amount": 74.00, "Bonus Total": 0.00, "Period Turnover": 0.00, "GGR": 74.00, "Balance": 0.00},
        {"Login": "Linny36", "Date Created": "27/03/2026", "Period Deposit Amount": 40.00, "Bonus Total": 0.00, "Period Turnover": 144.00, "GGR": 39.60, "Balance": 0.40},
        {"Login": "Vini2006", "Date Created": "27/03/2026", "Period Deposit Amount": 45.00, "Bonus Total": 0.00, "Period Turnover": 0.00, "GGR": 45.00, "Balance": 0.35},
        {"Login": "wendel9xis", "Date Created": "27/03/2026", "Period Deposit Amount": 20.00, "Bonus Total": 0.00, "Period Turnover": 20.00, "GGR": 20.00, "Balance": 0.00},
        {"Login": "Sla44", "Date Created": "27/03/2026", "Period Deposit Amount": 20.00, "Bonus Total": 0.00, "Period Turnover": 54.00, "GGR": 19.70, "Balance": 0.30},
        {"Login": "Fabriciotop1", "Date Created": "27/03/2026", "Period Deposit Amount": 20.00, "Bonus Total": 0.00, "Period Turnover": 0.00, "GGR": 20.00, "Balance": 0.00},
    ]
    df_q1 = pd.DataFrame(dados_q1)
    
    cond_freeroller = (df_q1['Period Deposit Amount'] == 0) & (df_q1['Bonus Total'] > 50) & (df_q1['Period Turnover'] > 0)
    cond_injusticado = (df_q1['Period Deposit Amount'] > 200) & (df_q1['GGR'] > 100) & (df_q1['Bonus Total'] == 0)
    cond_sanguessuga = (df_q1['Bonus Total'] > 100) & (df_q1['GGR'] < -50)
    
    df_q1['Perfil'] = 'Regular (Sem Bônus)'
    df_q1.loc[cond_freeroller, 'Perfil'] = 'Freeroller (Risco de Fraude)'
    df_q1.loc[cond_sanguessuga, 'Perfil'] = 'Caçador de Bônus (Prejuízo)'
    df_q1.loc[cond_injusticado, 'Perfil'] = 'VIP Injustiçado (Risco Churn)'
    return df_q1

df = carregar_dados_q1_2026()

# ==============================================================================
# 3. HEADER EXECUTIVO
# ==============================================================================
st.title("🎯 ANÁLISE DE OPERAÇÃO: Q1 2026 (Jan-Mar)")
st.markdown("<p style='color: #94A3B8; font-size: 1.1rem;'>Auditoria de Faturamento, Retenção e Alocação de Bônus (Dados Reais do Período)</p>", unsafe_allow_html=True)

total_ggr = df['GGR'].sum()
total_bonus = df['Bonus Total'].sum()
bonus_ratio = (total_bonus / total_ggr * 100) if total_ggr > 0 else 0
jogadores_ativos = len(df)
jogadores_zerados = len(df[df['Balance'] <= 0.5])
taxa_churn_imediato = (jogadores_zerados / jogadores_ativos * 100) if jogadores_ativos > 0 else 0

st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
c1.markdown(f"<div class='kpi-card'><div class='kpi-title'>GGR Bruto (Amostra Q1)</div><div class='kpi-value kpi-green'>R$ {total_ggr:,.2f}</div><div class='kpi-sub'>Receita Retida</div></div>", unsafe_allow_html=True)
col_bonus = "kpi-red" if bonus_ratio > 20 else "kpi-green"
c2.markdown(f"<div class='kpi-card'><div class='kpi-title'>Custo Promocional</div><div class='kpi-value kpi-red'>R$ {total_bonus:,.2f}</div><div class='kpi-sub'>Bônus Total Distribuído</div></div>", unsafe_allow_html=True)
c3.markdown(f"<div class='kpi-card'><div class='kpi-title'>Burn Rate de Contas</div><div class='kpi-value'>{taxa_churn_imediato:.1f}%</div><div class='kpi-sub'>Contas com Saldo Zerado</div></div>", unsafe_allow_html=True)
c4.markdown(f"<div class='kpi-card'><div class='kpi-title'>Risco de Evasão (VIPs)</div><div class='kpi-value kpi-red'>Crítico</div><div class='kpi-sub'>0% de retenção no Top Tier</div></div>", unsafe_allow_html=True)

# ==============================================================================
# 4. DASHBOARD
# ==============================================================================
st.markdown("<h2 class='section-title'>Dinâmica de Retenção: Onde está o nosso dinheiro?</h2>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 O Paradoxo do Bônus", "🚨 O Ralo (VIPs Fake & Freerollers)", "💎 A Traição aos VIPs Reais"])

with tab1:
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        df_bonus_dado = df[df['Bonus Total'] > 0].copy()
        df_bonus_dado['Situação'] = np.where(df_bonus_dado['GGR'] > 0, 'Gerou Lucro (Bom Bônus)', 'Causou Prejuízo (Bônus Mal Gasto)')
        if not df_bonus_dado.empty:
            fig_pie = px.pie(df_bonus_dado, values='Bonus Total', names='Situação', hole=0.5,
                             color='Situação', color_discrete_map={'Gerou Lucro (Bom Bônus)': '#10B981', 'Causou Prejuízo (Bônus Mal Gasto)': '#F43F5E'})
            fig_pie = aplicar_template_financeiro(fig_pie, "Destino Financeiro do Bônus")
            st.plotly_chart(fig_pie, use_container_width=True)
    with col_t2:
        fig_scatter = px.scatter(df, x='Period Deposit Amount', y='Bonus Total', color='Perfil',
                                 hover_data=['Login', 'GGR'], size='Period Deposit Amount',
                                 color_discrete_map={
                                     'Regular (Sem Bônus)': '#64748B', 
                                     'Freeroller (Risco de Fraude)': '#F43F5E',
                                     'Caçador de Bônus (Prejuízo)': '#F59E0B',
                                     'VIP Injustiçado (Risco Churn)': '#10B981'
                                 })
        fig_scatter = aplicar_template_financeiro(fig_scatter, "Esforço de Depósito vs Bônus Recebido")
        st.plotly_chart(fig_scatter, use_container_width=True)

with tab2:
    st.markdown("<h3 style='color:#F43F5E;'>Asfixiando o Caixa: Jogadores que ganham sem depositar</h3>", unsafe_allow_html=True)
    df_freeroller = df[df['Perfil'].isin(['Freeroller (Risco de Fraude)', 'Caçador de Bônus (Prejuízo)'])]
    df_freeroller = df_freeroller[['Login', 'Date Created', 'Bonus Total', 'Period Deposit Amount', 'Period Turnover', 'GGR', 'Balance']]
    df_freeroller = df_freeroller.sort_values(by='Bonus Total', ascending=False)
    
    # FORMATANDO SEM MATPLOTLIB
    st.dataframe(
        df_freeroller.style.format({
            "Bonus Total": "R$ {:,.2f}", "Period Deposit Amount": "R$ {:,.2f}", 
            "Period Turnover": "R$ {:,.2f}", "GGR": "R$ {:,.2f}", "Balance": "R$ {:,.2f}"
        }).map(color_negative_red, subset=['GGR']),
        use_container_width=True
    )

with tab3:
    st.markdown("<h3 style='color:#10B981;'>A Quebra de Retenção: VIPs que dão lucro e são ignorados</h3>", unsafe_allow_html=True)
    df_injusticados = df[df['Perfil'] == 'VIP Injustiçado (Risco Churn)']
    df_injusticados = df_injusticados[['Login', 'Date Created', 'Period Deposit Amount', 'GGR', 'Bonus Total', 'Balance']]
    df_injusticados = df_injusticados.sort_values(by='GGR', ascending=False)
    
    # FORMATANDO SEM MATPLOTLIB
    st.dataframe(
        df_injusticados.style.format({
            "Period Deposit Amount": "R$ {:,.2f}", "GGR": "R$ {:,.2f}", 
            "Bonus Total": "R$ {:,.2f}", "Balance": "R$ {:,.2f}"
        }).map(color_negative_red, subset=['GGR']),
        use_container_width=True
    )
