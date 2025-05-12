from timeclock import app

if __name__ == "__main__":
    # Explicitly set debug
    app.debug = True
    # Run with host=0.0.0.0 to make it accessible outside container
    app.run(host="0.0.0.0", port=5000)