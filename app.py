from website import create_app
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action='store_true')
    args = parser.parse_args()
    app = create_app()
    app.run(debug=args.debug is not None, host="0.0.0.0", port=80)
