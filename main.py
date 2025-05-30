from mcp.server.fastmcp import FastMCP
import requests
from dotenv import load_dotenv
import os

load_dotenv()
WEATHER_API_KEY=os.getenv("WEATHER_API_KEY")

# Create an MCP server
mcp = FastMCP("SimpleServer", "1.0.0")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two integers together.
    
    This tool performs simple addition of two numbers and returns their sum.
    It serves as a basic demonstration of MCP tool functionality.
    
    Args:
        a (int): The first integer to add
        b (int): The second integer to add
    
    Returns:
        int: The sum of a and b
            
    Example:
        >>> add(5, 3)
        8
    """
    return a + b

@mcp.tool()
def get_weather(city: str, country: str = "") -> dict:
    """
    Retrieve current weather information for a specified city.
    
    This tool fetches real-time weather data from the OpenWeatherMap API
    and returns formatted weather information including temperature,
    description, and humidity.
    
    Args:
        city (str): The name of the city to get weather data for
        country (str, optional): The country code to narrow down the search. 
                                 Defaults to empty string.
    
    Returns:
        dict: Weather information containing:
            - city: City name
            - country: Country code
            - temperature: Current temperature in Celsius
            - description: Weather condition description
            - humidity: Current humidity percentage
            
            Or on error:
            - error: Error message from the API or default message
            
    Example:
        >>> get_weather("London")
        {'city': 'London', 'country': 'GB', 'temperature': 15.2, 
         'description': 'scattered clouds', 'humidity': 76}
    """
    location = f"{city},{country}" if country else city
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }
    else:
        return {"error": data.get("message", "Failed to fetch weather")}



# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    weather = get_weather("London")
    print(weather)