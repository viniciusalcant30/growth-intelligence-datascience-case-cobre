from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def load_leads_with_deals(closed_path: str | Path | None = None,
                          qualified_path: str | Path | None = None):
    
    closed_path = DATA_DIR / "olist_closed_deals_dataset.csv" if closed_path is None else Path(closed_path)
    qualified_path = DATA_DIR / "olist_marketing_qualified_leads_dataset.csv" if qualified_path is None else Path(qualified_path)

    df_closed = pd.read_csv(closed_path).assign(conversed_lead=True)
    df_qualified = pd.read_csv(qualified_path)

    df_merged = pd.merge(df_qualified, df_closed, how="left", on="mql_id")
    df_merged["conversed_lead"] = df_merged['conversed_lead'].astype('boolean').fillna(False)
    df_merged["first_contact_date"] = pd.to_datetime(df_merged['first_contact_date'])
    df_merged["won_date"] = pd.to_datetime(df_merged["won_date"])

    return df_merged
