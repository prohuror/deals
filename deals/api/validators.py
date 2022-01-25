def validate_deals(deals):
    for deal in deals:
        if not str(deal['total']).isnumeric() or not str(deal['total']).isnumeric():
            return {'result': False, 'error': 'Total and quantity must be INT'}
        else:
            return {'result': True, 'error': ''}

