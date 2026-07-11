from datetime import datetime

class CustomLogger:
    def info(self, component, message):
        live_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # YYYY-MM-DD HH:MM:SS
        print(f"{live_time} [INFO] {component}: {message}")

    def warning(self, component, message):
        live_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{live_time} [WARNING] {component}: {message}")

    def error(self, component, message):
        live_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{live_time} [ERROR] {component}: {message}")

    def critical(self, component, message):
        live_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{live_time} [CRITICAL] {component}: {message}")


# Instantiate our custom class
logger = CustomLogger()

print("--- Simulating Live System Streams ---\n")

logger.info("AuthService", "User 'jdoe' logged in successfully from IP 192.168.1.45.")
logger.warning("DatabaseService", "Connection pool reaching 80% capacity (40/50 active).")
logger.error("PaymentGateway", "Transaction failed for ID txn_88322. Error: Timeout communicating with external API.")
logger.critical("DatabaseService", "Database connection pool exhausted! Deadlock detected on table 'orders'.")
    
