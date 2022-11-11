from typing import Protocol


class Animal(Protocol):
    def current_weight(self) -> float:
        pass

    def price(self) -> float:
        pass

    def sleep(self, hours):
        pass

    def eat(self, food):
        pass

    def draw(self, context):
        pass

    def go_to_position(self, position):
        pass

    def look_for_food(self):
        pass

    def hunger_level(self) -> float:
        pass

    def is_asleep(self) -> bool:
        pass

    def is_awake(self) -> bool:
        pass

    def current_position() -> Tuple[float, float, float]:
        pass

    def current_orientation() -> RotationMatrix:
        pass
    
    def current_transform3d() -> HomogeneousMatrix:
        pass


