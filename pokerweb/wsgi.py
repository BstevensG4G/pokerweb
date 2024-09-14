from pokerweb import create_app


app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
else:
    gunicorn_app = create_app()

