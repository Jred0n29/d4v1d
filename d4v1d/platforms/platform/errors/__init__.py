"""
Module containing Exceptions that can be
raised by platforms.
"""

class PlatformError(Exception):
    """
    Generic exception for platforms
    """
    pass

class EmptyGroupError(PlatformError):
    """
    Thrown, when no bots have been assigned
    to a group, but the group is asked to
    perform a task
    """
    pass

class NoGroupsError(PlatformError):
    """
    Thrown, when no groups of bots have been
    created for a platform
    """
    pass

class UnknownUserError(PlatformError):
    """
    Thrown, when a user is not known to the
    platform
    """
    pass

class BadAPIResponseError(PlatformError):
    """
    Thrown, when the API responds in an
    unexpected way or doesn't respond at all
    """
    pass
