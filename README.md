## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.


## Rationale
2.1 What refactoring signs (code smells) suggest this refactoring?
- Feature Envy: Rental needs price_code more, so it makes sense to manage it within Rental instead of relying on Movie.

2.2 what design principle suggests this refactoring? Why?

- Single Responsibility Principle (SRP): Each class should have a clear focus. Movie should handle movie details, while Rental should manage pricing. This separation reduces coupling and improves code clarity.

5.2 Describe where you implement this method and the reasons for your choice.  

I implemented ```price_code_for_movie()``` method in Movie class.
- High Cohesion: The Movie class is directly connected to price codes because it has the details needed to decide the price based on its year and genres. It makes sense to put the price code method in this class.
- Single Responsibility Principle: The Movie class is responsible for sharing information about the movie, including how it should be priced. Keeping the method here helps keep its job clear.
- Information Expert: The Movie class is an expert on its own details that affect pricing. It knows its release year and genre, which helps it accurately decide the right price code.
