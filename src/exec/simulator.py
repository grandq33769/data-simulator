# Standard Library
import os
from typing import Any, Dict

# Third Party Library
from loguru import logger as log

from ..model.base import Base
from ..model.config import Environment
from ..model.data import DataModel


class SimulationHandler(Base):
    def __init__(self, data_model: DataModel, env: Environment):
        self.model = data_model
        self.env = env

    def execute(self):
        for time in range(self.model.quantity):
            simulated_data = self.simulate(time)
            log.info(
                f'[{self.model.classname}-Process-{os.getpid()}] '
                f'Simulated Data: {simulated_data}'
            )
            self.model.callback.kwargs.update(
                {'data': simulated_data, 'model': self.model, 'env': self.env}
            )
            self.model.callback.func(**self.model.callback.kwargs)
            log.info(
                f'[{self.model.classname}-Process-{os.getpid()}] '
                f'Callback "{self.model.callback.func.__name__}" Completed.'
            )

    def simulate(self, time: int) -> dict:
        result: Dict[str, Any] = dict()
        for attribute_name in self.model.get_attributes():
            try:
                attribute = getattr(self.model, attribute_name)
                attribute.kwargs.update({'time': time, 'env': self.env})
                result.update(
                    {
                        attribute_name: attribute.get(
                            **attribute.kwargs, **result
                        )
                    }
                )
            except Exception as e:
                log.exception(
                    f'{attribute_name} simulation failed with {e}',
                    diagnose=True,
                )
        return result
