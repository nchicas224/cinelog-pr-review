# PR Response Doc — CineLog Watchlist Feature

## AI Usage
<!-- Fill in at the end — how you used AI tools during this project -->

## Comment 1 — Default Visibility
**My position:**
I agree with the dev-lead on this PR topic. The defaulted value of public=True for a user's watchlist may signal a loss of watchlist control and ownership to the user if the property field is not explicitly stated to the user.
**Reasoning:**
User's typically would prefer that their creations remain private unless the platform explicitly informs the user of its purpose. For this reason, I believe that the default value for the public property should be set to False and the option to change it to True should be directly shown to the user during the Watchlist creation.

I think we should also discuss whether the public property displays the watchlist to the entire userbase or to a user's community. Private watchlist may have the potential to be shared via a specialized link - which the user can then share to their friend.
**Tradeoff acknowledged:**
Private-by-default protects users from unintentionally exposing their interests, but it may reduce public discovery and sharing. If social discovery is a primary product goal, public-by-default with prominent disclosure could be justified. We should also clarify whether visibility applies to an entire watchlist or individual entries.

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
I agree with the maintainer on this comment. User's would benefit from seeing their most recently added films first rather than an alphabetical approach.
**Reasoning:**
Newest-first is a sensible default because it confirms recent additions and reflects current interest. However, it can bury older entries and is less useful when someone is looking for a known title. Ideally, the UI should support alternative sorting such as alphabetical, oldest-added, and newest-added, while using newest-first as the initial default.

Additionally, sorting only by date_added can be nondeterministic when two entries have the same timestamp. A stable ordering could add a secondary key: 
```
.order_by(
    WatchlistEntry.date_added.desc(),
    WatchlistEntry.id.asc(),
)
```
**Engagement with reviewer's point:**
I completely agree with your point here. User's are more likely to be interested in a film they've just recently added or heard of. Rather than having the user go through the roadblock of searching for what they've just added, we can just show their recents first. However, a strong tradeoff to this approach describes burying older entries under newer additions. This could be less useful to the user if they are limited to searching by date_added.

## Comment 6 — Rebase
**What conflicted:**
**How I resolved it:**
**How I verified no conflict remains:**

## PR Description
<!-- Written at the end — feature overview, design decisions, manual testing steps -->
