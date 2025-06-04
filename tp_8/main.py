from payment_processor import PaymentProcessor, PaymentRequest

if __name__ == "__main__":
    processor = PaymentProcessor()

    pedidos = [
        PaymentRequest(1, 500),
        PaymentRequest(2, 500),
        PaymentRequest(3, 500),
        PaymentRequest(4, 500),
        PaymentRequest(5, 500),
        PaymentRequest(6, 500),
        PaymentRequest(7, 500),
    ]

    for p in pedidos:
        processor.process(p)

    print("\nHistorial de pagos:")
    processor.list_payments()
