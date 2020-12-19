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
        for _ in range(self.model.quantity):
            simulated_data = self.simulate()
            self.model.callback(simulated_data, self.model, self.env)

    def simulate(self) -> dict:
        result = dict()
        for attribute_name in self.model.get_attributes():
            try:
                attribute = getattr(self.model, attribute_name)
                result.update(
                    {attribute_name: attribute.get(**attribute.kwargs)}
                )
            except Exception as e:
                log.exception(
                    f'{attribute_name} simulation failed with {e}',
                    diagnose=True,
                )
        return result
