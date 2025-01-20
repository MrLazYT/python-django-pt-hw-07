FAVORITES_KEY = "my_app/favorites"

def get_favorites(session):
    favorites = session.get(FAVORITES_KEY, [])

    return favorites

def add_to_favorites(session, movie_id):
    favorites = session.get(FAVORITES_KEY, [])

    if movie_id not in favorites:
        favorites.append(movie_id)

    session[FAVORITES_KEY] = favorites

def remove_from_favorites(session, movie_id):
    favorites = session.get(FAVORITES_KEY, [])

    if movie_id in favorites:
        favorites.remove(movie_id)

    session[FAVORITES_KEY] = favorites

def clear_favorites(session):
    session[FAVORITES_KEY] = []