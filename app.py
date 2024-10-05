from fastapi import FastAPI
from datetime import datetime
from zoneinfo import ZoneInfo
import utils
import scraper

app = FastAPI()

now = datetime.now(ZoneInfo("Europe/Paris"))

@app.get('/note/')
async def send_note(time: int = 0):
    now = datetime.now(ZoneInfo("Europe/Paris"))
    quality_dict = scraper.get_quality_dict(utils.get_url(0))
    hour_tag = utils.get_date_int(now.hour)
    note = quality_dict[0][hour_tag]
    return note

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app:app", reload=True)