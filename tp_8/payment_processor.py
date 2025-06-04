"""
Módulo principal para el procesamiento de pagos utilizando patrones de diseño:
Singleton, Chain of Responsibility e Iterator.
Versión 1.2
"""

import json
from datetime import datetime
from collections import deque


class TokenManager:
    """Singleton que gestiona las claves asociadas a los tokens (bancos)."""
    _instance = None
    _tokens = {}

    def __new__(cls, json_file='sitedata.json'):
        if cls._instance is None:
            cls._instance = super(TokenManager, cls).__new__(cls)
            with open(json_file, 'r') as file:
                cls._tokens = json.load(file)
        return cls._instance

    def get_key(self, token_name):
        return self._tokens.get(token_name)


class PaymentRequest:
    """Representa una solicitud de pago."""
    def __init__(self, number, amount):
        self.number = number
        self.amount = amount


class AccountHandler:
    """Handler base de la cadena de responsabilidad."""
    def __init__(self, token, balance):
        self.token = token
        self.balance = balance
        self.successor = None

    def set_successor(self, successor):
        self.successor = successor

    def handle(self, payment, visited=None):
        """Procesa el pago si hay saldo suficiente o lo pasa al siguiente handler si no lo intentó aún."""
        if visited is None:
            visited = set()

        if self.token in visited:
            # Ya se intentó con esta cuenta, no seguir
            print(f"Pago #{payment.number} rechazado. Fondos insuficientes en todas las cuentas.")
            return False

        visited.add(self.token)

        if self.balance >= payment.amount:
            self.balance -= payment.amount
            token_key = TokenManager().get_key(self.token)
            PaymentHistory.add(payment.number, self.token, token_key, payment.amount)
            print(f"Pago #{payment.number} realizado con {self.token} (${payment.amount})")
            return True

        if self.successor:
            return self.successor.handle(payment, visited)

        print(f"Pago #{payment.number} rechazado. Fondos insuficientes.")
        return False


class PaymentHistory:
    """Historial de pagos con patrón iterator."""
    _payments = deque()

    @classmethod
    def add(cls, number, token, token_key, amount):
        cls._payments.append({
            "numero": number,
            "token": token,
            "clave": token_key,
            "monto": amount,
            "timestamp": datetime.now().isoformat()
        })

    @classmethod
    def list(cls):
        for p in cls._payments:
            print(f"#{p['numero']} | Token: {p['token']} | Clave: {p['clave']} | Monto: ${p['monto']} | Hora: {p['timestamp']}")


class PaymentProcessor:
    """Procesador principal que intercala pagos entre cuentas."""
    def __init__(self):
        self.token1 = AccountHandler("token1", 1000)
        self.token2 = AccountHandler("token2", 2000)
        self.token1.set_successor(self.token2)
        self.token2.set_successor(self.token1)
        self.toggle = True  # Alternador

    def process(self, payment):
        if self.toggle:
            self.token1.handle(payment)
        else:
            self.token2.handle(payment)
        self.toggle = not self.toggle


    def list_payments(self):
        PaymentHistory.list()
