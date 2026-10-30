class DLColors:
    """
    A reusable color palette class providing:
    - Attribute access (DLColors.dlblue)
    - List of colors (DLColors.list)
    - Dictionary lookup (DLColors.dict)
    """

    # Define individual color hex codes
    dlblue = "#0096ff"  # Bright blue
    dlorange = "#FF9300"  # Orange
    dldarkred = "#C00000"  # Dark red
    dlmagenta = "#FF40FF"  # Magenta
    dlpurple = "#7030A0"  # Purple

    # Dictionary for name-based lookup
    dict = {
        "dlblue": dlblue,
        "dlorange": dlorange,
        "dldarkred": dldarkred,
        "dlmagenta": dlmagenta,
        "dlpurple": dlpurple,
    }

    # List for iteration / plotting
    list = [dlblue, dlorange, dldarkred, dlmagenta, dlpurple]

    @classmethod
    def get(cls, name: str) -> str:
        return cls.dict.get(name)
