import marimo

__generated_with = "0.19.9"
app = marimo.App(width="full")


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt

    return np, plt


@app.cell
def _():
    # Number of points
    num_points = 90000
    return (num_points,)


@app.cell
def _(np, num_points):
    # Function to estimate pi using Monte Carlo method
    def monte_carlo_pi(num_points):
        # Generate random points within a square of side length 2 (centered at origin)
        x = np.random.uniform(-1, 1, num_points)
        y = np.random.uniform(-1, 1, num_points)
    
        # Calculate the distance from the origin
        distances = np.sqrt(x**2 + y**2)
    
        # Count points inside the circle
        inside_circle = distances <= 1
    
        # Estimate pi
        pi_estimate = 4 * np.mean(inside_circle)
    
        return pi_estimate, x, y, inside_circle



    # Estimate pi
    pi_estimate, x, y, inside_circle = monte_carlo_pi(num_points)

    print(f"Estimated Pi: {pi_estimate}")
    return inside_circle, x, y


@app.cell
def _(inside_circle, num_points, plt, x, y):
    # Plotting
    plt.figure(figsize=(8, 8))
    plt.scatter(x[inside_circle], y[inside_circle], c='blue', alpha=0.6, label='Inside Circle')
    plt.scatter(x[~inside_circle], y[~inside_circle], c='red', alpha=0.6, label='Outside Circle')
    plt.title(f"Monte Carlo Estimate of Pi (n={num_points})")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

    return


app._unparsable_cell(
    r"""
    # Function to estimate the square root of 2 using gradient descent
    def estimate_sqrt_2(learning_rate=0.1, num_iterations=10000):
        # Initial guess
        x = 2.0
    
        for _ in range(num_iterations):
            squared_error =     # Calculate the square of the estimated value
            estimated_square = x * x
        
            # Calculate the error between the estimated square and 2
            error = estimated_square - 2
        
            # Update the error for the next iteration
            squared_error = error * error

            # Gradient calculation
            gradient = (2 * x - 2) / (2 * x)
        
            # Update the guess using gradient descent
            x -= learning_rate * gradient
    
        return x

    # Estimate sqrt(2)
    sqrt_2_estimate = estimate_sqrt_2()

    print(f"Estimated Square Root of 2: {sqrt_2_estimate}")
    """,
    name="_"
)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
