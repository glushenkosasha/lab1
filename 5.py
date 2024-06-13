from Figure import Figure

square_values = []
perimeter_values = []

if __name__ == "__main__":
    for file in ['input01.txt', 'input02.txt', 'input03.txt']:
        reader = Figure(file)
        figures = reader.read()

        for figure in figures:
            try:
                print(figure, "Perimeter =", figure.perimeter(), "Square =", figure.square())
            except AttributeError:
                print(figure, "Square =", figure.square())

        for figure in figures:
            square = figure.square()
            square_values.append(square)

            try:
                perimeter = figure.perimeter()
                perimeter_values.append(perimeter)
            except (AttributeError, TypeError):
                pass

        max_square = max(square_values)
        max_square_index = square_values.index(max_square)
        max_square_figure = figures[max_square_index]
        print("Biggest square:", max_square_figure, "Area =", max_square)

        max_perimeter = max(perimeter_values)
        max_perimeter_index = perimeter_values.index(max_perimeter)
        max_perimeter_figure = figures[max_perimeter_index]
        print("Biggest perimeter:", max_perimeter_figure, "Perimeter (length) =", max_perimeter)