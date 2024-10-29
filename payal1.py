class Component:
    def __init__(self, name, functionality, quality_rating):
        self.name = name
        self.functionality = functionality
        self.quality_rating = quality_rating
        self.is_adapted = False

    def evaluate(self):
        """Evaluates component quality rating."""
        return self.quality_rating >= 7  # Assume quality rating of 7+ is acceptable

    def adapt(self):
        """Modifies component for better integration."""
        self.is_adapted = True
        print(f"{self.name} has been adapted for integration.")

class CBSEProcess:
    def __init__(self):
        self.components = []

    def find_component(self, name, functionality, quality_rating):
        """Finds and adds a component to the system."""
        component = Component(name, functionality, quality_rating)
        self.components.append(component)
        print(f"Component '{name}' found and added.")

    def evaluate_components(self):
        """Evaluates each component for quality and adapts if necessary."""
        for component in self.components:
            if not component.evaluate():
                print(f"{component.name} does not meet quality standards.")
                component.adapt()
            else:
                print(f"{component.name} meets quality standards.")

    def integrate_components(self):
        """Integrates all components into the system."""
        print("Integrating components:")
        for component in self.components:
            print(f" - {component.name} (Adapted: {component.is_adapted})")
        print("System integration complete!")

# CBSE Process Example
cbse_process = CBSEProcess()
# Step 1: Find Components
cbse_process.find_component("UserAuth", "Authentication service", 8)
cbse_process.find_component("Payment", "Payment processing", 6)
cbse_process.find_component("Inventory", "Inventory management", 9)

# Step 2: Evaluate Components
cbse_process.evaluate_components()

# Step 3: Integrate Components
cbse_process.integrate_components()