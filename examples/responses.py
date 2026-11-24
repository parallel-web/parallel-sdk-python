#!/usr/bin/env -S rye run python

from parallel import Parallel


def main() -> None:
    prompt = "What is the capital of France? Answer in one sentence."
    with Parallel() as client:
        response = client.responses.create(model="parallel", input=prompt)
        for item in response.output:
            if item.type == "message":
                for part in item.content:
                    print(part.text)

        with client.responses.create(model="parallel", input=prompt, stream=True) as stream:
            for event in stream:
                if event.type == "response.output_text.delta":
                    print(event.delta, end="", flush=True)
        print()


if __name__ == "__main__":
    main()
