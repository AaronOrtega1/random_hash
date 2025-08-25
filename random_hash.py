import secrets
import string


class RandomHash:
    def __init__(self):
        self.alphabet = string.hexdigits.lower()

    def randomHashGenerator(self, n: int):
        for i in range(n):
            current_hash = "".join(secrets.choice(self.alphabet) for _ in range(32))
            if self.checkRandomHash(current_hash):
                print(f"Found after {i + 1} tries")
                return current_hash
        print("No hash starting with '00' found after 1000 tries")
        return None

    @staticmethod
    def checkRandomHash(randomHash: str) -> bool:
        return randomHash.startswith("00")


def main():
    test = RandomHash()
    result = test.randomHashGenerator(n=1000)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
