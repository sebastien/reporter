import time
import reporter

errors = reporter.FileReporter("errors.log", level=reporter.ERROR)
reporter.register(reporter.StdoutReporter())
reporter.register(errors)

reporter.error("Error {0}".format(time.time()))
