# Installation Steps

## Installing Node.js
1. Download the latest version of Node.js from the [official website](https://nodejs.org/).
2. Install Node.js using the installer for your operating system.
3. Verify the installation by running:
   ```bash
   node -v
   npm -v
   ```

## Installing Required Dependencies
1. Navigate to the frontend project directory.
2. Install the required dependencies:
   ```bash
   npm install
   ```

# Running the Project

## Starting the Backend Server
1. If you haven't done so, be sure to download the [backend files](https://github.com/dbrkani/430FinalFront)  and follow installation steps for this project.
2. Navigate to the backend directory.
3. Run the Flask server:
   ```bash
   python app.py
   ```
4. The backend will be available at `http://127.0.0.1:8080`.

## Starting the Frontend Server
1. Navigate to the frontend directory.
2. Replace Fetch Command URLs with your backend host URL.
3. Start the development server:
   ```bash
   npm start
   ```
4. The frontend will be available at `http://127.0.0.1:3000`.

# Frontend Code Explanation

The frontend of this project is built using **Next.js**, a React-based framework, to provide server-side rendering and optimized performance. Below is a breakdown of the key components and their responsibilities:

## Components

### 1. `Header.js`
The `Header.js` component serves as the navigation bar for the application. It includes the following functionalities:
- A **search bar** that allows users to search for products. 
    - Upon submitting a search query, it redirects to the `/products` page and opens a modal displaying the searched product with an "Add to Cart" button.
- A **login button** that triggers the login modal (`Login` component) and fetches the user's cart from the database upon successful login.
- Navigation links to access key sections of the website.

### 2. `ProductList.js`
- This component is rendered on the `/products` route and displays a grid of products.
- It fetches data from our database to populate product information dynamically.
- Implements pagination to limit the display to nine products per page for better performance and usability.

### 3. `ProductGrid.js`
- Used as the **homepage**, this component highlights featured or popular products.
- Like `ProductList`, it fetches product data from the Fake Store API.
- It focuses on providing a visually engaging layout for user engagement.

### 4. `Cart.js`
- Displays the user's shopping cart with the following functionalities:
  - Adjusting product quantities.
  - Removing items from the cart.
  - Initiating the checkout process.
- It uses context from `CartContext.js` for cart state management.

### 5. `Login.js`
- Handles user authentication through a modal.
- Includes fields for entering user credentials and a submit button to log in.
- Upon successful login, it fetches the user's cart data and updates the application state.

## Context and State Management

### `CartContext.js`
The `CartContext` provides global state for managing the shopping cart. It includes:
- Functions to **add**, **update**, and **remove items** from the cart.
- Functions to **save** the cart to the database and **fetch** it upon login.
- A checkout function to initiate the purchase process.

## API Integrations
- **Backend Routes**: 
    - `/checkout`: Completes the purchase.
    - Other cart and user-related operations that synchronize the frontend with the database.

## Routing
The app uses the following key routes:
- `/`: Displays the `ProductGrid` as the homepage.
- `/products`: Renders the `ProductList` to browse all available products.
- `/admin`: Accesses the admin panel for product management (for authorized users).

## Technologies
- **Next.js**: For efficient routing, SSR (Server-Side Rendering), and improved page performance.
- **React Context API**: For state management.
- **CSS Modules/Tailwind**: (if applicable) For styling components.
- **Axios/Fetch API**: For API requests.

## Key Features
- Fully responsive design for mobile and desktop.
- Dynamic product rendering with pagination.
- Seamless cart synchronization with the backend.
