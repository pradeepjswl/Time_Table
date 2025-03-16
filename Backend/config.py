import os

class Config:
    # PostgreSQL database URI
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:Anjali@2005@localhost/timetable_db')
    
    # # Disable modification tracking (optional but recommended)
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for session management and CSRF protection
    SECRET_KEY = os.getenv('SECRET_KEY', '73cee360d3026f4a4f092f4659b242ad4f4466dc6ecd54b4')

    # Flask debug mode (set to False in production)
    DEBUG = os.getenv('DEBUG', 'True') == 'True'

    # Flask environment (development, testing, production)
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')

    # CORS settings (if your frontend and backend are on different domains)
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:3000')  # Allow requests from this origin

    # JWT settings (if using JWT for authentication)
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'efb1013527e4f416575d74fece0d57d56c734fc35449e0e9')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 3600))  # Token expires in 1 hour

    # Email settings (if sending emails)
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'pradeepkumarjaiswal605@gmail.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'Anjali@2005')