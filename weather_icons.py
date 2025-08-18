WEATHER_ICONS = {
    "clear": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
            <circle cx="32" cy="32" r="20" fill="#FFD700" stroke="#FFA500" stroke-width="2"/>
            <circle cx="32" cy="32" r="15" fill="#FFFF00"/>
        </svg>
    """,
    "few_clouds": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
            <circle cx="32" cy="32" r="20" fill="#FFD700" stroke="#FFA500" stroke-width="2"/>
            <circle cx="32" cy="32" r="15" fill="#FFFF00"/>
            <path d="M20,40 Q30,30 40,40 Q50,50 30,50 Q20,50 20,40" fill="#FFFFFF" opacity="0.8"/>
        </svg>
    """,
    "scattered_clouds": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
            <path d="M15,40 Q25,30 45,30 Q55,35 50,45 Q45,55 30,55 Q15,55 15,40" fill="#FFFFFF" opacity="0.8"/>
            <path d="M30,35 Q40,25 50,35 Q60,45 45,50 Q35,55 25,45 Q20,35 30,35" fill="#FFFFFF" opacity="0.9"/>
        </svg>
    """,
    "clouds": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
            <path d="M10,40 Q20,30 40,30 Q50,35 45,45 Q40,55 25,55 Q10,55 10,40" fill="#FFFFFF" opacity="0.8"/>
            <path d="M25,35 Q35,25 45,35 Q55,45 40,50 Q30,55 20,45 Q15,35 25,35" fill="#FFFFFF" opacity="0.9"/>
            <path d="M35,30 Q45,20 55,30 Q65,40 50,45 Q40,50 30,40 Q25,30 35,30" fill="#FFFFFF" opacity="0.7"/>
        </svg>
    """,
    "rain": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
            <path d="M15,40 Q25,30 45,30 Q55,35 50,45 Q45,55 30,55 Q15,55 15,40" fill="#FFFFFF" opacity="0.8"/>
            <line x1="25" y1="50" x2="25" y2="60" stroke="#6495ED" stroke-width="2" stroke-linecap="round"/>
            <line x1="35" y1="50" x2="35" y2="60" stroke="#6495ED" stroke-width="2" stroke-linecap="round"/>
            <line x1="45" y1="50" x2="45" y2="60" stroke="#6495ED" stroke-width="2" stroke-linecap="round"/>
        </svg>
    """,
    "thunderstorm": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
            <path d="M15,40 Q25,30 45,30 Q55,35 50,45 Q45,55 30,55 Q15,55 15,40" fill="#303030" opacity="0.8"/>
            <polygon points="30,40 35,50 25,50 35,60" fill="#FFD700"/>
        </svg>
    """,
    "snow": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
            <path d="M15,40 Q25,30 45,30 Q55,35 50,45 Q45,55 30,55 Q15,55 15,40" fill="#FFFFFF" opacity="0.8"/>
            <path d="M30,50 L34,54 M32,48 L32,52 M34,50 L30,54" stroke="#87CEEB" stroke-width="1.5"/>
            <path d="M40,50 L44,54 M42,48 L42,52 M44,50 L40,54" stroke="#87CEEB" stroke-width="1.5"/>
            <path d="M50,50 L54,54 M52,48 L52,52 M54,50 L50,54" stroke="#87CEEB" stroke-width="1.5"/>
        </svg>
    """,
    "mist": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
            <path d="M15,35 Q25,25 45,25 Q55,30 50,40 Q45,50 30,50 Q15,50 15,35" fill="#F0F8FF" opacity="0.6"/>
            <path d="M10,40 L54,40" stroke="#A9A9A9" stroke-width="3" stroke-linecap="round" opacity="0.7"/>
            <path d="M15,45 L50,45" stroke="#A9A9A9" stroke-width="3" stroke-linecap="round" opacity="0.7"/>
            <path d="M20,50 L45,50" stroke="#A9A9A9" stroke-width="3" stroke-linecap="round" opacity="0.7"/>
        </svg>
    """,
    "drizzle": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
            <path d="M15,40 Q25,30 45,30 Q55,35 50,45 Q45,55 30,55 Q15,55 15,40" fill="#FFFFFF" opacity="0.8"/>
            <line x1="30" y1="45" x2="30" y2="50" stroke="#87CEEB" stroke-width="2" stroke-linecap="round"/>
            <line x1="40" y1="45" x2="40" y2="50" stroke="#87CEEB" stroke-width="2" stroke-linecap="round"/>
            <line x1="50" y1="45" x2="50" y2="50" stroke="#87CEEB" stroke-width="2" stroke-linecap="round"/>
        </svg>
    """,
    "unknown": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
            <circle cx="32" cy="32" r="20" fill="#FFD700" stroke="#FFA500" stroke-width="2"/>
            <text x="32" y="35" font-family="Arial" font-size="20" fill="black" text-anchor="middle">?</text>
        </svg>
    """
}