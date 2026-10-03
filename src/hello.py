def greet(name: str) -> str:
    """名前を受け取って挨拶文を返す。"""
    return f"こんにちは、{name}さん!"


if __name__ == "__main__":
    print(greet("世界"))
