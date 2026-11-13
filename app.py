import streamlit as st
from curl_cffi import requests

st.title("Sistema di Pronostici Calcio - Artiglieria Pesante")
st.write("Infiltrazione crittografica di livello militare per disintegrare Cloudflare.")

if st.button("Estrai Partite Odierne da Sofascore"):
    with st.spinner("Aggiramento crittografico in corso..."):
        url = "https://api.sofascore.com/api/v1/sport/football/events/schedule/today"
        
        try:
            # Impersoniamo Chrome 110 a livello crittografico profondo
            response = requests.get(url, impersonate="chrome110")
            
            if response.status_code == 200:
                st.success("BINGO! Difese disintegrate. Dati estratti con successo!")
                st.json(response.json())
            else:
                st.error(f"Muro ancora in piedi. Codice errore: {response.status_code}")
                
        except Exception as e:
            st.error(f"Errore tecnico di sistema: {e}")
