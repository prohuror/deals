# Работы с базой данных
from deals.models import Deal
from django.db.models import Sum
import logging

logger = logging.getLogger(__name__)


class DealRepository:

    @staticmethod
    def _get_common_gems(best_five_deals):
        for deal in best_five_deals:
            deal_copy = best_five_deals.copy()
            deal_copy.pop(best_five_deals.index(deal))
            current_deal_crossing_gems = []
            for deal_copy in deal_copy:
                crossing_gems = list(set(deal_copy['gems']) & set(deal_copy['gems']))
                if crossing_gems:
                    current_deal_crossing_gems.extend(crossing_gems)
            deal['gems'] = current_deal_crossing_gems

    @staticmethod
    def get_best_five_deals():
        best_five_deals = list(
            Deal.objects.values('customer')
                .annotate(total=Sum('total'))
                .order_by('-total')
        )[:5]
        best_five_deals = [{'username': item['customer'], 'spent_money': item['total']}
                           for item in best_five_deals]
        best_five_deals = [
            {
                'username': item['username'],
                'spent_money': item['spent_money'],
                'gems': list(
                    set(Deal.objects.filter(customer=item['username']).values_list('item', flat=True))
                )
            }
            for item in best_five_deals
        ]
        _get_common_gems(best_five_deals)
        return best_five_deals

    @staticmethod
    def get_best_customers_deals(best_five_customers):
        return list(Deal.objects.filter(customer__in=best_five_customers).values('customer', 'item'))

    @staticmethod
    def create_deals(deals):
        for deal in deals:
            try:
                Deal.objects.create(**deal)
            except BaseException as e:
                logger.error(f'error on create deal: {e}')
                return False
        return True
