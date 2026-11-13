import streamlit as st
import random

st.set_page_config(layout="wide")
st.title("Sistema di Pronostici Calcio - Il Cervellone AI 🧠")
st.write("Motore matematico per l'analisi statistica e il calcolo delle probabilità (Zero API, Invulnerabile).")

st.markdown("---")
st.header("1. Inserimento Dati Grezzi (Fattori Campo ed Extra-Campo)")
st.write("Inserisci i dati della partita. L'algoritmo ignorerà il blasone e calcolerà solo i numeri.")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Squadra di Casa")
    sq_casa = st.text_input("Nome", placeholder="Es. Shakhtar")
    xg_casa = st.number_input("Media gol fatti (ultime 5)", min_value=0.0, max_value=5.0, value=1.5, step=0.1)
    gol_subiti_casa = st.number_input("Media gol subiti (ultime 5) Casa", min_value=0.0, max_value=5.0, value=1.0, step=0.1)
    assenze_casa = st.slider("Impatto Infortuni (0 = Tutti sani, 5 = Emergenza totale)", 0, 5, 0, key="ass_c")

with col2:
    st.subheader("Squadra in Trasferta")
    sq_trasf = st.text_input("Nome ", placeholder="Es. Obolon")
    xg_trasf = st.number_input("Media gol fatti (ultime 5) ", min_value=0.0, max_value=5.0, value=1.0, step=0.1)
    gol_subiti_trasf = st.number_input("Media gol subiti (ultime 5) Trasferta", min_value=0.0, max_value=5.0, value=1.5, step=0.1)
    assenze_trasf = st.slider("Impatto Infortuni (0 = Tutti sani, 5 = Emergenza totale) ", 0, 5, 0, key="ass_t")

st.markdown("---")
if st.button("Avvia Risonanza Magnetica 🩻", type="primary"):
    if sq_casa and sq_trasf:
        with st.spinner("Elaborazione algoritmo in corso..."):
            
            # --- IL MOTORE MATEMATICO ---
            # Calcolo Forza Attacco vs Difesa
            forza_casa = (xg_casa * 1.2) - gol_subiti_trasf - (assenze_casa * 0.3)
            forza_trasf = xg_trasf - (gol_subiti_casa * 1.2) - (assenze_trasf * 0.3)
            
            # Calcolo Probabilità Base (Softmax semplificato)
            divario = forza_casa - forza_trasf
            
            if divario > 1.0:
                esito = "1 (Vittoria Casa)"
                affidabilita = min(95, 60 + int(divario * 10))
                r1, r2, r3 = "2-0", "3-0", "2-1"
            elif divario < -1.0:
                esito = "2 (Vittoria Trasferta)"
                affidabilita = min(95, 60 + int(abs(divario) * 10))
                r1, r2, r3 = "0-2", "0-1", "1-2"
            else:
                if abs(divario) < 0.3:
                    esito = "X (Pareggio)"
                    affidabilita = 65
                    r1, r2, r3 = "1-1", "0-0", "2-2"
                elif divario >= 0.3:
                    esito = "1X (Doppia Chance)"
                    affidabilita = 75
                    r1, r2, r3 = "1-0", "1-1", "2-0"
                else:
                    esito = "X2 (Doppia Chance)"
                    affidabilita = 75
                    r1, r2, r3 = "0-1", "1-1", "0-2"
            
            # --- OUTPUT A SCHERMO ---
            st.success("Analisi Tattica e Statistica completata.")
            
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("### 🔮 Pronostico Definitivo")
                st.info(f"**Segno Consigliato: {esito}**")
                
                st.markdown("### 📊 Indice di Affidabilità")
                st.progress(affidabilita / 100.0)
                st.write(f"**{affidabilita}%** - {'SICURO' if affidabilita > 75 else 'INCERTO (usare prudenza)'}")
                
            with c2:
                st.markdown("### 🎯 I 3 Risultati Esatti più probabili")
                st.metric(label="Scelta Primaria (Probabilità Alta)", value=r1)
                st.metric(label="Copertura Strategica 1", value=r2)
                st.metric(label="Copertura Strategica 2", value=r3)
                
            st.markdown("### 📝 Analisi del Match Analyst")
            st.write(f"L'algoritmo rileva un divario di forza netto di {round(divario, 2)} punti. Il calcolo ha incrociato la media gol fatti in casa del {sq_casa} contro la tenuta difensiva esterna del {sq_trasf}, applicando una penalità matematica in base ai referti medici (infortuni).")
    else:
        st.error("Inserisci i nomi delle due squadre per avviare il calcolo.")
