

def draw_animal(animal: Animal):
    context = make_drawing_context()
    transform = animal.current_transform3d()
    project(context, transform)
    animal.draw(context)
    return context


def life_management(animal: Animal):
    if animal.hunger_level() > 0.5 and animal.is_awake():
        food_position = animal.look_for_food()
        a_star_navigation(animal, food_position)
        self.eat(get_food(food_position))
    else:
        animal.sleep(hours=1.)
    

def purchase_decision(animal: Animal, budget: float) -> bool:
    transportation_cost = animal.current_weight() * transport_price_kg
    expenses = animal.price() + transportation_cost
    return expenses < budget*0.5  # don't buy if not much money left



class VisualEntity(Protocol):
    def current_transform3d() -> HomogeneousMatrix:
        pass

    def draw(self, context):
        pass


class MovingEntity(Protocol):
    def go_to_position(self, position):
        pass


class ZooAsset:
    def current_weight(self) -> float:
        pass

    def price(self) -> float:
        pass


class BehavingAgent:
    def sleep(self, hours):
        pass

    def eat(self, food):
        pass

    def look_for_food(self):
        pass

    def hunger_level(self) -> float:
        pass

    def is_awake(self) -> bool:
        pass
