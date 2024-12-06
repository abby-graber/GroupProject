from . import orders, order_details, menu_items, payments, resources, promotions, ratings_and_reviews


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(menu_items.router)
    app.include_router(payments.router)
    app.include_router(resources.router)
    app.include_router(promotions.router)
    app.include_router(ratings_and_reviews)
