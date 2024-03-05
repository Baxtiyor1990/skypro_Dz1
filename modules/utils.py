
class LoggingMixin:
    def __repr__(self):
        attrs = ', '.join([f"{attr}={getattr(self, attr)}" for attr in self.__dict__])
        return f"{self.__class__.__name__}({attrs})"
