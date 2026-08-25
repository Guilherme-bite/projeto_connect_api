from app import create_app

if __name__ == '__main__':
    app = create_app()
    port = 5000
    app.run(debug=True, port=port)