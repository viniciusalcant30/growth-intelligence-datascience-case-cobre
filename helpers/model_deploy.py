import joblib
from pathlib import Path
from datetime import datetime

def save_model(model, path: str | Path) -> Path:
    """
    Persist a trained scikit-learn model or pipeline to disk safely.

    - Ensures the directory exists.
    - Forces the .joblib extension (recommended for sklearn objects).
    - Appends a timestamp to avoid overwriting previous models.
    - Returns the absolute saved path.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    new_name = f"{path.stem}_{timestamp}.joblib"
    path = path.with_name(new_name)

    joblib.dump(model, path)
    return path.resolve()


def load_model(path: str | Path):
    return joblib.load(path)