import json

class BerryField:
    def __init__(self, field):
        self.field = field

    def grow(self):
        for row in range(len(self.field)):
            for col in range(len(self.field[row])):
                if self.field[row][col] < 10:
                    self.field[row][col] += 1

    def total_berries(self):
        return sum(sum(row) for row in self.field)

    def is_in_bounds(self, position):
        row, col = position
        return 0 <= row < len(self.field) and 0 <= col < len(self.field[0])

    def __getitem__(self, position):
        row, col = position
        return self.field[row][col]

    def __setitem__(self, position, value):
        row, col = position
        self.field[row][col] = value

    def __str__(self):
        return "\n".join(" ".join(f"{cell:>4}" for cell in row) for row in self.field)

class Bear:
    DIRECTIONS = {
        "N": (-1, 0),
        "S": (1, 0),
        "E": (0, 1),
        "W": (0, -1),
        "NE": (-1, 1),
        "NW": (-1, -1),
        "SE": (1, 1),
        "SW": (1, -1),
    }

    def __init__(self, row, col, direction):
        self.position = (row, col)
        self.direction = direction
        self.sleep_turns = 0

    def move(self, berry_field, tourists):
        if self.sleep_turns > 0:
            self.sleep_turns -= 1
            return

        dr, dc = Bear.DIRECTIONS[self.direction]
        new_row, new_col = self.position[0] + dr, self.position[1] + dc
        new_position = (new_row, new_col)

        if berry_field.is_in_bounds(new_position):
            berry_count = berry_field[new_position]
            berry_field[new_position] = 0
            self.position = new_position

            # Check interaction with tourists
            for tourist in tourists:
                if tourist.position == new_position:
                    self.sleep_turns = 3
                    tourist.leave_field()

    def is_sleeping(self):
        return self.sleep_turns > 0

    def __str__(self):
        status = f"Bear at {self.position} moving {self.direction}"
        if self.sleep_turns > 0:
            status += f" - Asleep for {self.sleep_turns} more turns"
        return status

class Tourist:
    def __init__(self, row, col):
        self.position = (row, col)
        self.turns_without_bear = 0
        self.in_field = True

    def update(self, berry_field, bears):
        if not self.in_field:
            return

        # Count bears in line of sight
        bears_in_sight = 0
        for bear in bears:
            br, bc = bear.position
            tr, tc = self.position

            if tr == br or tc == bc or abs(tr - br) == abs(tc - bc):
                bears_in_sight += 1

        if bears_in_sight >= 3:
            self.leave_field()
        elif bears_in_sight == 0:
            self.turns_without_bear += 1
            if self.turns_without_bear >= 3:
                self.leave_field()
        else:
            self.turns_without_bear = 0

    def leave_field(self):
        self.in_field = False

    def is_bored(self):
        return self.turns_without_bear >= 3

    def is_scared(self):
        return not self.in_field

    def __str__(self):
        status = f"Tourist at {self.position}, {self.turns_without_bear} turns without seeing a bear"
        if not self.in_field:
            status += " - Left the Field"
        return status

def main():
    file_name = input("Enter the json file name for the simulation => ").strip()
    print(file_name)

    with open(file_name, 'r') as f:
        data = json.load(f)

    # Initialize objects
    berry_field = BerryField(data["berry_field"])
    active_bears = [Bear(*bear_data) for bear_data in data["active_bears"]]
    active_tourists = [Tourist(*tourist_data) for tourist_data in data["active_tourists"]]

    print("\nStarting Configuration")
    print(f"Field has {berry_field.total_berries()} berries.")
    print(berry_field)
    print("\nActive Bears:")
    for bear in active_bears:
        print(bear)
    print("\nActive Tourists:")
    for tourist in active_tourists:
        print(tourist)

    # Run simulation for 5 turns
    for turn in range(1, 6):
        print(f"\nTurn: {turn}")

        # 1. Grow berries
        berry_field.grow()

        # 2. Move bears and update field
        for bear in active_bears[:]:
            if not bear.is_sleeping():
                bear.move(berry_field, active_tourists)
            if not berry_field.is_in_bounds(bear.position):
                print(f"{bear} - Left the Field")
                active_bears.remove(bear)

        # 3. Update tourists
        for tourist in active_tourists[:]:
            tourist.update(berry_field, active_bears)
            if tourist.is_bored() or not tourist.in_field:
                print(f"{tourist}")
                active_tourists.remove(tourist)

        # Report field state
        print(f"Field has {berry_field.total_berries()} berries.")
        print(berry_field)

        # Active bears and tourists
        print("\nActive Bears:")
        for bear in active_bears:
            print(bear)
        print("\nActive Tourists:")
        for tourist in active_tourists:
            print(tourist)

if __name__ == "__main__":
    file_name = input("Enter the json file name for the simulation => ").strip()
    print(file_name)
    
    with open(file_name, 'r') as f:
        data = json.load(f)
    
    # Initialize objects
    berry_field = BerryField(data["berry_field"])
    active_bears = [Bear(*bear_data) for bear_data in data["active_bears"]]
    active_tourists = [Tourist(*tourist_data) for tourist_data in data["active_tourists"]]
    
    print("\nStarting Configuration")
    print(f"Field has {berry_field.total_berries()} berries.")
    print(berry_field)
    print("\nActive Bears:")
    for bear in active_bears:
        print(bear)
    print("\nActive Tourists:")
    for tourist in active_tourists:
        print(tourist)

    # Run simulation for 5 turns
    for turn in range(1, 6):
        print(f"\nTurn: {turn}")
        
        # 1. Grow berries
        berry_field.grow()
        
        # 2. Move bears and update field
        for bear in active_bears[:]:  # Iterate over a copy to safely remove items
            if not bear.is_sleeping():
                bear.move(berry_field, active_tourists)
            if not berry_field.is_in_bounds(bear.position):
                print(f"{bear} - Left the Field")
                active_bears.remove(bear)
        
        # 3. Update tourists
        for tourist in active_tourists[:]:  # Iterate over a copy to safely remove items
            tourist.update(berry_field, active_bears)
            if tourist.is_bored() or tourist.is_scared():
                print(f"{tourist} - Left the Field")
                active_tourists.remove(tourist)

        # Report field state
        print(f"Field has {berry_field.total_berries()} berries.")
        print(berry_field)
        
        # Active bears and tourists
        print("\nActive Bears:")
        for bear in active_bears:
            print(bear)
        print("\nActive Tourists:")
        for tourist in active_tourists:
            print(tourist)
