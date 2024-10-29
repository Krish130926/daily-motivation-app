# Daily-Motivation-App

## Project Description
The Daily Motivation App is a simple, user-friendly web application designed to provide a fresh motivational quote each day, helping users find inspiration and positivity regularly. By displaying new quotes, the app addresses the common need for daily encouragement, particularly helpful for people seeking a quick boost in motivation or a moment of reflection.

## Problem Solved
In a busy world, it can be hard to maintain motivation. This app offers a quick, accessible way to enjoy a daily dose of inspiration, making it easier to stay motivated and centered with minimal effort. Users can refresh the page or click a button to retrieve a new quote whenever they need it, ensuring a continuous stream of positive messages.

## Setup and Run Instructions
### 1. Clone the repository: 
git clone https://github.com/yourusername/daily-motivation-app.git
### 2. Navigate to the project directory
cd daily-motivation-app
### 3. Install the project dependencies:
npm install
### 4. Start the application:
npm start
### The application will run locally, accessible at http://localhost:3000 by default.

## API Information and Integration

This application uses the Quotable API to retrieve random motivational quotes. The API is called using the fetch method within the main App.js component, and each response returns a new quote, which is then displayed for users.

API Integration Details
Endpoint: https://api.quotable.io/random
Functionality: When the page loads, or the "Get Another Quote" button is clicked, the app fetches a new quote from the API and updates the display.

## AI Assistance Credits

Some of the planning and structure of the code were assisted by OpenAI's ChatGPT. Specifically, AI assistance was used in:

Code Snippets: Portions of the fetch logic in App.js and error handling recommendations.
AI-generated code and suggestions were adapted and customized to align with the project requirements and personal understanding, as required by the assignment.
