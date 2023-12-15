# Barister-Meal Finder

Barister-Meal Finder is a Python application built using SQLAlchemy, offering efficient management of restaurant data. This project includes three main classes: `Restaurant`, `Customer`, and `Review`. Each class plays a crucial role in maintaining a comprehensive database schema.

## Key Features

### 1. **Restaurant Class:**
   - **Attributes:**
     - `id`: Unique identifier for each restaurant.
     - `name`: Name of the restaurant.
     - `price`: Price level indicator.
   - **Functionality:**
     - Manages restaurant information.
     - Tracks associated reviews.
     - Handles relationships with customers.

### 2. **Customer Class:**
   - **Attributes:**
     - `id`: Unique identifier for each customer.
     - `first_name` and `last_name`: Customer's name.
   - **Functionality:**
     - Captures customer details.
     - Manages customer reviews and associated restaurants.
     - Determines the customer's favorite restaurant.

### 3. **Review Class:**
   - **Attributes:**
     - `id`: Unique identifier for each review.
     - `rating`: Numeric rating provided by the customer.
   - **Functionality:**
     - Represents a customer's review for a specific restaurant.

### 4. **Database Schema:**
   - Defines relationships between restaurants, customers, and reviews.
   - Enables seamless data management and retrieval.

## Getting Started

1. **Installation:**
   - Clone the repository:
     ```bash
     git clone https://github.com/your-username/your-repo.git
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Usage:**
   - Execute `python models.py` to initialize the database and classes.
   - Explore `models.py` for sample operations, including adding reviews and identifying the fanciest restaurant.

3. **Customization:**
   - Adapt the classes and methods to suit specific project requirements.

## Dependencies

- SQLAlchemy

## Contributors

- [Your Name]
- [Other Contributors, if any]

## License

This project is licensed under the [MIT License](LICENSE.md) - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- I love to acknowledge Moringa School Limited's Technical Mentor: Senior Engineer Steve Otieno for the proficient teaching and guidance on key Python concepts. He has been a great revolutionarist who has impacted all prerequisite Python concepts in a totally efficient and technical fahion. Being my first sql Alchemy project, I am super grateful.

Feel free to explore and enhance the capabilities of Barister-Meal Finder for your unique project needs!
