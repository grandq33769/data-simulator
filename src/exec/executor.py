# Standard Library
from threading import Thread
from typing import List

# Third Party Library
from loguru import logger as log

from ..model.base import Base
from ..model.config import Config
from .simulator import SimulationHandler


def create_simulation(handler: SimulationHandler) -> None:
    for job, freq in zip(handler.model.jobs, handler.model.frequency):
        job().do(lambda: Thread(target=handler.execute).start())
        log.debug(
            f'[{handler.model.classname}] '
            f'frequency "{freq}" in '
            f'"{handler.model.scope}" scope initial success'
        )

    log.info(
        f'[{handler.model.classname}] '
        f'Scheduler initial success with {handler.model}'
    )


class ModuleHandler(Base):
    """A Handler for scheduling a list of data simulation in a module"""

    def __init__(self, module: Config):
        self.env = module.env
        self.simulation: List[SimulationHandler] = [
            SimulationHandler(data_model, self.env)
            for data_model in module.data
        ]
        log.info(f'[{module.classname}] Module initialization success.')
        log.debug(f'[{module.classname}] Details: {module}')

        for handler in self.simulation:
            create_simulation(handler)
