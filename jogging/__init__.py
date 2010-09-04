import logging as py_logging
from django.conf import settings
from django.http import Http404
import sys

VERSION = (0, 2, 2)

LOGGING_LEVELS = {
    'DEBUG': py_logging.DEBUG,
    'INFO': py_logging.INFO,
    'WARNING': py_logging.WARNING,
    'ERROR': py_logging.ERROR,
    'CRITICAL': py_logging.CRITICAL
    }

class LoggingWrapper(object):

    def debug(self, msg, *args, **kwargs):
        caller = sys._getframe(1).f_globals['__name__']
        self.log('DEBUG', msg, caller, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        caller = sys._getframe(1).f_globals['__name__']
        self.log('INFO', msg, caller, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        caller = sys._getframe(1).f_globals['__name__']
        self.log('WARNING', msg, caller, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        caller = sys._getframe(1).f_globals['__name__']
        self.log('ERROR', msg, caller, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        caller = sys._getframe(1).f_globals['__name__']
        self.log('CRITICAL', msg, caller, *args, **kwargs)

    def exception(self, msg='', exception=None, request=None, *args, **kwargs):
        import traceback

        # Can 404 errors can be ignored?
        if getattr(settings, 'GLOBAL_LOG_IGNORE_404', False) and isinstance(exception, Http404):
            return

        if exception:
            source, exc, trbk = sys.exc_info()
            try:
                source = source.__name__
            except:
                source = str(source)
            tb = ''.join(traceback.format_exception(source, exc, trbk))
        else:
            source = 'UnspecifiedException'
            tb = ''

        if request:
            #location = '%s://%s%s' % (request.is_secure() and 'https' or 'http',
            #                          request.get_host(), request.path)
            absolute_uri = request.build_absolute_uri()
            try:
                request_repr = repr(request)
            except StandardError:
                request_repr = "Request repr() unavailable"
            message = """Absolute URI: %s
========================================
%s%s
========================================
Request:
%s""" % (absolute_uri, msg, tb, request_repr)
        else:
            source = 'Exception'
            message = "%s%s" % (msg, tb)

        self.log('ERROR', message, source, *args, **kwargs)


    def log(self, level, msg, source=None, *args, **kwargs):

        if not source:
            source = sys._getframe(1).f_globals['__name__']

        logger = self.get_logger(source)

        # Don't log unless the level is higher than the threshold for this source
        log_level = LOGGING_LEVELS[level]
        log_threshold = self.get_level(source)

        if log_level >= log_threshold:
            if sys.version_info >= (2, 5):
                kwargs.update({'source':source})
                logger.log(level=LOGGING_LEVELS[level], msg=msg, extra=kwargs, *args)
            else:
                logger.log(level=LOGGING_LEVELS[level], msg=msg, *args, **kwargs)

    def get_logger(self, source):
        chunks = str(source).split('.')
        modules = ['default'] + ['.'.join(chunks[0:n]) for n in range(1, len(chunks) + 1)]
        modules.reverse()

        if hasattr(settings, 'LOGGING'):
            for source in modules:
                if source in settings.LOGGING:
                    return py_logging.getLogger(source)

        return py_logging.getLogger('') # root logger

    def get_level(self, source):
        """
        Returns the log level for a given source

        if settings.LOGGING exists, returns the matching level
        if settings.GLOBAL_LOG_LEVEL exists, returns that
        if settings.DEBUG set, return DEBUG
        otherwise, returns WARNING
        """

        chunks = str(source).split('.')
        modules = ['default'] + ['.'.join(chunks[0:n]) for n in range(1, len(chunks) + 1)]
        modules.reverse()

        if hasattr(settings, 'LOGGING'):
            for source in modules:
                if source in settings.LOGGING:
                    if 'level' in settings.LOGGING[source]:
                        return settings.LOGGING[source]['level']
                    elif 'handlers' in settings.LOGGING[source]:
                        # There could be several handlers with different levels
                        return py_logger.DEBUG

        if hasattr(settings, 'GLOBAL_LOG_LEVEL'):
            return settings.GLOBAL_LOG_LEVEL

        if hasattr(settings, 'DEBUG') and settings.DEBUG:
            return py_logger.DEBUG
        else:
            return py_logger.WARNING

logging = LoggingWrapper()
