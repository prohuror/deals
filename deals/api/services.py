from deals.api.repository import DealRepository


def get_best_five_clients():
    deals_repository = DealRepository()
    best_five_deals = deals_repository.get_best_five_deals()
    best_five_customers = [customer['customer'] for customer in best_five_deals]
    best_customers_deals = deals_repository.get_best_customers_deals(best_five_customers)
