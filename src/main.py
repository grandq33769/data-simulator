# Standard Library
from time import sleep

from .configs import CONFIGS
from .exec.executor import ModuleHandler
from .model.scheduler import SCHEDULE


def main():
    for module in CONFIGS:
        ModuleHandler(module)

    while 1:
        # use sleep to create bebounce, lowering CPU usage
        sleep(1)
        # due to global schedule object sharing,
        # start schedule would start all worker
        SCHEDULE.run_pending()


if __name__ == '__main__':
    main()
