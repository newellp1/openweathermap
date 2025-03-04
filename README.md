# openweathermap
A simple Python app that fetches weather from OpenWeatherMap API

## Recent Updats
- Implemented OpenWeatherMap API integration
  - Allows fetching current weather data and 5-day forecasts for any city or ZIP code.
- Added Support for searching by zip code
  - Users can now enter a ZIP code instead of a city name to get weather information.
- Improved 5-day forcaset display
  - Previously, the forecast showed multiple results for the same day. Now it correctly displays only one forecast per day.
- Secured API key using .en file
  - Prevented API key from being exposed by storing it in a `.env` file and ignoring it in Git.
- Update README.md with recent changes
  - Improved documentation to reflect new features and fixes.

## Issues
- **The comments in README.md would not show up in GitHub.**  
  - **Solution:** Ensured `git add README.md` was used before committing. Also checked if GitHub was updated with `git push origin main`.
  
- **.env file was accidentally committed to GitHub.**  
  - **Solution:** Used `git rm --cached .env`, updated `.gitignore`, and committed the changes.

- **Forecast data was showing hourly instead of daily.**  
  - **Solution:** Modified `get_forecast()` to filter results and display only one entry per day at 12:00 PM.

- **Git push was rejected due to remote changes.**  
  - **Solution:** Used `git pull origin main --rebase` before pushing again.

- **Spelling errors in README.md.**  
  - **Solution:** Fixed typos such as "forcaset" → "forecast" and "en" → "env".

## Future Enhancements
- [ ] Allow users to select Fahrenheit or Celsius for temperature display.
- [ ] Improve error handling for invalid city names or ZIP codes.
- [ ] Add a graphical user interface (GUI) instead of text-based input.
- [ ] Store previous searches to allow users to view weather history.
- [ ] Display weather alerts when available.  

## How to Run the Project
1. **Clone the repository:**
   ```sh
   git clone https://github.com/newellp1/openweathermap.git
   cd openweathermap
