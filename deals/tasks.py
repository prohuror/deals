from app.celery import app
from deals.api.validators import validate_deals
from deals.api.repository import DealRepository


@app.task
def import_deals(deals):
    if validate_deals(deals)['result']:
        DealRepository.create_deals(deals)
    else:
        return False
