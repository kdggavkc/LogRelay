import logging


class LogRelay:
    """
    Object representing a logger that allows assignment of additional functions to a logger level call, without
    having to make dedicated handlers. Purpose is to be able to tie additional calls to a logger level.
    """

    def __init__(self, name, relay_all=False):
        self.name = name
        self.logger = logging.getLogger(name)
        self.relay_all = relay_all

        self.setRoutes(levels=(10, 20, 30, 40, 50))  # assign logging levels to object

    def setLevel(self, level):
        self.logger.setLevel(level)

    def _methodFactory(self, level, callables=()):
        """
        Creates final function to first call the logger level provided, and then any supplied callables. Essentially,
        for each level-call, run these additional calls. Attached to same log-level method names (DEBUG, INFO, etc...)
        """

        def func(msg, relay=False, *args, **kwargs):
            logger_level_call = getattr(self.logger, level.lower())
            logger_level_call(msg)

            if self.relay_all or relay:
                for c in callables:
                    c(msg, *args, **kwargs)

        return func

    def setRoutes(self, levels=(30, 40, 50), callables=()):
        """
        Assigns provided callables to an instance method of the same logger level name provided.
        """
        for level_num in levels:
            level_name = logging.getLevelName(level_num)
            route = self._methodFactory(level_name, callables)
            setattr(self, level_name, route)

    def __repr__(self):
        return f"Interchange(name={self.name})"
