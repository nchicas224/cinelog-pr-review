# PR Response Doc — CineLog Watchlist Feature

## AI Usage
<!-- Fill in at the end — how you used AI tools during this project -->

## Comment 1 — Default Visibility
**My position:**
**Reasoning:**
**Tradeoff acknowledged:**

## Comment 2 — Missing test
**What I did:**
I added the test function test_add_to_watchlist_nonexistent_raises() to the test_watchlist module. This test enforces the film_id validation from the database in lines 29-31 of watchlist_service.py::add_to_watchlist - before a new WatchlistEntry is created.
**How I verified:**
I ran the test with pytest tests/test_watchlist.py::test_add_to_watchlist_nonexistent_raises and verified that the test passed. I then ran the entire test suite with pytest /tests and verified that all existing tests across the suit passed.

## Comment 3 — Rename
**What I did:**
To rename save_to_watchlist to add_to_watchlist, I ran the keyboard command Shift + F12 on the save_to_watchlist phrase which showed me all of the instances of the phrase in the project directory. I manually changed 'save' to 'add'.
**How I verified:**
This fix was verified by running a global search (CTRL + SHIFT + F) and running a search for 'save_to_watchlist'. The search returned empty.

## Comment 4 — Deduplication
**What I did:**
To resolve this bug, I noticed that the WatchlistEntry model in models.py and watchlist_service.py::add_to_watchlist did not include checks for duplication at the database and application layer.

Using the existing duplication check from collection_service.py, I created AlreadyInWatchlistError and implemented the application layer check in add_to_watchlist to raise that error if an entry is found.

Additionally, I added a unique constraint to at the database layer by adding the (user_id, film_id) constraint to the WatchlistEntry model.
**How I verified:**
The bug fix was verified by creating a new test_watchlist module with test_add_to_watchlist_duplicate_raises.

This test function test the fixed add_to_watchlist function and WatchlistEntry model to assert that AlreadyinWatchlistError raises if an entry is found before trying to add the film to the user's watchlist.

## Comment 5 — Sort order
**My position:**
**Reasoning:**
**Engagement with reviewer's point:**

## Comment 6 — Rebase
**What conflicted:**
**How I resolved it:**
**How I verified no conflict remains:**

## PR Description
<!-- Written at the end — feature overview, design decisions, manual testing steps -->
