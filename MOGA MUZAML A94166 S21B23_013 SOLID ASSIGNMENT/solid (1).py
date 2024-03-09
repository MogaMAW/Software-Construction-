class Employee(ABC):
    def __init__(self, identifier):
        self.identifier = identifier

    # Define abstract methods for subclasses to implement.
    @abstractmethod
    def compute_reward(self):
        """Determine the bonus amount for a staff member."""
        pass

    @abstractmethod
    def execute_tasks(self):
        """Carry out specific tasks based on the staff role."""
        pass

class Manager(Employee):
    # Calculate bonus for a Manager.
    def compute_reward(self):
        return 1000

    # Manager's specific task.
    def execute_tasks(self):
        print(f"{self.identifier} is managing the team.")

class Developer(Employee):
    # Determine bonus for an Developer.
    def compute_reward(self):
        return 500

    # Developer's specific task.
    def execute_tasks(self):
        print(f"{self.identifier} is conducting a code review.")

class ReportGenerator:
    # Create a role-based performance report.
    def create_report(self, staff):
        print(f"{staff.__class__.__name__} Report: {staff.identifier}")

class BonusCalculator:
    # Use staff member's method to calculate the bonus.
    def compute_bonus(self, staff):
        return staff.compute_reward()

if __name__ == "__main__":
    team_members = [Manager("Alice"), Developer("Bob")]

    performance_report = ReportGenerator()
    reward_calculator = BonusCalculator()

    for member in team_members:
        member.execute_tasks()
        performance_report.create_report(member)
        reward = reward_calculator.compute_bonus(member)
        print(f"{member.__class__.__name__} Bonus: ${reward}")