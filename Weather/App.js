// Replace with your OpenWeatherMap API key
const apiKey = 'YOUR_API_KEY';

// Function to fetch weather data and update the UI
function getWeather() {
    const city = document.getElementById('city').value.trim();

    if (!city) {
        showError('Please enter a city name');
        return;
    }

    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('City not found');
            }
            return response.json();
        })
        .then(data => {
            displayWeather(data);
        })
        .catch(error => {
            showError(error.message);
        });
}

// Function to display weather data on the UI
function displayWeather(data) {
    const weatherInfo = document.getElementById('weather-info');
    const errorMessage = document.getElementById('error-message');
    errorMessage.textContent = '';  // Clear any previous error message

    const temperature = data.main.temp;
    const description = data.weather[0].description;
    const humidity = data.main.humidity;
    const windSpeed = data.wind.speed;

    weatherInfo.innerHTML = `
        <h2>Weather in ${data.name}, ${data.sys.country}</h2>
        <p><strong>Temperature:</strong> ${temperature}°C</p>
        <p><strong>Description:</strong> ${description}</p>
        <p><strong>Humidity:</strong> ${humidity}%</p>
        <p><strong>Wind Speed:</strong> ${windSpeed} m/s</p>
    `;
}

// Function to display error messages
function showError(message) {
    const weatherInfo = document.getElementById('weather-info');
    const errorMessage = document.getElementById('error-message');
    weatherInfo.innerHTML = '';  // Clear any previous weather info
    errorMessage.textContent = message;
}
