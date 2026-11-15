# Busy Bodies

A workout tracker for working parents. Enter your height, weight, age, goal, schedule and equipment, and Busy Bodies builds a weekly workout plan, lets you log sets and reps, and tracks your progress.

**Live site:** https://tdesmond12.github.io/busy-bodies/

## Features
- **Profile** – BMI, calorie and protein estimates (Mifflin-St Jeor)
- **Plan** – weekly split based on goal, experience, days per week, time and equipment; swap any exercise
- **Log** – sets, reps and weight, with your last performance shown
- **Progress** – weekly goal tracking, streaks, volume, personal bests and history

## Data
Everything is saved in your browser (localStorage). Use **Profile → Your data** to download a backup or restore one.
Storage is isolated in one place in the code (`localBackend`) so Firestore can be added later.

## Coming next
- Meal tracking and recommendations
- User logins + Firestore
