import logging.config
from src.processmailer.read_msg import ProcessMessages


logging.config.fileConfig(fname='../logger.conf', disable_existing_loggers=False)

log = logging.getLogger(__name__)


def main():
    p = ProcessMessages()
    log.debug("Start Processing msgs.")
    msgs = p.processMessages()
    log.debug("Processed msgs.")

if __name__ == "__main__":
    main()