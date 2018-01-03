def print_models(unprinted_designs, completed_designs):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    :param unprinted_designs: designs to print
    :param completed_designs: printed designs
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3d print from the design
        print(f"Printing model: {current_design}")
        completed_designs.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

