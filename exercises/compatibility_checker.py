"""
Build Compatibility Checker — fill in the four functions below.

Same checks Lesson 1 describes doing by hand before buying anything: socket
match, RAM generation, and PSU headroom for transient spikes. Writing them as
code means you can actually re-run the check the next time you're picking
parts, instead of re-deriving the reasoning from scratch.

Run the tests as you go:  pytest exercises/test_compatibility_checker.py -v
All four start failing. Implement one function, re-run, watch it turn green,
move to the next.
"""


def sockets_match(cpu_socket, motherboard_socket):
    """Do the CPU and motherboard sockets match?

    Case-insensitive, since listings write socket names inconsistently
    ("AM5" vs "am5", "LGA1700" vs "lga 1700" minus the space).

    >>> sockets_match("AM5", "am5")
    True
    >>> sockets_match("LGA1700", "AM5")
    False
    """
    # TODO: compare cpu_socket and motherboard_socket case-insensitively
    raise NotImplementedError


def ram_generation_compatible(ram_generation, supported_generations):
    """Is ram_generation (e.g. "DDR5") one of the motherboard's
    supported_generations (a list, e.g. ["DDR5"])?

    Most boards support exactly one generation, but the function takes a
    list to stay correct for the rare board that lists more than one.

    >>> ram_generation_compatible("DDR5", ["DDR5"])
    True
    >>> ram_generation_compatible("DDR4", ["DDR5"])
    False
    """
    # TODO: return whether ram_generation is in supported_generations
    raise NotImplementedError


def recommended_psu_watts(components_load_watts, headroom_pct=20):
    """The minimum PSU wattage to buy, given the components' combined load
    and a headroom percentage for transient spikes (Lesson 1's GPU-spike
    point, made concrete).

    >>> recommended_psu_watts(400, headroom_pct=20)
    480.0
    >>> recommended_psu_watts(400, headroom_pct=50)
    600.0
    """
    # TODO: return components_load_watts * (1 + headroom_pct / 100)
    raise NotImplementedError


def has_sufficient_psu(psu_wattage, components_load_watts, headroom_pct=20):
    """Does psu_wattage meet or exceed the recommended headroom for this
    build's load?

    Reuse recommended_psu_watts() rather than recomputing the percentage
    math separately.

    >>> has_sufficient_psu(550, 400, headroom_pct=20)
    True
    >>> has_sufficient_psu(420, 400, headroom_pct=20)
    False
    """
    # TODO: return psu_wattage >= recommended_psu_watts(components_load_watts, headroom_pct)
    raise NotImplementedError
