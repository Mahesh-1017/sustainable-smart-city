from fastapi import APIRouter, UploadFile, File, HTTPException
import tempfile, os

from services.kpi_file_forecaster import forecast_kpi
from services.anomaly_checker import detect_anomalies

router = APIRouter()

@router.post("/upload", summary="Upload KPI CSV and get forecast & anomalies")
async def upload_kpi(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        contents = await file.read()
        tmp.write(contents)
        tmp_path = tmp.name

    forecast = forecast_kpi(tmp_path)
    anomalies = detect_anomalies(tmp_path)

    os.unlink(tmp_path)
    return {"forecast": forecast, "anomalies": anomalies}
