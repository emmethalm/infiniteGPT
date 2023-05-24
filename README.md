# InfiniteGPT 🚀

InfiniteGPT is a Python script that lets you input an unlimited size text into the OpenAI API. No more tedious copy & pasting. It's a single python script that can connect to any of the OpenAI API chat models (gpt-3.5-turbo, gpt4, etc.). 

How the script works:

1. Fetches text of arbitrary length from an input text file.
2. Splits the input text into chunks of 500 tokens (approximately 380 words) each.
3. Makes simultaneous calls to the OpenAI API to perform some operation (which you must specify by editing the system prompt) on each chunk.
4. Stitches the outputs together in an output file.

This eliminates the need for re-prompting when using a large text input or copying and pasting endless chunks of text into chatGPT. 📚

## Dependencies 📦

- python3
- openai

## BYOK (Bring Your Own Keys!) 🔑

Go to [OpenAI](https://www.openai.com) to get your personal API keys. 

This script does not hide your API keys, so please do so if you plan on integrating it into a public application. ⚠️

## Usage 🛠️

1. Clone the repository
2. Install the required dependencies
3. Add your API keys
4. Edit the system prompt for your use case
5. Run the script

## License 📄

MIT License. See [LICENSE](LICENSE) for more information.

## Connect with me 📣

I write about using AI tools & share my latest building on Twitter [@ehalm_](https://twitter.com/ehalm_). DM me with any questions. 🐦

## Happy building! 🎉
