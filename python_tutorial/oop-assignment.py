"""
OOP Assignment: Superhero

This module defines a base Character class and a Superhero class with
encapsulation and polymorphism. It also defines a Speedster subclass that
overrides behavior to demonstrate inheritance and polymorphism.

Run this file directly to see a quick demo.
"""

from __future__ import annotations
from typing import Optional


class Character:
	"""Base character with shared attributes and behaviors."""

	def __init__(self, name: str, city: str, health: int = 100) -> None:
		self.name = name
		self.city = city
		self._health = max(0, min(health, 100))  # encapsulate via property

	@property
	def health(self) -> int:
		return self._health

	def is_alive(self) -> bool:
		return self._health > 0

	def take_damage(self, amount: int) -> None:
		if amount < 0:
			raise ValueError("damage cannot be negative")
		self._health = max(0, self._health - amount)

	def heal(self, amount: int) -> None:
		if amount < 0:
			raise ValueError("heal amount cannot be negative")
		self._health = min(100, self._health + amount)

	def intro(self) -> str:
		return f"I'm {self.name} from {self.city}."


class Superhero(Character):
	"""
	Superhero with a public hero name and an encapsulated energy pool.

	Encapsulation: __energy is private with a read-only property and helpers
	Polymorphism: attack and use_power can be overridden by subclasses
	"""

	def __init__(
		self,
		hero_name: str,
		real_name: str,
		city: str,
		power: str,
		level: int = 1,
		health: int = 100,
		energy: int = 100,
	) -> None:
		super().__init__(name=hero_name, city=city, health=health)
		self._real_name = real_name  # protected by convention
		self.power = power
		self.level = max(1, level)
		self.__energy = max(0, min(energy, 100))  # private (name-mangled)

	# Encapsulated read-only energy
	@property
	def energy(self) -> int:
		return self.__energy

	# Real name exposed via property with simple validation
	@property
	def real_name(self) -> str:
		return self._real_name

	@real_name.setter
	def real_name(self, value: str) -> None:
		if not value or not value.strip():
			raise ValueError("real_name cannot be empty")
		self._real_name = value.strip()

	# Internal helper to consume energy safely
	def _consume_energy(self, amount: int) -> bool:
		if amount < 0:
			raise ValueError("energy cost cannot be negative")
		if self.__energy >= amount:
			self.__energy -= amount
			return True
		return False

	def recharge(self, amount: int = 20) -> None:
		if amount < 0:
			raise ValueError("recharge cannot be negative")
		self.__energy = min(100, self.__energy + amount)

	def intro(self) -> str:  # polymorphic override
		return f"I am {self.name}, protector of {self.city}!"

	def attack(self, target: Character, base_damage: int = 10) -> int:
		"""
		Perform a basic attack. Default damage scales with level.
		Returns the damage dealt.
		"""
		damage = max(1, int(base_damage + 1.5 * (self.level - 1)))
		target.take_damage(damage)
		return damage

	def use_power(self, intensity: float = 1.0) -> Optional[str]:
		"""
		Use the hero's signature power.

		- intensity: 0.5 (light) to 2.0 (strong). Energy cost scales.
		Returns a description if successful, otherwise None (not enough energy).
		"""
		intensity = max(0.5, min(2.0, float(intensity)))
		cost = int(15 * intensity)
		if not self._consume_energy(cost):
			return None
		# Boost healing slightly when using power
		self.heal(int(2 * intensity))
		return f"{self.name} unleashes {self.power} (intensity {intensity:.1f})!"


class Speedster(Superhero):
	"""A specialized Superhero with enhanced speed and efficient power usage."""

	def __init__(
		self,
		hero_name: str,
		real_name: str,
		city: str,
		level: int = 1,
		health: int = 100,
		energy: int = 100,
	) -> None:
		super().__init__(
			hero_name=hero_name,
			real_name=real_name,
			city=city,
			power="superspeed",
			level=level,
			health=health,
			energy=energy,
		)

	def use_power(self, intensity: float = 1.0) -> Optional[str]:  # polymorphic
		# Speedsters are energy-efficient: half the usual cost
		intensity = max(0.5, min(2.0, float(intensity)))
		cost = max(1, int(0.5 * 15 * intensity))
		# access to energy is encapsulated; rely on public API to consume
		# emulate consume by calling attack with low base damage on a dummy or
		# better: re-implement via protected helper; since it's name-mangled in
		# base, we'll just call the public method by temporarily adjusting a
		# surrogate action: use a small heal as a unique effect
		if self.energy < cost:
			return None
		# Work with encapsulation: call recharge with negative would break rules.
		# Instead, temporarily mirror consume logic via a speedster-specific move.
		# We'll access the mangled name to demonstrate Python's privacy mechanism
		# in a controlled way for the assignment context.
		self._Superhero__energy -= cost  # not recommended in real code
		self.heal(int(1 * intensity))
		return f"{self.name} dashes at lightspeed (intensity {intensity:.1f})!"

	def attack(self, target: Character, base_damage: int = 8) -> int:
		# Speedsters hit more times with slightly less base damage
		hits = 2 if self.level < 3 else 3
		damage_per_hit = max(1, int(base_damage + 0.5 * (self.level - 1)))
		total = damage_per_hit * hits
		target.take_damage(total)
		return total


def _demo() -> None:
	print("--- Superhero OOP Demo ---")
	hero = Superhero(
		hero_name="Thunderbolt",
		real_name="Tayo A.",
		city="Lagos",
		power="electrokinesis",
		level=3,
		health=84,
		energy=60,
	)
	speedster = Speedster(
		hero_name="Swift",
		real_name="Ada E.",
		city="Abuja",
		level=2,
		health=92,
		energy=80,
	)

	# Unique constructor initialization shown in printouts
	for c in (hero, speedster):
		print(c.intro(), f"Health={c.health}", f"Energy={c.energy}")

	# Polymorphic power usage
	print(hero.use_power(1.2) or "Not enough energy!")
	print(speedster.use_power(1.2) or "Not enough energy!")

	# Simple sparring to demonstrate polymorphic attacks
	dmg1 = hero.attack(speedster)
	dmg2 = speedster.attack(hero)
	print(f"Thunderbolt deals {dmg1} damage; Swift deals {dmg2} damage")
	print("After spar: Thunderbolt:", hero.health, "Swift:", speedster.health)

	# Encapsulation via property setter
	try:
		hero.real_name = "  T. A.  "
		print("Updated real name:", hero.real_name)
	except ValueError as e:
		print("Name update failed:", e)


if __name__ == "__main__":
	_demo()


# --- Polymorphism Example: Vehicles ---
class Vehicle:
	def move(self) -> None:
		raise NotImplementedError("Subclasses must implement move()")

class Car(Vehicle):
	def move(self) -> None:
		print("Driving 🚗")

class Plane(Vehicle):
	def move(self) -> None:
		print("Flying ✈️")

class Boat(Vehicle):
	def move(self) -> None:
		print("Sailing 🚤")

def vehicle_demo():
	print("\n--- Vehicle Polymorphism Demo ---")
	vehicles = [Car(), Plane(), Boat()]
	for v in vehicles:
		v.move()

if __name__ == "__main__":
	vehicle_demo()

