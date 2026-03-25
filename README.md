# ThinkForge — Adaptive Learning Platform

> Forge your knowledge with adaptive AI-powered learning.

ThinkForge is a modern adaptive learning platform that connects students with expert mentors through personalized, AI-driven courses. Built with asdfghkjlkjhgfdsadfghjkl;kjhgfdsasdfghjk.

---

##  Features

### For Students
- **Personalized Dashboard** - Track enrolled courses, progress and learning streaks
- **First-Time Login Setup**
  - Users select subjects of interest from a dropdown menu
  - Users take an assessment test to determine their skill level
  - The platform personalizes learning paths based on results
- **Streak System** - Duolingo-style daily learning motivation
- **Course View** - Videos, notes and MCQ quizzes per module
- **AI Assistant**
  - Helps users navigate the platform easily
  - Answers doubts and provides explanations in real-time
  - Uses Mem-Brain API search endpoint for intelligent responses
- **Progress Analytics** - Visual graphs showing your learning journey

### For Mentors
- **Course Creation** - Build courses with modules (video, notes and quizzes)
- **Leaderboard** - Ranking system with promotion/demotion zones

- **Student Analytics** - Monitor enrolled students and their progress
- **Leaderboard** - Ranking system with promotion/demotion zones


### Platform
- **Authentication** - Email/password signup & login with role selection (Student or Mentor)
- **Password Recovery** - Forgot password and reset password flows
- **Responsive Design** - Works on desktop, tablet, and mobile
- **Clean UI** - Professional blue & white theme with smooth animations

---

## 🛠 Tech Stack

| Layer       | Technology                        |
|-------------|-----------------------------------|
| Frontend    | HTML, CSS, JavaScript       |
| Styling     |            |
| Animations  |                      |
| Backend     | Node.js (Express)          |
| Auth        |                 |
| Database    |     |
| Charts      |                           |

---

## Getting Started

### Prerequisites
- Node.js 18+ 
 

### Installation

```bash
# Clone the repository
git clone <wsas ur url bro>
cd thinkforge

# Install dependencies
npm install

# Start the development server
npm run dev
```

The app will be available at `http://localhost:3000`.

### Environment

The project uses **something** for backend services (database, auth, serverless functions). `.env` file is needed — Cloud credentials are managed with membrain-api not sure about this part.

---

## Project Structure

```
project-root/
├── frontend/
│   ├── index.html        # Landing page
│   ├── login.html        # Login page
│   ├── signup.html       # Signup page
│   ├── dashboard.html    # User dashboard
│   ├── styles.css        # Global styles
│   └── script.js         # Frontend logic
|
├── backend/
│   ├── server.js         # Main server entry point
│   ├── routes/           # API route definitions
│   └── controllers/      # Business logic
|
├── .env                  # Environment variables (API keys, configs)
|
└── README.md             
```

---

## Design System

This platform uses a semantic design token system defined in `project-root/index.html`:

- **Primary**: Blue (`hsl(217, 91%, 50%)`)
- **Accent**: Cyan (`hsl(199, 89%, 48%)`)
- **Background**: Near-white (`hsl(210, 33%, 99%)`)
- **Gradients**: Primary gradient, hero background gradient
- **Shadows**: Card shadow, elevated shadow
- **Animations**: Fade-in, slide-in, float, pulse-glow

---

## License

This project is private. All rights reserved.

