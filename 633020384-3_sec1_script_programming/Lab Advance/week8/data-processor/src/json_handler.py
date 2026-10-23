import json
import os
from utils import ensure_directory_exists, setup_logging

logger = setup_logging(__name__)

class JSONHandler:
    """
    Handles reading, writing, and basic manipulation of JSON files.
    """
    def __init__(self):
        logger.info("JSONHandler initialized.")

    def read_json(self, file_path):
        """Reads a JSON file and returns the Python object."""
        if not os.path.exists(file_path):
            logger.error(f"JSON file not found: {file_path}")
            return None
        
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                data = json.load(file)
            logger.info(f"Successfully read JSON data from '{file_path}'.")
            return data
        except Exception as e:
            logger.error(f"Error reading JSON file '{file_path}': {e}")
            return None

    def write_json(self, data, file_path, indent=2):
        """Writes a Python object to a JSON file."""
        ensure_directory_exists(os.path.dirname(file_path))
        try:
            with open(file_path, mode='w', encoding='utf-8') as file:
                json.dump(data, file, indent=indent, ensure_ascii=False)
            logger.info(f"Successfully wrote JSON data to '{file_path}'.")
            return True
        except Exception as e:
            logger.error(f"Error writing JSON file '{file_path}': {e}")
            return False

    def update_inventory(self, inventory_data, product_id, new_stock):
        """Updates the stock quantity of a product by its ID."""
        # รองรับทั้งกรณีที่เป็น list ของสินค้า หรือ dict ที่เก็บ list อีกที
        products = inventory_data if isinstance(inventory_data, list) else inventory_data.get("products", [])
        
        updated = False
        for product in products:
            if product.get("id") == product_id:
                product["stock"] = new_stock
                logger.info(f"Updated product '{product_id}' stock to {new_stock}.")
                updated = True
                break
        
        if not updated:
            logger.warning(f"Product '{product_id}' not found in inventory.")

    def add_product(self, inventory_data, new_product):
        """Adds a new product entry to the inventory."""
        if isinstance(inventory_data, list):
            inventory_data.append(new_product)
            logger.info(f"Added new product '{new_product.get('id')}' to inventory list.")
        elif isinstance(inventory_data, dict) and "products" in inventory_data:
            inventory_data["products"].append(new_product)
            logger.info(f"Added new product '{new_product.get('id')}' to inventory dict.")
        else:
            logger.error("Invalid inventory data structure. Cannot add product.")
