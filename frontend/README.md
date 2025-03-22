# Hertz Car Rental Clone

A React-based make of car rental website UI. This project implements the core booking flow and vehicle browsing experience using React, Tailwind CSS, and ShadcN UI components.

## Features

- 🚗 Browse available vehicles
- 📅 Search with pickup/dropoff dates and locations
- 🔍 Detailed vehicle information pages
- 📱 Responsive design for all devices

## Prerequisites

Before you begin, ensure you have installed:
- Node.js (version 20 or higher)
- npm (comes with Node.js)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
```

2. Navigate to the project directory:
```bash
cd hertz-clone
```

3. Install dependencies:
```bash
npm install
```

4. Start the development server:
```bash
npm run dev
```

5. Open your browser and visit:
```
http://localhost:5000
```

## Project Structure

```
├── client/
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/         # Page components
│   │   ├── lib/           # Utilities and mock data
│   │   └── App.tsx        # Main application component
├── shared/
│   └── schema.ts          # Type definitions and schemas
└── theme.json             # Theme configuration
```

## Available Scripts

- `npm run dev` - Starts the development server
- `npm run build` - Builds the app for production
- `npm start` - Runs the built app in production mode

## Technologies Used

- React
- TypeScript
- Tailwind CSS
- ShadcN UI
- React Hook Form
- Zod (for validation)
- Wouter (for routing)
- date-fns (for date manipulation)

## Screenshots

### Homepage
![Homepage](https://www.hertz.com/content/dam/hertz/global/logos/hertz-logo.svg)
*The homepage features a search form and featured vehicles*

### Vehicle Selection
*Browse and select from available vehicles*

### Vehicle Details
*Detailed information about selected vehicles*
