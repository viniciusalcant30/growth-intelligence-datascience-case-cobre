import requests
import pandas as pd

def get_selic_data(start_date: str, end_date: str) -> pd.DataFrame:
    """
    Fetch historical daily SELIC (Brazil's basic interest rate) data from the
    Banco Central do Brasil (BCB) open data API.
    """

    # API example: https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2023
    # source: https://dadosabertos.bcb.gov.br/dataset/11-taxa-de-juros---selic/resource/b73edc07-bbac-430c-a2cb-b1639e605fa8

    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados"
    params = {
        "formato": "json",
        "dataInicial": start_date,
        "dataFinal": end_date
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if not data:
            raise RuntimeError("No data returned. Check the date range or format (YYYY-MM-DD).")
    except Exception as e:
        raise RuntimeError(f"Failed to fetch SELIC data: {e}")

    df = pd.DataFrame(data)
    df.rename(columns={"data": "date", "valor": "selic"}, inplace=True)
    df["date"] = pd.to_datetime(df["date"], dayfirst=True)
    df["selic"] = pd.to_numeric(df["selic"].str.replace(",", "."))

    return df.sort_values("date").reset_index(drop=True)
