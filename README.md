# Busy Bodies

A workout tracker for working parents. Enter your height, weight, age, goal, schedule and equipment, and Busy Bodies builds a weekly workout plan, lets you log sets and reps, and tracks your progress.

**Live site:** https://tdesmond12.github.io/busy-bodies/

## Features
- **Profile** – BMI, calorie and protein estimates (Mifflin-St Jeor)
- **Plan** – weekly split based on goal, experience, days per week, time and equipment; swap any exercise
- **Log** – sets, reps and weight, with your last performance shown
- **Progress** – weekly goal tracking, streaks, volume, personal bests and history
- **Coach** – an AI coach (Gemini via Firebase AI Logic) that sets up your profile by chatting, answers questions, and can swap exercises or adjust your plan with one tap

## Install on your phone
Open the live site in Safari (iPhone) or Chrome (Android) → **Share → Add to Home Screen** (iPhone) or **Install app** (Android). It opens full-screen with its own icon and loads even without a connection.

## Data
- **Signed in (Google):** saved in Firestore — `users/{uid}` (profile + plan), `users/{uid}/workouts/{id}`, `users/{uid}/coach/chat`. Security rules are in `firestore.rules`.
- **Signed out:** saved in the browser (localStorage). Anything saved there moves into your account the first time you sign in.
- **Profile → Your data** downloads or restores a backup.

## Firebase setup
- Authentication → Google provider on; `tdesmond12.github.io` in Authorized domains
- Firestore database with the rules in `firestore.rules`
- AI Logic → Gemini Developer API
- App Check → reCAPTCHA Enterprise; site key goes in `APPCHECK_SITE_KEY` in `index.html`

## Coming next
- Meal tracking and recommendations
