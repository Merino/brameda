class LoggingMiddleware(object):

    def process_exception(self, request, exception):
        from jogging import logging
        # Be very careful not to generate an exception when processing an exception
        try:
            logging.exception(exception=exception, request=request)
        except StandardError, e:
            import sys
            print >>sys.stdout, "ERROR: Exception occured while logging an exception: %s", repr(e)
