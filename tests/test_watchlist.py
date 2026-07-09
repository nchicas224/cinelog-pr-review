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
    AlreadyInWatchlistError
)


    