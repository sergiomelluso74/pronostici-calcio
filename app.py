import streamlit as st
import requests
import json

st.title("Sistema di Pronostici Calcio - Estrazione Diretta")
st.write("Questo software estrae i dati direttamente dalla fonte senza usare API a pagamento.")

if st.button("Estrai Partite Odierne da Sofascore"):
    with st.spinner("Infiltrazione in corso..."):
        # L'indirizzo interno nascosto che Sofascore usa per mostrare i risultati sul suo sito
        url = "https://api.sofascore.com/api/v1/sport/football/events/schedule/today"
        
        # Tecnica di camuffamento: diciamo al server che siamo un normale utente su Google Chrome
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "*/*",
            "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
            "Referer": "https://www.sofascore.com/"
        }
        
        try:
            # Eseguiamo la richiesta di estrazione
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                st.success("Dati estratti con successo e blocco superato!")
                dati = response.json()
                
                # Mostriamo a schermo i dati grezzi estratti
                st.json(dati)
            elif response.status_code == 403:
                st.error("Accesso negato: il buttafuori (Cloudflare) ha riconosciuto che siamo un bot. Dobbiamo potenziare il camuffamento.")
            else:
                st.error(f"Errore imprevisto. Codice: {response.status_code}")
                
        except Exception as e:
            st.error(f"Si è verificato un errore tecnico: {e}")