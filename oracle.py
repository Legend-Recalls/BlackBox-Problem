"""
oracle.py — shipping quote engine.

The rules the engine uses are hidden. Your job is to discover them by
calling quote() and observing what it returns.

Do not try to inspect the encoded blob below. If you do, you're not doing
the assignment — and your probe journal will make that obvious.
"""
import base64 as _b64
import marshal as _m

# --- Encoded implementation. Do not read. ---
_BLOB = (
    "4wAAAAAAAAAAAAAAAAIAAAAAAAAA8xIAAACXAGQAZAFsAFoAZAKEAFoBeQEpA+kAAAAATmMFAAAAAAAAAAAAAAAEAAAAAwAAAPO4AAAAlwB0AQAAAAAAAAAAagIAAAAAAAAAAAAAAAAAAAAAAAB8AGQBegUAAKsBAAAAAAAAZAF6CwAAfQV8BWQCegUAAHwBZAN6BQAAegAAAH0GfAJkBGsoAAByBnwGZAV6EgAAfQZuCnwCZAZrKAAAcgV8BmQHeg0AAH0GfAZkCGtEAAByBXwGZAl6EgAAfQZ8BGQKaygAAHIFfAZkC3oXAAB9BnQFAAAAAAAAAAB8BmQBqwIAAAAAAABTACkMTukCAAAAZwAAAAAAAERAZwAAAAAAAARA2gtlbGVjdHJvbmljc2fNzMzMzMz0P9oHZnJhZ2lsZWcAAAAAAMBiQGkgAwAAZ83MzMzMzOw/2glXRUxDT01FMTBnAAAAAAAAWUApA9oEbWF0aNoEY2VpbNoFcm91bmQpB9oJd2VpZ2h0X2tn2gtkaXN0YW5jZV9rbdoIY2F0ZWdvcnnaB2V4cHJlc3PaBmNvdXBvbtoBd9oFcHJpY2VzBwAAACAgICAgICD6CDxvcmFjbGU+2gVfaW1wbHITAAAAAgAAAHN7AAAAgADkCAyPCYkJkCmYYZEt0wggoDHRCCSAQeAMDZAEiUiQe6BT0Rco0QwogEXgBw+QPdIHINgIDZATiQyJBdgJEZBZ0gke2AgNkBWJDogF4AcMiHOCe9gIDZAUiQ2IBeAHDZAb0gcc2AgNkBWJDogF5AsQkBWYAYs/0AQa8wAAAAApAnIIAAAAchMAAACpAHIUAAAAchIAAAD6CDxtb2R1bGU+chYAAAABAAAAcw0AAADwAwEBAdsAC/MCEQEbchQAAAA="
)
_ns = {}
exec(_m.loads(_b64.b64decode(_BLOB)), _ns)
_impl = _ns["_impl"]
# --- End encoded implementation ---

_calls = 0


def quote(weight_kg, distance_km, category, express=False, coupon=""):
    """
    Return a shipping price.

    Parameters
    ----------
    weight_kg : float
        Item weight in kilograms. Reasonable range: 0.1 to 100.
    distance_km : float
        Shipping distance in kilometres. Reasonable range: 1 to 5000.
    category : str
        One of: "standard", "electronics", "fragile", "books", "clothing", "food".
        Other strings may raise or return junk — don't rely on them.
    express : bool, default False
        Express shipping flag.
    coupon : str, default ""
        Promo code (e.g. "WELCOME10"), or "" for no coupon.

    Returns
    -------
    float
        Price, rounded to 2 decimals.
    """
    global _calls
    _calls += 1
    return _impl(weight_kg, distance_km, category, express, coupon)


def queries_used():
    """Number of quote() calls made in this session."""
    return _calls


def reset_counter():
    """Reset the counter to 0. Useful if you're timing yourself."""
    global _calls
    _calls = 0
