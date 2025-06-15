"""
Mock database of athletic shoes for the shopping agent to use.
"""

SHOES_DATABASE = [
    {
        "id": 1,
        "name": "ZoomX Invincible",
        "brand": "Nike",
        "type": "Running",
        "price": 180.00,
        "sizes": [6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 12],
        "colors": ["Black/White", "White/Black", "Blue/Orange"],
        "features": ["High Cushioning", "Neutral Support", "Road Running"],
        "description": "Designed for maximum cushioning on long runs, featuring ZoomX foam for responsive energy return.",
        "rating": 4.7,
        "image_url": "https://example.com/zoomx_invincible.jpg"
    },
    {
        "id": 2,
        "name": "Ultraboost 23",
        "brand": "Adidas",
        "type": "Running",
        "price": 190.00,
        "sizes": [7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 13],
        "colors": ["Core Black", "Cloud White", "Solar Red"],
        "features": ["Boost Cushioning", "Responsive", "High Energy Return"],
        "description": "Features Boost cushioning for incredible energy return and a Primeknit+ upper for adaptive support and comfort.",
        "rating": 4.8,
        "image_url": "https://example.com/ultraboost_23.jpg"
    },
    {
        "id": 3,
        "name": "Gel-Kayano 29",
        "brand": "ASICS",
        "type": "Running",
        "price": 160.00,
        "sizes": [6, 7, 8, 9, 10, 11, 12],
        "colors": ["Black/White", "Blue/Yellow", "Grey/Blue"],
        "features": ["Stability", "GEL Technology", "Long Distance"],
        "description": "Designed for overpronation, features GEL technology cushioning and Dynamic DuoMax support system.",
        "rating": 4.6,
        "image_url": "https://example.com/gel_kayano_29.jpg"
    },
    {
        "id": 4,
        "name": "Metcon 8",
        "brand": "Nike",
        "type": "Training",
        "price": 130.00,
        "sizes": [7, 8, 9, 10, 11, 12, 13],
        "colors": ["Black/Volt", "White/Red", "Grey/Blue"],
        "features": ["Stable Base", "Durable", "Versatile Training"],
        "description": "Designed for weightlifting and high-intensity workouts with a stable heel and flexible forefoot.",
        "rating": 4.5,
        "image_url": "https://example.com/metcon_8.jpg"
    },
    {
        "id": 5,
        "name": "Nano X2",
        "brand": "Reebok",
        "type": "Training",
        "price": 135.00,
        "sizes": [7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 12],
        "colors": ["Black/White", "White/Gum", "Navy/Yellow"],
        "features": ["Stable", "Flexible", "Durable"],
        "description": "The ultimate training shoe designed for weightlifting, HIIT workouts, and cross-training.",
        "rating": 4.4,
        "image_url": "https://example.com/nano_x2.jpg"
    },
    {
        "id": 6,
        "name": "Fresh Foam 1080v12",
        "brand": "New Balance",
        "type": "Running",
        "price": 160.00,
        "sizes": [7, 8, 8.5, 9, 9.5, 10, 10.5, 11, 12],
        "colors": ["Black/Thunder", "White/Blue", "Grey/Black"],
        "features": ["Cushioned", "Neutral", "Road Running"],
        "description": "Premium cushioning for distance runners who want soft, responsive comfort for every mile.",
        "rating": 4.7,
        "image_url": "https://example.com/fresh_foam_1080.jpg"
    },
    {
        "id": 7,
        "name": "Hyperdunk 2023",
        "brand": "Nike",
        "type": "Basketball",
        "price": 140.00,
        "sizes": [8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 13],
        "colors": ["Black/Red", "White/Blue", "Grey/Orange"],
        "features": ["Responsive", "Ankle Support", "Cushioned"],
        "description": "Basketball shoes designed for explosive performance with Air Zoom cushioning and supportive fit.",
        "rating": 4.6,
        "image_url": "https://example.com/hyperdunk_2023.jpg"
    },
    {
        "id": 8,
        "name": "Trail Runner SL",
        "brand": "Salomon",
        "type": "Trail Running",
        "price": 130.00,
        "sizes": [7, 8, 9, 10, 11, 12],
        "colors": ["Black/Grey", "Blue/Yellow", "Red/Black"],
        "features": ["Trail Grip", "Waterproof", "Durable"],
        "description": "All-terrain trail running shoe with exceptional grip and protection for technical trails.",
        "rating": 4.8,
        "image_url": "https://example.com/trail_runner_sl.jpg"
    },
    {
        "id": 9,
        "name": "Wave Rider 26",
        "brand": "Mizuno",
        "type": "Running",
        "price": 140.00,
        "sizes": [7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 12],
        "colors": ["Blue/White", "Black/Silver", "Grey/Red"],
        "features": ["Responsive", "Cushioned", "Breathable"],
        "description": "Neutral daily trainer featuring Wave technology for smooth transitions and responsive feel.",
        "rating": 4.5,
        "image_url": "https://example.com/wave_rider_26.jpg"
    },
    {
        "id": 10,
        "name": "CloudFlow",
        "brand": "On",
        "type": "Running",
        "price": 150.00,
        "sizes": [7, 8, 9, 10, 11, 12],
        "colors": ["Black/White", "All Black", "Blue/Orange"],
        "features": ["Lightweight", "Responsive", "Road Running"],
        "description": "Features CloudTec® cushioning for explosive takeoffs and soft landings with ultralight performance.",
        "rating": 4.6,
        "image_url": "https://example.com/cloudflow.jpg"
    },
]

def get_all_shoes():
    """Return the entire shoes database."""
    return SHOES_DATABASE

def search_shoes(query=None, filters=None):
    """
    Search for shoes based on a search query and additional filters.
    
    Args:
        query (str): Search terms to match against shoe names, brands, types, or features
        filters (dict): Dictionary of filter criteria (brand, type, price_range, etc.)
        
    Returns:
        list: Matching shoes based on criteria
    """
    results = SHOES_DATABASE.copy()
    
    # Apply text search if provided
    if query and isinstance(query, str):
        query = query.lower()
        filtered_results = []
        for shoe in results:
            if (query in shoe['name'].lower() or 
                query in shoe['brand'].lower() or 
                query in shoe['type'].lower() or 
                any(query in feature.lower() for feature in shoe['features'])):
                filtered_results.append(shoe)
        results = filtered_results
    
    # Apply additional filters if provided
    if filters and isinstance(filters, dict):
        # Filter by brand
        if 'brand' in filters:
            results = [shoe for shoe in results if shoe['brand'].lower() == filters['brand'].lower()]
        
        # Filter by type
        if 'type' in filters:
            results = [shoe for shoe in results if shoe['type'].lower() == filters['type'].lower()]
        
        # Filter by price range
        if 'price_min' in filters:
            results = [shoe for shoe in results if shoe['price'] >= filters['price_min']]
        if 'price_max' in filters:
            results = [shoe for shoe in results if shoe['price'] <= filters['price_max']]
            
        # Filter by size
        if 'size' in filters:
            results = [shoe for shoe in results if filters['size'] in shoe['sizes']]
            
        # Filter by color
        if 'color' in filters:
            color_query = filters['color'].lower()
            results = [shoe for shoe in results if any(color_query in color.lower() for color in shoe['colors'])]
    
    return results