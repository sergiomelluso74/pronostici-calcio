import streamlit as st
import cloudscraper

st.title("Sistema di Pronostici Calcio - Infiltrazione Livello 2")
st.write("Questo software usa un browser fantasma per eludere i blocchi di sicurezza.")

if st.button("Estrai Partite Odierne da Sofascore"):
    with st.spinner("Infiltrazione avanzata in corso..."):
        url = "https://api.sofascore.com/api/v1/sport/football/events/schedule/today"
        
        # Creiamo un "browser fantasma" che simula al 100% un vero Google Chrome
        scraper = cloudscraper.create_scraper(browser={
            'browser': 'chrome',
            'platform': 'windows',
            'desktop': True
        })
        
        try:
            response = scraper.get(url)
            
            if response.status_code == 200:
                st.success("BINGO! Il buttafuori è stato ingannato. Dati estratti con successo!")
                # Mostra i dati catturati a schermo
                st.json(response.json())
            elif response.status_code == 403:
                st.error("Cloudflare ha gli scudi al massimo livello (Errore 403). Dobbiamo passare al Piano C.")
            else:
                st.error(f"Errore imprevisto dal server. Codice: {response.status_code}")
                
        except Exception as e:
            st.error(f"Errore tecnico di connessione: {e}")
