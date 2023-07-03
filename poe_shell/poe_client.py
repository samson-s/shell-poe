import poe
import pickle
import os

from .config import STORAGE_PATH


class PoeClient:
    API_KEY_PICKLE_FILE = STORAGE_PATH + "api_key.pickle"

    def connect(self) -> poe.Client:
        api_key = self.get_api_key()

        if api_key is None:
            api_key = self.set_api_key()

        self.client = poe.Client(self.get_api_key())
        return self.client

    def get_api_key(self) -> str | None:
        """Get the API Key from pickled file."""
        try:
            with open(self.API_KEY_PICKLE_FILE, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None

    def set_api_key(self):
        """Input the API Key and save it to a pickled file."""
        api_key = input("Please enter your POE API key: ").strip()

        with open(self.API_KEY_PICKLE_FILE, "wb") as f:
            pickle.dump(api_key, f)
        print("API key saved.")

        return api_key

    def remove_api_key(self):
        """Remove the API Key from the pickled file."""
        try:
            os.remove(self.API_KEY_PICKLE_FILE)
        except FileNotFoundError:
            pass
        print("API key removed.")
