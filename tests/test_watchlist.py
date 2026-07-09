"""
tests/test_watchlist.py - CineLog

Tests for the watchlist service.
"""

import pytest
from app import db
from models import User, Film, WatchlistEntry
from services.watchlist_service import (
    add_to_watchlist,
    get_watchlist,
    AlreadyInWatchlistError,
    FilmNotFoundError
)

# ── Deduplication ────────────────────────────────────────────────────────────

def test_add_to_watchlist_duplicate_raises(app, sample_user, sample_film):
    """
    Adding the same film twice to a user's watchlist should raise AlreadyInWatchlistError,
    not silently create a duplicate entry.
    """
    with app.app_context():
        add_to_watchlist(
            user_id=sample_user,
            film_id=sample_film,
        )

        with pytest.raises(AlreadyInWatchlistError):
            add_to_watchlist(
            user_id=sample_user,
            film_id=sample_film,
        )

        count = WatchlistEntry.query.filter_by(
            user_id=sample_user, film_id=sample_film
        ).count()
        assert count == 1

def test_add_to_watchlist_nonexistent_film_raises(app, sample_user, sample_film):
    """
    Adding a film_id that doesn't exist in the database should raise
    FilmNotFoundError, not a database integrity error.
    """
    with app.app_context():
        fake_film_id = "00000000-0000-0000-0000-000000000000"

        with pytest.raises(FilmNotFoundError):
            add_to_watchlist(
                user_id=sample_user,
                film_id=fake_film_id,
            )
        